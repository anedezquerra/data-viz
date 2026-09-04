dataviz.xai.uncertainty.confidence_attribution_bar_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.uncertainty</p></div>

.. currentmodule:: dataviz.xai.uncertainty

.. autofunction:: confidence_attribution_bar_static

Use case
--------

Use to attribute predictive uncertainty to individual features, identifying which inputs drive the model's lack of confidence.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.uncertainty import confidence_attribution_bar_static

   attribution = {
       "thin_credit_history": 0.142,
       "num_open_accounts": 0.087,
       "employment_years": 0.064,
       "loan_amount": 0.031,
       "annual_income": -0.028,
       "credit_score": -0.052,
   }
   ax = confidence_attribution_bar_static(
       attribution,
       title="Which features drive predictive uncertainty - applicant #992",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/uncertainty/confidence_attribution_bar_static.png" alt="confidence_attribution_bar_static example output"><figcaption>Example output</figcaption></figure></div>
