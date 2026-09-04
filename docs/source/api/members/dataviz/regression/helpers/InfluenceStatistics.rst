dataviz.regression.helpers.InfluenceStatistics
==============================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.regression.helpers</p></div>

.. currentmodule:: dataviz.regression.helpers

.. autoclass:: InfluenceStatistics
   :members:
   :show-inheritance:

Use case
--------

Returned by influence_statistics; carries per-observation leverage, Cook's distance, DFFITS, and DFBETAS.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.helpers import InfluenceStatistics

   y_true = np.array([3.0, 2.5, 4.2, 5.0, 4.7])
   y_pred = np.array([2.8, 2.7, 4.0, 5.1, 4.5])
   train_sizes = np.array([50, 100, 200])
   train_scores = np.array([0.82, 0.86, 0.89])
   validation_scores = np.array([0.76, 0.81, 0.84])

   result = InfluenceStatistics(leverage=None, residuals=None, standardized_residuals=None, studentized_residuals=None, cooks_distance=None, dffits=None, dfbetas=None, sigma_hat=0.5, n_features=5)
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
