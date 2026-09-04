dataviz.univariate.stats.zscore_outliers
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.stats</p></div>

.. currentmodule:: dataviz.univariate.stats

.. autofunction:: zscore_outliers

Use case
--------

Use to flag observations whose absolute z-score exceeds a threshold on roughly symmetric, light-tailed data.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.stats import zscore_outliers

   rng = np.random.default_rng(42)
   session_seconds = pd.Series(
       rng.normal(loc=180.0, scale=45.0, size=200).round(1),
       name="session_seconds",
   )
   result = zscore_outliers(session_seconds, threshold=3.0)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
