dataviz.regression.gof.normality_test_panel_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: normality_test_panel_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.gof import normality_test_panel_interactive

   rng = np.random.default_rng(42)
   residuals = rng.normal(0.0, 1.0, size=80)

   fig = normality_test_panel_interactive(residuals)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/gof/normality_test_panel_interactive.png" alt="normality_test_panel_interactive example output"><figcaption>Example output</figcaption></figure></div>
