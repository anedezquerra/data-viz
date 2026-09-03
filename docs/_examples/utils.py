"""Curated Complete-example snippets for dataviz.utils API pages."""

EXAMPLES = {
    "dataviz.utils.helpers.apply_theme": '''import matplotlib.pyplot as plt
from dataviz.utils.helpers import apply_theme

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])

apply_theme(ax, theme="default")
plt.show()
''',
    "dataviz.utils.validation.validate_positive_int": '''from dataviz.utils.validation import validate_positive_int

result = validate_positive_int(5, name="n")
print(result)
''',
    "dataviz.utils.validation.resolve_series": '''import numpy as np
import pandas as pd
from dataviz.utils.validation import resolve_series

rng = np.random.default_rng(42)
value = pd.Series(rng.normal(loc=10.0, scale=0.4, size=30), name="Value")

result = resolve_series(value)
print(result)
''',
    "dataviz.utils.validation.add_reference_lines": '''import numpy as np
import matplotlib.pyplot as plt
from dataviz.utils.validation import add_reference_lines

rng = np.random.default_rng(42)
fig, ax = plt.subplots()
ax.plot(np.arange(30), rng.normal(loc=10.0, scale=0.4, size=30))

add_reference_lines(ax, hline=10.0, vline=15)
plt.show()
''',
    "dataviz.utils.validation.add_plotly_reference_lines": '''import numpy as np
import plotly.graph_objects as go
from dataviz.utils.validation import add_plotly_reference_lines

rng = np.random.default_rng(42)
fig = go.Figure(go.Scatter(y=rng.normal(loc=10.0, scale=0.4, size=30)))

add_plotly_reference_lines(fig, hline=10.0)
fig.show()
''',
    "dataviz.utils.validation.numeric_dataframe": '''import numpy as np
import pandas as pd
from dataviz.utils.validation import numeric_dataframe

rng = np.random.default_rng(42)
df = pd.DataFrame({
    "Speed": rng.normal(loc=100.0, scale=5.0, size=30),
    "Pressure": rng.normal(loc=50.0, scale=2.0, size=30),
    "Label": rng.choice(["A", "B"], size=30),
})

result = numeric_dataframe(df)
print(result)
''',
}
