dataviz.regression.cv_extended.repeated_kfold_violin_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: repeated_kfold_violin_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.cv_extended import repeated_kfold_violin_interactive

   rng = np.random.default_rng(42)
   repeats = ["Repeat 1", "Repeat 2", "Repeat 3", "Repeat 4"]
   scores_per_repeat = [rng.normal(0.8, 0.05, size=5) for _ in range(4)]

   fig = repeated_kfold_violin_interactive(repeats, scores_per_repeat, metric_name="R2")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/regression/cv_extended/repeated_kfold_violin_interactive.png" alt="repeated_kfold_violin_interactive example output"><figcaption>Example output</figcaption></figure></div>
