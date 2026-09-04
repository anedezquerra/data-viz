dataviz.classification.gain_lift.gain_chart_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.gain_lift</p></div>

.. currentmodule:: dataviz.classification.gain_lift

.. autofunction:: gain_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.gain_lift import gain_chart_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = gain_chart_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/classification/gain_lift/gain_chart_interactive.png" alt="gain_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
