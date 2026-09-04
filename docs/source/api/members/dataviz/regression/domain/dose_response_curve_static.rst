dataviz.regression.domain.dose_response_curve_static
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: dose_response_curve_static

Use case
--------

Use in pharmacology or toxicology to plot response versus dose with an optional CI band and log-scaled dose axis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.domain import dose_response_curve_static

   rng = np.random.default_rng(42)
   dose = pd.Series(np.logspace(-1, 2, 14), name="dose_mg")
   response = pd.Series(100 / (1 + (dose / 12) ** -1.1) + rng.normal(0, 3, 14),
                        name="response_pct")
   lo = response - 6.0
   hi = response + 6.0

   ax = dose_response_curve_static(dose, response, lower=lo, upper=hi,
                                   title="Compound B: Dose-Response (EC50)",
                                   color="#2a7f62")
   ax.set_ylabel("Response (% of max)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/domain/dose_response_curve_static.png" alt="dose_response_curve_static example output"><figcaption>Example output</figcaption></figure></div>
