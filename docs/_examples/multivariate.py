"""Curated Complete-example snippets for dataviz.multivariate API pages."""

EXAMPLES = {
    "dataviz.multivariate.charts.heatmap": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.charts import heatmap

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
})

ax = heatmap(df, title="Process heatmap")
plt.show()
''',
    "dataviz.multivariate.charts.parallel_coordinates": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.charts import parallel_coordinates

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
})

ax = parallel_coordinates(df, title="Parallel coordinates")
plt.show()
''',
    "dataviz.multivariate.heatmap.heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.heatmap import heatmap_static

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
})

ax = heatmap_static(df, title="Process heatmap")
plt.show()
''',
    "dataviz.multivariate.heatmap.heatmap_interactive": '''import numpy as np
import pandas as pd
from dataviz.multivariate.heatmap import heatmap_interactive

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
})

fig = heatmap_interactive(df, title="Process heatmap")
fig.show()
''',
}
