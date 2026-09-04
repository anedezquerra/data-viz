dataviz.univariate.dashboard.univariate_analysis_dashboard_interactive
======================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.dashboard</p></div>

.. currentmodule:: dataviz.univariate.dashboard

.. autofunction:: univariate_analysis_dashboard_interactive

Use case
--------

Use to get a multi-panel interactive overview of one variable combining several univariate views in a single figure.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.dashboard import univariate_analysis_dashboard_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = univariate_analysis_dashboard_interactive(values)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/dashboard/univariate_analysis_dashboard_interactive.png" alt="univariate_analysis_dashboard_interactive example output"><figcaption>Example output</figcaption></figure></div>
