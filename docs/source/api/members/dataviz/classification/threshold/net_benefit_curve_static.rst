dataviz.classification.threshold.net_benefit_curve_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold</p></div>

.. currentmodule:: dataviz.classification.threshold

.. autofunction:: net_benefit_curve_static

Use case
--------

Use for decision-curve analysis in clinical or policy settings; compares model net benefit against treat-all and treat-none.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold import net_benefit_curve_static

   rng = np.random.default_rng(42)
   # medical screening: decision-curve analysis vs treat-all / treat-none
   n = 150
   y_true = (rng.random(n) < 0.2).astype(int)
   y_prob = np.clip(
       y_true * rng.beta(6, 2.5, n) + (1 - y_true) * rng.beta(2.5, 6, n), 0, 1)

   ax = net_benefit_curve_static(y_true, y_prob,
                                 title="Screening test: net benefit")
   ax.set_ylim(-0.05, 0.25)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold/net_benefit_curve_static.png" alt="net_benefit_curve_static example output"><figcaption>Example output</figcaption></figure></div>
