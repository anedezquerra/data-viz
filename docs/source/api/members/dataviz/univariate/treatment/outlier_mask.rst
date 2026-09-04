dataviz.univariate.treatment.outlier_mask
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.treatment</p></div>

.. currentmodule:: dataviz.univariate.treatment

.. autofunction:: outlier_mask

Use case
--------

Use to get a boolean outlier mask from a named rule (iqr, zscore, or mad) as a shared input to treatment workflows.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.treatment import outlier_mask

   rng = np.random.default_rng(42)
   latency = rng.normal(loc=120.0, scale=15.0, size=180).round(1)
   latency[[9, 54, 121, 160]] = [520.0, 610.0, 480.0, 700.0]
   latency_ms = pd.Series(latency, name="latency_ms")
   result = outlier_mask(latency_ms, rule="iqr", multiplier=1.5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
