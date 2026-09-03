dataviz.utils.validation.add_plotly_reference_lines
===================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.utils.validation</p></div>

.. currentmodule:: dataviz.utils.validation

.. autofunction:: add_plotly_reference_lines

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import plotly.graph_objects as go
   from dataviz.utils.validation import add_plotly_reference_lines

   rng = np.random.default_rng(42)
   fig = go.Figure(go.Scatter(y=rng.normal(loc=10.0, scale=0.4, size=30)))

   add_plotly_reference_lines(fig, hline=10.0)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../_static/api/dataviz/utils/validation/add_plotly_reference_lines.png" alt="add_plotly_reference_lines example output"><figcaption>Example output</figcaption></figure></div>
