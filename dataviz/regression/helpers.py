"""Shared compute helpers for the regression sub-package.

Provides reusable, backend-agnostic numerical helpers used by the regression
chart functions: metric summaries, influence statistics, prediction-interval
construction, OLS coefficient tables, and autocorrelation utilities. Keeping
these in one place lets the chart modules stay focused on rendering.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

from ..types import ArrayLike, MatrixLike


def _as_array(x: ArrayLike) -> np.ndarray:
    if isinstance(x, pd.Series):
        return x.to_numpy()
    return np.asarray(x, dtype=float)


def _as_matrix(x: MatrixLike) -> np.ndarray:
    if isinstance(x, pd.DataFrame):
        return x.to_numpy(dtype=float)
    arr = np.asarray(x, dtype=float)
    if arr.ndim == 1:
        arr = arr.reshape(-1, 1)
    return arr


def _residuals(y_true: ArrayLike, y_pred: ArrayLike) -> np.ndarray:
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    if y_t.shape != y_p.shape:
        raise ValueError("y_true and y_pred must have the same shape.")
    return y_t - y_p


@dataclass(frozen=True)
class RegressionMetrics:
    """Summary metrics for a regression prediction."""

    n: int
    mae: float
    mse: float
    rmse: float
    medae: float
    mape: float
    smape: float
    r2: float
    adj_r2: Optional[float]
    explained_variance: float
    max_error: float

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)


def compute_regression_metrics(
    y_true: ArrayLike,
    y_pred: ArrayLike,
    n_features: Optional[int] = None,
    eps: float = 1e-12,
) -> RegressionMetrics:
    """Compute standard regression metrics without external dependencies.

    Args:
        y_true: Observed target values.
        y_pred: Predicted target values.
        n_features: Number of predictors used in the model. When supplied,
            an adjusted R² is returned alongside the unadjusted score.
        eps: Small value used to avoid divide-by-zero in MAPE / sMAPE.

    Returns:
        :class:`RegressionMetrics` with sample size and per-row error stats.
    """
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    if y_t.shape != y_p.shape:
        raise ValueError("y_true and y_pred must share the same shape.")
    if y_t.size == 0:
        raise ValueError("y_true is empty.")
    err = y_t - y_p
    abs_err = np.abs(err)
    sq_err = err ** 2
    mae = float(np.mean(abs_err))
    mse = float(np.mean(sq_err))
    rmse = float(np.sqrt(mse))
    medae = float(np.median(abs_err))
    denom_mape = np.maximum(np.abs(y_t), eps)
    mape = float(np.mean(abs_err / denom_mape) * 100.0)
    smape = float(
        np.mean(2.0 * abs_err / np.maximum(np.abs(y_t) + np.abs(y_p), eps)) * 100.0
    )
    ss_res = float(np.sum(sq_err))
    ss_tot = float(np.sum((y_t - np.mean(y_t)) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    adj = None
    if n_features is not None and y_t.size - n_features - 1 > 0 and not np.isnan(r2):
        adj = 1.0 - (1.0 - r2) * (y_t.size - 1) / (y_t.size - n_features - 1)
    var_y = float(np.var(y_t))
    explained = 1.0 - float(np.var(err)) / var_y if var_y > 0 else float("nan")
    return RegressionMetrics(
        n=int(y_t.size),
        mae=mae,
        mse=mse,
        rmse=rmse,
        medae=medae,
        mape=mape,
        smape=smape,
        r2=r2,
        adj_r2=adj,
        explained_variance=explained,
        max_error=float(np.max(abs_err)),
    )


@dataclass(frozen=True)
class InfluenceStatistics:
    """Per-observation diagnostics for an OLS-style regression fit."""

    leverage: np.ndarray
    residuals: np.ndarray
    standardized_residuals: np.ndarray
    studentized_residuals: np.ndarray
    cooks_distance: np.ndarray
    dffits: np.ndarray
    dfbetas: np.ndarray
    sigma_hat: float
    n_features: int


def influence_statistics(
    X: MatrixLike,
    y_true: ArrayLike,
    y_pred: ArrayLike,
    include_intercept: bool = True,
) -> InfluenceStatistics:
    """Compute leverage, Cook's distance, DFFITS, and DFBETAS for OLS.

    The design matrix ``X`` is augmented with an intercept column when
    ``include_intercept`` is ``True``. The implementation uses the hat matrix
    ``H = X (XᵀX)⁻¹ Xᵀ`` so it works for any linear-in-parameters model whose
    fitted values can be expressed as ``ŷ = H y``. For non-OLS models the
    returned statistics remain useful descriptive diagnostics although the
    distributional assumptions no longer hold.
    """
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    y_p = _as_array(y_pred)
    if include_intercept:
        X_mat = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
    n, p = X_mat.shape
    if n <= p:
        raise ValueError("Need more observations than parameters for influence stats.")
    xtx_inv = np.linalg.pinv(X_mat.T @ X_mat)
    hat = X_mat @ xtx_inv @ X_mat.T
    leverage = np.clip(np.diag(hat), 0.0, 1.0)
    resid = y_t - y_p
    df_resid = max(n - p, 1)
    sigma2 = float(np.sum(resid ** 2) / df_resid)
    sigma = float(np.sqrt(sigma2)) if sigma2 > 0 else 0.0
    denom_std = np.sqrt(np.maximum(sigma2 * (1.0 - leverage), 1e-12))
    std_resid = resid / denom_std
    stud_resid = std_resid * np.sqrt(
        np.maximum((df_resid - 1) / np.maximum(df_resid - std_resid ** 2, 1e-12), 0.0)
    )
    cooks = (std_resid ** 2 / p) * (leverage / np.maximum(1.0 - leverage, 1e-12))
    dffits = stud_resid * np.sqrt(leverage / np.maximum(1.0 - leverage, 1e-12))
    beta = xtx_inv @ X_mat.T @ y_t
    resid_internal = y_t - X_mat @ beta
    se_beta = np.sqrt(np.maximum(np.diag(xtx_inv) * sigma2, 0.0))
    dfbetas = np.zeros_like(X_mat)
    for j in range(p):
        scale = se_beta[j] if se_beta[j] > 0 else 1.0
        dfbetas[:, j] = (
            xtx_inv[j] @ X_mat.T * resid_internal / np.maximum(1.0 - leverage, 1e-12)
        ) / scale
    return InfluenceStatistics(
        leverage=leverage,
        residuals=resid,
        standardized_residuals=std_resid,
        studentized_residuals=stud_resid,
        cooks_distance=cooks,
        dffits=dffits,
        dfbetas=dfbetas,
        sigma_hat=sigma,
        n_features=p - (1 if include_intercept else 0),
    )


def prediction_intervals(
    y_pred: ArrayLike,
    residuals: ArrayLike,
    confidence: float = 0.95,
    method: str = "empirical",
) -> Tuple[np.ndarray, np.ndarray]:
    """Build symmetric prediction intervals around ``y_pred``.

    Supported methods:

    * ``"empirical"`` - use empirical quantiles of the residual distribution
      (no normality assumption).
    * ``"normal"`` - assume residuals are zero-mean normal with the sample
      standard deviation and use ±z·σ bounds.
    """
    if not 0.0 < confidence < 1.0:
        raise ValueError("confidence must be in (0, 1).")
    y_p = _as_array(y_pred)
    res = _as_array(residuals)
    alpha = 1.0 - confidence
    if method == "empirical":
        lo_q = float(np.quantile(res, alpha / 2))
        hi_q = float(np.quantile(res, 1.0 - alpha / 2))
        return y_p + lo_q, y_p + hi_q
    if method == "normal":
        sigma = float(np.std(res, ddof=1)) if res.size > 1 else 0.0
        from math import erf, sqrt
        # Inverse standard-normal CDF via Newton on erf (good enough for plot bands).
        def _ppf(p: float) -> float:
            # Beasley-Springer-Moro approximation.
            a = [-3.969683028665376e1, 2.209460984245205e2, -2.759285104469687e2,
                 1.383577518672690e2, -3.066479806614716e1, 2.506628277459239]
            b = [-5.447609879822406e1, 1.615858368580409e2, -1.556989798598866e2,
                 6.680131188771972e1, -1.328068155288572e1]
            c = [-7.784894002430293e-3, -3.223964580411365e-1, -2.400758277161838,
                 -2.549732539343734, 4.374664141464968, 2.938163982698783]
            d = [7.784695709041462e-3, 3.224671290700398e-1, 2.445134137142996,
                 3.754408661907416]
            plow = 0.02425
            phigh = 1 - plow
            if p < plow:
                q = sqrt(-2 * np.log(p))
                return (((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
                       ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
            if p <= phigh:
                q = p - 0.5
                r = q * q
                return (((((a[0]*r + a[1])*r + a[2])*r + a[3])*r + a[4])*r + a[5])*q / \
                       (((((b[0]*r + b[1])*r + b[2])*r + b[3])*r + b[4])*r + 1)
            q = sqrt(-2 * np.log(1 - p))
            return -(((((c[0]*q + c[1])*q + c[2])*q + c[3])*q + c[4])*q + c[5]) / \
                    ((((d[0]*q + d[1])*q + d[2])*q + d[3])*q + 1)
        z = _ppf(1.0 - alpha / 2)
        return y_p - z * sigma, y_p + z * sigma
    raise ValueError(f"Unknown prediction-interval method: {method!r}")


def coefficient_table(
    X: MatrixLike,
    y_true: ArrayLike,
    feature_names: Optional[Sequence[str]] = None,
    include_intercept: bool = True,
) -> pd.DataFrame:
    """Fit OLS and return a coefficient table with SE, t-stat and 95% CI."""
    X_mat = _as_matrix(X)
    y_t = _as_array(y_true)
    cols: List[str]
    if feature_names is None:
        cols = [f"x{i}" for i in range(X_mat.shape[1])]
    else:
        cols = list(feature_names)
        if len(cols) != X_mat.shape[1]:
            raise ValueError("feature_names length must match X columns.")
    if include_intercept:
        X_mat = np.column_stack([np.ones(X_mat.shape[0]), X_mat])
        cols = ["intercept", *cols]
    n, p = X_mat.shape
    xtx_inv = np.linalg.pinv(X_mat.T @ X_mat)
    beta = xtx_inv @ X_mat.T @ y_t
    resid = y_t - X_mat @ beta
    sigma2 = float(np.sum(resid ** 2) / max(n - p, 1))
    se = np.sqrt(np.maximum(np.diag(xtx_inv) * sigma2, 0.0))
    t_stat = np.divide(beta, np.where(se > 0, se, np.nan))
    ci_lo = beta - 1.96 * se
    ci_hi = beta + 1.96 * se
    return pd.DataFrame(
        {
            "feature": cols,
            "coef": beta,
            "std_err": se,
            "t": t_stat,
            "ci_low": ci_lo,
            "ci_high": ci_hi,
        }
    )


def autocorrelation(values: ArrayLike, max_lag: int = 20) -> np.ndarray:
    """Sample autocorrelation function up to ``max_lag`` (lag 0 included)."""
    x = _as_array(values)
    x = x - np.mean(x)
    denom = float(np.dot(x, x))
    if denom <= 0:
        return np.zeros(max_lag + 1)
    lags = np.arange(0, max_lag + 1)
    acf = np.array([float(np.dot(x[: x.size - k], x[k:])) / denom for k in lags])
    return acf


def partial_autocorrelation(values: ArrayLike, max_lag: int = 20) -> np.ndarray:
    """Partial autocorrelation function via Durbin-Levinson recursion."""
    r = autocorrelation(values, max_lag=max_lag)
    pacf = np.zeros(max_lag + 1)
    pacf[0] = 1.0
    phi = np.zeros((max_lag + 1, max_lag + 1))
    for k in range(1, max_lag + 1):
        if k == 1:
            phi[k, k] = r[1]
        else:
            num = r[k] - np.sum(phi[k - 1, 1:k] * r[1:k][::-1])
            den = 1.0 - np.sum(phi[k - 1, 1:k] * r[1:k])
            phi[k, k] = num / den if abs(den) > 1e-12 else 0.0
            for j in range(1, k):
                phi[k, j] = phi[k - 1, j] - phi[k, k] * phi[k - 1, k - j]
        pacf[k] = phi[k, k]
    return pacf


def runs_test_signs(residuals: ArrayLike) -> Tuple[int, int, int]:
    """Return (n_runs, n_positive, n_negative) for a residual sign sequence."""
    r = _as_array(residuals)
    signs = np.sign(r)
    signs = signs[signs != 0]
    if signs.size == 0:
        return 0, 0, 0
    runs = int(1 + np.sum(np.diff(signs) != 0))
    return runs, int(np.sum(signs > 0)), int(np.sum(signs < 0))


__all__ = [
    "RegressionMetrics",
    "InfluenceStatistics",
    "compute_regression_metrics",
    "influence_statistics",
    "prediction_intervals",
    "coefficient_table",
    "autocorrelation",
    "partial_autocorrelation",
    "runs_test_signs",
    "variance_inflation_factors",
    "breusch_pagan_statistic",
    "white_test_statistic",
    "ljung_box_statistic",
    "jarque_bera_statistic",
    "durbin_watson_statistic",
    "box_cox_loglikelihood",
    "yeo_johnson_loglikelihood",
    "conformal_quantile",
    "jackknife_plus_intervals",
]


# ---------------------------------------------------------------------------
# Diagnostic statistics used by goodness-of-fit / multicollinearity charts.
# ---------------------------------------------------------------------------

def variance_inflation_factors(X: MatrixLike, include_intercept: bool = True) -> np.ndarray:
    """Return one VIF per column of ``X`` using OLS regressions of each on the rest."""
    Xm = _as_matrix(X)
    n, p = Xm.shape
    vif = np.zeros(p)
    for j in range(p):
        others = np.delete(Xm, j, axis=1)
        Z = np.column_stack([np.ones(n), others]) if include_intercept else others
        beta = np.linalg.pinv(Z.T @ Z) @ Z.T @ Xm[:, j]
        pred = Z @ beta
        ss_res = float(np.sum((Xm[:, j] - pred) ** 2))
        ss_tot = float(np.sum((Xm[:, j] - Xm[:, j].mean()) ** 2))
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
        vif[j] = 1.0 / max(1.0 - r2, 1e-12)
    return vif


def breusch_pagan_statistic(X: MatrixLike, residuals: ArrayLike) -> Tuple[float, float]:
    """Return (LM statistic, p-value-like) for Breusch–Pagan heteroscedasticity test.

    The "p-value-like" output is ``1 - F_chi2(LM, df=p)`` evaluated with a
    Wilson–Hilferty cube-root approximation. Sufficient for diagnostic charts.
    """
    Xm = _as_matrix(X)
    r = _as_array(residuals)
    n = r.size
    sigma2 = float(np.mean(r ** 2))
    if sigma2 <= 0:
        return 0.0, 1.0
    g = r ** 2 / sigma2
    Z = np.column_stack([np.ones(n), Xm])
    beta = np.linalg.pinv(Z.T @ Z) @ Z.T @ g
    fitted = Z @ beta
    ss_reg = float(np.sum((fitted - g.mean()) ** 2))
    lm = 0.5 * ss_reg
    p = Z.shape[1] - 1
    return float(lm), _chi2_sf(lm, p)


def white_test_statistic(X: MatrixLike, residuals: ArrayLike) -> Tuple[float, float]:
    """White heteroscedasticity test using ``X``, ``X**2`` and cross-products."""
    Xm = _as_matrix(X)
    r = _as_array(residuals)
    n, p = Xm.shape
    feats = [np.ones(n), Xm, Xm ** 2]
    for i in range(p):
        for j in range(i + 1, p):
            feats.append((Xm[:, i] * Xm[:, j]).reshape(-1, 1))
    Z = np.column_stack(feats)
    g = r ** 2
    beta = np.linalg.pinv(Z.T @ Z) @ Z.T @ g
    fitted = Z @ beta
    ss_res = float(np.sum((g - fitted) ** 2))
    ss_tot = float(np.sum((g - g.mean()) ** 2))
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 0.0
    lm = n * r2
    df = Z.shape[1] - 1
    return float(lm), _chi2_sf(lm, df)


def ljung_box_statistic(residuals: ArrayLike, lags: int = 10) -> Tuple[float, float]:
    """Ljung–Box Q-statistic up to ``lags`` and its approximate p-value."""
    r = _as_array(residuals)
    n = r.size
    acf = autocorrelation(r, max_lag=lags)
    q = n * (n + 2) * np.sum(acf[1:] ** 2 / (n - np.arange(1, lags + 1)))
    return float(q), _chi2_sf(float(q), lags)


def jarque_bera_statistic(residuals: ArrayLike) -> Tuple[float, float]:
    """Jarque–Bera normality test statistic and approximate p-value."""
    r = _as_array(residuals)
    n = r.size
    if n < 2:
        return 0.0, 1.0
    m = r - r.mean()
    s2 = float(np.mean(m ** 2))
    if s2 <= 0:
        return 0.0, 1.0
    skew = float(np.mean(m ** 3) / s2 ** 1.5)
    kurt = float(np.mean(m ** 4) / s2 ** 2) - 3.0
    jb = n / 6.0 * (skew ** 2 + (kurt ** 2) / 4.0)
    return float(jb), _chi2_sf(float(jb), 2)


def durbin_watson_statistic(residuals: ArrayLike) -> float:
    """Durbin–Watson statistic for first-order residual autocorrelation."""
    r = _as_array(residuals)
    if r.size < 2:
        return 2.0
    diff = np.diff(r)
    return float(np.sum(diff ** 2) / max(np.sum(r ** 2), 1e-12))


def box_cox_loglikelihood(y: ArrayLike, lambdas: ArrayLike) -> np.ndarray:
    """Profile log-likelihood for the Box–Cox transform across ``lambdas``.

    ``y`` must be strictly positive. Returns an array shaped like ``lambdas``.
    """
    y_arr = _as_array(y)
    if np.any(y_arr <= 0):
        raise ValueError("Box-Cox requires strictly positive y.")
    lambdas_arr = _as_array(lambdas)
    n = y_arr.size
    log_y = np.log(y_arr)
    out = np.zeros_like(lambdas_arr, dtype=float)
    for i, lam in enumerate(lambdas_arr):
        if abs(lam) < 1e-8:
            y_t = log_y
        else:
            y_t = (y_arr ** lam - 1.0) / lam
        var = float(np.var(y_t, ddof=0))
        out[i] = -n / 2.0 * np.log(max(var, 1e-12)) + (lam - 1.0) * np.sum(log_y)
    return out


def yeo_johnson_loglikelihood(y: ArrayLike, lambdas: ArrayLike) -> np.ndarray:
    """Profile log-likelihood for the Yeo–Johnson transform across ``lambdas``."""
    y_arr = _as_array(y)
    lambdas_arr = _as_array(lambdas)
    n = y_arr.size
    out = np.zeros_like(lambdas_arr, dtype=float)
    pos = y_arr >= 0
    neg = ~pos
    for i, lam in enumerate(lambdas_arr):
        y_t = np.zeros_like(y_arr)
        if abs(lam) < 1e-8:
            y_t[pos] = np.log1p(y_arr[pos])
        else:
            y_t[pos] = ((y_arr[pos] + 1.0) ** lam - 1.0) / lam
        if abs(lam - 2.0) < 1e-8:
            y_t[neg] = -np.log1p(-y_arr[neg])
        else:
            y_t[neg] = -(((-y_arr[neg] + 1.0) ** (2.0 - lam)) - 1.0) / (2.0 - lam)
        var = float(np.var(y_t, ddof=0))
        sign = np.where(pos, 1.0, -1.0)
        log_term = np.sum(sign * np.log1p(np.abs(y_arr)))
        out[i] = -n / 2.0 * np.log(max(var, 1e-12)) + (lam - 1.0) * log_term
    return out


def conformal_quantile(residuals_calibration: ArrayLike, alpha: float = 0.1) -> float:
    """Split-conformal quantile of absolute residuals at level ``1-alpha``."""
    r = np.abs(_as_array(residuals_calibration))
    n = r.size
    k = int(np.ceil((n + 1) * (1.0 - alpha)))
    k = max(1, min(n, k))
    return float(np.partition(r, k - 1)[k - 1])


def jackknife_plus_intervals(
    leave_one_out_predictions: MatrixLike,
    y_calibration: ArrayLike,
    new_predictions: ArrayLike,
    alpha: float = 0.1,
) -> Tuple[np.ndarray, np.ndarray]:
    """Jackknife+ prediction intervals (Barber et al. 2021).

    ``leave_one_out_predictions`` has shape ``(n_calibration, n_test)``; each
    row ``i`` holds predictions for the test set from the model trained
    without calibration point ``i``. ``y_calibration`` are the calibration
    targets and ``new_predictions`` are the standard predictions on the test set.
    """
    L = _as_matrix(leave_one_out_predictions)
    y_c = _as_array(y_calibration)
    y_n = _as_array(new_predictions)
    if L.shape[0] != y_c.size:
        raise ValueError("rows of leave_one_out_predictions must equal y_calibration length.")
    if L.shape[1] != y_n.size:
        raise ValueError("cols of leave_one_out_predictions must equal new_predictions length.")
    abs_res = np.abs(y_c[:, None] - L)
    lo = np.quantile(L - abs_res, alpha, axis=0)
    hi = np.quantile(L + abs_res, 1.0 - alpha, axis=0)
    return lo, hi


# ---------------------------------------------------------------------------
# Approximate chi-squared survival function (no scipy dependency).
# ---------------------------------------------------------------------------

def _chi2_sf(x: float, df: int) -> float:
    """1 - F_chi2(x; df) via Wilson–Hilferty approximation."""
    if x <= 0 or df <= 0:
        return 1.0
    h = 2.0 / (9.0 * df)
    z = ((x / df) ** (1.0 / 3.0) - (1.0 - h)) / np.sqrt(h)
    # Standard normal survival via erf complement.
    from math import erf, sqrt
    return float(0.5 * (1.0 - erf(z / sqrt(2.0))))
