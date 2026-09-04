dataviz.bivariate.stats.BivariateStats
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.bivariate.stats</p></div>

.. currentmodule:: dataviz.bivariate.stats

.. autoclass:: BivariateStats
   :members:
   :show-inheritance:

Use case
--------

Returned by bivariate_summary; carries correlations, covariance, fit coefficients, and descriptive statistics for downstream reporting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.bivariate.stats import bivariate_summary

   rng = np.random.default_rng(42)
   n = 80
   study_hours = pd.Series(rng.uniform(low=1.0, high=15.0, size=n), name="Study hours")
   exam_score = pd.Series(45.0 + 3.5 * study_hours + rng.normal(loc=0.0, scale=6.0, size=n), name="Exam score")

   result = bivariate_summary(study_hours, exam_score)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
