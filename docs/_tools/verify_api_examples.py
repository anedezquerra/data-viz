"""Execute every generated API "Complete example" and report failures.

Windows/POSIX portable. Run from the repository root:

    python docs/_tools/verify_api_examples.py
"""

from __future__ import annotations

import sys
import traceback
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from generate_api import example_for, module_name, public_members  # noqa: E402

PACKAGE_ROOT = Path(__file__).resolve().parents[2] / "dataviz"


def main() -> int:
    import plotly.graph_objects as go

    go.Figure.show = lambda self, *args, **kwargs: None  # headless

    only_pkg = None
    if "--pkg" in sys.argv:
        only_pkg = sys.argv[sys.argv.index("--pkg") + 1]

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
                plt.close("all")
            except Exception:
                failures.append((tag, traceback.format_exc(limit=2)))
                plt.close("all")

    print(f"executed: {total}, failed: {len(failures)}")
    for tag, tb in failures:
        last = tb.strip().splitlines()[-1]
        print(f"FAIL {tag}: {last}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
