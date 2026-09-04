dataviz.univariate.tail.ConcentrationStats
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.tail</p></div>

.. currentmodule:: dataviz.univariate.tail

.. autoclass:: ConcentrationStats
   :members:
   :show-inheritance:

Use case
--------

Immutable record of total, Gini coefficient, and top-10/top-20 shares summarizing inequality in non-negative values.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.tail import ConcentrationStats

   result = ConcentrationStats(
       total=1240500.0,
       gini=0.47,
       top_10_share=0.38,
       top_20_share=0.56,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
