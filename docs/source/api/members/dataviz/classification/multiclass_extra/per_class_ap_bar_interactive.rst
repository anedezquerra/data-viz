dataviz.classification.multiclass_extra.per_class_ap_bar_interactive
====================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.classification.multiclass_extra</p></div>

.. currentmodule:: dataviz.classification.multiclass_extra

.. autofunction:: per_class_ap_bar_interactive

Use case
--------

Use to rank classes by Average Precision and find classes whose ranking quality drags down a multiclass model.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.classification.multiclass_extra import per_class_ap_bar_interactive

   # per-class average precision from a 4-class defect-inspection model
   ap_per_class = {
       "scratch": 0.71,
       "dent": 0.64,
       "discoloration": 0.55,
       "crack": 0.83,
   }

   fig = per_class_ap_bar_interactive(ap_per_class,
                                      title="Defect model: per-class AP")
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/classification/multiclass_extra/per_class_ap_bar_interactive.png" alt="per_class_ap_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
