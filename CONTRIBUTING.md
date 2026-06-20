# Contributing to DataViz

Thank you for considering a contribution. This document explains how to set up
a development environment, run the quality gates locally, and prepare a pull
request that will sail through review.

## Quick start

```bash
git clone https://github.com/anedezquerra/data-viz.git
cd data-viz
python -m venv .venv
source .venv/bin/activate            # Windows: .\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev,docs]"
```

## Quality gates

Run these locally before opening a pull request. The same commands run in CI.

```bash
black --check dataviz tests
flake8 dataviz tests
mypy dataviz
pytest --cov=dataviz --cov-report=term-missing
```

To rebuild the documentation site:

```bash
python -m sphinx -b html -W --keep-going docs/source docs/build/html
```

## Branch naming

Use a type prefix followed by a kebab-case description, with no personal names
or initials:

* `feat/<short-description>` — new functionality.
* `fix/<short-description>` — bug fixes.
* `docs/<short-description>` — documentation only.
* `chore/<short-description>` — tooling, CI, packaging.
* `refactor/<short-description>` — internal restructuring.
* `test/<short-description>` — test additions or fixes.

Include an issue identifier when one exists, e.g. `feat/123-spc-cusum-chart`.

## Commit messages

Use Conventional Commits:

```
<type>(<scope>): <subject>

<optional body explaining what and why, not how>
```

* Imperative mood, lowercase subject, no trailing period.
* Subject line capped at 72 characters.
* Reserve longer rationale and migration steps for `CHANGELOG.md` and the
  README, not the commit body.

## Pull requests

* Keep PRs focused on a single concern.
* Add or update tests for any behavior change.
* Update the `CHANGELOG.md` under the `Unreleased` section with a single
  one-line entry of the form `- <type>: <what changed>`.
* Update relevant documentation in `docs/source/` and the API docstrings.
* Ensure the Sphinx build runs warning-free under `-W --keep-going`.

## Adding a new chart

1. Place the new function in the appropriate submodule
   (`dataviz/<module>/<chart_family>.py`).
2. Implement both a `*_static` (returns `matplotlib.axes.Axes`) and a
   `*_interactive` (returns `plotly.graph_objects.Figure`) variant with
   identical parameters.
3. Re-export both variants from the module's `__init__.py` and add a
   convenience alias (`name = name_static`) when unambiguous.
4. Add unit tests for both variants under `tests/<module>/`.
5. If the chart is a top-level entry point, re-export it from
   `dataviz/__init__.py`.

## Code of conduct

Participation in this project is governed by the
[Code of Conduct](CODE_OF_CONDUCT.md).
