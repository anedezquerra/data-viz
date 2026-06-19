"""Sphinx configuration for the DataViz documentation site."""

from __future__ import annotations

import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", str(ROOT / "docs" / "build" / ".matplotlib"))


def project_version() -> str:
    """Read the package version without importing optional plotting backends."""
    pyproject = ROOT / "pyproject.toml"
    try:
        import tomllib

        with pyproject.open("rb") as stream:
            return str(tomllib.load(stream)["project"]["version"])
    except (ImportError, KeyError, OSError):
        return "0.1.0"


project = "DataViz"
author = "Aned Esquerra-Arguelles"
copyright = "2026, Aned Esquerra-Arguelles"
version = project_version()
release = version

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.githubpages",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
]

copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = False
copybutton_remove_prompts = True

autodoc_class_signature = "separated"
autodoc_default_options = {
    "show-inheritance": True,
}
autodoc_member_order = "bysource"
autodoc_typehints = "description"
autodoc_typehints_format = "short"

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_param = True
napoleon_use_rtype = True

# A docs-only environment can opt into mocks. The GitHub workflow installs the
# package and its runtime dependencies, so published API signatures use real
# imports.
if os.getenv("SPHINX_MOCK_IMPORTS") == "1":
    autodoc_mock_imports = [
        "matplotlib",
        "numpy",
        "pandas",
        "plotly",
        "scipy",
        "seaborn",
    ]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
source_suffix = {".rst": "restructuredtext"}
master_doc = "index"
language = "en"

html_theme = "sphinx_rtd_theme"
html_title = f"DataViz {release} documentation"
html_short_title = "DataViz"
html_baseurl = "https://anedezquerra.github.io/data-viz/"
html_logo = "_static/dataviz-mark.svg"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = True
html_show_sphinx = True
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "prev_next_buttons_location": "both",
    "sticky_navigation": True,
    "style_external_links": True,
    "style_nav_header_background": "#174f6f",
}
html_context = {
    "display_github": True,
    "github_user": "anedezquerra",
    "github_repo": "data-viz",
    "github_version": "main",
    "conf_py_path": "/docs/source/",
}

linkcheck_ignore = [
    r"https://github.com/anedezquerra/data-viz/(actions|settings)(/.*)?",
]
