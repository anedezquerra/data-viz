dataviz.univariate.weighted.weighted_ecdf_values
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.weighted</p></div>

.. currentmodule:: dataviz.univariate.weighted

.. autofunction:: weighted_ecdf_values

Use case
--------

Use to get sorted values and weight-normalized cumulative probabilities for custom weighted ECDF rendering.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.weighted import weighted_ecdf_values

   rng = np.random.default_rng(42)
   nps_score = pd.Series(rng.integers(0, 11, size=250), name="nps_score")
   sample_weight = pd.Series(rng.uniform(0.5, 2.5, size=250).round(2), name="sample_weight")
   result = weighted_ecdf_values(nps_score, sample_weight)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
