dataviz.regression.cv_extended.repeated_kfold_violin_interactive
================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.cv_extended</p></div>

.. currentmodule:: dataviz.regression.cv_extended

.. autofunction:: repeated_kfold_violin_interactive

Use case
--------

Use to show the full score distribution per repeat in repeated K-fold, quantifying how much results vary with the random split.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.cv_extended import repeated_kfold_violin_interactive

   rng = np.random.default_rng(42)
   repeats = ["Repeat 1", "Repeat 2", "Repeat 3"]
   scores = [rng.normal(0.78, 0.04, 5),
             rng.normal(0.81, 0.03, 5),
             rng.normal(0.79, 0.05, 5)]

   fig = repeated_kfold_violin_interactive(
       repeats, scores,
       title="Soil Moisture Model: Repeated 5-Fold R2",
       metric_name="R2", color="#2a7f62", template="plotly_white")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/cv_extended/repeated_kfold_violin_interactive.png" alt="repeated_kfold_violin_interactive example output"><figcaption>Example output</figcaption></figure></div>
