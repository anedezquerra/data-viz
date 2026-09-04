dataviz.xai.concept.attention_heatmap_interactive
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.concept</p></div>

.. currentmodule:: dataviz.xai.concept

.. autofunction:: attention_heatmap_interactive

Use case
--------

Use to visualize attention weights across tokens or features in transformer-style models during error analysis.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.xai.concept import attention_heatmap_interactive

   rng = np.random.default_rng(42)
   tokens = ["the", "model", "denied", "the", "loan", "due", "to", "debt"]
   weights = rng.random((len(tokens), len(tokens))) + 0.6 * np.eye(len(tokens))
   attention = weights / weights.sum(axis=1, keepdims=True)

   fig = attention_heatmap_interactive(
       attention,
       tokens,
       title="Attention Weights - Adverse-Action Explanation Head",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/concept/attention_heatmap_interactive.png" alt="attention_heatmap_interactive example output"><figcaption>Example output</figcaption></figure></div>
