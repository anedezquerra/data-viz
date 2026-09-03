"""Render every API "Complete example" and save its figure as a PNG.

Images land under ``docs/source/_static/api/<module>/<member>.png`` and are
picked up by ``docs/generate_api.py`` on the next run, so generate images
before regenerating member pages. Run from the repository root:

    python docs/_tools/generate_api_images.py [--pkg <subpackage>]
"""

from __future__ import annotations

import shutil
import sys
import traceback
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generate_api import example_for, module_name, public_members  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PACKAGE_ROOT = ROOT / "dataviz"
IMAGE_ROOT = ROOT / "docs" / "source" / "_static" / "api"


def image_path(dotted: str, member_name: str) -> Path:
    """Return the PNG path mirroring the generated member-page layout."""
    return IMAGE_ROOT / Path(*dotted.split(".")) / f"{member_name}.png"


def render(dotted: str, member_name: str, code: str) -> bool:
    """Execute *code* and save the produced figure, if any."""
    import plotly.graph_objects as go

    plotly_figures: list[go.Figure] = []
    go.Figure.show = lambda self, *args, **kwargs: plotly_figures.append(self)
    try:
        exec(compile(code, f"{dotted}.{member_name}", "exec"), {})  # noqa: S102
        path = image_path(dotted, member_name)
        if plotly_figures:
            path.parent.mkdir(parents=True, exist_ok=True)
            plotly_figures[-1].write_image(
                str(path), width=960, height=540, scale=2
            )
            return True
        if plt.get_fignums():
            path.parent.mkdir(parents=True, exist_ok=True)
            plt.figure(plt.get_fignums()[0]).savefig(
                str(path), dpi=110, bbox_inches="tight"
            )
            return True
        return False
    finally:
        plt.close("all")


def main() -> int:
    only_pkg = None
    if "--pkg" in sys.argv:
        only_pkg = sys.argv[sys.argv.index("--pkg") + 1]

    if IMAGE_ROOT.exists():
        shutil.rmtree(IMAGE_ROOT)
    IMAGE_ROOT.mkdir(parents=True)

    rendered = skipped = 0
    failures: list[tuple[str, str]] = []
    for path in sorted(PACKAGE_ROOT.rglob("*.py")):
        if path.name == "__init__.py":
            continue
        dotted = module_name(path)
        if only_pkg and not dotted.startswith(f"dataviz.{only_pkg}."):
            continue
        for member in public_members(path):
            tag = f"{dotted}.{member.name}"
            try:
                if render(dotted, member.name, example_for(dotted, member)):
                    rendered += 1
                else:
                    skipped += 1
            except Exception:
                failures.append((tag, traceback.format_exc(limit=2)))

    print(f"rendered: {rendered}, no figure: {skipped}, failed: {len(failures)}")
    for tag, tb in failures:
        last = tb.strip().splitlines()[-1]
        print(f"FAIL {tag}: {last}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
