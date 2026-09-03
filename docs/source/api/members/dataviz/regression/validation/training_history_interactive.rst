dataviz.regression.validation.training_history_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.validation</p></div>

.. currentmodule:: dataviz.regression.validation

.. autofunction:: training_history_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.validation import training_history_interactive

   epochs = np.linspace(0.0, 2.0, 50)
   history = {
       "loss": list(np.exp(-epochs) + 0.10),
       "val_loss": list(np.exp(-0.8 * epochs) + 0.15),
   }

   fig = training_history_interactive(history)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/validation/training_history_interactive.png" alt="training_history_interactive example output"><figcaption>Example output</figcaption></figure></div>
