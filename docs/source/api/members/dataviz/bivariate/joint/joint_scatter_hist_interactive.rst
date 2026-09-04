dataviz.bivariate.joint.joint_scatter_hist_interactive
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.bivariate.joint</p></div>

.. currentmodule:: dataviz.bivariate.joint

.. autofunction:: joint_scatter_hist_interactive

Use case
--------

Use to see a two-variable relationship and each marginal distribution in one figure during exploratory analysis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.bivariate.joint import joint_scatter_hist_interactive

   x = pd.Series([1, 2, 3, 4, 5], name="Input")
   y = pd.Series([1.2, 1.9, 3.4, 3.7, 5.1], name="Output")

   fig = joint_scatter_hist_interactive(x, y)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/bivariate/joint/joint_scatter_hist_interactive.png" alt="joint_scatter_hist_interactive example output"><figcaption>Example output</figcaption></figure></div>
