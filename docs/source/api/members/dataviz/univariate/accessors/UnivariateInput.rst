dataviz.univariate.accessors.UnivariateInput
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.accessors</p></div>

.. currentmodule:: dataviz.univariate.accessors

.. autoclass:: UnivariateInput
   :members:
   :show-inheritance:

Use case
--------

Immutable resolved input carrying the cleaned Series, display name, inferred kind, and missing count; consumed by wrappers that normalize univariate inputs.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.univariate.accessors import UnivariateInput

   # Resolved input summary produced by a support-ticket logging system
   wait_times = pd.Series(
       [4.2, 6.1, 3.8, 5.5, 7.0, 4.9, 6.6, 5.1, 3.4, 8.2],
       name="wait_time_min",
   )
   result = UnivariateInput(
       values=wait_times,
       name="wait_time_min",
       kind="numeric",
       missing_count=0,
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
