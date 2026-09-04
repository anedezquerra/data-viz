dataviz.univariate.inference.BootstrapCI
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.inference</p></div>

.. currentmodule:: dataviz.univariate.inference

.. autoclass:: BootstrapCI
   :members:
   :show-inheritance:

Use case
--------

Immutable result carrying the original estimate, percentile bootstrap bounds, confidence level, and resample count; consumed by reports and downstream interval checks.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.inference import BootstrapCI

   result = BootstrapCI(
       statistic="mean",
       estimate=9.84,
       lower=9.12,
       upper=10.61,
       confidence_level=0.95,
       n_resamples=2000,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
