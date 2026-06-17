import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";

const root = "C:/Projects/repos/data-viz";
const website = path.join(root, "website");
const ctx = { window: {} };
vm.createContext(ctx);
vm.runInContext(fs.readFileSync(path.join(website, "assets", "data.js"), "utf8"), ctx);

const modules = ctx.window.DATAVIZ_MODULES;

function walk(dir) {
  const output = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === "__pycache__") continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) output.push(...walk(full));
    if (entry.isFile() && entry.name.endsWith(".py")) output.push(full);
  }
  return output;
}

function bracketBalance(text) {
  let balance = 0;
  for (const char of text) {
    if ("([{".includes(char)) balance += 1;
    if (")]}".includes(char)) balance -= 1;
  }
  return balance;
}

function cleanSignature(signature) {
  return signature.replace(/\s+/g, " ").replace(/,\s*\)/g, ")").trim();
}

function collectSymbols() {
  const symbols = {};
  for (const slug of Object.keys(modules)) symbols[slug] = {};

  for (const slug of Object.keys(modules)) {
    const modDir = path.join(root, "dataviz", slug);
    if (!fs.existsSync(modDir)) continue;

    for (const file of walk(modDir)) {
      const source = path.relative(root, file).replace(/\\/g, "/");
      const submodule = path.basename(file, ".py");
      const text = fs.readFileSync(file, "utf8");
      const lines = text.split(/\r?\n/);

      for (let i = 0; i < lines.length; i += 1) {
        const line = lines[i];
        const def = line.match(/^def\s+([A-Za-z_]\w*)\s*\(/);
        const cls = line.match(/^class\s+([A-Za-z_]\w*)\s*(?:\(([^)]*)\))?:/);

        if (def) {
          let signature = line.trim();
          let j = i;
          while ((!signature.trim().endsWith(":") || bracketBalance(signature) > 0) && j + 1 < lines.length) {
            j += 1;
            signature += ` ${lines[j].trim()}`;
          }
          symbols[slug][def[1]] = {
            kind: "function",
            signature: cleanSignature(signature.replace(/:$/, "")),
            source,
            submodule,
          };
          i = j;
        } else if (cls) {
          symbols[slug][cls[1]] = {
            kind: "class",
            signature: cleanSignature(line.trim().replace(/:$/, "")),
            source,
            submodule,
          };
        }
      }

      for (const match of text.matchAll(/^([A-Z][A-Z0-9_]+)\s*=\s*/gm)) {
        if (!symbols[slug][match[1]]) {
          symbols[slug][match[1]] = {
            kind: "constant",
            signature: match[1],
            source,
            submodule,
          };
        }
      }
    }
  }

  return symbols;
}

function splitParams(signature) {
  const start = signature.indexOf("(");
  const end = signature.lastIndexOf(")");
  if (start < 0 || end < start) return [];

  const body = signature.slice(start + 1, end);
  const parts = [];
  let current = "";
  let depth = 0;

  for (const char of body) {
    if (char === "," && depth === 0) {
      if (current.trim()) parts.push(current.trim());
      current = "";
      continue;
    }
    current += char;
    if ("([{".includes(char)) depth += 1;
    if (")]}".includes(char)) depth -= 1;
  }
  if (current.trim()) parts.push(current.trim());

  return parts
    .filter((part) => part && part !== "self")
    .map((part) => {
      const raw = part;
      const clean = part.replace(/^\*\*?/, "");
      const name = clean.split(":")[0].split("=")[0].trim();
      const hasDefault = clean.includes("=");
      const type = clean.includes(":") ? clean.split(":").slice(1).join(":").split("=")[0].trim() : "Any";
      return { name, raw, type, required: !hasDefault && !raw.startsWith("*") };
    });
}

function moduleTitle(slug) {
  return modules[slug]?.title || slug.replace(/-/g, " ");
}

function modeFor(name, kind) {
  if (kind === "class") return "type";
  if (kind === "constant") return "constant";
  if (name.endsWith("_static")) return "static";
  if (name.endsWith("_interactive")) return "interactive";
  if (/^[A-Z]/.test(name)) return "type";
  return "helper";
}

function sourceFor(symbols, slug, name) {
  if (symbols[slug]?.[name]) return symbols[slug][name];
  if (name.endsWith("_interactive")) {
    const staticName = name.replace(/_interactive$/, "_static");
    if (symbols[slug]?.[staticName]) {
      return {
        ...symbols[slug][staticName],
        signature: symbols[slug][staticName].signature.replace(staticName, name),
      };
    }
  }
  if (symbols[slug]?.[`${name}_static`]) {
    return {
      ...symbols[slug][`${name}_static`],
      signature: symbols[slug][`${name}_static`].signature.replace(`${name}_static`, name),
    };
  }
  if (symbols[slug]?.[`${name}_interactive`]) {
    return {
      ...symbols[slug][`${name}_interactive`],
      signature: symbols[slug][`${name}_interactive`].signature.replace(`${name}_interactive`, name),
    };
  }
  return {
    kind: /^[A-Z]/.test(name) ? "class" : "function",
    signature: `${name}(...)`,
    source: `dataviz/${slug}/__init__.py`,
    submodule: "reference",
  };
}

function fileName(name) {
  return `${name.replace(/[^A-Za-z0-9_]+/g, "_")}.html`;
}

function hrefFor(slug, submodule, name) {
  return `modules/${slug}/${submodule}/${fileName(name)}`;
}

function label(name) {
  return name.replace(/_/g, " ").replace(/\b\w/g, (char) => char.toUpperCase());
}

function descriptionForParam(name) {
  const descriptions = {
    data: "Input observations, usually a pandas Series, dataframe, list, NumPy array, or matrix-like object.",
    values: "Observed values used by the chart or statistical helper.",
    value: "Column name or one-dimensional input value to profile.",
    x: "Horizontal values, feature values, timestamps, or first paired measurement.",
    y: "Vertical values, response values, scores, or second paired measurement.",
    category: "Category labels used to group or count observations.",
    group: "Optional grouping labels used to split traces, colors, or summaries.",
    hue: "Optional grouping labels used for color encodings.",
    weights: "Non-negative sample weights aligned with the input observations.",
    defects: "Defect counts for attribute control charts.",
    defectives: "Number of nonconforming units in each sample.",
    n: "Sample size or subgroup size associated with each observation.",
    units: "Inspection units or exposure counts used to compute rates.",
    lsl: "Lower specification limit for process capability calculations.",
    usl: "Upper specification limit for process capability calculations.",
    labels: "Display labels for classes, clusters, features, or categories.",
    cm: "Confusion matrix values arranged by true and predicted class.",
    fpr: "False-positive-rate values for ROC curve plotting.",
    tpr: "True-positive-rate values for ROC curve plotting.",
    precision: "Precision values across classification thresholds.",
    recall: "Recall values across classification thresholds.",
    y_true: "Observed target values.",
    y_pred: "Predicted target values.",
    train_sizes: "Training set sizes used to compute learning-curve scores.",
    train_scores: "Training scores aligned with train_sizes.",
    validation_scores: "Validation scores aligned with train_sizes.",
    importances: "Feature importance values.",
    feature_names: "Names aligned with model features.",
    shap_values: "SHAP-like contribution values.",
    feature_values: "Feature grid values used for dependence curves.",
    pd_values: "Partial-dependence response values.",
    thresholds: "Thresholds used for exceedance or classification analysis.",
    sentinels: "Sentinel values that should be counted as quality defects.",
    alpha: "Transparency or significance level, depending on context.",
    title: "Optional plot title.",
    figsize: "Matplotlib figure size in inches.",
    template: "Plotly template name.",
    height: "Interactive figure height in pixels.",
    width: "Interactive figure width in pixels.",
  };
  return descriptions[name] || "Optional configuration value forwarded to the underlying calculation or plotting backend.";
}

function returnType(signature, name, mode) {
  const match = signature.match(/->\s*([^:]+)$/);
  if (match) return match[1].trim();
  if (mode === "static") return "MatplotlibAxes";
  if (mode === "interactive") return "PlotlyFigure";
  if (/Stats$|Summary$|Result$|Interval$|Input$|Limits$|Violation$|Constants$/.test(name)) {
    return "dataclass or structured object";
  }
  if (/table|summary|counts|terms/.test(name)) return "pandas DataFrame or Series";
  if (/values|curve|distribution|quantile/.test(name)) return "numeric arrays or scalar values";
  return "Python object";
}

function purpose(name, slug, mode) {
  const readable = label(name);
  const moduleName = moduleTitle(slug);
  if (mode === "static") {
    return `${readable} creates a static matplotlib/seaborn-style visualization in the ${moduleName} module. Use it when you need a publication-ready axis, notebook output, or a chart that can be composed with other matplotlib objects.`;
  }
  if (mode === "interactive") {
    return `${readable} creates a Plotly-based interactive visualization in the ${moduleName} module. Use it when hover labels, zooming, legends, or browser-delivered exploration will make the result easier to inspect.`;
  }
  if (mode === "type") {
    return `${readable} is a structured type used by the ${moduleName} module to move analysis results through the package with named fields instead of loose dictionaries.`;
  }
  if (mode === "constant") {
    return `${readable} stores reusable reference data for the ${moduleName} module. Use it when downstream code needs the same validated constants as the plotting helpers.`;
  }
  return `${readable} is a ${moduleName} helper that prepares, summarizes, validates, or transforms data before visualization. Use it to keep calculations explicit and testable before drawing charts.`;
}

function definitionsFor(slug, name, params) {
  const defs = ["import dataviz as dv", "import pandas as pd", "import numpy as np"];
  const required = new Set(params.filter((param) => param.required).map((param) => param.name));
  const add = (line) => {
    if (!defs.includes(line)) defs.push(line);
  };

  if (slug === "bivariate" || required.has("x") || required.has("y")) {
    add('x = pd.Series([1, 2, 3, 4, 5], name="Input")');
    add('y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")');
  }
  if (slug === "univariate" || required.has("data") || required.has("values") || required.has("value")) {
    add('values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")');
  }
  if (slug === "eda" || name.includes("missing") || slug === "multivariate") {
    add('df = pd.DataFrame({"a": [1, 2, np.nan, 4], "b": [4, 3, 2, 1], "segment": ["A", "A", "B", "B"]})');
  }
  if (slug === "classification" || required.has("cm")) {
    add("cm = np.array([[32, 4], [5, 29]])");
    add("fpr = np.array([0.0, 0.1, 0.3, 1.0])");
    add("tpr = np.array([0.0, 0.7, 0.9, 1.0])");
    add("precision = np.array([1.0, 0.86, 0.72])");
    add("recall = np.array([0.2, 0.7, 1.0])");
  }
  if (slug === "regression" || required.has("y_true") || required.has("y_pred")) {
    add("y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])");
    add("y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])");
    add("train_sizes = np.array([50, 100, 200])");
    add("train_scores = np.array([0.82, 0.86, 0.89])");
    add("validation_scores = np.array([0.76, 0.81, 0.84])");
  }
  if (slug === "clustering") {
    add("x = np.array([1.0, 1.2, 4.1, 4.3])");
    add("y = np.array([1.1, 0.9, 4.0, 4.4])");
    add("labels = np.array([0, 0, 1, 1])");
    add("k_values = np.array([1, 2, 3, 4])");
    add("inertias = np.array([10.0, 4.2, 2.6, 2.1])");
    add("linkage_matrix = np.array([[0, 1, 0.3, 2], [2, 3, 0.4, 2], [4, 5, 3.0, 4]])");
  }
  if (slug === "xai") {
    add("importances = np.array([0.42, 0.31, 0.18])");
    add('feature_names = ["age", "income", "tenure"]');
    add("shap_values = np.array([[0.1, -0.2, 0.3], [0.2, -0.1, 0.1]])");
    add("feature_values = np.array([0, 1, 2, 3])");
    add("pd_values = np.array([0.2, 0.25, 0.31, 0.34])");
  }
  if (slug === "spc") {
    add('values = pd.Series([10.1, 9.9, 10.2, 10.4, 10.0, 9.8], name="Diameter")');
    add("defects = pd.Series([2, 1, 3, 0, 2, 1])");
    add("defectives = pd.Series([3, 2, 5, 1, 4, 2])");
    add("n = pd.Series([100, 100, 100, 100, 100, 100])");
    add("units = pd.Series([50, 48, 52, 51, 50, 49])");
    add('matrix = pd.DataFrame({"x1": [1.0, 1.1, 0.9, 1.2], "x2": [2.0, 2.1, 1.8, 2.2]})');
  }
  if (name.includes("weighted")) add('weights = pd.Series([1.0, 1.5, 0.8, 1.2, 1.0, 1.1], name="Weight")');
  if (name.includes("sentinel")) add('sentinels = [-1, 999, "missing"]');
  if (name.includes("exceedance")) add("thresholds = [10, 12, 14]");
  if (name.includes("event") || name.includes("interarrival")) {
    add('timestamps = pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-04", "2026-01-10"])');
  }
  if (name.includes("term") || name.includes("string") || name.includes("token")) {
    add('texts = pd.Series(["fast reliable process", "reliable visual process", "fast chart"], name="Comment")');
  }
  if (name.includes("boolean")) add('flags = pd.Series([True, False, True, True, False], name="Passed")');
  if (name.includes("category") || name.includes("frequency") || name.includes("pareto") || name.includes("ordinal") || name.includes("likert")) {
    add('categories = pd.Series(["low", "medium", "high", "medium", "low"], name="Priority")');
  }

  return defs;
}

function argFor(param, name, slug) {
  const paramName = param.name;
  const lowerName = name.toLowerCase();
  if (paramName === "data") {
    if (slug === "multivariate" || slug === "eda") return "df";
    if (lowerName.includes("hotelling")) return "matrix";
    if (lowerName.includes("event") || lowerName.includes("interarrival")) return "timestamps";
    if (lowerName.includes("term") || lowerName.includes("string") || lowerName.includes("token")) return "texts";
    if (lowerName.includes("boolean")) return "flags";
    if (lowerName.includes("category") || lowerName.includes("frequency") || lowerName.includes("pareto") || lowerName.includes("ordinal") || lowerName.includes("likert")) return "categories";
    return "values";
  }

  const args = {
    values: "values",
    value: '"Value"',
    x: "x",
    y: "y",
    category: "categories",
    categories: "categories",
    group: "categories",
    groups: "categories",
    hue: "categories",
    weights: "weights",
    sentinels: "sentinels",
    thresholds: "thresholds",
    defects: "defects",
    defectives: "defectives",
    n: "n",
    units: "units",
    matrix: "matrix",
    cm: "cm",
    fpr: "fpr",
    tpr: "tpr",
    precision: "precision",
    recall: "recall",
    y_true: "y_true",
    y_pred: "y_pred",
    train_sizes: "train_sizes",
    train_scores: "train_scores",
    validation_scores: "validation_scores",
    importances: "importances",
    feature_names: "feature_names",
    shap_values: "shap_values",
    feature_values: "feature_values",
    pd_values: "pd_values",
    labels: slug === "clustering" ? "labels" : '["No", "Yes"]',
    k_values: "k_values",
    inertias: "inertias",
    linkage_matrix: "linkage_matrix",
    lsl: "9.5",
    usl: "10.5",
    subgroup_size: "3",
    alpha: "0.05",
  };
  return args[paramName] || null;
}

function callFor(slug, name, params, mode) {
  if (mode === "type") {
    const factories = {
      univariate: "univariate_summary(values)",
      bivariate: "bivariate_summary(x, y)",
    };
    let factory = factories[slug];
    if (slug === "spc") {
      if (name === "SPCConstants") factory = "get_spc_constants(5)";
      else if (name === "CapabilityStats") factory = "capability_summary(values, lsl=9.5, usl=10.5)";
      else if (name === "HotellingT2Result") factory = "hotelling_t2_summary(matrix)";
      else factory = "individuals_limits(values)";
    }
    return factory ? `result = dv.${slug}.${factory}\nprint(result)` : `# ${name} is returned by ${moduleTitle(slug)} helper functions.\nprint(dv.${slug})`;
  }
  if (mode === "constant") return `print(dv.${slug}.${name})`;

  const required = params.filter((param) => param.required && param.name !== "self");
  let args = required.map((param) => argFor(param, name, slug)).filter(Boolean);
  if (!args.length) {
    if (slug === "classification") args = name.includes("roc") ? ["fpr", "tpr"] : name.includes("precision") ? ["precision", "recall"] : ["cm"];
    else if (slug === "regression") args = name.includes("learning") ? ["train_sizes", "train_scores", "validation_scores"] : ["y_true", "y_pred"];
    else if (slug === "clustering") args = name.includes("dendrogram") ? ["linkage_matrix"] : name.includes("elbow") ? ["k_values", "inertias"] : ["x", "y", "labels"];
    else if (slug === "xai") args = name.includes("shap") ? ["shap_values", "feature_names"] : name.includes("partial") ? ["feature_values", "pd_values"] : ["importances", "feature_names"];
    else if (slug === "spc") args = name.includes("p_chart") ? ["defectives", "n"] : name.includes("np_chart") ? ["defectives", "n"] : name.includes("c_chart") ? ["defects"] : name.includes("u_chart") ? ["defects", "units"] : name.includes("hotelling") ? ["matrix"] : ["values"];
    else if (slug === "bivariate") args = ["x", "y"];
    else if (slug === "eda") args = name.includes("class") ? ["categories"] : ["df"];
    else if (slug === "multivariate") args = ["df"];
    else if (name.includes("weighted")) args = ["values", "weights"];
    else if (name.includes("sentinel")) args = ["values", "sentinels"];
    else if (name.includes("exceedance")) args = ["values", "thresholds"];
    else if (name.includes("event") || name.includes("interarrival")) args = ["timestamps"];
    else if (name.includes("term") || name.includes("string") || name.includes("token")) args = ["texts"];
    else if (name.includes("boolean")) args = ["flags"];
    else if (name.includes("category") || name.includes("frequency") || name.includes("pareto") || name.includes("ordinal") || name.includes("likert")) args = ["categories"];
    else args = ["values"];
  }

  const assignment = mode === "static" ? "ax" : mode === "interactive" ? "fig" : "result";
  let extra = "";
  if (name === "capability_summary" || name.includes("capability_histogram")) extra = ", lsl=9.5, usl=10.5";
  if (name === "bootstrap_ci" || name.includes("bootstrap_distribution")) extra = ", seed=42";
  if (name === "fit_distribution" || name.includes("fitted_distribution")) extra = ', distribution="norm"';
  if (name === "compare_distributions") extra = ', distributions=["norm", "lognorm"]';
  if (name === "weighted_quantile") extra = ", quantile=0.5";
  if (name === "detect_rule_violations") {
    return "limits = dv.spc.individuals_limits(values)\nresult = dv.spc.detect_rule_violations(values, limits)\nprint(result)";
  }
  return `${assignment} = dv.${slug}.${name}(${args.join(", ")}${extra})\nprint(${assignment})`;
}

function exampleFor(slug, name, params, mode) {
  return `${definitionsFor(slug, name, params).join("\n")}\n\n${callFor(slug, name, params, mode)}`;
}

function returnsText(name, mode, returnTypeText) {
  if (mode === "static") return `Returns ${returnTypeText}, usually a matplotlib Axes object with the chart already drawn.`;
  if (mode === "interactive") return `Returns ${returnTypeText}, usually a Plotly Figure that can be shown, exported, or embedded in a dashboard.`;
  if (mode === "type") return `Represents ${returnTypeText}; inspect its named attributes rather than indexing unnamed tuples.`;
  if (mode === "constant") return `Returns or exposes ${returnTypeText}; treat it as read-only reference data.`;
  return `Returns ${returnTypeText}; the exact object is chosen to make downstream analysis and plotting convenient.`;
}

function errorsText(mode) {
  if (mode === "static" || mode === "interactive") {
    return "Raises ValueError for empty, incompatible, or length-mismatched data. Backend errors from matplotlib, seaborn, Plotly, NumPy, pandas, or SciPy may be propagated when inputs cannot be rendered.";
  }
  return "Raises ValueError for invalid configuration or empty inputs, TypeError for unsupported input shapes or dtypes, and may propagate pandas/NumPy validation errors.";
}

function explanationFor(name, mode, entry) {
  const details = [];
  if (mode === "static") details.push("Prefer this function for scripts, reports, notebooks, and saved image outputs where deterministic layout matters.");
  if (mode === "interactive") details.push("Prefer this function when users need hover inspection, zooming, browser embedding, or interactive legends.");
  if (mode === "helper") details.push("Run this helper before plotting when you want to validate assumptions, reuse calculated values, or add tests around the analysis step.");
  if (mode === "type") details.push("These result objects make package APIs easier to read because each field has a meaningful name.");
  if (name.includes("summary")) details.push("Summary helpers are especially useful as the numeric companion to visual exploration.");
  if (name.includes("outlier")) details.push("Outlier-related helpers should be treated as decision support; inspect the flagged records before removing or capping values.");
  if (name.includes("interactive")) details.push("The returned figure can be modified with regular Plotly methods such as update_layout or add_trace.");
  if (name.includes("static")) details.push("The returned axis can be further customized with normal matplotlib calls before saving.");
  return details.join(" ") || `${label(name)} belongs to the ${entry.title} documentation surface and follows the same conventions as the rest of the module.`;
}

const symbols = collectSymbols();
const functionDocs = {};
const generated = [];

for (const [slug, entry] of Object.entries(modules)) {
  if (entry.status !== "complete") continue;
  functionDocs[slug] = {};

  for (const name of entry.functions || []) {
    const symbol = sourceFor(symbols, slug, name);
    const mode = modeFor(name, symbol.kind);
    const params = splitParams(symbol.signature);
    const submodule = symbol.submodule || "reference";
    const href = hrefFor(slug, submodule, name);
    const base = name.replace(/_(static|interactive)$/, "");
    const related = entry.functions
      .filter((other) => other !== name && other.replace(/_(static|interactive)$/, "") === base)
      .slice(0, 8);

    functionDocs[slug][name] = {
      name,
      title: label(name),
      module: slug,
      moduleTitle: entry.title,
      submodule,
      mode,
      kind: symbol.kind,
      href,
      source: symbol.source,
      signature: symbol.signature,
      summary: purpose(name, slug, mode),
      parameters: params.map((param) => ({
        name: param.name,
        type: param.type,
        required: param.required,
        description: descriptionForParam(param.name),
      })),
      returns: returnsText(name, mode, returnType(symbol.signature, name, mode)),
      errors: errorsText(mode),
      example: exampleFor(slug, name, params, mode),
      explanation: explanationFor(name, mode, entry),
      related,
    };

    const outDir = path.join(website, "modules", slug, submodule);
    fs.mkdirSync(outDir, { recursive: true });
    const page = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${name} - DataViz Documentation</title>
  <link rel="stylesheet" href="../../../assets/site.css">
</head>
<body data-page="function" data-root="../../.." data-function-module="${slug}" data-function-name="${name}">
  <div class="layout">
    <aside class="sidebar">
      <a class="brand" href="../../../index.html"><span class="brand-title">DataViz</span><span class="brand-subtitle">Visualization toolkit docs</span></a>
      <input class="search" type="search" placeholder="Filter navigation" data-search>
      <nav data-nav></nav>
    </aside>
    <main class="content">
      <div class="main" data-function-page></div>
    </main>
  </div>
  <script src="../../../assets/data.js"></script>
  <script src="../../../assets/functions.js"></script>
  <script src="../../../assets/site.js"></script>
</body>
</html>
`;
    fs.writeFileSync(path.join(outDir, fileName(name)), page);
    generated.push(path.relative(website, path.join(outDir, fileName(name))).replace(/\\/g, "/"));
  }
}

fs.writeFileSync(
  path.join(website, "assets", "functions.js"),
  `window.DATAVIZ_FUNCTION_DOCS = ${JSON.stringify(functionDocs, null, 2)};\n`,
);

console.log(JSON.stringify({
  generated: generated.length,
  metadata: "website/assets/functions.js",
  first: generated[0],
  last: generated[generated.length - 1],
}, null, 2));
