// Curated clustering documentation content: real use-case descriptions and
// complete, copy-paste code samples per chart family. Consumed by
// _generate_function_docs.mjs to replace the auto-generated boilerplate on
// clustering function pages. Image galleries come from
// assets/examples/clustering/manifest.json.
//
// Keys are chart-family base names (without the _static/_interactive suffix).
// Each entry provides:
//   useCase          - full description of when and why to use the chart.
//   setup            - shared data-preparation lines for the code sample.
//   staticCall       - call + display lines for the *_static form.
//   interactiveCall  - call + display lines for the *_interactive form.

export const CLUSTERING_OVERRIDES = {
  scatter_clusters: {
    useCase:
      "Use the cluster scatter plot to see how an algorithm has partitioned two features \u2014 whether groups are compact and well separated or bleed into one another. Colouring points by their assigned label exposes borderline assignments, oddly shaped clusters, and outliers at a glance. It is the natural sanity check after running k-means or any flat clustering on two-dimensional data or a 2-D projection.",
    setup:
      "rng = np.random.default_rng(0)\nx = np.concatenate(\n    [rng.normal(0.0, 0.4, 40), rng.normal(3.0, 0.4, 40), rng.normal(1.5, 0.4, 40)]\n)\ny = np.concatenate(\n    [rng.normal(0.0, 0.4, 40), rng.normal(3.0, 0.4, 40), rng.normal(5.0, 0.4, 40)]\n)\nlabels = np.repeat([0, 1, 2], 40)",
    staticCall:
      'ax = dv.clustering.scatter_clusters_static(\n    x, y, labels, title="Cluster assignments"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.clustering.scatter_clusters_interactive(\n    x, y, labels, title="Cluster assignments"\n)\nfig.show()',
  },
  dendrogram: {
    useCase:
      "Use the dendrogram to read the full merge history of a hierarchical clustering as a tree. The height of each merge shows the distance at which clusters were combined, so long vertical gaps suggest natural places to cut the tree into flat clusters. It reveals nested subgroup structure that a single flat partition hides, and works for any number of clusters without choosing k up front.",
    setup:
      "linkage_matrix = np.array(\n    [\n        [0.0, 1.0, 0.15, 2.0],\n        [2.0, 3.0, 0.22, 2.0],\n        [4.0, 5.0, 0.18, 2.0],\n        [6.0, 7.0, 0.55, 4.0],\n        [8.0, 9.0, 1.10, 6.0],\n    ]\n)\nlabels = [\"S1\", \"S2\", \"S3\", \"S4\", \"S5\", \"S6\"]",
    staticCall:
      'ax = dv.clustering.dendrogram_static(\n    linkage_matrix, labels=labels, title="Hierarchical clustering"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.clustering.dendrogram_interactive(\n    linkage_matrix, labels=labels, title="Hierarchical clustering"\n)\nfig.show()',
  },
  elbow_plot: {
    useCase:
      "Use the elbow plot to pick the number of clusters for k-means by plotting within-cluster inertia against k. Inertia always falls as k grows, but the curve typically bends where adding another cluster stops paying off \u2014 the \u201celbow\u201d is the smallest k that captures most of the structure. When no clear bend appears, that is itself evidence that the data may not contain well-separated groups.",
    setup:
      "n_clusters = np.arange(1, 11)\ninertias = np.array(\n    [900.0, 420.0, 260.0, 190.0, 160.0, 140.0, 128.0, 120.0, 115.0, 110.0]\n)",
    staticCall:
      'ax = dv.clustering.elbow_plot_static(\n    n_clusters, inertias, elbow_idx=2, title="Elbow plot"\n)\nplt.show()',
    interactiveCall:
      'fig = dv.clustering.elbow_plot_interactive(\n    n_clusters, inertias, elbow_idx=2, title="Elbow plot"\n)\nfig.show()',
  },
};
