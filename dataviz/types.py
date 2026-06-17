"""Shared type aliases for public plotting APIs."""

from typing import Any, Mapping, Optional, Sequence, Tuple, Union

import matplotlib.axes as mpl_axes
import matplotlib.figure as mpl_figure
import numpy as np
import pandas as pd
import plotly.graph_objects as go

ArrayLike = Union[Sequence[float], np.ndarray, pd.Series]
MatrixLike = Union[Sequence[Sequence[float]], np.ndarray, pd.DataFrame]
SeriesLike = Union[pd.Series, Sequence[float], np.ndarray]
FrameLike = Union[pd.DataFrame, np.ndarray, Sequence[Sequence[float]]]
Labels = Sequence[str]
FigureSize = Tuple[int, int]
PlotKwargs = Mapping[str, Any]
MatplotlibAxes = mpl_axes.Axes
MatplotlibFigure = mpl_figure.Figure
PlotlyFigure = go.Figure
MaybeLabels = Optional[Labels]

__all__ = [
    "ArrayLike",
    "MatrixLike",
    "SeriesLike",
    "FrameLike",
    "Labels",
    "FigureSize",
    "PlotKwargs",
    "MatplotlibAxes",
    "MatplotlibFigure",
    "PlotlyFigure",
    "MaybeLabels",
]
