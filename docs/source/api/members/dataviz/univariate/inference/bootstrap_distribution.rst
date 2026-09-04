dataviz.univariate.inference.bootstrap_distribution
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.inference</p></div>

.. currentmodule:: dataviz.univariate.inference

.. autofunction:: bootstrap_distribution

Use case
--------

Use to generate resampled values of a mean, median, or std so you can inspect sampling variability without parametric assumptions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.inference import bootstrap_distribution

   rng = np.random.default_rng(42)
   wait_minutes = pd.Series(
       rng.lognormal(mean=2.2, sigma=0.6, size=180).round(1),
       name="wait_minutes",
   )
   result = bootstrap_distribution(wait_minutes, statistic="median", n_resamples=1000, seed=7)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
