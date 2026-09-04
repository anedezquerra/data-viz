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

   import pandas as pd
   from dataviz.univariate.datetime import interarrival_times

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")
   timestamps = pd.to_datetime(["2026-01-01", "2026-01-03", "2026-01-04", "2026-01-10"])

   result = interarrival_times(values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
