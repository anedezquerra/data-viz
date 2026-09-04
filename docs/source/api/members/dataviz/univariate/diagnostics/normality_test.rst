dataviz.univariate.diagnostics.normality_test
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.diagnostics</p></div>

.. currentmodule:: dataviz.univariate.diagnostics

.. autofunction:: normality_test

Use case
--------

Use to formally test whether a numeric variable departs from normality before applying methods that assume it.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.diagnostics import normality_test

   # Final exam scores for one section of an introductory course
   rng = np.random.default_rng(42)
   scores = pd.Series(
       np.round(rng.normal(loc=78.0, scale=9.0, size=52), 1),
       name="exam_score",
   )

   result = normality_test(scores, method="shapiro", alpha=0.05)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
