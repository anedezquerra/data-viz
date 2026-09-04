dataviz.utils.validation.add_reference_lines
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.utils.validation</p></div>

.. currentmodule:: dataviz.utils.validation

.. autofunction:: add_reference_lines

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   from dataviz.utils.validation import add_reference_lines

   rng = np.random.default_rng(42)
   fig, ax = plt.subplots()
   ax.plot(np.arange(30), rng.normal(loc=10.0, scale=0.4, size=30))

   add_reference_lines(ax, hline=10.0, vline=15)
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/utils/validation/add_reference_lines.png" alt="add_reference_lines example output"><figcaption>Example output</figcaption></figure></div>
