dataviz.xai.importance_more.gain_importance_bar_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: gain_importance_bar_static

Use case
--------

Use to rank features by gradient-boosting gain, optionally overlaying split counts on a second axis to spot overused weak splits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_more import gain_importance_bar_static

   gain = {"age": 0.18, "income": 0.34, "tenure": 0.07, "debt": 0.12}
   split_count = {"age": 42.0, "income": 65.0, "tenure": 18.0, "debt": 27.0}

   ax = gain_importance_bar_static(gain, split_count=split_count)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/gain_importance_bar_static.png" alt="gain_importance_bar_static example output"><figcaption>Example output</figcaption></figure></div>
