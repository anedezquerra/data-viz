"""Curated Complete-example snippets for dataviz.univariate API pages."""

EXAMPLES = {
    "dataviz.univariate.accessors.resolve_univariate_data": '''import numpy as np
import pandas as pd
from dataviz.univariate.accessors import resolve_univariate_data

rng = np.random.default_rng(42)
value = pd.Series(rng.normal(loc=10.0, scale=0.4, size=30), name="Value")

result = resolve_univariate_data(value)
print(result)
''',
    "dataviz.univariate.advanced.ridgeline_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.univariate.advanced import ridgeline_plot_static

rng = np.random.default_rng(42)
data = pd.DataFrame({
    "Line A": rng.normal(loc=10.0, scale=0.4, size=50),
    "Line B": rng.normal(loc=10.5, scale=0.5, size=50),
    "Line C": rng.normal(loc=9.8, scale=0.3, size=50),
})

ax = ridgeline_plot_static(data, title="Ridgeline plot")
plt.show()
''',
    "dataviz.univariate.advanced.ridgeline_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.advanced import ridgeline_plot_interactive

rng = np.random.default_rng(42)
data = pd.DataFrame({
    "Line A": rng.normal(loc=10.0, scale=0.4, size=50),
    "Line B": rng.normal(loc=10.5, scale=0.5, size=50),
    "Line C": rng.normal(loc=9.8, scale=0.3, size=50),
})

fig = ridgeline_plot_interactive(data, title="Ridgeline plot")
fig.show()
''',
    "dataviz.univariate.ordinal.likert_summary": '''import numpy as np
import pandas as pd
from dataviz.univariate.ordinal import likert_summary

rng = np.random.default_rng(42)
order = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
data = pd.Series(rng.choice(order, size=60), name="Response")

result = likert_summary(data, order=order)
print(result)
''',
    "dataviz.univariate.profile.auto_profile": '''import numpy as np
import pandas as pd
from dataviz.univariate.profile import auto_profile

rng = np.random.default_rng(42)
value = pd.Series(rng.normal(loc=10.0, scale=0.4, size=30), name="Value")

result = auto_profile(value)
print(result)
''',
    "dataviz.univariate.profile.auto_profile_chart_interactive": '''import numpy as np
import pandas as pd
from dataviz.univariate.profile import auto_profile_chart_interactive

rng = np.random.default_rng(42)
value = pd.Series(rng.normal(loc=10.0, scale=0.4, size=30), name="Value")

fig = auto_profile_chart_interactive(value, title="Automatic profile")
fig.show()
''',
    "dataviz.univariate.robust.validate_proportion": '''from dataviz.univariate.robust import validate_proportion

result = validate_proportion(0.05, name="alpha")
print(result)
''',
}
