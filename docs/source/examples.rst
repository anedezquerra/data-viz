Examples
========

Univariate profiling
--------------------

.. code-block:: python

   import pandas as pd
   import dataviz as dv

   sales = pd.Series([105, 112, 98, 121, 119, 110], name="Sales")
   profile = dv.auto_profile(sales)
   interval = dv.bootstrap_ci(sales, statistic="mean", seed=42)
   figure = dv.auto_profile_chart_interactive(sales)

   print(profile)
   print(interval)
   figure.show()

Bivariate analysis
------------------

.. code-block:: python

   import pandas as pd
   import dataviz as dv

   height = pd.Series([160, 168, 172, 180, 185], name="Height")
   weight = pd.Series([58, 66, 71, 82, 89], name="Weight")

   summary = dv.bivariate_summary(height, weight)
   ax = dv.regression_plot(height, weight)
   fig = dv.joint_scatter_hist_interactive(height, weight)

   print(summary)
   ax.figure.show()
   fig.show()

Statistical process control
---------------------------

.. code-block:: python

   import pandas as pd
   import dataviz as dv

   diameter = pd.Series([10.1, 9.9, 10.2, 10.4, 10.0, 9.8])
   limits = dv.spc.individuals_limits(diameter)
   violations = dv.spc.detect_rule_violations(diameter, limits)
   capability = dv.spc.capability_summary(diameter, lsl=9.5, usl=10.5)
   dashboard = dv.spc.spc_dashboard_interactive(diameter)

   print(violations)
   print(capability)
   dashboard.show()
