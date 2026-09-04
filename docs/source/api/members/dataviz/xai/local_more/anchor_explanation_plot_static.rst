dataviz.xai.local_more.anchor_explanation_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: anchor_explanation_plot_static

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import anchor_explanation_plot_static

   rules = [
       "income > 50k",
       "income > 50k AND tenure > 3",
       "income > 50k AND tenure > 3 AND debt <= 5k",
   ]
   precision = [0.72, 0.85, 0.93]
   coverage = [0.40, 0.25, 0.12]

   ax = anchor_explanation_plot_static(rules, precision, coverage)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/anchor_explanation_plot_static.png" alt="anchor_explanation_plot_static example output"><figcaption>Example output</figcaption></figure></div>
