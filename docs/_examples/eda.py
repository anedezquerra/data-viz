"""Curated Complete-example snippets for dataviz.eda API pages."""

EXAMPLES = {
    "dataviz.eda.charts.missing_data_plot": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.charts import missing_data_plot

rng = np.random.default_rng(42)
n = 100
df = pd.DataFrame({
    "Customer ID": np.arange(1, n + 1),
    "Age": rng.integers(18, 75, size=n).astype(float),
    "Income": rng.normal(loc=60000.0, scale=15000.0, size=n),
    "Email": rng.choice(["user@example.com", None], size=n, p=[0.8, 0.2]),
    "Last purchase": rng.choice(["2024-05-01", None], size=n, p=[0.9, 0.1]),
})
df.loc[rng.choice(n, size=12, replace=False), "Age"] = np.nan
df.loc[rng.choice(n, size=8, replace=False), "Income"] = np.nan

ax = missing_data_plot(df, title="CRM Export Missing Data Profile")
plt.show()
''',
    "dataviz.eda.charts.distribution_summary": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.charts import distribution_summary

rng = np.random.default_rng(42)
n = 120
df = pd.DataFrame({
    "Order value (USD)": rng.lognormal(mean=4.0, sigma=0.5, size=n),
    "Items per order": rng.poisson(lam=3.0, size=n),
    "Discount (%)": rng.uniform(low=0.0, high=25.0, size=n),
    "Delivery days": rng.integers(1, 10, size=n).astype(float),
})

fig = distribution_summary(df, title="Order Metrics Distribution Summary")
plt.show()
''',
    "dataviz.eda.charts.class_distribution": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.charts import class_distribution

rng = np.random.default_rng(42)
tickets = pd.Series(
    rng.choice(["Low", "Medium", "High", "Critical"], size=150, p=[0.45, 0.3, 0.18, 0.07]),
    name="Ticket priority",
)

ax = class_distribution(tickets, title="Support Ticket Priority Balance")
plt.show()
''',
    "dataviz.eda.class_dist.class_distribution_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.class_dist import class_distribution_static

rng = np.random.default_rng(42)
tickets = pd.Series(
    rng.choice(["Low", "Medium", "High", "Critical"], size=150, p=[0.45, 0.3, 0.18, 0.07]),
    name="Ticket priority",
)

ax = class_distribution_static(
    tickets,
    title="Support Ticket Priority Balance",
    color="steelblue",
    sort=True,
)
plt.show()
''',
    "dataviz.eda.class_dist.class_distribution_interactive": '''import numpy as np
import pandas as pd
from dataviz.eda.class_dist import class_distribution_interactive

rng = np.random.default_rng(42)
tickets = pd.Series(
    rng.choice(["Low", "Medium", "High", "Critical"], size=150, p=[0.45, 0.3, 0.18, 0.07]),
    name="Ticket priority",
)

fig = class_distribution_interactive(
    tickets,
    title="Support Ticket Priority Balance",
    color="steelblue",
    sort=True,
)
fig.show()
''',
    "dataviz.eda.distribution.distribution_summary_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.distribution import distribution_summary_static

rng = np.random.default_rng(42)
n = 120
df = pd.DataFrame({
    "Order value (USD)": rng.lognormal(mean=4.0, sigma=0.5, size=n),
    "Items per order": rng.poisson(lam=3.0, size=n),
    "Discount (%)": rng.uniform(low=0.0, high=25.0, size=n),
    "Delivery days": rng.integers(1, 10, size=n).astype(float),
})

fig = distribution_summary_static(
    df,
    title="Order Metrics Distribution Summary",
    bins=25,
    color="slategray",
)
plt.show()
''',
    "dataviz.eda.distribution.distribution_summary_interactive": '''import numpy as np
import pandas as pd
from dataviz.eda.distribution import distribution_summary_interactive

rng = np.random.default_rng(42)
n = 120
df = pd.DataFrame({
    "Order value (USD)": rng.lognormal(mean=4.0, sigma=0.5, size=n),
    "Items per order": rng.poisson(lam=3.0, size=n),
    "Discount (%)": rng.uniform(low=0.0, high=25.0, size=n),
    "Delivery days": rng.integers(1, 10, size=n).astype(float),
})

fig = distribution_summary_interactive(
    df,
    title="Order Metrics Distribution Summary",
    bins=25,
)
fig.show()
''',
    "dataviz.eda.missing_data.missing_data_plot_static": '''import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dataviz.eda.missing_data import missing_data_plot_static

rng = np.random.default_rng(42)
n = 100
df = pd.DataFrame({
    "Customer ID": np.arange(1, n + 1),
    "Age": rng.integers(18, 75, size=n).astype(float),
    "Income": rng.normal(loc=60000.0, scale=15000.0, size=n),
    "Email": rng.choice(["user@example.com", None], size=n, p=[0.8, 0.2]),
    "Last purchase": rng.choice(["2024-05-01", None], size=n, p=[0.9, 0.1]),
})
df.loc[rng.choice(n, size=12, replace=False), "Age"] = np.nan
df.loc[rng.choice(n, size=8, replace=False), "Income"] = np.nan

ax = missing_data_plot_static(
    df,
    title="CRM Export Missing Data Profile",
    color="indianred",
)
plt.show()
''',
    "dataviz.eda.missing_data.missing_data_plot_interactive": '''import numpy as np
import pandas as pd
from dataviz.eda.missing_data import missing_data_plot_interactive

rng = np.random.default_rng(42)
n = 100
df = pd.DataFrame({
    "Customer ID": np.arange(1, n + 1),
    "Age": rng.integers(18, 75, size=n).astype(float),
    "Income": rng.normal(loc=60000.0, scale=15000.0, size=n),
    "Email": rng.choice(["user@example.com", None], size=n, p=[0.8, 0.2]),
    "Last purchase": rng.choice(["2024-05-01", None], size=n, p=[0.9, 0.1]),
})
df.loc[rng.choice(n, size=12, replace=False), "Age"] = np.nan
df.loc[rng.choice(n, size=8, replace=False), "Income"] = np.nan

fig = missing_data_plot_interactive(
    df,
    title="CRM Export Missing Data Profile",
    color="indianred",
)
fig.show()
''',
}
