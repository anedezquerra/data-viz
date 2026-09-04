dataviz.regression.helpers.yeo_johnson_loglikelihood
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: yeo_johnson_loglikelihood

Use case
--------

Use to compute the Yeo-Johnson profile log-likelihood when transforming responses that include negatives.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.helpers import yeo_johnson_loglikelihood

   rng = np.random.default_rng(42)
   hospital_stay_days = pd.Series(rng.gamma(2.0, 2.5, 40) + 0.5,
                                  name="length_of_stay_days")
   lambdas = np.linspace(-2.0, 2.0, 25)

   centered = hospital_stay_days - hospital_stay_days.median()
   loglik = yeo_johnson_loglikelihood(centered, lambdas)
   best = lambdas[int(np.argmax(loglik))]
   print(f"best lambda: {best:.2f}")

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
