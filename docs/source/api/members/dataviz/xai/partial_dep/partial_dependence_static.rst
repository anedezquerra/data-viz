dataviz.xai.partial_dep.partial_dependence_static
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.partial_dep</p></div>

.. currentmodule:: dataviz.xai.partial_dep

.. autofunction:: partial_dependence_static

Use case
--------

Use to show the average marginal effect of one feature on predictions, with optional confidence band and rug marks for data density.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.partial_dep import partial_dependence_static

   rng = np.random.default_rng(42)
   credit_score = np.linspace(300, 850, 40)
   logit = -4.0 + 0.010 * (credit_score - 300)
   predictions = 1.0 / (1.0 + np.exp(-logit))
   predictions = predictions + rng.normal(0, 0.01, size=credit_score.size)
   spread = 0.04 + 0.02 * (credit_score - 300) / 550
   ci = np.column_stack([predictions - spread, predictions + spread])
   ax = partial_dependence_static(
       credit_score, predictions, feature_name="credit_score",
       title="Partial dependence of default risk on credit score",
       ylabel="Predicted default probability", color="darkred",
       show_confidence=True, confidence_interval=ci,
   )
   ax.set_ylim(0, 1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/partial_dep/partial_dependence_static.png" alt="partial_dependence_static example output"><figcaption>Example output</figcaption></figure></div>
