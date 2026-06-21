"""Lint generated documentation for redundant 'package' wording.

Fails (non-zero exit) when the auto-generated or templated docs reintroduce
boilerplate patterns we have deliberately removed, e.g.:

* ``(this package)`` in example requirements blocks (one mention per file is
  considered redundant — the dependency line directly under it already names
  ``dataviz``).
* ``<dotted.name> package`` as a Sphinx H1 in auto-generated API pages, where
  the dotted name alone is sufficient.
* Repeated standalone occurrences of the bare word ``package`` inside a
  single generated file beyond a low threshold.

Run from the repo root::

    python docs/_tools/check_package_wording.py

Used as a CI gate in ``.github/workflows/docs.yml``. Extend ``FORBIDDEN``
or ``MAX_BARE_OCCURRENCES`` as new generator templates are added.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCS_SOURCE = ROOT / "docs" / "source"

# (glob, regex, human description)
FORBIDDEN: list[tuple[str, re.Pattern[str], str]] = [
    (
        "examples/*.rst",
        re.compile(r"\(this package\)", re.IGNORECASE),
        "example pages must not contain '(this package)' — drop it from the "
        "template in docs/_tools/generate_example_pages.py",
    ),
    (
        "api/*.rst",
        re.compile(r"^[A-Za-z0-9_.]+\s+package\s*$", re.MULTILINE),
        "API page headings must be the dotted name only, not "
        "'<name> package' — see docs/generate_api.py:write_package_page",
    ),
]

# Hard cap on the number of bare 'package' tokens per generated doc file.
# Headings and requirements blocks are the noisy offenders; >2 is suspicious.
MAX_BARE_OCCURRENCES = 2
BARE_GLOBS = ("examples/*.rst", "api/*.rst")
BARE_PATTERN = re.compile(r"\bpackage(s)?\b", re.IGNORECASE)


def main() -> int:
    failures: list[str] = []

    for rel_glob, regex, message in FORBIDDEN:
        for path in sorted(DOCS_SOURCE.glob(rel_glob)):
            text = path.read_text(encoding="utf-8")
            for match in regex.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                failures.append(
                    f"{path.relative_to(ROOT)}:{line_no}: {message}"
                )

    for rel_glob in BARE_GLOBS:
        for path in sorted(DOCS_SOURCE.glob(rel_glob)):
            text = path.read_text(encoding="utf-8")
            hits = BARE_PATTERN.findall(text)
            if len(hits) > MAX_BARE_OCCURRENCES:
                failures.append(
                    f"{path.relative_to(ROOT)}: {len(hits)} occurrences of "
                    f"'package' (max {MAX_BARE_OCCURRENCES}); reduce in the "
                    "generator template before regenerating"
                )

    if failures:
        print("Redundant 'package' wording detected:")
        for line in failures:
            print(f"  - {line}")
        print(
            "\nFix the generator templates "
            "(docs/_tools/generate_example_pages.py, docs/generate_api.py) "
            "and regenerate the pages, then re-run this check."
        )
        return 1

    print("OK — no redundant 'package' wording in generated docs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
