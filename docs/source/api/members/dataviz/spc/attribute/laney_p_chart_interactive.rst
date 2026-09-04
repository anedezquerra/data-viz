dataviz.spc.attribute.laney_p_chart_interactive
===============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: laney_p_chart_interactive

Use case
--------

Use when a p chart shows over-dispersion from large sample sizes; the Laney p' chart adjusts limits so only true special causes signal.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import laney_p_chart_interactive

   rng = np.random.default_rng(42)
   # Large, widely varying supplier-lot samples with overdispersion
   sample_sizes = rng.integers(400, 900, size=30)
   defects = rng.binomial(sample_sizes, 0.05)
   defects[24] = 120  # special cause from a tooling drift

   fig = laney_p_chart_interactive(defects, sample_sizes, title="Supplier Lots - Defect Rate (Laney p-prime)")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/laney_p_chart_interactive.png" alt="laney_p_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
