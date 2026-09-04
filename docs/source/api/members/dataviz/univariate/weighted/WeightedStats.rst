dataviz.univariate.weighted.WeightedStats
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.weighted</p></div>

.. currentmodule:: dataviz.univariate.weighted

.. autoclass:: WeightedStats
   :members:
   :show-inheritance:

Use case
--------

Immutable record of weighted count, weight sum, mean, population variance, std, and quartiles for survey or grouped data.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.weighted import WeightedStats

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = WeightedStats(count=5, weight_sum=0.5, mean=0.5, variance=0.5, std=0.5, q1=0.5, median=0.5, q3=0.5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
