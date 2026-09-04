dataviz.xai.importance_extra.drop_column_importance_bar_static
==============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_extra</p></div>

.. currentmodule:: dataviz.xai.importance_extra

.. autofunction:: drop_column_importance_bar_static

Use case
--------

Use to measure each feature's contribution by retraining without it; signed values show helpful vs. harmful columns.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_extra import drop_column_importance_bar_static

   deltas = {"age": 0.018, "income": 0.074, "tenure": 0.004, "debt": 0.031}

   ax = drop_column_importance_bar_static(deltas)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_extra/drop_column_importance_bar_static.png" alt="drop_column_importance_bar_static example output"><figcaption>Example output</figcaption></figure></div>
