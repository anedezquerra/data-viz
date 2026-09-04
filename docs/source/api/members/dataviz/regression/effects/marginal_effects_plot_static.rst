dataviz.regression.effects.marginal_effects_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.effects</p></div>

.. currentmodule:: dataviz.regression.effects

.. autofunction:: marginal_effects_plot_static

Use case
--------

Use to report average marginal effect per feature with optional confidence intervals, e.g. for econometric model interpretation.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.regression.effects import marginal_effects_plot_static

   features = ["discount_pct", "shelf_position", "weekend", "ad_impressions_k"]
   effects = np.array([1.9, 0.7, 0.4, 0.15])
   lo = effects - np.array([0.4, 0.3, 0.35, 0.2])
   hi = effects + np.array([0.45, 0.3, 0.35, 0.22])

   ax = marginal_effects_plot_static(
       features, effects, ci_lower=lo, ci_upper=hi,
       title="Promo Response Model: Average Marginal Effects",
       color="#2a7f62")
   ax.set_xlabel("Effect on daily units sold")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/effects/marginal_effects_plot_static.png" alt="marginal_effects_plot_static example output"><figcaption>Example output</figcaption></figure></div>
