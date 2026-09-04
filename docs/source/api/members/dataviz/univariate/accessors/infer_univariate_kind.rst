dataviz.univariate.accessors.infer_univariate_kind
==================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.accessors</p></div>

.. currentmodule:: dataviz.univariate.accessors

.. autofunction:: infer_univariate_kind

Use case
--------

Use to classify a column as numeric, categorical, datetime, boolean, or text so downstream code can pick the right chart.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.accessors import infer_univariate_kind

   # Survey satisfaction responses recorded as short text labels
   rng = np.random.default_rng(42)
   satisfaction = pd.Series(
       rng.choice(
           ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied"],
           size=50,
           p=[0.35, 0.35, 0.20, 0.10],
       ),
       name="satisfaction",
   )

   result = infer_univariate_kind(satisfaction)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
