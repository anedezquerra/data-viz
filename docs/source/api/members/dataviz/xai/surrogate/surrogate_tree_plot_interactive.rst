dataviz.xai.surrogate.surrogate_tree_plot_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.surrogate</p></div>

.. currentmodule:: dataviz.xai.surrogate

.. autofunction:: surrogate_tree_plot_interactive

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.surrogate import surrogate_tree_plot_interactive

   rules = [
       {"depth": 0, "condition": "income <= 50k"},
       {"depth": 1, "condition": "debt <= 10k", "parent": 0, "prediction": "approve"},
       {"depth": 1, "condition": "debt > 10k", "parent": 0, "prediction": "review"},
       {"depth": 0, "condition": "income > 50k", "prediction": "approve"},
   ]

   fig = surrogate_tree_plot_interactive(rules)
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
