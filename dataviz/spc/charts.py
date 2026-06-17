"""Compatibility wrappers for Statistical Process Control charts."""

from typing import Any

from ..types import MatplotlibAxes
from .control import control_chart_static
from .x_range import x_range_chart_static


def control_chart(*args: Any, **kwargs: Any) -> MatplotlibAxes:
    """Create a static statistical process control chart.

    Args:
        *args (Any): Positional arguments forwarded to ``control_chart_static``.
        **kwargs (Any): Keyword arguments forwarded to ``control_chart_static``.

    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the control chart.

    Raises:
        TypeError: If inputs cannot be converted to numeric observations.
        ValueError: If inputs are empty or options are invalid.

    Examples:
        ```python
        ax = control_chart(data)
        ```

    Notes:
        This wrapper preserves the legacy ``dataviz.spc.charts`` API.
    """
    return control_chart_static(*args, **kwargs)


def x_range_chart(*args: Any, **kwargs: Any) -> MatplotlibAxes:
    """Create a static X-range chart for individual values and range monitoring.

    Args:
        *args (Any): Positional arguments forwarded to ``x_range_chart_static``.
        **kwargs (Any): Keyword arguments forwarded to ``x_range_chart_static``.

    Returns:
        matplotlib.axes.Axes: Configured matplotlib axes containing the X-range chart.

    Raises:
        TypeError: If inputs cannot be converted to numeric observations.
        ValueError: If inputs are empty or options are invalid.

    Examples:
        ```python
        ax = x_range_chart(data)
        ```

    Notes:
        This wrapper preserves the legacy ``dataviz.spc.charts`` API.
    """
    return x_range_chart_static(*args, **kwargs)
