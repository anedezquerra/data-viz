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

   original = pd.Series([98.0, 105.0, 102.0, 480.0], name="latency_ms")
   treated = pd.Series([98.0, 105.0, 102.0, 180.0], name="latency_ms")
   mask = pd.Series([False, False, False, True])
   result = OutlierTreatmentResult(
       original=original,
       treated=treated,
       mask=mask,
       method="cap",
       rule="iqr",
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
