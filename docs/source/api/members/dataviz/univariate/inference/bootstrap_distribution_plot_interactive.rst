dataviz.univariate.inference.bootstrap_distribution_plot_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.inference</p></div>

.. currentmodule:: dataviz.univariate.inference

.. autofunction:: bootstrap_distribution_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.inference import bootstrap_distribution_plot_interactive

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   fig = bootstrap_distribution_plot_interactive(values, seed=42)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/inference/bootstrap_distribution_plot_interactive.png" alt="bootstrap_distribution_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
