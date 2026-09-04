dataviz.classification.gain_lift.cumulative_accuracy_profile_interactive
========================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.gain_lift</p></div>

.. currentmodule:: dataviz.classification.gain_lift

.. autofunction:: cumulative_accuracy_profile_interactive

Use case
--------

Use to compare the model CAP curve against perfect and random baselines and read the accuracy ratio.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python


   import numpy as np
   from dataviz.classification.gain_lift import cumulative_accuracy_profile_interactive

   rng = np.random.default_rng(42)
   y_prob = rng.beta(2.0, 5.0, size=200)
   y_true = rng.binomial(1, y_prob)

   fig = cumulative_accuracy_profile_interactive(y_true, y_prob)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/gain_lift/cumulative_accuracy_profile_interactive.png" alt="cumulative_accuracy_profile_interactive example output"><figcaption>Example output</figcaption></figure></div>
