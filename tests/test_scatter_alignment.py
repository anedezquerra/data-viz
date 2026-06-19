"""Regression tests for scatter metadata and missing-value alignment."""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest

from dataviz.bivariate.scatter import (
    scatter_plot_interactive,
    scatter_plot_static,
)
from dataviz.utils.validation import resolve_xy_data

SCATTER_CONSTRUCTORS = [scatter_plot_static, scatter_plot_interactive]


@pytest.fixture
def scatter_frame() -> pd.DataFrame:
    """Return paired data with a missing observation in the middle."""
    return pd.DataFrame(
        {
            "x": [1.0, None, 3.0],
            "y": [10.0, 20.0, 30.0],
            "group": ["A", "B", "C"],
            "label": ["first", "removed", "third"],
        }
    )


def test_static_scatter_aligns_hue_and_annotations_after_na_drop(
    scatter_frame: pd.DataFrame,
) -> None:
    """Categorical hue and annotations follow the retained source rows."""
    ax = scatter_plot_static(
        "x",
        "y",
        data=scatter_frame,
        hue="group",
        annotate_points=scatter_frame["label"],
    )

    assert [text.get_text() for text in ax.texts] == ["first", "third"]
    assert ax.get_legend_handles_labels()[1] == ["A", "C"]
    plt.close(ax.figure)


def test_interactive_scatter_aligns_group_text_after_na_drop(
    scatter_frame: pd.DataFrame,
) -> None:
    """Each Plotly group receives only text from its retained observations."""
    fig = scatter_plot_interactive(
        "x",
        "y",
        data=scatter_frame,
        hue="group",
        text=scatter_frame["label"],
    )

    traces = {trace.name: trace for trace in fig.data}
    assert list(traces) == ["A", "C"]
    assert list(traces["A"].x) == [1.0]
    assert list(traces["A"].text) == ["first"]
    assert list(traces["C"].x) == [3.0]
    assert list(traces["C"].text) == ["third"]


def test_static_scatter_aligns_numeric_hue_after_na_drop() -> None:
    """Continuous marker colors use the same row mask as paired values."""
    ax = scatter_plot_static(
        [1.0, None, 3.0],
        [10.0, 20.0, 30.0],
        hue=[100.0, 200.0, 300.0],
    )

    assert ax.collections[0].get_array().tolist() == [100.0, 300.0]
    plt.close(ax.figure)


def test_resolve_xy_data_pairs_series_by_position() -> None:
    """Differently indexed Series remain positionally paired."""
    x_values, y_values = resolve_xy_data(
        pd.Series([1.0, np.nan, 3.0], index=[10, 11, 12]),
        pd.Series([10.0, 20.0, 30.0], index=[20, 21, 22]),
    )

    assert x_values.tolist() == [1.0, 3.0]
    assert y_values.tolist() == [10.0, 30.0]


@pytest.mark.parametrize("constructor", SCATTER_CONSTRUCTORS)
def test_scatter_rejects_metadata_with_wrong_length(constructor) -> None:
    """Metadata length mismatches fail rather than being silently truncated."""
    with pytest.raises(ValueError, match="Input lengths must match"):
        constructor([1, 2, 3], [4, 5, 6], hue=["A", "B"])
