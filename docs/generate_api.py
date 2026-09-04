"""Generate Sphinx API indexes and one page per public function or class.

Each member page embeds a self-contained "Complete example". Run
``python docs/generate_api.py --verify`` to execute them all headlessly.
"""

from __future__ import annotations

import ast
import importlib
import inspect
import shutil
import sys
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


IMAGE_ROOT = ROOT / "docs" / "source" / "_static" / "api"


def member_image_path(dotted_module: str, member: Member) -> Path:
    """Return the PNG path mirroring the generated member-page layout."""
    return IMAGE_ROOT / Path(*dotted_module.split(".")) / f"{member.name}.png"


def gallery_for(dotted_module: str, member: Member) -> str:
    """Return the real example image when rendered, else placeholders."""
    image = member_image_path(dotted_module, member)
    if image.exists():
        rst = member_rst_path(dotted_module, member)
        src = Path(*[".."] * len(rst.relative_to(OUTPUT_ROOT).parts))
        src = src / image.relative_to(ROOT / "docs" / "source")
        card = (
            f'<figure class="spc-image-slot spc-image-real">'
            f'<img src="{src.as_posix()}" alt="{member.name} example output">'
            f"<figcaption>Example output</figcaption></figure>"
        )
        return (
            "\nOutput gallery\n--------------\n\n.. raw:: html\n\n"
            f'   <div class="spc-image-grid">{card}</div>\n'
        )
    cards = "".join(
        f'<figure class="spc-image-slot"><div aria-hidden="true">{index:02d}</div><figcaption>Future example image {index}</figcaption></figure>'
        for index in range(1, 5)
    )
    return f'\nOutput gallery\n--------------\n\n.. raw:: html\n\n   <div class="spc-image-grid">{cards}</div>\n'


MODULE_TOOLKITS = {
    "bivariate": "Bivariate toolkit",
    "classification": "Classification toolkit",
    "clustering": "Clustering toolkit",
    "eda": "EDA toolkit",
    "multivariate": "Multivariate toolkit",
    "regression": "Regression toolkit",
    "spc": "SPC toolkit",
    "univariate": "Univariate toolkit",
    "utils": "Utilities",
    "xai": "XAI toolkit",
}

PACKAGE_SUMMARIES = {
    "bivariate": "Explore relationships between two variables.",
    "classification": "Evaluate and compare classification models.",
    "clustering": "Inspect cluster structure and choose cluster counts.",
    "eda": "Audit data quality, missingness, and class balance.",
    "multivariate": "Visualize structure across many variables at once.",
    "regression": "Diagnose and compare regression models.",
    "univariate": "Profile, test, and visualize a single variable.",
    "utils": "Shared validation, theming, and plotting helpers.",
    "xai": "Explain model predictions and feature effects.",
}

# Deterministic sample data, keyed by the parameter or variable name used in
# generated examples. Ported from the website docs generator.
GENERIC_FIXTURES = {
    "x": 'x = pd.Series([1, 2, 3, 4, 5], name="Input")',
    "y": 'y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")',
    "values": 'values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")',
    "df": 'df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})',
    "cm": "cm = np.array([[32, 4], [5, 29]])",
    "fpr": "fpr = np.array([0.0, 0.1, 0.3, 1.0])",
    "tpr": "tpr = np.array([0.0, 0.7, 0.9, 1.0])",
    "precision": "precision = np.array([1.0, 0.86, 0.72])",
    "recall": "recall = np.array([0.2, 0.7, 1.0])",
    "y_true": "y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])",
    "y_pred": "y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])",
    "train_sizes": "train_sizes = np.array([50, 100, 200])",
    "train_scores": "train_scores = np.array([0.82, 0.86, 0.89])",
    "validation_scores": "validation_scores = np.array([0.76, 0.81, 0.84])",
    "labels": "labels = np.array([0, 0, 1, 1])",
    "k_values": "k_values = np.array([1, 2, 3, 4])",
    "inertias": "inertias = np.array([10.0, 4.2, 2.6, 2.1])",
    "linkage_matrix": "linkage_matrix = np.array([[0, 1, 0.3, 2], [2, 3, 0.4, 2], [4, 5, 3.0, 4]])",
    "importances": "importances = np.array([0.42, 0.31, 0.18])",
    "feature_names": 'feature_names = ["age", "income", "tenure"]',
    "shap_values": "shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])",
    "feature_values": "feature_values = np.array([0, 1, 2, 3])",
    "pd_values": "pd_values = np.array([0.2, 0.25, 0.31, 0.34])",
    "weights": 'weights = pd.Series([1.0, 1.5, 0.8, 1.2, 1.0, 1.1], name="Weight")',
    "sentinels": 'sentinels = [-1, 999, "missing"]',
    "thresholds": "thresholds = [10, 12, 14]",
    "timestamps": 'timestamps = pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-04", "2026-01-10"])',
    "texts": 'texts = pd.Series(["fast reliable process", "reliable visual process", "fast chart"], name="Comment")',
    "flags": 'flags = pd.Series([True, False, True, True, False], name="Passed")',
    "categories": 'categories = pd.Series(["low", "medium", "high", "medium", "low"], name="Priority")',
    "defects": "defects = pd.Series([2, 1, 3, 0, 2, 1])",
    "defectives": "defectives = pd.Series([3, 2, 5, 1, 4, 2])",
    "n": "n = pd.Series([100, 100, 100, 100, 100, 100])",
    "units": "units = pd.Series([50, 48, 52, 51, 50, 49])",
    "matrix": 'matrix = pd.DataFrame({"x1": [1.0, 1.1, 0.9, 1.2], "x2": [2.0, 2.1, 1.8, 2.2]})',
}

# Parameter name -> argument expression used in generated calls.
GENERIC_ARGS = {
    "values": "values",
    "value": '"Value"',
    "x": "x",
    "y": "y",
    "data": "values",
    "category": "categories",
    "categories": "categories",
    "group": "categories",
    "groups": "categories",
    "hue": "categories",
    "weights": "weights",
    "sentinels": "sentinels",
    "thresholds": "thresholds",
    "labels": "labels",
    "cm": "cm",
    "fpr": "fpr",
    "tpr": "tpr",
    "precision": "precision",
    "recall": "recall",
    "y_true": "y_true",
    "y_pred": "y_pred",
    "train_sizes": "train_sizes",
    "train_scores": "train_scores",
    "validation_scores": "validation_scores",
    "importances": "importances",
    "feature_names": "feature_names",
    "shap_values": "shap_values",
    "feature_values": "feature_values",
    "pd_values": "pd_values",
    "k_values": "k_values",
    "inertias": "inertias",
    "linkage_matrix": "linkage_matrix",
    "defects": "defects",
    "defectives": "defectives",
    "n": "n",
    "units": "units",
    "matrix": "matrix",
    "lsl": "9.5",
    "usl": "10.5",
    "subgroup_size": "5",
    "sample_size": "100",
    "alpha": "0.05",
}

# Extra keyword arguments for functions whose defaults are not illustrative.
GENERIC_EXTRA_KWARGS = (
    (("capability",), "lsl=9.5, usl=10.5"),
    (("bootstrap",), "seed=42"),
    (("fit_distribution", "fitted_distribution"), 'distribution="norm"'),
    (("compare_distributions",), 'distributions=["norm", "lognorm"]'),
    (("weighted_quantile",), "quantile=0.5"),
)


def resolve_member(dotted_module: str, name: str) -> object | None:
    """Import *dotted_module* and return the member object, if available."""
    try:
        module = importlib.import_module(dotted_module)
        return getattr(module, name, None)
    except Exception:
        return None


def required_params(dotted_module: str, member: Member) -> list[str]:
    """Return required parameter names for a function, by introspection."""
    if member.kind != "function":
        return []
    target = resolve_member(dotted_module, member.name)
    if target is None:
        return []
    try:
        signature = inspect.signature(target)
    except (TypeError, ValueError):
        return []
    return [
        param.name
        for param in signature.parameters.values()
        if param.default is inspect.Parameter.empty
        and param.kind
        in (param.POSITIONAL_ONLY, param.POSITIONAL_OR_KEYWORD, param.KEYWORD_ONLY)
    ]


def generic_fixture(pkg: str, name: str, required: list[str]) -> list[str]:
    """Return deterministic setup lines for a generated example."""
    keys: list[str] = []
    required_set = set(required)

    def need(*fixture_keys: str) -> None:
        for key in fixture_keys:
            if key not in keys:
                keys.append(key)

    if pkg == "bivariate" or {"x", "y"} & required_set:
        need("x", "y")
    if pkg == "univariate" or {"data", "values", "value"} & required_set:
        need("values")
    if pkg in {"eda", "multivariate"} or "missing" in name:
        need("df")
    if pkg == "classification" or "cm" in required_set:
        need("cm", "fpr", "tpr", "precision", "recall")
    if pkg == "regression" or {"y_true", "y_pred"} & required_set:
        need("y_true", "y_pred", "train_sizes", "train_scores", "validation_scores")
    if pkg == "clustering":
        need("x", "y", "labels", "k_values", "inertias", "linkage_matrix")
    if pkg == "xai":
        need("importances", "feature_names", "shap_values", "feature_values", "pd_values")
    if "weighted" in name:
        need("weights")
    if "sentinel" in name:
        need("sentinels")
    if "exceedance" in name:
        need("thresholds")
    if "event" in name or "interarrival" in name:
        need("timestamps")
    if "term" in name or "string" in name or "token" in name:
        need("texts")
    if "boolean" in name:
        need("flags")
    if any(
        token in name
        for token in ("category", "frequency", "pareto", "ordinal", "likert")
    ):
        need("categories")
    for param in required:
        if param in GENERIC_FIXTURES:
            need(param)
    return [GENERIC_FIXTURES[key] for key in keys]


def generic_fallback_args(pkg: str, name: str) -> list[str]:
    """Return fallback positional arguments when introspection is unavailable."""
    if pkg == "spc":
        if "np_chart" in name:
            return ["defectives"]
        if "p_chart" in name:
            return ["defectives", "n"]
        if "c_chart" in name:
            return ["defects"]
        if "u_chart" in name:
            return ["defects", "units"]
        if "hotelling" in name:
            return ["matrix"]
        return ["values"]
    if pkg == "classification":
        if "roc" in name:
            return ["fpr", "tpr"]
        if "precision" in name:
            return ["precision", "recall"]
        return ["cm"]
    if pkg == "regression":
        if "learning" in name:
            return ["train_sizes", "train_scores", "validation_scores"]
        return ["y_true", "y_pred"]
    if pkg == "clustering":
        if "dendrogram" in name:
            return ["linkage_matrix"]
        if "elbow" in name:
            return ["k_values", "inertias"]
        return ["x", "y", "labels"]
    if pkg == "xai":
        if "shap" in name:
            return ["shap_values", "feature_names"]
        if "partial" in name or "dependence" in name:
            return ["feature_values", "pd_values"]
        return ["importances", "feature_names"]
    if pkg == "bivariate":
        return ["x", "y"]
    if pkg in {"eda", "multivariate"}:
        if pkg == "eda" and "class" in name:
            return ["categories"]
        return ["df"]
    if "weighted" in name:
        return ["values", "weights"]
    if "sentinel" in name:
        return ["values", "sentinels"]
    if "exceedance" in name:
        return ["values", "thresholds"]
    if "event" in name or "interarrival" in name:
        return ["timestamps"]
    if "term" in name or "string" in name or "token" in name:
        return ["texts"]
    if "boolean" in name:
        return ["flags"]
    if any(
        token in name
        for token in ("category", "frequency", "pareto", "ordinal", "likert")
    ):
        return ["categories"]
    return ["values"]


def class_value_for(name: str, annotation: object) -> str:
    """Return a representative literal for a dataclass field."""
    text = str(annotation)
    if "float" in text:
        return "0.5"
    if "int" in text:
        return "5"
    if "bool" in text:
        return "True"
    if "str" in text:
        return '"label"'
    if "DataFrame" in text:
        return 'pd.DataFrame({"a": [1, 2], "b": [3, 4]})'
    if "Series" in text or "ArrayLike" in text:
        return 'pd.Series([1.0, 2.0, 3.0], name="Value")'
    if "dict" in text or "Mapping" in text:
        return '{"a": 1.0}'
    if "list" in text or "Sequence" in text or "tuple" in text:
        return "[1.0, 2.0, 3.0]"
    return "None"


def generic_call(dotted_module: str, member: Member) -> tuple[list[str], list[str]]:
    """Return invocation and result-display lines for a generated example."""
    pkg = dotted_module.split(".")[1]
    name = member.name
    if member.kind == "class":
        target = resolve_member(dotted_module, name)
        try:
            signature = inspect.signature(target) if target is not None else None
        except (TypeError, ValueError):
            signature = None
        kwargs = []
        if signature is not None:
            for param in signature.parameters.values():
                if param.default is inspect.Parameter.empty:
                    kwargs.append(f"{param.name}={class_value_for(param.name, param.annotation)}")
        return [f"result = {name}({', '.join(kwargs)})"], ["print(result)"]

    required = required_params(dotted_module, member)
    args = [GENERIC_ARGS[param] for param in required if param in GENERIC_ARGS]
    if len(args) != len(required):
        args = generic_fallback_args(pkg, name)
    extra = ""
    for tokens, suffix in GENERIC_EXTRA_KWARGS:
        if any(token in name for token in tokens):
            extra = f", {suffix}"
            break
    if name.endswith("_static"):
        return [f"ax = {name}({', '.join(args)}{extra})"], ["plt.show()"]
    if name.endswith("_interactive"):
        return [f"fig = {name}({', '.join(args)}{extra})"], ["fig.show()"]
    return [f"result = {name}({', '.join(args)}{extra})"], ["print(result)"]


def generic_example(dotted_module: str, member: Member) -> str:
    """Build a standalone, copy-pasteable example for a non-SPC API member."""
    pkg = dotted_module.split(".")[1]
    required = required_params(dotted_module, member)
    fixture = generic_fixture(pkg, member.name, required)
    invocation, display = generic_call(dotted_module, member)
    imports = []
    if any("np." in line for line in fixture):
        imports.append("import numpy as np")
    if any(("pd." in line) for line in fixture):
        imports.append("import pandas as pd")
    if member.name.endswith("_static"):
        imports.append("import matplotlib.pyplot as plt")
    imports.append(f"from {dotted_module} import {member.name}")
    lines = imports + ([""] + fixture if fixture else []) + [""] + invocation + display
    return "\n".join(lines)


def curated_examples() -> dict[str, str]:
    """Load curated per-module examples from docs/_examples/<pkg>.py files."""
    registry: dict[str, str] = {}
    examples_dir = ROOT / "docs" / "_examples"
    if not examples_dir.exists():
        return registry
    for path in sorted(examples_dir.glob("*.py")):
        namespace: dict[str, object] = {}
        exec(path.read_text(encoding="utf-8"), namespace)  # noqa: S102
        registry.update(namespace.get("EXAMPLES", {}))
    return registry


CURATED_EXAMPLES = curated_examples()


def example_for(dotted_module: str, member: Member) -> str:
    """Build a standalone, copy-pasteable example for an API member."""
    curated = CURATED_EXAMPLES.get(f"{dotted_module}.{member.name}")
    if curated is not None:
        return curated
    if dotted_module.startswith("dataviz.spc."):
        try:
            return spc_example(dotted_module, member)
        except KeyError:
            pass  # member added after the curated SPC table; use generic sample
    return generic_example(dotted_module, member)


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
    member_label = "Class" if member.kind == "class" else "Function"
    intro = (
        ".. raw:: html\n\n"
        f'   <div class="spc-api-hero"><span>{member_label}</span><p>{dotted_module}</p></div>\n\n'
    )
    example = example_for(dotted_module, member)
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
        f"{gallery_for(dotted_module, member)}"
    )
    path.write_text(content, encoding="utf-8")
    return path.relative_to(OUTPUT_ROOT).with_suffix("").as_posix()


def write_module_page(path: Path) -> None:
    """Write a submodule index linking to one page per public member."""
    dotted_name = module_name(path)
    members = public_members(path)
    lines = [heading(f"{dotted_name} module")]
    parts = dotted_name.split(".")
    if len(parts) >= 2:
        pkg, leaf = parts[1], parts[-1]
        if dotted_name.startswith("dataviz.spc."):
            summary = SPC_MODULE_SUMMARIES.get(
                leaf, "Statistical process control tools and visualizations."
            )
        else:
            summary = PACKAGE_SUMMARIES.get(
                pkg, "Tools and visualizations from the DataViz package."
            )
        toolkit = MODULE_TOOLKITS.get(pkg, "DataViz toolkit")
        lines.append(
            "\n.. raw:: html\n\n"
            f'   <div class="spc-module-hero"><span>{toolkit}</span><h2>{leaf.replace("_", " ").title()}</h2><p>{summary}</p></div>\n'
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
            [f"\n{heading(title, '-')}", "\n.. toctree::\n   :maxdepth: 1\n\n"]
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


def verify_examples(only_pkg: str | None = None) -> int:
    """Execute every generated Complete example; return the failure count."""
    import traceback

    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import plotly.graph_objects as go

    go.Figure.show = lambda self, *args, **kwargs: None  # headless

    failures: list[tuple[str, str]] = []
    total = 0
    for path in sorted(PACKAGE_ROOT.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        dotted = module_name(path)
        if only_pkg and not dotted.startswith(f"dataviz.{only_pkg}."):
            continue
        for member in public_members(path):
            total += 1
            code = example_for(dotted, member)
            tag = f"{dotted}.{member.name}"
            try:
                exec(compile(code, tag, "exec"), {})  # noqa: S102
            except Exception:
                failures.append((tag, traceback.format_exc(limit=2)))
            finally:
                plt.close("all")

    print(f"executed: {total}, failed: {len(failures)}")
    for tag, tb in failures:
        last = tb.strip().splitlines()[-1]
        print(f"FAIL {tag}: {last}")
    return len(failures)


def main() -> int:
    """Generate API pages, or execute their Complete examples with --verify."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify",
        action="store_true",
        help="execute every generated Complete example instead of writing pages",
    )
    parser.add_argument("--pkg", help="verify only one subpackage, e.g. spc")
    args = parser.parse_args()
    if args.verify:
        return 1 if verify_examples(args.pkg) else 0
    generate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
