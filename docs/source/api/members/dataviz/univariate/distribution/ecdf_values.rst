dataviz.univariate.distribution.ecdf_values
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.distribution</p></div>

.. currentmodule:: dataviz.univariate.distribution

.. autofunction:: ecdf_values

Use case
--------

Use to compute sorted values and cumulative probabilities for an empirical CDF when you need the arrays, not the chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.distribution import ecdf_values

   # Rental durations for a bike-share station over one week
   rng = np.random.default_rng(42)
   duration_min = pd.Series(
       np.round(rng.gamma(shape=2.2, scale=9.0, size=38), 1),
       name="rental_min",
   )

   values, probabilities = ecdf_values(duration_min)
   print("n =", len(values), "median =", np.median(values))

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
