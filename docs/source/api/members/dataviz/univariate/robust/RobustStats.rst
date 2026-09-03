dataviz.univariate.robust.RobustStats
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.robust</p></div>

.. currentmodule:: dataviz.univariate.robust

.. autoclass:: RobustStats
   :members:
   :show-inheritance:

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.robust import RobustStats

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = RobustStats(count=5, median=0.5, mad=0.5, scaled_mad=0.5, trimmed_mean=0.5, winsorized_mean=0.5, q1=0.5, q3=0.5, iqr=0.5, lower_fence=0.5, upper_fence=0.5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
