dataviz.eda.class_dist.class_distribution_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.eda.class_dist</p></div>

.. currentmodule:: dataviz.eda.class_dist

.. autofunction:: class_distribution_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.eda.class_dist import class_distribution_interactive

   rng = np.random.default_rng(42)
   series = pd.Series(rng.choice(["Pass", "Fail", "Rework"], size=60, p=[0.8, 0.1, 0.1]), name="Result")

   fig = class_distribution_interactive(series, title="Class distribution")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/eda/class_dist/class_distribution_interactive.png" alt="class_distribution_interactive example output"><figcaption>Example output</figcaption></figure></div>
