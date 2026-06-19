#-*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..')) # Apbackground a la raíz de tu paquete

# Project information
project = 'Data-Viz'
copyright = '2026, Aned Esquerra Arguelles' # Update year/name as you prefer
author = 'Aned Esquerra Arguelles'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',  # Extrae docstrings automáticamente
    'sphinx.ext.napoleon', # Soporta formatos Google/NumPy
]
html_theme = 'sphinx_rtd_theme' # El tema clásico azul/gris de Mlxtend
