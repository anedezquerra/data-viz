"""Generate a compact gallery of univariate examples."""

import numpy as np
import pandas as pd

import dataviz as dv


def main() -> None:
    """Create representative univariate figures.

    Args:
        None: This script uses generated example data.

    Returns:
        None: Figures are created in memory for interactive exploration.

    Raises:
        ImportError: If optional plotting dependencies are not installed.
        ValueError: If generated example data is invalid.

    Examples:
        ```bash
        python examples/univariate_gallery.py
        ```

    Notes:
        The script intentionally avoids writing image files so it can run in local notebooks or shells.
    """
    rng = np.random.default_rng(42)
    numeric = pd.Series(rng.normal(loc=10, scale=2, size=200), name="Process Value")
    categories = pd.Series(rng.choice(["Low", "Medium", "High"], size=120), name="Rating")
    timestamps = pd.date_range("2026-01-01", periods=80, freq="D")
    text = pd.Series(["red blue", "red green", "blue"] * 20, name="Tags")
    weights = rng.uniform(0.5, 2.0, size=len(numeric))

    dv.histogram(numeric)
    dv.univariate_analysis_dashboard_interactive(numeric)
    dv.weighted_ecdf_plot_interactive(numeric, weights)
    dv.ordinal_bar_interactive(categories, order=["Low", "Medium", "High"])
    dv.event_frequency_plot_interactive(timestamps, freq="W")
    dv.top_terms_bar_interactive(text, top_n=5)


if __name__ == "__main__":
    main()

