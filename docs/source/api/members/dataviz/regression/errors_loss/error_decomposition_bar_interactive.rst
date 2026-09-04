dataviz.regression.errors_loss.error_decomposition_bar_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.errors_loss</p></div>

.. currentmodule:: dataviz.regression.errors_loss

.. autofunction:: error_decomposition_bar_interactive

Use case
--------

Use to break total error into components such as bias squared, variance, and noise when explaining where error comes from.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.errors_loss import error_decomposition_bar_interactive

   components = ["bias^2", "variance", "irreducible noise"]
   values = np.array([12.4, 28.7, 9.1])

   fig = error_decomposition_bar_interactive(
       components, values,
       title="Turbine Output Model: Bias-Variance Decomposition",
       color="#1f6fb2", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/errors_loss/error_decomposition_bar_interactive.png" alt="error_decomposition_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
