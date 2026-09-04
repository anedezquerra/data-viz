dataviz.univariate.diagnostics.NormalityTestResult
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autoclass:: NormalityTestResult
   :members:
   :show-inheritance:

Use case
--------

Result of a normality test carrying the statistic, p-value, and verdict; consumed when deciding if a variable is plausibly normal.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.diagnostics import NormalityTestResult

   # Summary object returned by a Shapiro-Wilk check on exam scores
   result = NormalityTestResult(
       statistic=0.973,
       p_value=0.31,
       method="shapiro",
       is_normal=True,
       alpha=0.05,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
