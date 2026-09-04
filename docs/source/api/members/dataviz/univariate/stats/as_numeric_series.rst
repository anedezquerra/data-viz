dataviz.univariate.stats.as_numeric_series
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.stats</p></div>

.. currentmodule:: dataviz.univariate.stats

.. autofunction:: as_numeric_series

Use case
--------

Use to coerce series-like input into a clean non-missing numeric Series before computing univariate statistics.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.stats import as_numeric_series

   rng = np.random.default_rng(42)
   session_seconds = rng.normal(loc=180.0, scale=45.0, size=200).round(1)
   result = as_numeric_series(session_seconds, name="session_seconds")
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
