dataviz.univariate.datetime.interarrival_times
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.datetime</p></div>

.. currentmodule:: dataviz.univariate.datetime

.. autofunction:: interarrival_times

Use case
--------

Use to compute elapsed time between consecutive events, e.g. gaps between orders or failures, in a chosen unit.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.datetime import interarrival_times

   # Equipment failure timestamps from a fleet monitoring system
   rng = np.random.default_rng(42)
   failures = pd.Series(
       pd.Timestamp("2026-02-01")
       + pd.to_timedelta(np.sort(rng.uniform(0, 120 * 24, size=32)), unit="h"),
       name="failure_time",
   )

   result = interarrival_times(failures, unit="h")
   print(result.describe())

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
