dataviz.regression.uncertainty.coverage_by_segment_bar_static
=============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: coverage_by_segment_bar_static

Use case
--------

Use to detect coverage gaps across data segments; bars below the nominal line show subgroups where intervals under-cover.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.regression.uncertainty import coverage_by_segment_bar_static

   segments = ["Urban", "Suburban", "Rural", "Coastal", "Mountain"]
   coverage = [0.93, 0.91, 0.84, 0.88, 0.79]

   ax = coverage_by_segment_bar_static(
       segments, coverage, nominal=0.9,
       title="Property value model: conformal coverage by market segment",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/coverage_by_segment_bar_static.png" alt="coverage_by_segment_bar_static example output"><figcaption>Example output</figcaption></figure></div>
