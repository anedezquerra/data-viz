"""Shared pytest fixtures."""

import matplotlib
import pytest

matplotlib.use("Agg")


@pytest.fixture(autouse=True)
def _close_matplotlib_figures():
    """Close all matplotlib figures after each test to avoid state leakage."""
    yield
    import matplotlib.pyplot as plt

    plt.close("all")
