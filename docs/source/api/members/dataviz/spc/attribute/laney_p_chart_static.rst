dataviz.spc.attribute.laney_p_chart_static
==========================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.attribute</p></div>

.. currentmodule:: dataviz.spc.attribute

.. autofunction:: laney_p_chart_static

Use case
--------

Use when a p chart shows over-dispersion from large sample sizes; the Laney p' chart adjusts limits so only true special causes signal.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.spc.attribute import laney_p_chart_static

   rng = np.random.default_rng(42)
   # Large, widely varying supplier-lot samples with overdispersion
   sample_sizes = rng.integers(400, 900, size=30)
   defects = rng.binomial(sample_sizes, 0.05)
   defects[24] = 120  # special cause from a tooling drift

   ax = laney_p_chart_static(defects, sample_sizes, title="Supplier Lots - Defect Rate (Laney p-prime)")
   ax.set_xlabel("Lot")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/spc/attribute/laney_p_chart_static.png" alt="laney_p_chart_static example output"><figcaption>Example output</figcaption></figure></div>
