dataviz.univariate.text.boolean_bar_static
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autofunction:: boolean_bar_static

Use case
--------

Use to plot true/false counts for a binary indicator as a semantic wrapper around categorical frequency bars.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.text import boolean_bar_static

   rng = np.random.default_rng(42)
   subscribed = pd.Series(rng.random(120) < 0.42, name="newsletter_subscribed")
   ax = boolean_bar_static(
       subscribed,
       title="Newsletter Subscription Status",
       color="seagreen",
       theme="minimal",
   )
   ax.set_ylabel("Number of customers")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/text/boolean_bar_static.png" alt="boolean_bar_static example output"><figcaption>Example output</figcaption></figure></div>
