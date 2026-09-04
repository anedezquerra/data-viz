dataviz.xai.local_more.anchor_explanation_plot_static
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: anchor_explanation_plot_static

Use case
--------

Use to present anchor rules with precision and coverage side by side, showing how reliable and how broad each if-then rule is.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import anchor_explanation_plot_static

   rules = [
       "tenure <= 6 AND support_calls > 3",
       "tenure <= 6 AND contract = month-to-month",
       "late_payments > 1 AND monthly_charges > 80",
       "tenure <= 12 AND no_auto_pay",
   ]
   precision = [0.97, 0.93, 0.88, 0.81]
   coverage = [0.12, 0.21, 0.15, 0.27]
   ax = anchor_explanation_plot_static(
       rules, precision, coverage,
       title="Anchor rules for high-risk churn segment",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/anchor_explanation_plot_static.png" alt="anchor_explanation_plot_static example output"><figcaption>Example output</figcaption></figure></div>
