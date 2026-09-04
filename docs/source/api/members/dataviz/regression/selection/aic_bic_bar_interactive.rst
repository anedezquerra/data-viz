dataviz.regression.selection.aic_bic_bar_interactive
====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.selection</p></div>

.. currentmodule:: dataviz.regression.selection

.. autofunction:: aic_bic_bar_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.selection import aic_bic_bar_interactive

   model_names = ["M1", "M2", "M3"]
   aic = np.array([120.5, 115.2, 118.7])
   bic = np.array([125.5, 119.7, 124.7])

   fig = aic_bic_bar_interactive(model_names, aic, bic)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/selection/aic_bic_bar_interactive.png" alt="aic_bic_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
