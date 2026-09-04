dataviz.univariate.treatment.OutlierTreatmentResult
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.treatment</p></div>

.. currentmodule:: dataviz.univariate.treatment

.. autoclass:: OutlierTreatmentResult
   :members:
   :show-inheritance:

Use case
--------

Immutable record of original values, treated values, outlier mask, method, and rule, preserving both series for auditability.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.treatment import OutlierTreatmentResult

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = OutlierTreatmentResult(original=pd.Series([1.0, 2.0, 3.0], name="Value"), treated=pd.Series([1.0, 2.0, 3.0], name="Value"), mask=pd.Series([1.0, 2.0, 3.0], name="Value"), method="label", rule="label")
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
