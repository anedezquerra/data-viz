dataviz.spc.constants.get_d2
============================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.constants</p></div>

.. currentmodule:: dataviz.spc.constants

.. autofunction:: get_d2

Use case
--------

Use to look up the d2 constant for a moving-range span when deriving sigma estimates for individuals charts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.spc.constants import get_d2

   # Estimate sigma from the mean moving range of a filling line
   mean_moving_range = 0.32
   result = mean_moving_range / get_d2(2)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
