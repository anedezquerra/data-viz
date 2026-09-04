dataviz.univariate.inference.bootstrap_ci
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.inference</p></div>

.. currentmodule:: dataviz.univariate.inference

.. autofunction:: bootstrap_ci

Use case
--------

Use when you need a confidence interval for a mean, median, or std but cannot rely on normality or a closed-form formula.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.inference import bootstrap_ci

   rng = np.random.default_rng(42)
   wait_minutes = pd.Series(
       rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
       name="wait_minutes",
   )
   result = bootstrap_ci(wait_minutes, statistic="mean", confidence_level=0.90, n_resamples=1500, seed=7)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
