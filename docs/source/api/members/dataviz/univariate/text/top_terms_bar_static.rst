dataviz.univariate.text.top_terms_bar_static
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autofunction:: top_terms_bar_static

Use case
--------

Use to chart the most common terms in a text column for quick exploratory profiling.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   import matplotlib.pyplot as plt
   from dataviz.univariate.text import top_terms_bar_static

   rng = np.random.default_rng(42)
   vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
   reviews = pd.Series(
       [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
       name="review",
   )
   ax = top_terms_bar_static(
       reviews,
       top_n=8,
       title="Most Common Terms in Product Reviews",
       color="coral",
       theme="minimal",
   )
   ax.set_xlabel("Occurrences")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/text/top_terms_bar_static.png" alt="top_terms_bar_static example output"><figcaption>Example output</figcaption></figure></div>
