dataviz.univariate.robust.RobustStats
=====================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.robust</p></div>

.. currentmodule:: dataviz.univariate.robust

.. autoclass:: RobustStats
   :members:
   :show-inheritance:

Use case
--------

Immutable record of median, MAD, scaled MAD, trimmed and winsorized means, quartiles, IQR, and Tukey fences for one numeric variable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.robust import RobustStats

   result = RobustStats(
       count=150,
       median=41200.0,
       mad=9800.0,
       scaled_mad=14523.6,
       trimmed_mean=44750.0,
       winsorized_mean=46310.0,
       q1=31800.0,
       q3=58900.0,
       iqr=27100.0,
       lower_fence=-8850.0,
       upper_fence=99550.0,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
