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

   from dataviz.univariate.weighted import WeightedStats

   result = WeightedStats(
       count=250,
       weight_sum=372.5,
       mean=6.8,
       variance=5.1,
       std=2.26,
       q1=5.0,
       median=7.0,
       q3=9.0,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
