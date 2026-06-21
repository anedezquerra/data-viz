"""Generate Sphinx API indexes and one page per public function or class."""

from __future__ import annotations

import ast
import shutil
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = ROOT / "dataviz"
OUTPUT_ROOT = ROOT / "docs" / "source" / "api"


@dataclass(frozen=True)
class Member:
    """A public function or class declared directly in a Python module."""

    name: str
    kind: str


SPC_MODULE_SUMMARIES = {
    "attribute": "Monitor defective units and defect rates with p, np, c, and u charts.",
    "capability": "Measure process performance against lower and upper specification limits.",
    "charts": "Use stable compatibility entry points for core static SPC charts.",
    "constants": "Look up traditional control-chart constants for rational subgroups.",
    "control": "Build individuals control charts for continuous process observations.",
    "dashboard": "Combine control, variation, distribution, and rule signals in one view.",
    "diagnostics": "Investigate runs, zones, violations, distributions, and Pareto priorities.",
    "multivariate": "Monitor correlated process variables with Hotelling T-squared statistics.",
    "rules": "Calculate control limits and detect common process-behavior rule violations.",
    "variable": "Monitor variable data with moving-range, Xbar, EWMA, and CUSUM charts.",
    "x_range": "Compare individual measurements with their short-term moving variation.",
}


def spc_fixture(module_leaf: str, member_name: str) -> list[str]:
    """Return deterministic setup lines for an executable SPC example."""
    if module_leaf == "attribute":
        if member_name.startswith("p_chart"):
            return [
                "defects = np.array([3, 5, 4, 6, 2, 7, 4, 5, 3, 6])",
                "sample_sizes = np.array([100, 105, 98, 110, 102, 108, 100, 104, 99, 106])",
            ]
        if member_name.startswith("np_chart"):
            return ["defects = np.array([3, 5, 4, 6, 2, 7, 4, 5, 3, 6])"]
        if member_name.startswith("u_chart"):
            return [
                "defects = np.array([8, 12, 9, 15, 7, 11, 10, 13, 8, 12])",
                "units = np.array([40, 50, 45, 55, 42, 48, 50, 52, 44, 49])",
            ]
        return ["defects = np.array([8, 12, 9, 15, 7, 11, 10, 13, 8, 12])"]
    if module_leaf == "multivariate":
        return [
            "rng = np.random.default_rng(42)",
            "data = rng.multivariate_normal([10.0, 25.0, 4.0], [[1.0, 0.5, 0.2], [0.5, 2.0, 0.3], [0.2, 0.3, 0.5]], size=40)",
        ]
    if member_name in {"xbar_r_limits", "xbar_s_limits"} or member_name.startswith(
        ("xbar_r_chart", "xbar_s_chart")
    ):
        return [
            "rng = np.random.default_rng(42)",
            "data = rng.normal(loc=10.0, scale=0.35, size=(20, 5))",
        ]
    if member_name.startswith("pareto_chart"):
        return [
            'categories = ["Surface", "Dimension", "Assembly", "Packaging"]',
            "counts = [38, 24, 13, 7]",
        ]
    if member_name == "subgroup_matrix":
        return ["data = np.arange(1.0, 21.0)"]
    if member_name == "get_spc_constants":
        return []
    if member_name in {
        "ControlLimits",
        "RuleViolation",
        "SPCConstants",
        "CapabilityStats",
        "HotellingT2Result",
    }:
        return []
    return [
        "rng = np.random.default_rng(42)",
        "data = rng.normal(loc=10.0, scale=0.4, size=30)",
        "data[24] = 11.8  # Deliberate special-cause signal",
    ]


def spc_call(module_leaf: str, member: Member) -> tuple[list[str], list[str]]:
    """Return invocation and result-display lines for an SPC member."""
    name = member.name
    calls = {
        "p_chart_static": 'ax = p_chart_static(defects, sample_sizes, title="Supplier defect proportion")',
        "p_chart_interactive": 'fig = p_chart_interactive(defects, sample_sizes, title="Supplier defect proportion")',
        "np_chart_static": 'ax = np_chart_static(defects, sample_size=100, title="Defectives per lot")',
        "np_chart_interactive": 'fig = np_chart_interactive(defects, sample_size=100, title="Defectives per lot")',
        "c_chart_static": 'ax = c_chart_static(defects, title="Surface defects per panel")',
        "c_chart_interactive": 'fig = c_chart_interactive(defects, title="Surface defects per panel")',
        "u_chart_static": 'ax = u_chart_static(defects, units, title="Defects per inspected unit")',
        "u_chart_interactive": 'fig = u_chart_interactive(defects, units, title="Defects per inspected unit")',
        "capability_summary": "result = capability_summary(data, lsl=9.0, usl=11.0)",
        "capability_histogram_static": "ax = capability_histogram_static(data, lsl=9.0, usl=11.0, bins=12)",
        "capability_histogram_interactive": "fig = capability_histogram_interactive(data, lsl=9.0, usl=11.0, bins=12)",
        "control_chart": 'ax = control_chart(data, title="Filling process")',
        "x_range_chart": 'ax = x_range_chart(data, subgroup_size=5, title="Filling process variation")',
        "control_chart_static": 'ax = control_chart_static(data, title="Filling process", ylabel="Fill weight (g)")',
        "control_chart_interactive": 'fig = control_chart_interactive(data, title="Filling process", ylabel="Fill weight (g)")',
        "spc_dashboard_static": 'fig = spc_dashboard_static(data, bins=12, title="Filling process overview")',
        "spc_dashboard_interactive": 'fig = spc_dashboard_interactive(data, bins=12, title="Filling process overview")',
        "run_chart_static": 'ax = run_chart_static(data, title="Filling process run chart")',
        "run_chart_interactive": 'fig = run_chart_interactive(data, title="Filling process run chart")',
        "rule_violation_chart_static": 'ax = rule_violation_chart_static(data, title="Process rule signals")',
        "rule_violation_chart_interactive": 'fig = rule_violation_chart_interactive(data, title="Process rule signals")',
        "pareto_chart_static": 'ax = pareto_chart_static(categories, counts, title="Defect priorities")',
        "pareto_chart_interactive": 'fig = pareto_chart_interactive(categories, counts, title="Defect priorities")',
        "process_distribution_static": "ax = process_distribution_static(data, bins=12)",
        "process_distribution_interactive": "fig = process_distribution_interactive(data, bins=12)",
        "zone_chart_static": 'ax = zone_chart_static(data, title="Process zones")',
        "zone_chart_interactive": 'fig = zone_chart_interactive(data, title="Process zones")',
        "hotelling_t2_summary": "result = hotelling_t2_summary(data, limit_quantile=0.95)",
        "hotelling_t2_chart_static": "ax = hotelling_t2_chart_static(data, limit_quantile=0.95)",
        "hotelling_t2_chart_interactive": "fig = hotelling_t2_chart_interactive(data, limit_quantile=0.95)",
        "as_numeric_series": 'result = as_numeric_series(data, name="Fill weight")',
        "individuals_limits": "result = individuals_limits(data)",
        "moving_ranges": "result = moving_ranges(data, span=2)",
        "subgroup_matrix": "result = subgroup_matrix(data, subgroup_size=5)",
        "xbar_r_limits": "x_limits, r_limits, means, ranges = xbar_r_limits(data)",
        "xbar_s_limits": "x_limits, s_limits, means, stds = xbar_s_limits(data)",
        "detect_rule_violations": "result = detect_rule_violations(data)",
        "violations_by_index": "result = violations_by_index(detect_rule_violations(data))",
        "moving_range_chart_static": "ax = moving_range_chart_static(data, span=2)",
        "moving_range_chart_interactive": "fig = moving_range_chart_interactive(data, span=2)",
        "xbar_r_chart_static": "ax = xbar_r_chart_static(data)",
        "xbar_r_chart_interactive": "fig = xbar_r_chart_interactive(data)",
        "xbar_s_chart_static": "ax = xbar_s_chart_static(data)",
        "xbar_s_chart_interactive": "fig = xbar_s_chart_interactive(data)",
        "ewma_chart_static": "ax = ewma_chart_static(data, lambda_=0.2)",
        "ewma_chart_interactive": "fig = ewma_chart_interactive(data, lambda_=0.2)",
        "cusum_chart_static": "ax = cusum_chart_static(data, target=10.0, k=0.25, h=4.0)",
        "cusum_chart_interactive": "fig = cusum_chart_interactive(data, target=10.0, k=0.25, h=4.0)",
        "x_range_chart_static": "ax = x_range_chart_static(data, subgroup_size=5)",
        "x_range_chart_interactive": "fig = x_range_chart_interactive(data, subgroup_size=5)",
        "get_spc_constants": "result = get_spc_constants(5)",
        "ControlLimits": "result = ControlLimits(center=10.0, lower=8.8, upper=11.2, sigma=0.4)",
        "RuleViolation": 'result = RuleViolation(index=24, value=11.8, rule="beyond_limits", message="Point outside control limits")',
        "SPCConstants": "result = SPCConstants(n=5, a2=0.577, d3=0.0, d4=2.114, a3=1.427, b3=0.0, b4=2.089, c4=0.94)",
        "CapabilityStats": "result = CapabilityStats(n=30, mean=10.0, std=0.4, lsl=9.0, usl=11.0, cp=0.833, cpk=0.833, ppm_below=0.0, ppm_above=0.0, ppm_below_normal=6209.7, ppm_above_normal=6209.7, ppm_total_normal=12419.4)",
        "HotellingT2Result": 'result = HotellingT2Result(scores=pd.Series([0.5, 1.2], name="T2"), center=pd.Series([10.0, 25.0]), covariance=pd.DataFrame([[1.0, 0.2], [0.2, 2.0]]), limit=1.1)',
    }
    call = calls[name]
    imports: list[str] = []
    if name == "violations_by_index":
        imports.append("from dataviz.spc.rules import detect_rule_violations")
    if name == "HotellingT2Result":
        imports.append("import pandas as pd")
    if name.endswith("_static") or (
        module_leaf == "charts" and member.kind == "function"
    ):
        return imports + [call], ["plt.show()"]
    if name.endswith("_interactive"):
        return imports + [call], ["fig.show()"]
    if name == "xbar_r_limits":
        return imports + [call], [
            "print(x_limits)",
            "print(r_limits)",
            "print(means.head())",
        ]
    if name == "xbar_s_limits":
        return imports + [call], [
            "print(x_limits)",
            "print(s_limits)",
            "print(stds.head())",
        ]
    return imports + [call], ["print(result)"]


def spc_example(dotted_module: str, member: Member) -> str:
    """Build a standalone, copy-pasteable example for an SPC API member."""
    module_leaf = dotted_module.rsplit(".", 1)[-1]
    fixture = spc_fixture(module_leaf, member.name)
    invocation, display = spc_call(module_leaf, member)
    imports = ["import numpy as np"]
    if member.name.endswith("_static") or (
        module_leaf == "charts" and member.kind == "function"
    ):
        imports.append("import matplotlib.pyplot as plt")
    imports.append(f"from {dotted_module} import {member.name}")
    lines = (
        imports
        + invocation[:-1]
        + ([""] + fixture if fixture else [])
        + [""]
        + invocation[-1:]
        + display
    )
    return "\n".join(lines)


def spc_gallery() -> str:
    """Return four future-image placeholders in a responsive gallery."""
    cards = "".join(
        f'<figure class="spc-image-slot"><div aria-hidden="true">{index:02d}</div><figcaption>Future example image {index}</figcaption></figure>'
        for index in range(1, 5)
    )
    return f'\nOutput gallery\n--------------\n\n.. raw:: html\n\n   <div class="spc-image-grid">{cards}</div>\n'


def heading(title: str, marker: str = "=") -> str:
    """Return a reStructuredText heading."""
    return f"{title}\n{marker * len(title)}\n"


def module_name(path: Path) -> str:
    """Convert a package source path to its dotted import path."""
    relative = path.relative_to(ROOT).with_suffix("")
    parts = list(relative.parts)
    if parts[-1] == "__init__":
        parts.pop()
    return ".".join(parts)


def public_members(path: Path) -> list[Member]:
    """Return public functions and classes declared directly in *path*."""
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    members: list[Member] = []
    for node in tree.body:
        if isinstance(
            node, (ast.FunctionDef, ast.AsyncFunctionDef)
        ) and not node.name.startswith("_"):
            members.append(Member(node.name, "function"))
        elif isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
            members.append(Member(node.name, "class"))
    return members


def rst_path_for_module(dotted_name: str) -> Path:
    """Return the generated index path for a module or package."""
    return OUTPUT_ROOT / f"{dotted_name}.rst"


def member_rst_path(dotted_module: str, member: Member) -> Path:
    """Return the generated detail-page path for a member."""
    return (
        OUTPUT_ROOT / "members" / Path(*dotted_module.split(".")) / f"{member.name}.rst"
    )


def write_member_page(dotted_module: str, member: Member) -> str:
    """Write one API page and return its source-relative toctree path."""
    path = member_rst_path(dotted_module, member)
    path.parent.mkdir(parents=True, exist_ok=True)
    qualified_name = f"{dotted_module}.{member.name}"
    directive = "autofunction" if member.kind == "function" else "autoclass"
    options = "\n   :members:\n   :show-inheritance:" if member.kind == "class" else ""
    if dotted_module.startswith("dataviz.spc."):
        member_label = "Class" if member.kind == "class" else "Function"
        intro = (
            ".. raw:: html\n\n"
            f'   <div class="spc-api-hero"><span>{member_label}</span><p>{dotted_module}</p></div>\n\n'
        )
        example = spc_example(dotted_module, member)
        code_block = "".join(
            f"   {line}\n" if line else "\n" for line in example.splitlines()
        )
        content = (
            f"{heading(qualified_name)}\n{intro}"
            f".. currentmodule:: {dotted_module}\n\n"
            f".. {directive}:: {member.name}{options}\n\n"
            "Complete example\n----------------\n\n"
            "The following example is self-contained and can be copied into a Python session or script.\n\n"
            f".. code-block:: python\n\n{code_block}"
            f"{spc_gallery()}"
        )
    else:
        content = (
            f"{heading(qualified_name)}\n"
            f".. currentmodule:: {dotted_module}\n\n"
            f".. {directive}:: {member.name}{options}\n"
        )
    path.write_text(content, encoding="utf-8")
    return path.relative_to(OUTPUT_ROOT).with_suffix("").as_posix()


def write_module_page(path: Path) -> None:
    """Write a submodule index linking to one page per public member."""
    dotted_name = module_name(path)
    members = public_members(path)
    lines = [heading(f"{dotted_name} module")]
    if dotted_name.startswith("dataviz.spc."):
        leaf = dotted_name.rsplit(".", 1)[-1]
        summary = SPC_MODULE_SUMMARIES.get(
            leaf, "Statistical process control tools and visualizations."
        )
        lines.append(
            "\n.. raw:: html\n\n"
            f'   <div class="spc-module-hero"><span>SPC toolkit</span><h2>{leaf.replace("_", " ").title()}</h2><p>{summary}</p></div>\n'
        )
    lines.append(f"\n.. automodule:: {dotted_name}\n")
    if members:
        lines.extend(
            ["\nPublic API\n----------\n", "\n.. toctree::\n   :maxdepth: 1\n\n"]
        )
        for member in members:
            lines.append(f"   {write_member_page(dotted_name, member)}\n")
    else:
        lines.append("\nThis module does not declare public functions or classes.\n")
    rst_path_for_module(dotted_name).write_text("".join(lines), encoding="utf-8")


def immediate_children(package_dir: Path) -> tuple[list[str], list[str]]:
    """Return immediate subpackage and submodule import paths."""
    subpackages = [
        module_name(child / "__init__.py")
        for child in sorted(package_dir.iterdir())
        if child.is_dir()
        and (child / "__init__.py").exists()
        and child.name != "__pycache__"
    ]
    submodules = [
        module_name(child)
        for child in sorted(package_dir.glob("*.py"))
        if child.name != "__init__.py"
    ]
    return subpackages, submodules


def write_package_page(package_dir: Path) -> None:
    """Write a navigational package page without duplicating member docs."""
    dotted_name = module_name(package_dir / "__init__.py")
    subpackages, submodules = immediate_children(package_dir)
    lines = [heading(dotted_name)]
    for title, children in (("Subpackages", subpackages), ("Submodules", submodules)):
        if not children:
            continue
        lines.extend(
            [f"\n{heading(title, '-')}", "\n.. toctree::\n   :maxdepth: 2\n\n"]
        )
        lines.extend(f"   {child}\n" for child in children)
    rst_path_for_module(dotted_name).write_text("".join(lines), encoding="utf-8")


def generate() -> None:
    """Replace the generated API tree with the current package structure."""
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    OUTPUT_ROOT.mkdir(parents=True)

    package_dirs = sorted(
        {path.parent for path in PACKAGE_ROOT.rglob("__init__.py")},
        key=lambda path: (len(path.parts), str(path)),
    )
    for package_dir in package_dirs:
        write_package_page(package_dir)

    for path in sorted(PACKAGE_ROOT.rglob("*.py")):
        if path.name != "__init__.py":
            write_module_page(path)

    (OUTPUT_ROOT / "modules.rst").write_text(
        f"{heading('API reference')}\n.. toctree::\n   :maxdepth: 4\n\n   dataviz\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    generate()
