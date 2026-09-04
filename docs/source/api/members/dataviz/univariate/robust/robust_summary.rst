dataviz.univariate.robust.robust_summary
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.robust</p></div>

.. currentmodule:: dataviz.univariate.robust

.. autofunction:: robust_summary

Use case
--------

Use to get center, spread, and fence statistics that resist heavy tails and isolated extreme observations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.robust import robust_summary

   rng = np.random.default_rng(42)
   income_k = rng.gamma(shape=2.5, scale=22.0, size=150).round(1)
   income_k[[12, 77, 130]] = [950.0, 1200.0, 875.0]
   household_income = pd.Series(income_k, name="household_income_k")
   result = robust_summary(household_income, trim_proportion=0.1, winsor_limits=0.05)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
