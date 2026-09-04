dataviz.univariate.stats.univariate_summary
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.stats</p></div>

.. currentmodule:: dataviz.univariate.stats

.. autofunction:: univariate_summary

Use case
--------

Use for a complete descriptive summary of one numeric variable, including quartiles, skewness, kurtosis, SEM, and MAD.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.stats import univariate_summary

   rng = np.random.default_rng(42)
   session_seconds = pd.Series(
       rng.normal(loc=180.0, scale=45.0, size=200).round(1),
       name="session_seconds",
   )
   result = univariate_summary(session_seconds)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
