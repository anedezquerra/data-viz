dataviz.univariate.accessors.resolve_univariate_data
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.accessors</p></div>

.. currentmodule:: dataviz.univariate.accessors

.. autofunction:: resolve_univariate_data

Use case
--------

Use to resolve a column name or series-like into a validated UnivariateInput, applying missing-value policy and optional numeric coercion before plotting.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.accessors import resolve_univariate_data

   # Call-center log with a few abandoned calls recorded as missing
   rng = np.random.default_rng(42)
   calls = pd.DataFrame({
       "wait_time_min": np.round(rng.gamma(shape=2.0, scale=2.5, size=60), 1),
       "agent": rng.choice(["North", "South", "East", "West"], size=60),
   })
   calls.loc[rng.choice(calls.index, size=4, replace=False), "wait_time_min"] = np.nan

   result = resolve_univariate_data(
       "wait_time_min",
       data=calls,
       na_policy="drop",
       require_numeric=True,
   )
   print(result.name, result.kind, result.missing_count)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
