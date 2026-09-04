dataviz.univariate.categorical.frequency_bar_static
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.categorical</p></div>

.. currentmodule:: dataviz.univariate.categorical

.. autofunction:: frequency_bar_static

Use case
--------

Use to show how often each category occurs, with normalize=True when proportions matter more than raw counts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.categorical import frequency_bar_static

   # Exit-survey responses for a public library membership program
   rng = np.random.default_rng(42)
   ratings = pd.Series(
       rng.choice(
           ["Excellent", "Good", "Average", "Poor"],
           size=180,
           p=[0.45, 0.32, 0.16, 0.07],
       ),
       name="rating",
   )

   ax = frequency_bar_static(
       ratings,
       normalize=True,
       title="Library Exit Survey Ratings",
       xlabel="Rating",
       ylabel="Proportion of Responses",
       color="slateblue",
       rotation=0,
       theme="minimal",
   )
   ax.set_ylabel("Proportion of Responses")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/categorical/frequency_bar_static.png" alt="frequency_bar_static example output"><figcaption>Example output</figcaption></figure></div>
