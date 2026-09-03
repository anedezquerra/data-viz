"""Curated Complete-example snippets for dataviz.eda API pages."""

EXAMPLES = {
    "dataviz.eda.charts.class_distribution": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.charts import class_distribution

rng = np.random.default_rng(42)
series = pd.Series(rng.choice(["Pass", "Fail", "Rework"], size=60, p=[0.8, 0.1, 0.1]), name="Result")

ax = class_distribution(series, title="Class distribution")
plt.show()
''',
    "dataviz.eda.class_dist.class_distribution_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.class_dist import class_distribution_static

rng = np.random.default_rng(42)
series = pd.Series(rng.choice(["Pass", "Fail", "Rework"], size=60, p=[0.8, 0.1, 0.1]), name="Result")

ax = class_distribution_static(series, title="Class distribution")
plt.show()
''',
    "dataviz.eda.class_dist.class_distribution_interactive": '''import numpy as np
import pandas as pd
from dataviz.eda.class_dist import class_distribution_interactive

rng = np.random.default_rng(42)
series = pd.Series(rng.choice(["Pass", "Fail", "Rework"], size=60, p=[0.8, 0.1, 0.1]), name="Result")

fig = class_distribution_interactive(series, title="Class distribution")
fig.show()
''',
}
