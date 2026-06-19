"""Tests for package build metadata and backend compatibility."""

from pathlib import Path


def test_setuptools_supports_pep_621_project_metadata() -> None:
    """The minimum build backend must understand the ``[project]`` table."""
    pyproject = Path("pyproject.toml").read_text()
    build_system = pyproject.split("[project]", maxsplit=1)[0]

    assert "setuptools>=61" in build_system
