"""Curated Complete-example snippets for dataviz.bivariate API pages."""

EXAMPLES = {
    "dataviz.bivariate.advanced.bubble_plot_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.bivariate.advanced import bubble_plot_static

rng = np.random.default_rng(42)
x = rng.normal(loc=10.0, scale=2.0, size=30)
y = 2.0 * x + rng.normal(loc=0.0, scale=1.0, size=30)
size = rng.uniform(low=10.0, high=100.0, size=30)

ax = bubble_plot_static(x, y, size, title="Bubble plot")
plt.show()
''',
    "dataviz.bivariate.advanced.bubble_plot_interactive": '''import numpy as np
from dataviz.bivariate.advanced import bubble_plot_interactive

rng = np.random.default_rng(42)
x = rng.normal(loc=10.0, scale=2.0, size=30)
y = 2.0 * x + rng.normal(loc=0.0, scale=1.0, size=30)
size = rng.uniform(low=10.0, high=100.0, size=30)

fig = bubble_plot_interactive(x, y, size, title="Bubble plot")
fig.show()
''',
    "dataviz.bivariate.categorical.grouped_bar_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.categorical import grouped_bar_static

rng = np.random.default_rng(42)
category = pd.Series(np.repeat(["Line A", "Line B", "Line C"], 10), name="Line")
values = pd.Series(rng.normal(loc=10.0, scale=1.0, size=30), name="Output")

ax = grouped_bar_static(category, values, title="Mean output by line")
plt.show()
''',
    "dataviz.bivariate.categorical.grouped_bar_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.categorical import grouped_bar_interactive

rng = np.random.default_rng(42)
category = pd.Series(np.repeat(["Line A", "Line B", "Line C"], 10), name="Line")
values = pd.Series(rng.normal(loc=10.0, scale=1.0, size=30), name="Output")

fig = grouped_bar_interactive(category, values, title="Mean output by line")
fig.show()
''',
    "dataviz.bivariate.categorical.crosstab_heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.categorical import crosstab_heatmap_static

rng = np.random.default_rng(42)
row_category = pd.Series(rng.choice(["Line A", "Line B", "Line C"], size=60), name="Line")
column_category = pd.Series(rng.choice(["Pass", "Fail"], size=60), name="Result")

ax = crosstab_heatmap_static(row_category, column_category, normalize="index")
plt.show()
''',
    "dataviz.bivariate.categorical.crosstab_heatmap_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.categorical import crosstab_heatmap_interactive

rng = np.random.default_rng(42)
row_category = pd.Series(rng.choice(["Line A", "Line B", "Line C"], size=60), name="Line")
column_category = pd.Series(rng.choice(["Pass", "Fail"], size=60), name="Result")

fig = crosstab_heatmap_interactive(row_category, column_category, normalize="index")
fig.show()
''',
    "dataviz.bivariate.charts.scatter_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.charts import scatter_plot

rng = np.random.default_rng(42)
x = pd.Series(rng.normal(loc=10.0, scale=2.0, size=30), name="Input")
y = pd.Series(2.0 * x + rng.normal(loc=0.0, scale=1.0, size=30), name="Output")

ax = scatter_plot(x, y, title="Input vs output")
plt.show()
''',
    "dataviz.bivariate.charts.line_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.charts import line_plot

rng = np.random.default_rng(42)
x = pd.Series(np.arange(30), name="Day")
y = pd.Series(np.cumsum(rng.normal(loc=0.1, scale=1.0, size=30)), name="Output")

ax = line_plot(x, y, title="Output over time")
plt.show()
''',
    "dataviz.bivariate.charts.correlation_heatmap": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.charts import correlation_heatmap

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
})

ax = correlation_heatmap(df, title="Process correlation")
plt.show()
''',
    "dataviz.bivariate.correlation.correlation_heatmap_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.bivariate.correlation import correlation_heatmap_static

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
})

ax = correlation_heatmap_static(df, title="Process correlation")
plt.show()
''',
    "dataviz.bivariate.correlation.correlation_heatmap_interactive": '''import numpy as np
import pandas as pd
from dataviz.bivariate.correlation import correlation_heatmap_interactive

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Yield": rng.normal(loc=90.0, scale=3.0, size=30),
})

fig = correlation_heatmap_interactive(df, title="Process correlation")
fig.show()
''',
    "dataviz.bivariate.trends.area_between_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.bivariate.trends import area_between_static

x = np.arange(30)
y_lower = np.sin(x / 5.0)
y_upper = y_lower + 0.5

ax = area_between_static(x, y_lower, y_upper, title="Tolerance band")
plt.show()
''',
    "dataviz.bivariate.trends.area_between_interactive": '''import numpy as np
from dataviz.bivariate.trends import area_between_interactive

x = np.arange(30)
y_lower = np.sin(x / 5.0)
y_upper = y_lower + 0.5

fig = area_between_interactive(x, y_lower, y_upper, title="Tolerance band")
fig.show()
''',
}
