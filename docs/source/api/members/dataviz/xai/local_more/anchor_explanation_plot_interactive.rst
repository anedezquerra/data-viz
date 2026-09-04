dataviz.xai.local_more.anchor_explanation_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: anchor_explanation_plot_interactive

Use case
--------

Use to present anchor rules with precision and coverage side by side, showing how reliable and how broad each if-then rule is.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.local_more import anchor_explanation_plot_interactive

   rules = [
       "income > 50k",
       "income > 50k AND tenure > 3",
       "income > 50k AND tenure > 3 AND debt <= 5k",
   ]
   precision = [0.72, 0.85, 0.93]
   coverage = [0.40, 0.25, 0.12]

   fig = anchor_explanation_plot_interactive(rules, precision, coverage)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/anchor_explanation_plot_interactive.png" alt="anchor_explanation_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
