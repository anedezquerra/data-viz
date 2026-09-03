dataviz.regression.domain.yield_curve_fit_plot_interactive
==========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.regression.domain</p></div>

.. currentmodule:: dataviz.regression.domain

.. autofunction:: yield_curve_fit_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.regression.domain import yield_curve_fit_plot_interactive

   rng = np.random.default_rng(42)
   maturities = np.array([0.25, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0])
   observed_yields = np.array([1.8, 2.0, 2.3, 2.6, 3.0, 3.2, 3.4])
   fitted_yields = observed_yields + rng.normal(0.0, 0.03, size=7)

   fig = yield_curve_fit_plot_interactive(maturities, observed_yields, fitted_yields)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
