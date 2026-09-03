dataviz.classification.errors.loss_distribution_plot_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.errors</p></div>

.. currentmodule:: dataviz.classification.errors

.. autofunction:: loss_distribution_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.errors import loss_distribution_plot_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = loss_distribution_plot_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/errors/loss_distribution_plot_interactive.png" alt="loss_distribution_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
