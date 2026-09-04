dataviz.regression.var_engineering.target_encoding_curve_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.var_engineering</p></div>

.. currentmodule:: dataviz.regression.var_engineering

.. autofunction:: target_encoding_curve_interactive

Use case
--------

Use to sanity-check target encoding by plotting category mean target vs sample size; small-n categories far from the prior are unreliable.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.var_engineering import target_encoding_curve_interactive

   zip_means = [385, 402, 291, 450, 318, 512, 366, 277, 429, 341, 470, 305, 398, 260, 445]
   zip_counts = [210, 95, 640, 38, 480, 22, 150, 720, 61, 390, 45, 540, 120, 810, 88]
   prior = np.average(zip_means, weights=zip_counts)

   fig = target_encoding_curve_interactive(
       zip_means, zip_counts, prior=round(float(prior), 1),
       title="Home prices by ZIP: target-encoded mean vs sample size (k$)",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/var_engineering/target_encoding_curve_interactive.png" alt="target_encoding_curve_interactive example output"><figcaption>Example output</figcaption></figure></div>
