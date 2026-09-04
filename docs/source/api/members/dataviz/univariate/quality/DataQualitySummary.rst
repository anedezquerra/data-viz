dataviz.univariate.quality.DataQualitySummary
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.quality</p></div>

.. currentmodule:: dataviz.univariate.quality

.. autoclass:: DataQualitySummary
   :members:
   :show-inheritance:

Use case
--------

Immutable record of count, missingness, uniqueness, duplicate, zero, and negative rates; consumed as a quick screening profile for one variable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.quality import DataQualitySummary

   result = DataQualitySummary(
       count=140,
       missing=6,
       missing_rate=6 / 140,
       unique=129,
       duplicate_rate=0.036,
       zero_rate=0.01,
       negative_rate=0.02,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
