dataviz.xai.surrogate.surrogate_tree_plot_interactive
=====================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.surrogate</p></div>

.. currentmodule:: dataviz.xai.surrogate

.. autofunction:: surrogate_tree_plot_interactive

Use case
--------

Use to render a shallow interpretable tree distilled from a black-box model, supplied as a list of depth/condition/prediction rule dicts.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.xai.surrogate import surrogate_tree_plot_interactive

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
   fig = surrogate_tree_plot_interactive(
       rules, title="Surrogate tree approximating the credit-risk black box",
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/surrogate/surrogate_tree_plot_interactive.png" alt="surrogate_tree_plot_interactive example output"><figcaption>Example output</figcaption></figure></div>
