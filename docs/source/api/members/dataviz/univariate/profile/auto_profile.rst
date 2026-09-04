dataviz.univariate.profile.auto_profile
=======================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.profile</p></div>

.. currentmodule:: dataviz.univariate.profile

.. autofunction:: auto_profile

Use case
--------

Use to get a type-aware first-pass profile of one variable, including quality metrics and kind-appropriate summary statistics.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.profile import auto_profile

   rng = np.random.default_rng(42)
   customers = pd.DataFrame(
       {"monthly_spend": rng.gamma(shape=3.0, scale=28.0, size=150).round(2)}
   )
   customers.loc[[5, 41, 96], "monthly_spend"] = np.nan
   result = auto_profile("monthly_spend", data=customers)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
