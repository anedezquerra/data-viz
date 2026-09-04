dataviz.utils.helpers.apply_theme
=================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.utils.helpers</p></div>

.. currentmodule:: dataviz.utils.helpers

.. autofunction:: apply_theme

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.utils.helpers import apply_theme

   fig, ax = plt.subplots()
   ax.plot([1, 2, 3], [1, 4, 9])

   apply_theme(ax, theme="default")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/utils/helpers/apply_theme.png" alt="apply_theme example output"><figcaption>Example output</figcaption></figure></div>
