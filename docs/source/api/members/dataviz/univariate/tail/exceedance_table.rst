dataviz.univariate.tail.exceedance_table
========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: exceedance_table

Use case
--------

Use to tabulate how often values exceed candidate thresholds, for example SLA breaches or regulatory limits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.tail import exceedance_table

   rng = np.random.default_rng(42)
   claim_amounts = pd.Series(
       (rng.pareto(a=2.5, size=160) * 5000 + 1000).round(0),
       name="claim_amount",
   )
   thresholds = [5000, 10000, 25000, 50000]
   result = exceedance_table(claim_amounts, thresholds=thresholds)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
