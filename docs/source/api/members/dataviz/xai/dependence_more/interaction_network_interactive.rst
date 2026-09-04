dataviz.xai.dependence_more.interaction_network_interactive
===========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.dependence_more</p></div>

.. currentmodule:: dataviz.xai.dependence_more

.. autofunction:: interaction_network_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import pandas as pd
   from dataviz.xai.dependence_more import interaction_network_interactive

   interaction_matrix = pd.DataFrame(
       [[0.0, 0.32, 0.05], [0.32, 0.0, 0.11], [0.05, 0.11, 0.0]],
       index=["age", "income", "tenure"],
       columns=["age", "income", "tenure"],
   )

   fig = interaction_network_interactive(interaction_matrix)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/dependence_more/interaction_network_interactive.png" alt="interaction_network_interactive example output"><figcaption>Example output</figcaption></figure></div>
