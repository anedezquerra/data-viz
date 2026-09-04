dataviz.classification.threshold_extra.predictive_value_curve_static
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.threshold_extra</p></div>

.. currentmodule:: dataviz.classification.threshold_extra

.. autofunction:: predictive_value_curve_static

Use case
--------

Use to show how PPV and NPV shift with prevalence for a test of fixed sensitivity and specificity.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.threshold_extra import predictive_value_curve_static

   # fixed test characteristics: PPV collapses at low prevalence
   ax = predictive_value_curve_static(
       sensitivity=0.92, specificity=0.88,
       prevalences=np.linspace(0.001, 0.5, 150),
       title="Screening test: PPV / NPV vs prevalence")
   ax.axvline(0.02, color="grey", linestyle=":", linewidth=1)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/threshold_extra/predictive_value_curve_static.png" alt="predictive_value_curve_static example output"><figcaption>Example output</figcaption></figure></div>
