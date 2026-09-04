dataviz.regression.helpers.runs_test_signs
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autofunction:: runs_test_signs

Use case
--------

Use to get run counts of residual signs when testing residuals for randomness.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.regression.helpers import runs_test_signs

   rng = np.random.default_rng(42)
   noise = rng.normal(0.0, 1.0, 30)
   residuals = pd.Series(
       np.array([noise[0]] + [0.55 * noise[i - 1] + noise[i] for i in range(1, 30)]),
       index=pd.date_range("2025-01-01", periods=30, freq="D"),
       name="streamflow_residuals")

   runs, n_pos, n_neg = runs_test_signs(residuals)
   print(f"runs={runs}, positive={n_pos}, negative={n_neg}")

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
