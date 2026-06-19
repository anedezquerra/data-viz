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

# Add these theme options to enable deep, expandable sidebar navigation
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # Keeps the navigation expansion synced dynamically 
    # with the current active page context.
    'sticky_navigation': True,
    
    # Setting this to True ensures items that are not relevant 
    # to the current active page automatically collapse.
    'collapse_navigation': True,
    
    # Controls how deep the sidebar tree expands by default.
    # Adjust this integer value to restrict or allow nesting depths.
    'navigation_depth': 4,
}

