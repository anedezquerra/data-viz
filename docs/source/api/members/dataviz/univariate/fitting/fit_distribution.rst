dataviz.univariate.fitting.fit_distribution
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.fitting</p></div>

.. currentmodule:: dataviz.univariate.fitting

.. autofunction:: fit_distribution

Use case
--------

Use to fit a named SciPy continuous distribution to a numeric variable and recover its estimated parameters.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.fitting import fit_distribution

   # Insurance claim severities recorded by an auto portfolio
   rng = np.random.default_rng(42)
   claims = pd.Series(
       np.round(rng.lognormal(mean=8.1, sigma=0.9, size=56), 0),
       name="claim_usd",
   )

   result = fit_distribution(claims, distribution="lognorm")
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
