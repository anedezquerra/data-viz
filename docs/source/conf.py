# Configuration file for the Sphinx documentation builder.
# For the full list of built-in settings, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
# Path setup: Climb up two levels (out of source/ and docs/) to find your code root
sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
project = 'Data-Viz'
copyright = '2026, Aned Esquerra Arguelles'
author = 'Aned Esquerra Arguelles'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',      # Automatically parses docstrings out of your files
    'sphinx.ext.napoleon',     # Adds parsing support for Google/NumPy-style docstrings
    'sphinx.ext.viewcode',     # Adds explicit source links directly next to your HTML API pages
    'sphinx.ext.githubpages',  # Prevents Jekyll processing conflicts on GitHub deployments
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
