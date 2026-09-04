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

   from dataviz.univariate.fitting import DistributionFit

   # Fitted summary for claim severities modeled with a lognormal law
   result = DistributionFit(
       distribution="lognorm",
       parameters=(0.42, 2.1, 8.9),
       statistic=0.061,
       p_value=0.58,
       aic=412.3,
       bic=420.1,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
