"""Generate the RST gallery pages from the example registry.

Each page documents two examples in depth: description, situation, code,
sample chart, requirements and notes. Run from the repository root::

    python docs/_tools/generate_example_pages.py

The script reads its code snippets directly from
``docs/_tools/generate_examples.py`` so the documentation stays in sync
with the executable example registry.
"""

from __future__ import annotations

import importlib.util
import inspect
import textwrap
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EX_PATH = HERE / "generate_examples.py"
OUT_DIR = ROOT / "docs" / "source" / "examples"
OUT_DIR.mkdir(parents=True, exist_ok=True)

spec = importlib.util.spec_from_file_location("_ex", EX_PATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore[union-attr]

# slug -> metadata
META = {
    "univariate_histogram": dict(
        title="Histogram of cycle times",
        function="dv.histogram_static",
        situation="A production engineer collects 400 cycle-time measurements from an assembly line and wants to inspect the spread, central tendency and skewness of the process at a glance.",
        notes="Increase ``bins`` for high-resolution data; reduce it for small samples. The static version returns a matplotlib ``Axes`` so any subsequent customization (annotations, vertical lines for spec limits, etc.) can be applied directly.",
    ),
    "univariate_density": dict(
        title="Kernel density estimate",
        function="dv.density_static",
        situation="An analyst wants a smooth, bin-free view of a continuous variable (here, standardized scores) to discuss its shape with stakeholders without committing to a specific bin width.",
        notes="Pandas is required because ``density_static`` delegates to ``Series.plot.kde``. Pass ``fill=True`` to shade the area below the curve.",
    ),
    "univariate_box_plot": dict(
        title="Box plot of service times",
        function="dv.box_plot_static",
        situation="A call-center supervisor needs a robust summary of service-time spread that emphasises medians and outliers rather than means, suitable for non-symmetric, right-skewed data.",
        notes="Box plots are robust to outliers but hide multi-modality. Combine with a violin or ridgeline plot when the underlying distribution may be multi-modal.",
    ),
    "univariate_violin_plot": dict(
        title="Violin plot of standardized scores",
        function="dv.violin_plot_static",
        situation="A data scientist wants to communicate both the spread and the density shape of a feature in a single visual, which a box plot alone cannot convey.",
        notes="Violin plots can be misleading on small samples (``n < 50``). Prefer a strip or dot plot when sample sizes are small.",
    ),
    "univariate_ecdf": dict(
        title="Empirical cumulative distribution",
        function="dv.ecdf_plot_static",
        situation="An SRE inspects a wait-time distribution and wants to read percentile thresholds (p50, p95, p99) directly off the chart without smoothing assumptions.",
        notes="ECDFs are non-parametric and well-suited to skewed or heavy-tailed data. They scale well to large samples.",
    ),
    "univariate_qq": dict(
        title="Quantile-quantile plot vs. normal",
        function="dv.qq_plot_static",
        situation="A statistician wants to assess whether a sample is plausibly normal before applying a Gaussian-assumption test (t-test, ANOVA, etc.).",
        notes="Points that depart from the reference line on the tails indicate non-normality. Pair with a formal test (Shapiro-Wilk, Anderson-Darling) for confirmation.",
    ),
    "univariate_cumhist": dict(
        title="Cumulative histogram of latencies",
        function="dv.cumulative_histogram_static",
        situation="A platform engineer wants to estimate the proportion of requests below a target latency, e.g. ``P[latency < 60 ms]``, directly from a histogram.",
        notes="Cumulative histograms are easier to read than ECDFs for audiences unfamiliar with statistics while preserving similar information.",
    ),
    "univariate_outlier": dict(
        title="Outlier inspection plot",
        function="dv.outlier_plot_static",
        situation="A quality engineer suspects a small set of measurements deviates strongly from the bulk of the data and wants to visualize how many points exceed the typical range before deciding to remove or investigate them.",
        notes="The helper flags points outside 1.5 * IQR by default. Always investigate flagged points before discarding — outliers may be the most informative observations.",
    ),
    "univariate_strip": dict(
        title="Strip plot for small samples",
        function="dv.strip_plot_static",
        situation="A researcher has a small sample (n = 80) and prefers to show every individual observation rather than smoothing it into a density or histogram.",
        notes="Strip plots avoid the binning artefacts of histograms and are ideal for n in the 10-200 range.",
    ),
    "univariate_dot": dict(
        title="Dot plot of integer ratings",
        function="dv.dot_plot_static",
        situation="A UX team summarises survey ratings on a 1-10 integer scale and wants every observation to remain visible while emphasising frequency.",
        notes="Dot plots work best on discrete, low-cardinality values. They are a natural alternative to bar charts when sample sizes are modest.",
    ),
    "univariate_lollipop": dict(
        title="Lollipop chart of item counts",
        function="dv.lollipop_chart_static",
        situation="A product manager ranks items by count and wants a less visually heavy alternative to a bar chart that still emphasises differences in magnitude.",
        notes="The input is expected to be a pandas ``Series`` indexed by category name. Sort it beforehand to make the ranking visually obvious.",
    ),
    "univariate_lorenz": dict(
        title="Lorenz curve of income inequality",
        function="dv.lorenz_curve_static",
        situation="An economist studies the distribution of incomes in a sample and wants a graphical view of inequality that can be paired with the Gini coefficient.",
        notes="A perfectly equal distribution traces the 45-degree diagonal. The further the curve bows below the diagonal, the greater the inequality.",
    ),
    "univariate_ridgeline": dict(
        title="Ridgeline plot by group",
        function="dv.ridgeline_plot_static",
        situation="An analyst compares the distributions of four product cohorts in a compact, visually engaging format that makes shifts in mean and shape easy to spot.",
        notes="Each column of the input ``DataFrame`` becomes one ridge. Use a wide, long figure (``figsize=(10, 8)``) to keep the ridges legible.",
    ),
    "univariate_frequency_bar": dict(
        title="Frequency bar chart for categories",
        function="dv.frequency_bar_static",
        situation="A marketing analyst summarises the count of each product category in a transactional dataset and wants the bars ordered by frequency.",
        notes="The chart works on raw labels; no aggregation is needed. For high-cardinality categories, truncate to the top-N before plotting.",
    ),
    "bivariate_scatter": dict(
        title="Scatter plot of feature vs. target",
        function="dv.scatter_plot_static",
        situation="A modeller assesses the relationship between a numeric feature and a continuous target before fitting a regression model.",
        notes="Add ``alpha`` for large samples to mitigate overplotting; switch to a hexbin or 2-D histogram beyond ~5000 points.",
    ),
    "bivariate_line": dict(
        title="Line chart of a time series",
        function="dv.line_plot_static",
        situation="A business analyst tracks the daily evolution of an index over six months and needs a clean line chart to share with stakeholders.",
        notes="Pass ``pandas`` time-indexed ``Series`` directly — matplotlib will format the x-axis with date locators automatically.",
    ),
    "bivariate_correlation": dict(
        title="Correlation heatmap",
        function="dv.correlation_heatmap_static",
        situation="A data scientist inspects pairwise linear correlations across six engineered features and a target column to spot strong drivers and potential collinearities.",
        notes="The helper computes Pearson correlations by default. For non-linear or rank-based associations, pre-compute with ``df.corr(method='spearman')`` and pass the resulting matrix.",
    ),
    "bivariate_hexbin": dict(
        title="Hexbin density plot",
        function="dv.hexbin_plot_static",
        situation="An analyst inspects a 5000-point joint distribution where a standard scatter plot would saturate due to overplotting.",
        notes="``gridsize`` controls cell resolution. Larger grids show finer structure but become noisy on small samples.",
    ),
    "bivariate_regression": dict(
        title="Regression fit overlay",
        function="dv.regression_plot_static",
        situation="An educator visualises the linear relationship between study hours and exam scores together with the fitted regression line for a classroom demo.",
        notes="The helper fits an ordinary least-squares line. For non-linear relationships, pre-transform the predictor (log, square) before plotting.",
    ),
    "bivariate_bubble": dict(
        title="Bubble chart sized by a third variable",
        function="dv.bubble_plot_static",
        situation="A marketing team plots spend versus revenue and encodes customer count as the bubble size to convey three dimensions in a single static chart.",
        notes="Scale ``size`` to a reasonable range (e.g. 20-500). Very large bubbles can mask underlying density.",
    ),
    "bivariate_grouped_bar": dict(
        title="Aggregated bar chart by category",
        function="dv.grouped_bar_static",
        situation="A finance analyst aggregates revenue per quarter across multiple stores using the mean and presents the results as a bar chart.",
        notes="Pass ``aggfunc='median'`` (or any callable) to switch the aggregation. The helper automatically labels the y-axis with the aggregation name.",
    ),
    "bivariate_step": dict(
        title="Step plot for stock levels",
        function="dv.step_plot_static",
        situation="A warehouse operator plots daily inventory level where the value only changes at discrete time points; a step chart better reflects the underlying piecewise-constant process than a line chart.",
        notes="Use step plots whenever the underlying process is piecewise-constant (inventory, queue length, event counts).",
    ),
    "bivariate_bland_altman": dict(
        title="Bland-Altman agreement plot",
        function="dv.bland_altman_static",
        situation="A clinical engineer compares two measurement devices and wants to assess whether they agree across the measurement range, not merely whether they correlate.",
        notes="The horizontal axis is the mean of the two measurements and the vertical axis is their difference. The reference lines mark mean ± 1.96 SD of the differences.",
    ),
    "bivariate_box_by_category": dict(
        title="Box plot split by category",
        function="dv.box_by_category_static",
        situation="An analyst compares the distribution of a continuous variable across three categorical groups to assess whether group means and spreads differ.",
        notes="For more than ~10 groups the chart becomes crowded — consider a violin or strip plot, or sort groups by median.",
    ),
    "bivariate_errorbar": dict(
        title="Error bar plot with uncertainty",
        function="dv.errorbar_plot_static",
        situation="A scientist plots a daily measurement together with its measurement uncertainty to communicate both the value and its confidence.",
        notes="Use symmetric error bars when the error is roughly Gaussian. For skewed or bounded quantities, prefer asymmetric error bars (pass ``yerr`` as a 2-row array).",
    ),
    "bivariate_lag": dict(
        title="Lag plot for autocorrelation",
        function="dv.lag_plot_static",
        situation="A time-series analyst diagnoses serial dependence in a signal by plotting each observation against its predecessor — a tight diagonal indicates strong lag-1 autocorrelation.",
        notes="A diffuse cloud suggests white noise; a clear linear pattern indicates strong autocorrelation. Vary ``lag`` to probe different lags.",
    ),
    "multivariate_heatmap": dict(
        title="Value heatmap of a matrix",
        function="dv.multivariate.heatmap_static",
        situation="A geneticist visualises a 12 × 8 matrix of normalized expression values to spot row and column patterns at a glance.",
        notes="The diverging colormap defaults are tuned for centered-on-zero data; pass ``cmap='viridis'`` for non-negative matrices.",
    ),
    "multivariate_pairplot": dict(
        title="Pairwise scatter matrix",
        function="dv.multivariate.pairplot_static",
        situation="An exploratory analyst inspects all pairwise relationships among four features in a 150-row dataset to identify candidates for modelling.",
        notes="Pairplots scale quadratically in the number of features. Keep the feature count below ~8 or sample the data to keep the figure legible.",
    ),
    "multivariate_parallel": dict(
        title="Parallel coordinates plot",
        function="dv.multivariate.parallel_coordinates_static",
        situation="A multivariate analyst inspects five features simultaneously across 120 observations to detect crossings and clusters that scatter plots cannot reveal.",
        notes="Reorder columns to place the most discriminating features adjacent to each other — this maximises information conveyed by the line crossings.",
    ),
    "eda_missing": dict(
        title="Missing-data map",
        function="dv.missing_data_plot_static",
        situation="A data engineer audits a fresh extract by visualising the per-column and per-row pattern of missing values before deciding on imputation strategy.",
        notes="Vertical stripes reveal columns with widespread missingness; horizontal stripes reveal rows that are systematically incomplete.",
    ),
    "eda_distribution_summary": dict(
        title="Distribution summary across features",
        function="dv.distribution_summary_static",
        situation="An analyst inspects the shape of every numeric column in a fresh dataset on a single figure to identify skewed, multi-modal or bounded variables.",
        notes="Useful as a first-pass EDA step. Combine with ``dv.missing_data_plot_static`` to assess completeness alongside shape.",
    ),
    "eda_class_distribution": dict(
        title="Class balance for classification",
        function="dv.class_distribution_static",
        situation="An ML engineer audits the class distribution before training a classifier to decide whether resampling or class weights are required.",
        notes="When the smallest class is below ~5 %, consider stratified sampling, SMOTE-style oversampling or class-weighted losses.",
    ),
    "spc_control": dict(
        title="Individuals (I) control chart",
        function="dv.control_chart_static",
        situation="A quality engineer monitors the diameter of a machined part and wants to flag points outside the natural ±3-sigma control limits.",
        notes="The helper computes control limits from the data itself. For ongoing monitoring, freeze the limits from a baseline period and reuse them.",
    ),
    "spc_x_range": dict(
        title="X-bar / R chart for subgrouped data",
        function="dv.x_range_chart_static",
        situation="A manufacturing engineer groups 150 measurements into 30 subgroups of five and monitors both the subgroup mean (X-bar) and within-subgroup range (R).",
        notes="``subgroup_size`` should reflect the rational subgrouping of the process, typically 4-6 observations per subgroup.",
    ),
    "spc_run": dict(
        title="Run chart of daily throughput",
        function="dv.run_chart_static",
        situation="An operations lead reviews daily throughput and looks for runs, trends and cycles before computing formal control limits.",
        notes="Run charts are a useful precursor to a control chart and require fewer distributional assumptions.",
    ),
    "spc_rules": dict(
        title="Western Electric rule violations",
        function="dv.rule_violation_chart_static",
        situation="A reliability engineer flags subtle process shifts that would not trigger a 3-sigma rule but match Western Electric patterns (e.g. eight points on one side of the mean).",
        notes="The function highlights points that violate the standard pattern rules. Investigate clusters of violations rather than isolated ones.",
    ),
    "spc_capability": dict(
        title="Process capability histogram",
        function="dv.capability_histogram_static",
        situation="A quality manager evaluates whether the process distribution fits within engineering specification limits (LSL, USL) and reports Cp / Cpk values.",
        notes="Capability indices assume an in-control, approximately normal process. Verify both assumptions with a control chart and a normality test before reporting.",
    ),
    "spc_moving_range": dict(
        title="Moving-range chart",
        function="dv.moving_range_chart_static",
        situation="A process engineer monitors short-term variation in a continuous reading where natural subgrouping is not feasible.",
        notes="Use the moving-range chart together with an individuals chart (``dv.control_chart_static``) for full SPC coverage.",
    ),
    "spc_ewma": dict(
        title="EWMA chart for small process shifts",
        function="dv.ewma_chart_static",
        situation="An engineer monitors a process where the shift of interest is small (< 1 sigma) and a standard control chart would react too slowly.",
        notes="Smaller ``lambda_`` values increase sensitivity to small persistent shifts at the cost of reacting more slowly to large shocks.",
    ),
    "spc_cusum": dict(
        title="CUSUM chart",
        function="dv.cusum_chart_static",
        situation="A reliability engineer accumulates deviations from a target value to detect small but persistent biases that would be missed by a standard control chart.",
        notes="CUSUM charts are reset whenever the cumulative sum touches zero or crosses the decision interval ``h``. Tune ``h`` and ``k`` for the target detection performance.",
    ),
    "regression_residual": dict(
        title="Residuals vs. fitted",
        function="dv.residual_plot_static",
        situation="A modeller inspects residuals against fitted values to check the linearity and homoscedasticity assumptions of a regression model.",
        notes="A funnel or fan shape indicates heteroscedasticity; a U-shape indicates a missing non-linear term.",
    ),
    "regression_prediction": dict(
        title="Predicted vs. actual",
        function="dv.prediction_plot_static",
        situation="A team showcases the calibration of a regression model by plotting predicted values against ground truth alongside the ``y = x`` reference line.",
        notes="A tight band around the 45-degree line indicates a well-calibrated model. Systematic departures suggest a misspecified or biased estimator.",
    ),
    "regression_learning": dict(
        title="Learning curve",
        function="dv.learning_curve_static",
        situation="An ML engineer diagnoses whether a model would benefit from more training data by plotting train and validation scores against training-set size.",
        notes="A persistent gap between training and validation scores indicates overfitting; converging curves at a low score indicate underfitting.",
    ),
    "classification_confusion": dict(
        title="Confusion matrix heatmap",
        function="dv.confusion_matrix_plot_static",
        situation="An ML engineer evaluates a three-class classifier and inspects which class pairs are most often confused with each other.",
        notes="Pass a precomputed confusion matrix. Use ``sklearn.metrics.confusion_matrix(y_true, y_pred)`` when working with real predictions.",
    ),
    "classification_roc": dict(
        title="ROC curve with AUC",
        function="dv.roc_curve_static",
        situation="A team reports the trade-off between true positive rate and false positive rate of a binary classifier across all decision thresholds.",
        notes="The ROC curve is threshold-agnostic; pair it with a precision-recall curve when the positive class is rare.",
    ),
    "classification_pr": dict(
        title="Precision-recall curve",
        function="dv.precision_recall_curve_static",
        situation="A modelling team works with a heavily imbalanced binary problem (e.g. fraud detection) where ROC-AUC overstates performance.",
        notes="On imbalanced problems, the area under the precision-recall curve (PR-AUC) is more informative than ROC-AUC.",
    ),
    "classification_multiclass_roc": dict(
        title="One-vs-rest ROC curves",
        function="dv.classification.multiclass_roc_curve_static",
        situation="A multiclass model is evaluated by computing one-vs-rest ROC curves for each class so individual class trade-offs can be compared on a single panel.",
        notes="The helper accepts a mapping of class label to ``(fpr, tpr)`` arrays so any upstream computation (scikit-learn ``roc_curve``, custom rank-based code, etc.) can feed the plot.",
    ),
    "classification_multiclass_pr": dict(
        title="One-vs-rest precision-recall curves",
        function="dv.classification.multiclass_pr_curve_static",
        situation="On a multiclass problem with imbalanced classes, the team prefers per-class precision-recall curves over ROC because PR is more sensitive to the minority class.",
        notes="Pair this view with ``per_class_auc_bar`` or ``per_class_ap_bar`` to summarise the curves in a single scalar per class.",
    ),
    "classification_calibration": dict(
        title="Reliability diagram (calibration curve)",
        function="dv.classification.calibration_curve_static",
        situation="A risk-scoring team needs to know whether predicted probabilities are well calibrated so that downstream decision rules (thresholds, expected-cost calculations) are reliable.",
        notes="Use ``strategy='quantile'`` when scores are skewed so each bin contains a comparable number of samples. Pair with ``calibration_with_confidence`` to add bootstrap confidence bands.",
    ),
    "classification_prob_hist": dict(
        title="Probability histogram by class",
        function="dv.classification.probability_histogram_static",
        situation="A team inspects whether the score distributions for positives and negatives are well separated, which directly determines whether a single threshold can achieve high precision and high recall simultaneously.",
        notes="If the two histograms strongly overlap the model has weak discrimination — invest in features rather than threshold tuning.",
    ),
    "classification_threshold": dict(
        title="Precision / recall / F1 vs. threshold",
        function="dv.classification.threshold_metric_curve_static",
        situation="An ML engineer needs to pick an operating threshold and wants to see precision, recall, F1 and accuracy plotted simultaneously over the full threshold range.",
        notes="Pick the threshold from the validation set, not the test set, to avoid information leakage. Combine with ``discrimination_threshold_dashboard`` for the queue-rate view.",
    ),
    "classification_ks": dict(
        title="Kolmogorov-Smirnov plot",
        function="dv.classification.ks_statistic_plot_static",
        situation="A credit-scoring analyst reports the maximum vertical gap between the cumulative score distributions of positives and negatives (the KS statistic) — a standard benchmark in scoring problems.",
        notes="KS is correlated with AUC but emphasises the threshold where the two populations are most separated. A KS below 0.20 is typically considered weak in credit risk applications.",
    ),
    "classification_det": dict(
        title="Detection error trade-off (DET) curve",
        function="dv.classification.det_curve_static",
        situation="A speaker-verification or biometric team prefers a DET plot (FNR vs. FPR on a normal-deviate scale) over ROC because the operating region of interest contains very small error rates.",
        notes="The normal-deviate axes spread the low-error region so small differences are visible. No external dependency on scipy: the inverse-erf approximation is implemented in pure NumPy.",
    ),
    "classification_net_benefit": dict(
        title="Decision-curve analysis (net benefit)",
        function="dv.classification.net_benefit_curve_static",
        situation="A clinical team applies decision-curve analysis to compare ``treat all`` and ``treat none`` strategies against the model across the full range of clinically plausible threshold probabilities.",
        notes="Net benefit explicitly trades true positives against false positives using the threshold probability as the exchange rate. Reasonable thresholds in clinical contexts span 0.05 to 0.30.",
    ),
    "classification_gain": dict(
        title="Cumulative gain chart",
        function="dv.classification.gain_chart_static",
        situation="A marketing team ranks customers by predicted purchase probability and asks: if we contact the top-30 % of the ranked list, what fraction of all positives do we capture?",
        notes="The diagonal is the random-targeting baseline; the closer the gain curve is to the top-left corner, the better the ranking.",
    ),
    "classification_lift": dict(
        title="Decile lift chart",
        function="dv.classification.lift_chart_static",
        situation="The same marketing team also wants the multiplicative gain over random targeting in each decile of the ranked list — a direct campaign-ROI input.",
        notes="``n_bins`` defaults to 10 (deciles). Use 20 for finer granularity on large lists.",
    ),
    "classification_class_balance": dict(
        title="Class balance: true vs. predicted",
        function="dv.classification.class_balance_bar_static",
        situation="An ML engineer audits a fresh model and wants to confirm that the predicted-class distribution matches the true-class distribution closely enough for downstream consumers.",
        notes="Large deviations between the two bars indicate threshold mis-calibration or strong class-prior shift between training and the audit window.",
    ),
    "classification_per_class_metrics": dict(
        title="Per-class precision / recall / F1",
        function="dv.classification.per_class_metrics_bar_static",
        situation="A multiclass model is profiled to identify the weakest class so engineering effort (more data, better features, re-balancing) can be focused where it matters.",
        notes="Combine with ``classification_report_heatmap`` for a one-page artefact suitable for model-review meetings.",
    ),
    "classification_normalized_cm": dict(
        title="Row-normalized confusion matrix",
        function="dv.classification.normalized_confusion_matrix_static",
        situation="On an imbalanced multiclass problem, raw counts in a confusion matrix are dominated by the majority class. Row-normalising turns each row into recall per class.",
        notes="Use ``normalize='pred'`` for per-prediction precision or ``normalize='all'`` for global fractions.",
    ),
    "classification_error_grid": dict(
        title="Error analysis grid",
        function="dv.classification.error_analysis_grid_static",
        situation="An ML engineer drills into the off-diagonal cells of the confusion matrix to identify systematic confusion patterns (e.g. class ``B`` and ``C`` are routinely swapped).",
        notes="The error grid masks the diagonal so the visual emphasis is fully on mistakes. Pair with ``misclassification_cluster_heatmap`` to slice errors by score bin.",
    ),
    "classification_score_dist": dict(
        title="Score distribution by class",
        function="dv.classification.score_distribution_by_class_static",
        situation="A team inspects how cleanly the positive and negative populations separate in score space — a stronger diagnostic than a histogram when one class is rare.",
        notes="Set ``kind='box'`` for a more compact summary on dashboards or ``kind='strip'`` for sample sizes below 100.",
    ),
    "classification_decision_boundary": dict(
        title="2-D decision boundary",
        function="dv.classification.decision_boundary_plot_static",
        situation="A practitioner inspects how a 2-D classifier carves up feature space — useful for teaching, debugging or comparing model families on the same dataset.",
        notes="The helper accepts any ``predict_fn`` callable taking an ``(n, 2)`` array, so it works with scikit-learn estimators (``model.predict``), custom decision rules, or kernel-density classifiers.",
    ),
    "classification_f_beta": dict(
        title="F-beta vs. threshold",
        function="dv.classification.f_beta_curve_static",
        situation="A team weighs precision and recall asymmetrically (e.g. recall twice as important as precision) and reads the optimum threshold straight from the F-beta curve.",
        notes="``beta < 1`` emphasises precision; ``beta > 1`` emphasises recall. F1 (``beta = 1``) is the symmetric default.",
    ),
    "classification_mcc": dict(
        title="Matthews correlation vs. threshold",
        function="dv.classification.mcc_curve_static",
        situation="On heavily imbalanced problems MCC is widely preferred to F1 because it accounts for all four cells of the confusion matrix. The team reads the MCC-maximising threshold off the curve.",
        notes="MCC ranges from -1 (perfectly wrong) through 0 (random) to +1 (perfect). Values near zero on imbalanced data often correspond to ``always predict majority``.",
    ),
    "classification_per_class_auc": dict(
        title="Per-class one-vs-rest AUC",
        function="dv.classification.per_class_auc_bar_static",
        situation="A multiclass model is summarised by collapsing each ROC curve to its AUC and ranking classes from worst to best — a fast triage for follow-up modelling.",
        notes="The function expects a precomputed ``{class: auc}`` mapping so any AUC implementation (sklearn, NumPy ``np.trapezoid``, custom rank-based) can feed the chart.",
    ),
    "classification_top_k": dict(
        title="Top-K accuracy curve",
        function="dv.classification.top_k_accuracy_curve_static",
        situation="On problems with many classes (image classification, product recommendation) the team reports the fraction of times the true class falls inside the model's top-K predictions, not only the top-1.",
        notes="Top-K is a strict monotone-increasing function of K. Report top-1 alongside top-5 for vision tasks and top-3 alongside top-10 for retrieval tasks.",
    ),
    "classification_multilabel_grid": dict(
        title="Per-label confusion grid (multilabel)",
        function="dv.classification.multilabel_confusion_grid_static",
        situation="A multilabel model (tags, attributes) is audited label-by-label by laying out one 2×2 confusion matrix per label in a grid so the per-label trade-off is visible at a glance.",
        notes="The function returns a ``numpy.ndarray`` of matplotlib Axes — call ``.ravel()[0].figure`` to grab the parent figure if you need to save it.",
    ),
    "classification_label_cooccurrence": dict(
        title="Label co-occurrence (Jaccard)",
        function="dv.classification.label_cooccurrence_heatmap_static",
        situation="A taxonomy lead inspects how often pairs of multilabel tags co-occur in the dataset — pairs with high Jaccard suggest redundant labels or a hierarchical structure.",
        notes="Toggle ``normalize=False`` to display absolute co-occurrence counts. The diagonal is always 1.0 (Jaccard of a set with itself).",
    ),
    "classification_segment_metric": dict(
        title="Per-segment accuracy / precision / recall",
        function="dv.classification.per_segment_metric_bar_static",
        situation="A fairness lead computes accuracy, precision and recall for each demographic segment (or business segment) to surface performance gaps.",
        notes="``groups`` can be any array of categorical labels (strings, ints). Pair with ``fairness_disparity_heatmap`` for the relative-deviation view.",
    ),
    "classification_fairness_disparity": dict(
        title="Fairness disparity heatmap",
        function="dv.classification.fairness_disparity_heatmap_static",
        situation="A team quantifies how much each segment deviates from the population-level metric across multiple metrics (accuracy, FPR, FNR) on a single heatmap.",
        notes="Cells far from zero indicate disparity. The sign convention is segment_value - population_value, so positive cells mean the segment outperforms the average.",
    ),
    "classification_discrimination": dict(
        title="Discrimination threshold dashboard",
        function="dv.classification.discrimination_threshold_dashboard_static",
        situation="A team picks an operating threshold by simultaneously balancing precision, recall, F1 and queue rate (the fraction of samples flagged).",
        notes="Inspired by the Yellowbrick ``DiscriminationThreshold``. The red dotted line marks the F1-maximising threshold.",
    ),
    "classification_loss_distribution": dict(
        title="Per-sample log-loss distribution",
        function="dv.classification.loss_distribution_plot_static",
        situation="An ML engineer hunts for high-loss outliers — samples that contribute disproportionately to the average loss — to investigate label noise or covariate shift.",
        notes="Samples in the right tail are the highest priority for manual review. Combine with ``confidence_by_correctness_histogram`` for a complementary view.",
    ),
    "classification_metrics_radar": dict(
        title="Model comparison radar",
        function="dv.classification.metrics_radar_chart_static",
        situation="A team compares three candidate models across precision, recall, F1 and AUC on a single radar so trade-offs are obvious to non-technical reviewers.",
        notes="Keep all metrics on a common ``[0, 1]`` scale. For non-bounded metrics, normalise upstream before plotting.",
    ),
    "classification_psi": dict(
        title="Population Stability Index (PSI)",
        function="dv.classification.psi_bar_static",
        situation="A production monitoring team flags drift by comparing the current score distribution against a reference window and reporting the PSI contribution of each bin.",
        notes="Rule of thumb: PSI < 0.10 stable, 0.10-0.25 moderate shift, > 0.25 major shift requiring investigation.",
    ),
    "classification_validation_curve": dict(
        title="Validation curve with std bands",
        function="dv.classification.validation_curve_static",
        situation="A practitioner sweeps a single hyperparameter (regularisation strength ``C``, tree depth, ...) across cross-validation folds and looks for the sweet spot between under- and over-fitting.",
        notes="``train_scores`` and ``val_scores`` can be 2-D ``(n_params, n_folds)`` arrays (one score per fold) or 1-D means. The shaded band shows ±1 standard deviation across folds.",
    ),
    "classification_training_history": dict(
        title="Training history (loss and accuracy)",
        function="dv.classification.training_history_curve_static",
        situation="A deep-learning practitioner inspects per-epoch loss and accuracy on training and validation splits to monitor for divergence and over-fitting.",
        notes="Series whose name starts with ``val_`` or contains ``validation`` are drawn dashed automatically, making the train/val split visually unambiguous.",
    ),
    "clustering_scatter": dict(
        title="Scatter plot of cluster assignments",
        function="dv.clustering.scatter_clusters_static",
        situation="A clustering analyst visualises K-means assignments on a synthetic 3-cluster, 2-D dataset to inspect cluster separation and overlap.",
        notes="For high-dimensional data, project to 2-D with PCA, t-SNE or UMAP before plotting.",
    ),
    "clustering_elbow": dict(
        title="Elbow plot for k selection",
        function="dv.clustering.elbow_plot_static",
        situation="A practitioner sweeps K-means from k=1 to k=10 and uses the elbow of the inertia curve to pick a reasonable number of clusters.",
        notes="The elbow heuristic is informal — complement it with silhouette scores or domain knowledge.",
    ),
    "clustering_dendrogram": dict(
        title="Hierarchical clustering dendrogram",
        function="dv.clustering.dendrogram_static",
        situation="An analyst uses Ward linkage on a 20-observation, 4-feature dataset and inspects the dendrogram to choose a cut height that yields meaningful clusters.",
        notes="Requires ``scipy``. Different linkage methods (single, complete, average, ward) produce different tree structures — try several.",
    ),
    "xai_feature_importance": dict(
        title="Feature importance ranking",
        function="dv.xai.feature_importance_static",
        situation="An interpretability lead presents the top-K most important features from a trained model to non-technical stakeholders.",
        notes="The helper accepts a pandas ``Series`` indexed by feature name. For permutation importances, pass the mean of repeated permutations.",
    ),
    "xai_shap": dict(
        title="SHAP summary plot",
        function="dv.xai.shap_plot_static",
        situation="A data scientist summarises per-feature SHAP contributions across 80 test points to explain a tree-based classifier's predictions.",
        notes="This helper renders a static summary view. For dot/swarm-style SHAP plots, use the ``shap`` library directly.",
    ),
    "xai_partial_dependence": dict(
        title="Partial dependence plot",
        function="dv.xai.partial_dependence_static",
        situation="An interpretability analyst inspects how the model's predicted mean response changes as a single feature varies, marginalising over the others.",
        notes="Partial dependence assumes feature independence. When features are correlated, prefer accumulated local effects (ALE).",
    ),
}

# Pages: list of (page_slug, page_title, intro, [slug, slug])
PAGES = [
    ("univariate_01", "Univariate I: Histograms and densities", "Quick-look distributional plots for a single numeric variable.",
        ["univariate_histogram", "univariate_density"]),
    ("univariate_02", "Univariate II: Box and violin plots", "Robust summaries of spread and shape for a single variable.",
        ["univariate_box_plot", "univariate_violin_plot"]),
    ("univariate_03", "Univariate III: ECDF and Q-Q plot", "Non-parametric and quantile-based views of a sample.",
        ["univariate_ecdf", "univariate_qq"]),
    ("univariate_04", "Univariate IV: Cumulative views and outliers", "Cumulative summaries and outlier inspection for univariate data.",
        ["univariate_cumhist", "univariate_outlier"]),
    ("univariate_05", "Univariate V: Strip and dot plots", "Compact, observation-level views ideal for small samples.",
        ["univariate_strip", "univariate_dot"]),
    ("univariate_06", "Univariate VI: Lollipop and Lorenz", "Ranking and inequality views.",
        ["univariate_lollipop", "univariate_lorenz"]),
    ("univariate_07", "Univariate VII: Ridgeline and frequency bars", "Group-wise distributional comparison and categorical frequencies.",
        ["univariate_ridgeline", "univariate_frequency_bar"]),
    ("bivariate_01", "Bivariate I: Scatter and line", "Two-variable plots for the most common analytic patterns.",
        ["bivariate_scatter", "bivariate_line"]),
    ("bivariate_02", "Bivariate II: Correlation and density", "Pairwise correlation summaries and dense 2-D scatter alternatives.",
        ["bivariate_correlation", "bivariate_hexbin"]),
    ("bivariate_03", "Bivariate III: Regression fit and bubble chart", "Annotated linear fits and three-variable bubble views.",
        ["bivariate_regression", "bivariate_bubble"]),
    ("bivariate_04", "Bivariate IV: Grouped bars and step plots", "Categorical aggregations and piecewise-constant time series.",
        ["bivariate_grouped_bar", "bivariate_step"]),
    ("bivariate_05", "Bivariate V: Method comparison and group-wise boxes", "Agreement plots and grouped distributional comparisons.",
        ["bivariate_bland_altman", "bivariate_box_by_category"]),
    ("bivariate_06", "Bivariate VI: Error bars and lag plots", "Uncertainty annotation and time-series autocorrelation views.",
        ["bivariate_errorbar", "bivariate_lag"]),
    ("multivariate_01", "Multivariate I: Heatmap and pairplot", "Matrix views and pairwise scatter for multi-feature exploration.",
        ["multivariate_heatmap", "multivariate_pairplot"]),
    ("mixed_01", "Multivariate and EDA: Parallel coordinates and missingness", "High-dimensional line views and dataset-completeness audits.",
        ["multivariate_parallel", "eda_missing"]),
    ("eda_01", "Exploratory data analysis: Distributions and class balance", "Fast first-pass EDA helpers.",
        ["eda_distribution_summary", "eda_class_distribution"]),
    ("spc_01", "SPC I: Individuals and X-bar / R", "Foundational Shewhart charts for continuous data.",
        ["spc_control", "spc_x_range"]),
    ("spc_02", "SPC II: Run charts and rule violations", "Pre-control views and Western Electric pattern detection.",
        ["spc_run", "spc_rules"]),
    ("spc_03", "SPC III: Capability and moving range", "Process capability assessment and short-term variation.",
        ["spc_capability", "spc_moving_range"]),
    ("spc_04", "SPC IV: EWMA and CUSUM", "Memory-based charts for small process shifts.",
        ["spc_ewma", "spc_cusum"]),
    ("regression_01", "Regression diagnostics I: Residual and prediction", "Standard residual and calibration diagnostics for regression models.",
        ["regression_residual", "regression_prediction"]),
    ("mixed_02", "Regression and classification: Learning curve and confusion matrix", "Model-quality views that span regression and classification workflows.",
        ["regression_learning", "classification_confusion"]),
    ("classification_01", "Classification I: ROC and precision-recall", "Threshold-free quality views for binary and one-vs-rest classifiers.",
        ["classification_roc", "classification_pr"]),
    ("classification_02", "Classification II: Multiclass ROC and PR", "One-vs-rest curves and per-class summary for multiclass problems.",
        ["classification_multiclass_roc", "classification_multiclass_pr"]),
    ("classification_03", "Classification III: Probability calibration", "Reliability diagrams and probability histograms for well-calibrated scoring.",
        ["classification_calibration", "classification_prob_hist"]),
    ("classification_04", "Classification IV: Threshold metric and KS", "Threshold sweeps and the Kolmogorov-Smirnov separation statistic.",
        ["classification_threshold", "classification_ks"]),
    ("classification_05", "Classification V: DET and decision-curve analysis", "Detection error trade-off and net-benefit views for operating-point selection.",
        ["classification_det", "classification_net_benefit"]),
    ("classification_06", "Classification VI: Gain and lift", "Cumulative gain and decile lift charts for ranked-list targeting.",
        ["classification_gain", "classification_lift"]),
    ("classification_07", "Classification VII: Class balance and per-class metrics", "Group composition and per-class quality summary for multiclass models.",
        ["classification_class_balance", "classification_per_class_metrics"]),
    ("classification_08", "Classification VIII: Confusion-matrix extensions", "Row-normalized confusion matrix and error-analysis grid.",
        ["classification_normalized_cm", "classification_error_grid"]),
    ("classification_09", "Classification IX: Score distributions and decision regions", "Score separation by class and 2-D decision-boundary visualisation.",
        ["classification_score_dist", "classification_decision_boundary"]),
    ("classification_10", "Classification X: F-beta and MCC threshold curves", "Asymmetric and imbalance-robust threshold scoring curves.",
        ["classification_f_beta", "classification_mcc"]),
    ("classification_11", "Classification XI: Per-class AUC and top-K", "Per-class one-vs-rest AUC bars and top-K accuracy curve.",
        ["classification_per_class_auc", "classification_top_k"]),
    ("classification_12", "Classification XII: Multilabel diagnostics", "Per-label confusion grid and Jaccard co-occurrence heatmap.",
        ["classification_multilabel_grid", "classification_label_cooccurrence"]),
    ("classification_13", "Classification XIII: Fairness and segments", "Per-segment metrics and population-relative disparity heatmap.",
        ["classification_segment_metric", "classification_fairness_disparity"]),
    ("classification_14", "Classification XIV: Errors and losses", "Discrimination threshold dashboard and per-sample log-loss distribution.",
        ["classification_discrimination", "classification_loss_distribution"]),
    ("classification_15", "Classification XV: Model comparison and monitoring", "Multi-model radar comparison and Population Stability Index for score drift.",
        ["classification_metrics_radar", "classification_psi"]),
    ("classification_16", "Classification XVI: Training diagnostics", "Validation curve over a hyperparameter and per-epoch training-history curves.",
        ["classification_validation_curve", "classification_training_history"]),
    ("clustering_01", "Clustering I: Cluster scatter and elbow", "Visual diagnostics for partitional clustering.",
        ["clustering_scatter", "clustering_elbow"]),
    ("mixed_03", "Clustering and XAI: Dendrogram and feature importance", "Hierarchical clustering structure and interpretability rankings.",
        ["clustering_dendrogram", "xai_feature_importance"]),
    ("xai_01", "Explainable AI: SHAP and partial dependence", "Per-prediction and per-feature interpretability views.",
        ["xai_shap", "xai_partial_dependence"]),
]


def code_for(slug: str) -> str:
    fn = getattr(mod, "ex_" + slug.split("_", 1)[1]) if False else None
    # Map slug -> function name via EXAMPLES tuple
    for s, f in mod.EXAMPLES:
        if s == slug:
            fn = f
            break
    if fn is None:
        raise KeyError(slug)
    src = inspect.getsource(fn)
    body = textwrap.dedent("\n".join(src.splitlines()[1:]))
    lines = [ln for ln in body.splitlines() if not ln.strip().startswith("save(")]
    body = "\n".join(lines).rstrip()
    if "from scipy" in body:
        extra_import = ""
    else:
        extra_import = ""
    preamble = (
        "import numpy as np\n"
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "import dataviz as dv\n"
        "\n"
        "rng = np.random.default_rng(0)\n"
    )
    return preamble + "\n" + body + "\n\nplt.show()\n"


def render_example(slug: str) -> str:
    meta = META[slug]
    code = code_for(slug)
    code_block = "\n".join("   " + ln if ln else "" for ln in code.splitlines())
    title = meta["title"]
    underline = "-" * len(title)
    return f"""{title}
{underline}

:Function: ``{meta["function"]}``
:Example slug: ``{slug}``

Situation
~~~~~~~~~

{meta["situation"]}

Requirements
~~~~~~~~~~~~

* ``dataviz`` (this package)
* ``numpy``, ``pandas`` and ``matplotlib`` (installed as ``dataviz`` dependencies)
* No additional services or data files — the example uses a deterministic
  synthetic dataset generated from ``numpy.random.default_rng(0)``.

Code (copy-paste ready)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python
   :linenos:

{code_block}

Sample chart
~~~~~~~~~~~~

.. image:: ../_static/examples/{slug}.png
   :alt: {title}
   :align: center

Notes
~~~~~

{meta["notes"]}
"""


def render_page(page_slug: str, page_title: str, intro: str, slugs: list) -> str:
    underline = "=" * len(page_title)
    parts = [
        f"{page_title}",
        f"{underline}",
        "",
        f"{intro}",
        "",
        ".. contents::",
        "   :local:",
        "   :depth: 1",
        "",
    ]
    for slug in slugs:
        parts.append(render_example(slug))
        parts.append("")
    return "\n".join(parts)


def main() -> None:
    seen = set()
    for page_slug, title, intro, slugs in PAGES:
        for s in slugs:
            seen.add(s)
        out = OUT_DIR / f"{page_slug}.rst"
        out.write_text(render_page(page_slug, title, intro, slugs), encoding="utf-8")
        print("Wrote", out.relative_to(ROOT))
    missing = set(META) - seen
    extra = seen - set(META)
    if missing:
        print("WARNING: examples in META not on any page:", missing)
    if extra:
        print("WARNING: pages reference unknown slugs:", extra)
    print(f"Generated {len(PAGES)} pages covering {len(seen)} examples.")


if __name__ == "__main__":
    main()
