dataviz.xai.surrogate.surrogate_tree_plot_static
================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.surrogate</p></div>

.. currentmodule:: dataviz.xai.surrogate

.. autofunction:: surrogate_tree_plot_static

Use case
--------

Use to render a shallow interpretable tree distilled from a black-box model, supplied as a list of depth/condition/prediction rule dicts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.surrogate import surrogate_tree_plot_static

   rules = [
       {"depth": 0, "condition": "credit_score < 620"},
       {"depth": 1, "parent": 0, "condition": "debt_to_income >= 0.43"},
       {"depth": 1, "parent": 0, "condition": "debt_to_income < 0.43"},
       {"depth": 2, "parent": 1, "condition": "late_payments > 0",
        "prediction": "deny (p=0.91)"},
       {"depth": 2, "parent": 1, "condition": "late_payments = 0",
        "prediction": "manual review (p=0.55)"},
       {"depth": 2, "parent": 2, "condition": "employment_years < 2",
        "prediction": "deny (p=0.74)"},
       {"depth": 2, "parent": 2, "condition": "employment_years >= 2",
        "prediction": "approve (p=0.68)"},
   ]
   ax = surrogate_tree_plot_static(
       rules, title="Surrogate tree approximating the credit-risk black box",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/surrogate/surrogate_tree_plot_static.png" alt="surrogate_tree_plot_static example output"><figcaption>Example output</figcaption></figure></div>
