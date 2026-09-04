dataviz.univariate.accessors.numeric_or_none
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.accessors</p></div>

.. currentmodule:: dataviz.univariate.accessors

.. autofunction:: numeric_or_none

Use case
--------

Use in permissive profiling code to attempt numeric coercion, returning None instead of raising when no usable numeric values remain.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.accessors import numeric_or_none

   # Device readings exported as text, with occasional sensor error codes
   readings = pd.Series(
       ["21.4", "22.0", "ERR", "21.8", "23.1", "ERR", "22.6", "21.9",
        "22.3", "21.7", "22.8", "ERR", "21.5", "22.1", "22.4"],
       name="temperature_c",
   )

   result = numeric_or_none(readings)
   print(result.describe())

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
