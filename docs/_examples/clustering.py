"""Curated Complete-example snippets for dataviz.clustering API pages."""

EXAMPLES = {
    "dataviz.clustering.charts.scatter_clusters": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.clustering.charts import scatter_clusters

rng = np.random.default_rng(42)
centers = [(2.0, 2.0), (8.0, 3.0), (5.0, 9.0)]
points = [rng.normal(loc=c, scale=0.9, size=(30, 2)) for c in centers]
data = np.vstack(points)
labels = np.repeat([0, 1, 2], 30)

ax = scatter_clusters(data[:, 0], data[:, 1], labels, title="Customer Segment Clusters")
plt.show()
''',
    "dataviz.clustering.charts.elbow_plot": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.clustering.charts import elbow_plot

n_clusters = np.arange(1, 11)
inertias = np.array([520.0, 210.0, 120.0, 90.0, 74.0, 66.0, 61.0, 57.0, 54.0, 52.0])

ax = elbow_plot(n_clusters, inertias, title="K-Means Elbow Plot")
plt.show()
''',
    "dataviz.clustering.charts.dendrogram": '''import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from dataviz.clustering.charts import dendrogram

rng = np.random.default_rng(42)
data = np.vstack([
    rng.normal(loc=0.0, scale=0.8, size=(10, 2)),
    rng.normal(loc=5.0, scale=0.8, size=(10, 2)),
    rng.normal(loc=[5.0, 0.0], scale=0.8, size=(10, 2)),
])
linkage_matrix = linkage(data, method="ward")
labels = [f"Sensor {i + 1}" for i in range(len(data))]

ax = dendrogram(linkage_matrix, labels=labels, title="Sensor Network Dendrogram")
plt.show()
''',
    "dataviz.clustering.dendrogram.dendrogram_static": '''import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from dataviz.clustering.dendrogram import dendrogram_static

rng = np.random.default_rng(42)
data = np.vstack([
    rng.normal(loc=0.0, scale=0.8, size=(10, 2)),
    rng.normal(loc=5.0, scale=0.8, size=(10, 2)),
    rng.normal(loc=[5.0, 0.0], scale=0.8, size=(10, 2)),
])
linkage_matrix = linkage(data, method="ward")
labels = [f"Sensor {i + 1}" for i in range(len(data))]

ax = dendrogram_static(
    linkage_matrix,
    labels=labels,
    title="Sensor Network Dendrogram",
    color_threshold=4.0,
    leaf_font_size=9,
)
plt.show()
''',
    "dataviz.clustering.dendrogram.dendrogram_interactive": '''import numpy as np
from scipy.cluster.hierarchy import linkage
from dataviz.clustering.dendrogram import dendrogram_interactive

rng = np.random.default_rng(42)
data = np.vstack([
    rng.normal(loc=0.0, scale=0.8, size=(10, 2)),
    rng.normal(loc=5.0, scale=0.8, size=(10, 2)),
    rng.normal(loc=[5.0, 0.0], scale=0.8, size=(10, 2)),
])
linkage_matrix = linkage(data, method="ward")
labels = [f"Sensor {i + 1}" for i in range(len(data))]

fig = dendrogram_interactive(
    linkage_matrix,
    labels=labels,
    title="Sensor Network Dendrogram",
    color_threshold=4.0,
)
fig.show()
''',
    "dataviz.clustering.elbow.elbow_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.clustering.elbow import elbow_plot_static

n_clusters = np.arange(1, 11)
inertias = np.array([520.0, 210.0, 120.0, 90.0, 74.0, 66.0, 61.0, 57.0, 54.0, 52.0])

ax = elbow_plot_static(
    n_clusters,
    inertias,
    title="K-Means Elbow Plot",
    color="darkslateblue",
    elbow_idx=2,
)
plt.show()
''',
    "dataviz.clustering.elbow.elbow_plot_interactive": '''import numpy as np
from dataviz.clustering.elbow import elbow_plot_interactive

n_clusters = np.arange(1, 11)
inertias = np.array([520.0, 210.0, 120.0, 90.0, 74.0, 66.0, 61.0, 57.0, 54.0, 52.0])

fig = elbow_plot_interactive(
    n_clusters,
    inertias,
    title="K-Means Elbow Plot",
    line_color="darkslateblue",
    elbow_idx=2,
)
fig.show()
''',
    "dataviz.clustering.elbow_enhanced.elbow_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.clustering.elbow_enhanced import elbow_plot_static

n_clusters = np.arange(1, 11)
inertias = np.array([520.0, 210.0, 120.0, 90.0, 74.0, 66.0, 61.0, 57.0, 54.0, 52.0])

ax = elbow_plot_static(
    n_clusters,
    inertias,
    title="Customer Segmentation Elbow",
    color="teal",
    elbow_idx=2,
    elbow_color="crimson",
    grid=True,
)
plt.show()
''',
    "dataviz.clustering.elbow_enhanced.elbow_plot_interactive": '''import numpy as np
from dataviz.clustering.elbow_enhanced import elbow_plot_interactive

n_clusters = np.arange(1, 11)
inertias = np.array([520.0, 210.0, 120.0, 90.0, 74.0, 66.0, 61.0, 57.0, 54.0, 52.0])

fig = elbow_plot_interactive(
    n_clusters,
    inertias,
    title="Customer Segmentation Elbow",
    line_color="teal",
    elbow_idx=2,
    elbow_color="crimson",
)
fig.show()
''',
    "dataviz.clustering.scatter_clusters.scatter_clusters_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.clustering.scatter_clusters import scatter_clusters_static

rng = np.random.default_rng(42)
centers = [(2.0, 2.0), (8.0, 3.0), (5.0, 9.0)]
points = [rng.normal(loc=c, scale=0.9, size=(30, 2)) for c in centers]
data = np.vstack(points)
labels = np.repeat([0, 1, 2], 30)

ax = scatter_clusters_static(
    data[:, 0],
    data[:, 1],
    labels,
    title="Customer Segment Clusters",
    xlabel="Annual spending (k USD)",
    ylabel="Visit frequency",
    show_centroids=True,
)
plt.show()
''',
    "dataviz.clustering.scatter_clusters.scatter_clusters_interactive": '''import numpy as np
from dataviz.clustering.scatter_clusters import scatter_clusters_interactive

rng = np.random.default_rng(42)
centers = [(2.0, 2.0), (8.0, 3.0), (5.0, 9.0)]
points = [rng.normal(loc=c, scale=0.9, size=(30, 2)) for c in centers]
data = np.vstack(points)
labels = np.repeat([0, 1, 2], 30)

fig = scatter_clusters_interactive(
    data[:, 0],
    data[:, 1],
    labels,
    title="Customer Segment Clusters",
    xlabel="Annual spending (k USD)",
    ylabel="Visit frequency",
    show_centroids=True,
)
fig.show()
''',
}
