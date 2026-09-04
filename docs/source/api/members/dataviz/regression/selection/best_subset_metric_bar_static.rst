dataviz.regression.selection.best_subset_metric_bar_static
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: best_subset_metric_bar_static

Use case
--------

Compare a fit metric across candidate feature subsets in best-subset selection; the highlighted minimum marks the subset to keep.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.regression.selection import best_subset_metric_bar_static

   subsets = ["{temp}", "{temp, press}", "{temp, cat}", "{press, cat}",
              "{temp, press, cat}", "{all 5}"]
   mallows_cp = [38.2, 12.5, 9.8, 21.4, 4.1, 6.0]

   ax = best_subset_metric_bar_static(
       subsets, mallows_cp, metric_name="Mallows Cp",
       title="Reactor yield: best-subset search by Mallows Cp",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/selection/best_subset_metric_bar_static.png" alt="best_subset_metric_bar_static example output"><figcaption>Example output</figcaption></figure></div>
