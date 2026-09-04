dataviz.regression.uncertainty.coverage_by_segment_bar_interactive
==================================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.uncertainty</p></div>

.. currentmodule:: dataviz.regression.uncertainty

.. autofunction:: coverage_by_segment_bar_interactive

Use case
--------

Use to detect coverage gaps across data segments; bars below the nominal line show subgroups where intervals under-cover.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.regression.uncertainty import coverage_by_segment_bar_interactive

   segments = ["Urban", "Suburban", "Rural", "Coastal", "Mountain"]
   coverage = [0.93, 0.91, 0.84, 0.88, 0.79]

   fig = coverage_by_segment_bar_interactive(
       segments, coverage, nominal=0.9,
       title="Property value model: conformal coverage by market segment",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/regression/uncertainty/coverage_by_segment_bar_interactive.png" alt="coverage_by_segment_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
