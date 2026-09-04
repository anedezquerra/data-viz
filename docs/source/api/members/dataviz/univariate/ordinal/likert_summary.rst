dataviz.univariate.ordinal.likert_summary
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.ordinal</p></div>

.. currentmodule:: dataviz.univariate.ordinal

.. autofunction:: likert_summary

Use case
--------

Use to tabulate one Likert-scale item with counts, proportions, and cumulative proportions for survey reporting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.ordinal import likert_summary

   rng = np.random.default_rng(42)
   order = ["Strongly disagree", "Disagree", "Neutral", "Agree", "Strongly agree"]
   data = pd.Series(rng.choice(order, size=60), name="Response")

   result = likert_summary(data, order=order)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
