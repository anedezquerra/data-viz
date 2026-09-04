dataviz.univariate.fitting.fitted_pdf_values
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.fitting</p></div>

.. currentmodule:: dataviz.univariate.fitting

.. autofunction:: fitted_pdf_values

Use case
--------

Use to compute x and density values of a fitted distribution when you need the curve arrays rather than a chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.fitting import fitted_pdf_values

   # Insurance claim severities recorded by an auto portfolio
   rng = np.random.default_rng(42)
   claims = pd.Series(
       np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
       name="claim_usd",
   )

   x_values, pdf_values, fit = fitted_pdf_values(
       claims,
       distribution="lognorm",
       points=150,
   )
   print("curve points:", len(x_values), "KS p-value:", round(fit.p_value, 3))

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
