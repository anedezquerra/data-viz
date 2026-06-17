"""Utility functions for DataViz package."""

from .helpers import setup_plot, apply_theme
from .validation import (
    add_plotly_reference_lines,
    add_reference_lines,
    numeric_dataframe,
    resolve_series,
    resolve_xy_data,
    validate_alpha,
    validate_equal_length,
    validate_positive_int,
)

__all__ = [
    "setup_plot",
    "apply_theme",
    "add_plotly_reference_lines",
    "add_reference_lines",
    "numeric_dataframe",
    "resolve_series",
    "resolve_xy_data",
    "validate_alpha",
    "validate_equal_length",
    "validate_positive_int",
]
