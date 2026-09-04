dataviz.univariate.datetime.event_frequency_plot_static
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.datetime</p></div>

.. currentmodule:: dataviz.univariate.datetime

.. autofunction:: event_frequency_plot_static

Use case
--------

Use to chart how event counts evolve over time from raw datetime observations at a chosen frequency.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.datetime import event_frequency_plot_static

   # Newsletter signup timestamps exported from a marketing platform
   rng = np.random.default_rng(42)
   signups = pd.Series(
       pd.Timestamp("2026-01-05")
       + pd.to_timedelta(rng.uniform(0, 90 * 24, size=40), unit="h"),
       name="signup_time",
   )

   ax = event_frequency_plot_static(
       signups,
       freq="W",
       title="Weekly Newsletter Signups",
       xlabel="Week",
       ylabel="Signups",
       color="darkcyan",
       theme="minimal",
   )
   ax.set_ylabel("Signups")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/datetime/event_frequency_plot_static.png" alt="event_frequency_plot_static example output"><figcaption>Example output</figcaption></figure></div>
