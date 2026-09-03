dataviz.regression.gof.residual_dependence_test_panel_interactive
=================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.gof</p></div>

.. currentmodule:: dataviz.regression.gof

.. autofunction:: residual_dependence_test_panel_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.gof import residual_dependence_test_panel_interactive

   rng = np.random.default_rng(42)
   X = rng.normal(0.0, 1.0, size=(60, 3))
   residuals = rng.normal(0.0, 1.0, size=60)

   fig = residual_dependence_test_panel_interactive(X, residuals)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/gof/residual_dependence_test_panel_interactive.png" alt="residual_dependence_test_panel_interactive example output"><figcaption>Example output</figcaption></figure></div>
