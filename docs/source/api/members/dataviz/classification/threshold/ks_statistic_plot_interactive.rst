dataviz.classification.threshold.ks_statistic_plot_interactive
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold</p></div>

.. currentmodule:: dataviz.classification.threshold

.. autofunction:: ks_statistic_plot_interactive

Use case
--------

Use in credit scoring to measure class separation; plots class CDFs and marks the maximum KS gap.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.threshold import ks_statistic_plot_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = ks_statistic_plot_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold/ks_statistic_plot_interactive.png" alt="ks_statistic_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
