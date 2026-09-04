dataviz.spc.rules.as_numeric_series
===================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.rules</p></div>

.. currentmodule:: dataviz.spc.rules

.. autofunction:: as_numeric_series

Use case
--------

Use to coerce raw array-like process data into a numeric Series before computing limits or detecting rule violations.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.spc.rules import as_numeric_series

   # Raw fill-weight log entries from a text export (strings and a gap)
   raw = ["500.2", "499.8", None, "501.1", "500.6", "499.5", "500.9"]
   result = as_numeric_series(raw, name="Fill Weight")
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
