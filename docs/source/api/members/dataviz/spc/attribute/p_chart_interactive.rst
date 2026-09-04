dataviz.spc.attribute.p_chart_interactive
=========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: p_chart_interactive

Use case
--------

Use when monitoring a supplier's defect rate across lots of varying size to catch special-cause shifts in proportion nonconforming.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.attribute import p_chart_interactive

   rng = np.random.default_rng(42)
   # 30 shifts of filling-line inspection with varying sample sizes
   sample_sizes = rng.integers(180, 260, size=30)
   defects = rng.binomial(sample_sizes, 0.04)
   defects[24] = 28  # special cause after a supplier lot change

   fig = p_chart_interactive(defects, sample_sizes, title="Filling Line - Proportion Defective per Shift")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/p_chart_interactive.png" alt="p_chart_interactive example output"><figcaption>Example output</figcaption></figure></div>
