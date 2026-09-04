dataviz.regression.errors_loss.ranked_error_plot_interactive
============================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: ranked_error_plot_interactive

Use case
--------

Use to see how quickly errors grow from typical to worst case by plotting errors sorted by magnitude.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.errors_loss import ranked_error_plot_interactive

   rng = np.random.default_rng(42)
   errors = np.abs(rng.normal(0.0, 0.7, size=60))

   fig = ranked_error_plot_interactive(errors)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/ranked_error_plot_interactive.png" alt="ranked_error_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
