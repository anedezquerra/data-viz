"""Curated Complete-example snippets for dataviz.clustering API pages."""

EXAMPLES = {
    "dataviz.clustering.charts.scatter_clusters": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.clustering.charts import scatter_clusters

rng = np.random.default_rng(42)
x = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
y = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
labels = np.repeat([0, 1], 20)

ax = scatter_clusters(x, y, labels, title="Cluster visualization")
plt.show()
''',
    "dataviz.clustering.scatter_clusters.scatter_clusters_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.clustering.scatter_clusters import scatter_clusters_static

rng = np.random.default_rng(42)
x = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
y = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
labels = np.repeat([0, 1], 20)

ax = scatter_clusters_static(x, y, labels, title="Cluster visualization")
plt.show()
''',
    "dataviz.clustering.scatter_clusters.scatter_clusters_interactive": '''import numpy as np
from dataviz.clustering.scatter_clusters import scatter_clusters_interactive

rng = np.random.default_rng(42)
x = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
y = np.concatenate([rng.normal(loc=0.0, size=20), rng.normal(loc=5.0, size=20)])
labels = np.repeat([0, 1], 20)

fig = scatter_clusters_interactive(x, y, labels, title="Cluster visualization")
fig.show()
''',
}
