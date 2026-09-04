dataviz.univariate.tail.concentration_summary
=============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: concentration_summary

Use case
--------

Use to quantify inequality or concentration with Gini and top-share metrics for revenue, income, or claim amounts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.tail import concentration_summary

   rng = np.random.default_rng(42)
   claim_amounts = pd.Series(
       (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
       name="claim_amount",
   )
   result = concentration_summary(claim_amounts)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
