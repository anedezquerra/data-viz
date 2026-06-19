dataviz.spc.multivariate.hotelling_t2_chart_interactive
=======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.spc.multivariate</p></div>

.. currentmodule:: dataviz.spc.multivariate

.. autofunction:: hotelling_t2_chart_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   from dataviz.spc.multivariate import hotelling_t2_chart_interactive

   rng = np.random.default_rng(42)
   data = rng.multivariate_normal([10.0, 25.0, 4.0], [[1.0, 0.5, 0.2], [0.5, 2.0, 0.3], [0.2, 0.3, 0.5]], size=40)

   fig = hotelling_t2_chart_interactive(data, limit_quantile=0.95)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
