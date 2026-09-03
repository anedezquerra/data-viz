dataviz.xai.shap_extra.shap_dependence_plot_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.shap_extra</p></div>

.. currentmodule:: dataviz.xai.shap_extra

.. autofunction:: shap_dependence_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.xai.shap_extra import shap_dependence_plot_interactive

   rng = np.random.default_rng(39)
   feature_values = rng.uniform(20.0, 80.0, 80)
   shap_age = 0.02 * (feature_values - 50.0) + rng.normal(0.0, 0.03, 80)
   interaction = rng.uniform(0.0, 1.0, 80)

   fig = shap_dependence_plot_interactive(
       shap_age, feature_values, interaction_values=interaction,
       feature_name="age", interaction_name="tenure",
   )
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
