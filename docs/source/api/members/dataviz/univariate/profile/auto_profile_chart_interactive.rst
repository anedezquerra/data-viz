dataviz.univariate.profile.auto_profile_chart_interactive
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.profile</p></div>

.. currentmodule:: dataviz.univariate.profile

.. autofunction:: auto_profile_chart_interactive

Use case
--------

Use when you want one sensible interactive chart chosen automatically from the inferred variable type.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.profile import auto_profile_chart_interactive

   rng = np.random.default_rng(42)
   value = pd.Series(rng.normal(loc=10.0, scale=0.4, size=30), name="Value")

   fig = auto_profile_chart_interactive(value, title="Automatic profile")
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/profile/auto_profile_chart_interactive.png" alt="auto_profile_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
