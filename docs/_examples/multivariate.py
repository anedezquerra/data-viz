"""Curated Complete-example snippets for dataviz.multivariate API pages."""

EXAMPLES = {
    "dataviz.multivariate.charts.pairplot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.charts import pairplot

rng = np.random.default_rng(42)
n = 80
horsepower = rng.normal(loc=150.0, scale=30.0, size=n)
df = pd.DataFrame({
    "Horsepower": horsepower,
    "Weight (kg)": 1200.0 + 3.0 * horsepower + rng.normal(loc=0.0, scale=100.0, size=n),
    "Fuel economy (mpg)": 45.0 - 0.08 * horsepower + rng.normal(loc=0.0, scale=2.0, size=n),
    "Price (k USD)": 15.0 + 0.12 * horsepower + rng.normal(loc=0.0, scale=3.0, size=n),
})

fig = pairplot(df, title="Vehicle Specs Pairplot")
plt.show()
''',
    "dataviz.multivariate.charts.heatmap": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.charts import heatmap

rng = np.random.default_rng(42)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [f"{h}:00" for h in range(6, 22, 2)]
traffic = rng.integers(50, 500, size=(len(days), len(hours))).astype(float)
traffic[5:, :3] *= 0.4
df = pd.DataFrame(traffic, index=days, columns=hours)

ax = heatmap(df, title="Store Foot Traffic by Day and Hour", cmap="YlOrRd")
plt.show()
''',
    "dataviz.multivariate.charts.parallel_coordinates": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.charts import parallel_coordinates

rng = np.random.default_rng(42)
n = 60
df = pd.DataFrame({
    "Battery (h)": rng.normal(loc=12.0, scale=2.0, size=n),
    "Weight (g)": rng.normal(loc=180.0, scale=25.0, size=n),
    "Screen (in)": rng.normal(loc=6.1, scale=0.4, size=n),
    "Price (USD)": rng.normal(loc=700.0, scale=150.0, size=n),
    "Rating": rng.uniform(low=3.0, high=5.0, size=n),
})

ax = parallel_coordinates(df, title="Smartphone Model Comparison")
plt.show()
''',
    "dataviz.multivariate.heatmap.heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.heatmap import heatmap_static

rng = np.random.default_rng(42)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [f"{h}:00" for h in range(6, 22, 2)]
traffic = rng.integers(50, 500, size=(len(days), len(hours))).astype(float)
traffic[5:, :3] *= 0.4
df = pd.DataFrame(traffic, index=days, columns=hours)

ax = heatmap_static(
    df,
    title="Store Foot Traffic by Day and Hour",
    cmap="YlOrRd",
    fmt=".0f",
    linewidths=0.4,
)
plt.show()
''',
    "dataviz.multivariate.heatmap.heatmap_interactive": '''import numpy as np
import pandas as pd
from dataviz.multivariate.heatmap import heatmap_interactive

rng = np.random.default_rng(42)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [f"{h}:00" for h in range(6, 22, 2)]
traffic = rng.integers(50, 500, size=(len(days), len(hours))).astype(float)
traffic[5:, :3] *= 0.4
df = pd.DataFrame(traffic, index=days, columns=hours)

fig = heatmap_interactive(
    df,
    title="Store Foot Traffic by Day and Hour",
    colorscale="YlOrRd",
)
fig.show()
''',
    "dataviz.multivariate.pairplot.pairplot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.pairplot import pairplot_static

rng = np.random.default_rng(42)
n = 80
horsepower = rng.normal(loc=150.0, scale=30.0, size=n)
df = pd.DataFrame({
    "Horsepower": horsepower,
    "Weight (kg)": 1200.0 + 3.0 * horsepower + rng.normal(loc=0.0, scale=100.0, size=n),
    "Fuel economy (mpg)": 45.0 - 0.08 * horsepower + rng.normal(loc=0.0, scale=2.0, size=n),
    "Price (k USD)": 15.0 + 0.12 * horsepower + rng.normal(loc=0.0, scale=3.0, size=n),
})

fig = pairplot_static(
    df,
    title="Vehicle Specs Pairplot",
    diag_kind="hist",
    plot_kind="scatter",
    bins=15,
    alpha=0.6,
)
plt.show()
''',
    "dataviz.multivariate.pairplot.pairplot_interactive": '''import numpy as np
import pandas as pd
from dataviz.multivariate.pairplot import pairplot_interactive

rng = np.random.default_rng(42)
n = 80
horsepower = rng.normal(loc=150.0, scale=30.0, size=n)
df = pd.DataFrame({
    "Horsepower": horsepower,
    "Weight (kg)": 1200.0 + 3.0 * horsepower + rng.normal(loc=0.0, scale=100.0, size=n),
    "Fuel economy (mpg)": 45.0 - 0.08 * horsepower + rng.normal(loc=0.0, scale=2.0, size=n),
    "Price (k USD)": 15.0 + 0.12 * horsepower + rng.normal(loc=0.0, scale=3.0, size=n),
})

fig = pairplot_interactive(
    df,
    title="Vehicle Specs Pairplot",
    marker_size=5,
)
fig.show()
''',
    "dataviz.multivariate.parallel.parallel_coordinates_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.multivariate.parallel import parallel_coordinates_static

rng = np.random.default_rng(42)
n = 60
df = pd.DataFrame({
    "Battery (h)": rng.normal(loc=12.0, scale=2.0, size=n),
    "Weight (g)": rng.normal(loc=180.0, scale=25.0, size=n),
    "Screen (in)": rng.normal(loc=6.1, scale=0.4, size=n),
    "Price (USD)": rng.normal(loc=700.0, scale=150.0, size=n),
    "Rating": rng.uniform(low=3.0, high=5.0, size=n),
})

ax = parallel_coordinates_static(
    df,
    title="Smartphone Model Comparison",
    alpha=0.4,
    linewidth=1.2,
)
plt.show()
''',
    "dataviz.multivariate.parallel.parallel_coordinates_interactive": '''import numpy as np
import pandas as pd
from dataviz.multivariate.parallel import parallel_coordinates_interactive

rng = np.random.default_rng(42)
n = 60
df = pd.DataFrame({
    "Battery (h)": rng.normal(loc=12.0, scale=2.0, size=n),
    "Weight (g)": rng.normal(loc=180.0, scale=25.0, size=n),
    "Screen (in)": rng.normal(loc=6.1, scale=0.4, size=n),
    "Price (USD)": rng.normal(loc=700.0, scale=150.0, size=n),
    "Rating": rng.uniform(low=3.0, high=5.0, size=n),
})

fig = parallel_coordinates_interactive(
    df,
    title="Smartphone Model Comparison",
    color_col="Rating",
    colorscale="Viridis",
)
fig.show()
''',
}
