dataviz.univariate.stats.recommended_bin_count
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.stats</p></div>

.. currentmodule:: dataviz.univariate.stats

.. autofunction:: recommended_bin_count

Use case
--------

Use to pick a defensible histogram bin count from Freedman-Diaconis, Sturges, Rice, or square-root rules.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.stats import recommended_bin_count

   rng = np.random.default_rng(42)
   session_seconds = pd.Series(
       rng.normal(loc=180.0, scale=45.0, size=200).round(1),
       name="session_seconds",
   )
   result = recommended_bin_count(session_seconds, method="fd")
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
