dataviz.univariate.fitting.DistributionFit
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.fitting</p></div>

.. currentmodule:: dataviz.univariate.fitting

.. autoclass:: DistributionFit
   :members:
   :show-inheritance:

Use case
--------

Fitted SciPy distribution summary carrying the distribution name, parameters, and fit quality; consumed by ranking and overlay helpers.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.fitting import DistributionFit

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = DistributionFit(distribution="label", parameters=0.5, statistic=0.5, p_value=0.5, aic=0.5, bic=0.5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
