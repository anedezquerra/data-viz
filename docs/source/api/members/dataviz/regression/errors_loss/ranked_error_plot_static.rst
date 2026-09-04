dataviz.regression.errors_loss.ranked_error_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: ranked_error_plot_static

Use case
--------

Use to see how quickly errors grow from typical to worst case by plotting errors sorted by magnitude.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.regression.errors_loss import ranked_error_plot_static

   rng = np.random.default_rng(42)
   actual = pd.Series(rng.uniform(200, 900, 28), name="actual_repair_cost")
   predicted = pd.Series(actual * rng.normal(1.0, 0.12, 28),
                         name="predicted_repair_cost")
   errors = actual - predicted

   ax = ranked_error_plot_static(errors,
                                 title="Repair Cost Model: Ranked Errors",
                                 color="#c0392b")
   ax.set_xlabel("Rank (sorted by error)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/ranked_error_plot_static.png" alt="ranked_error_plot_static example output"><figcaption>Example output</figcaption></figure></div>
