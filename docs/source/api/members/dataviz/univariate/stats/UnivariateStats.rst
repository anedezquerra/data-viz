dataviz.univariate.stats.UnivariateStats
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.stats</p></div>

.. currentmodule:: dataviz.univariate.stats

.. autoclass:: UnivariateStats
   :members:
   :show-inheritance:

Use case
--------

Immutable record of count, center, spread, shape, and robust spread statistics returned by univariate_summary; convertible with dataclasses.asdict.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.stats import UnivariateStats

   result = UnivariateStats(
       count=200,
       missing=0,
       mean=181.2,
       median=179.5,
       std=44.8,
       variance=2007.0,
       minimum=62.0,
       q1=149.0,
       q3=211.0,
       maximum=312.0,
       iqr=62.0,
       skewness=0.21,
       kurtosis=-0.12,
       sem=3.17,
       mad=37.5,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
