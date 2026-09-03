"""Curated Complete-example snippets for dataviz.spc API pages."""

EXAMPLES = {
    "dataviz.spc.attribute.g_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import g_chart_static

rng = np.random.default_rng(42)
counts = rng.geometric(p=0.02, size=30)

ax = g_chart_static(counts, title="Units between defects")
plt.show()
''',
    "dataviz.spc.attribute.g_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import g_chart_interactive

rng = np.random.default_rng(42)
counts = rng.geometric(p=0.02, size=30)

fig = g_chart_interactive(counts, title="Units between defects")
fig.show()
''',
    "dataviz.spc.attribute.t_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import t_chart_static

rng = np.random.default_rng(42)
times = rng.exponential(scale=2.0, size=30)

ax = t_chart_static(times, title="Hours between failures")
plt.show()
''',
    "dataviz.spc.attribute.t_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import t_chart_interactive

rng = np.random.default_rng(42)
times = rng.exponential(scale=2.0, size=30)

fig = t_chart_interactive(times, title="Hours between failures")
fig.show()
''',
    "dataviz.spc.attribute.laney_p_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.attribute import laney_p_chart_static

rng = np.random.default_rng(42)
defects = rng.binomial(n=100, p=0.05, size=30)
sample_sizes = rng.integers(low=80, high=150, size=30)

ax = laney_p_chart_static(defects, sample_sizes, title="Defect rate (p')")
plt.show()
''',
    "dataviz.spc.attribute.laney_p_chart_interactive": '''import numpy as np
from dataviz.spc.attribute import laney_p_chart_interactive

rng = np.random.default_rng(42)
defects = rng.binomial(n=100, p=0.05, size=30)
sample_sizes = rng.integers(low=80, high=150, size=30)

fig = laney_p_chart_interactive(defects, sample_sizes, title="Defect rate (p')")
fig.show()
''',
    "dataviz.spc.constants.get_d2": '''from dataviz.spc.constants import get_d2

result = get_d2(5)
print(result)
''',
    "dataviz.spc.variable.median_chart_static": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.spc.variable import median_chart_static

rng = np.random.default_rng(42)
data = rng.normal(loc=10.0, scale=0.4, size=30)

ax = median_chart_static(data, subgroup_size=5, title="Filling process")
plt.show()
''',
    "dataviz.spc.variable.median_chart_interactive": '''import numpy as np
from dataviz.spc.variable import median_chart_interactive

rng = np.random.default_rng(42)
data = rng.normal(loc=10.0, scale=0.4, size=30)

fig = median_chart_interactive(data, subgroup_size=5, title="Filling process")
fig.show()
''',
}
