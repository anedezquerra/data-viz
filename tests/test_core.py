"""Tests for dataviz package - static and interactive versions."""

import pytest
import numpy as np
import pandas as pd
import dataviz as dv


class TestUnivariateStatic:
    """Tests for static (matplotlib) univariate visualization functions."""
    
    def test_histogram_static(self):
        """Test static histogram creation."""
        s = pd.Series([1, 2, 3, 4, 5])
        ax = dv.histogram_static(s, bins=10)
        assert ax is not None
    
    def test_density_static(self):
        """Test static density plot creation."""
        s = pd.Series(np.random.randn(100))
        ax = dv.density_static(s)
        assert ax is not None


class TestUnivariateInteractive:
    """Tests for interactive (plotly) univariate visualization functions."""
    
    def test_histogram_interactive(self):
        """Test interactive histogram creation."""
        s = pd.Series([1, 2, 3, 4, 5])
        fig = dv.histogram_interactive(s, bins=10)
        assert fig is not None
    
    def test_density_interactive(self):
        """Test interactive density plot creation."""
        s = pd.Series(np.random.randn(100))
        fig = dv.density_interactive(s)
        assert fig is not None


class TestBivariateStatic:
    """Tests for static bivariate visualization functions."""
    
    def test_scatter_plot_static(self):
        """Test static scatter plot creation."""
        x = pd.Series([1, 2, 3, 4, 5], name='X')
        y = pd.Series([2, 4, 6, 8, 10], name='Y')
        ax = dv.scatter_plot_static(x, y)
        assert ax is not None
    
    def test_line_plot_static(self):
        """Test static line plot creation."""
        x = pd.Series([1, 2, 3, 4, 5])
        y = pd.Series([2, 4, 6, 8, 10])
        ax = dv.line_plot_static(x, y)
        assert ax is not None


class TestBivariateInteractive:
    """Tests for interactive bivariate visualization functions."""
    
    def test_scatter_plot_interactive(self):
        """Test interactive scatter plot creation."""
        x = pd.Series([1, 2, 3, 4, 5], name='X')
        y = pd.Series([2, 4, 6, 8, 10], name='Y')
        fig = dv.scatter_plot_interactive(x, y)
        assert fig is not None
    
    def test_line_plot_interactive(self):
        """Test interactive line plot creation."""
        x = pd.Series([1, 2, 3, 4, 5])
        y = pd.Series([2, 4, 6, 8, 10])
        fig = dv.line_plot_interactive(x, y)
        assert fig is not None


class TestEDAStatic:
    """Tests for static EDA visualization functions."""
    
    def test_missing_data_plot_static(self):
        """Test static missing data plot."""
        df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [1, None, 3, 4, 5]
        })
        ax = dv.missing_data_plot_static(df)
        assert ax is not None
    
    def test_class_distribution_static(self):
        """Test static class distribution plot."""
        s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])
        ax = dv.class_distribution_static(s)
        assert ax is not None


class TestEDAInteractive:
    """Tests for interactive EDA visualization functions."""
    
    def test_missing_data_plot_interactive(self):
        """Test interactive missing data plot."""
        df = pd.DataFrame({
            'A': [1, 2, None, 4, 5],
            'B': [1, None, 3, 4, 5]
        })
        fig = dv.missing_data_plot_interactive(df)
        assert fig is not None
    
    def test_class_distribution_interactive(self):
        """Test interactive class distribution plot."""
        s = pd.Series(['A', 'B', 'A', 'C', 'B', 'A'])
        fig = dv.class_distribution_interactive(s)
        assert fig is not None


class TestRegressionStatic:
    """Tests for static regression visualization functions."""
    
    def test_residual_plot_static(self):
        """Test static residual plot."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1.1, 2.1, 2.9, 4.1, 4.9])
        ax = dv.residual_plot_static(y_true, y_pred)
        assert ax is not None
    
    def test_prediction_plot_static(self):
        """Test static prediction plot."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1.1, 2.1, 2.9, 4.1, 4.9])
        ax = dv.prediction_plot_static(y_true, y_pred)
        assert ax is not None


class TestRegressionInteractive:
    """Tests for interactive regression visualization functions."""
    
    def test_residual_plot_interactive(self):
        """Test interactive residual plot."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1.1, 2.1, 2.9, 4.1, 4.9])
        fig = dv.residual_plot_interactive(y_true, y_pred)
        assert fig is not None
    
    def test_prediction_plot_interactive(self):
        """Test interactive prediction plot."""
        y_true = np.array([1, 2, 3, 4, 5])
        y_pred = np.array([1.1, 2.1, 2.9, 4.1, 4.9])
        fig = dv.prediction_plot_interactive(y_true, y_pred)
        assert fig is not None


class TestClassificationStatic:
    """Tests for static classification visualization functions."""
    
    def test_confusion_matrix_plot_static(self):
        """Test static confusion matrix plot."""
        cm = np.array([[85, 15], [10, 90]])
        ax = dv.confusion_matrix_plot_static(cm, labels=['Negative', 'Positive'])
        assert ax is not None
    
    def test_roc_curve_static(self):
        """Test static ROC curve plot."""
        fpr = np.array([0, 0.1, 0.5, 1])
        tpr = np.array([0, 0.7, 0.9, 1])
        ax = dv.roc_curve_static(fpr, tpr, auc=0.85)
        assert ax is not None


class TestClassificationInteractive:
    """Tests for interactive classification visualization functions."""
    
    def test_confusion_matrix_plot_interactive(self):
        """Test interactive confusion matrix plot."""
        cm = np.array([[85, 15], [10, 90]])
        fig = dv.confusion_matrix_plot_interactive(cm, labels=['Negative', 'Positive'])
        assert fig is not None
    
    def test_roc_curve_interactive(self):
        """Test interactive ROC curve plot."""
        fpr = np.array([0, 0.1, 0.5, 1])
        tpr = np.array([0, 0.7, 0.9, 1])
        fig = dv.roc_curve_interactive(fpr, tpr, auc=0.85)
        assert fig is not None


class TestSPC:
    """Tests for statistical process control charts."""
    
    def test_control_chart_static(self):
        """Test static control chart creation."""
        data = np.array([1, 2, 3, 2, 3, 4, 3, 2, 1, 2])
        ax = dv.spc.control_chart_static(data)
        assert ax is not None
    
    def test_control_chart_interactive(self):
        """Test interactive control chart creation."""
        data = np.array([1, 2, 3, 2, 3, 4, 3, 2, 1, 2])
        fig = dv.spc.control_chart_interactive(data)
        assert fig is not None


class TestXAI:
    """Tests for XAI visualization functions."""
    
    def test_feature_importance_static(self):
        """Test static feature importance plot."""
        importances = pd.Series(
            [0.3, 0.25, 0.2, 0.15, 0.1],
            index=['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E']
        )
        ax = dv.xai.feature_importance_static(importances, top_n=3)
        assert ax is not None
    
    def test_feature_importance_interactive(self):
        """Test interactive feature importance plot."""
        importances = pd.Series(
            [0.3, 0.25, 0.2, 0.15, 0.1],
            index=['Feature A', 'Feature B', 'Feature C', 'Feature D', 'Feature E']
        )
        fig = dv.xai.feature_importance_interactive(importances, top_n=3)
        assert fig is not None
