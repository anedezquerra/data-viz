dataviz.univariate.tail.lorenz_curve_values
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autofunction:: lorenz_curve_values

Use case
--------

Use to get cumulative population and value share coordinates for custom Lorenz curve rendering.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.tail import lorenz_curve_values

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2, 12.4], name="Value")

   result = lorenz_curve_values(values)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
