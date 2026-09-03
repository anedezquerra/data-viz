dataviz.univariate.inference.BootstrapCI
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.inference</p></div>

.. currentmodule:: dataviz.univariate.inference

.. autoclass:: BootstrapCI
   :members:
   :show-inheritance:

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.inference import BootstrapCI

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = BootstrapCI(statistic="label", estimate=0.5, lower=0.5, upper=0.5, confidence_level=0.5, n_resamples=5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
