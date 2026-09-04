dataviz.univariate.text.BooleanSummary
======================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autoclass:: BooleanSummary
   :members:
   :show-inheritance:

Use case
--------

Immutable record of true/false counts and the true rate for one boolean indicator variable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.text import BooleanSummary

   result = BooleanSummary(count=120, true_count=50, false_count=70, true_rate=50 / 120)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
