dataviz.univariate.text.BooleanRateInterval
===========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autoclass:: BooleanRateInterval
   :members:
   :show-inheritance:

Use case
--------

Immutable record of an observed true rate with Wilson confidence bounds; consumed when reporting binary proportions.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.text import BooleanRateInterval

   result = BooleanRateInterval(
       true_rate=0.42,
       lower=0.33,
       upper=0.51,
       confidence_level=0.95,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
