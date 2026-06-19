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
    path.write_text(
        f"{heading(qualified_name)}\n"
        f".. currentmodule:: {dotted_module}\n\n"
        f".. {directive}:: {member.name}{options}\n",
        encoding="utf-8",
    )
    return path.relative_to(OUTPUT_ROOT).with_suffix("").as_posix()


def write_module_page(path: Path) -> None:
    """Write a submodule index linking to one page per public member."""
    dotted_name = module_name(path)
    members = public_members(path)
    lines = [heading(f"{dotted_name} module"), f"\n.. automodule:: {dotted_name}\n"]
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
    lines = [heading(f"{dotted_name} package")]
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
