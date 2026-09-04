dataviz.xai.local_more.contrastive_explanation_bar_static
=========================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.local_more</p></div>

.. currentmodule:: dataviz.xai.local_more

.. autofunction:: contrastive_explanation_bar_static

Use case
--------

Use to show why a prediction holds (pertinent positives) versus what minimal changes would flip it (pertinent negatives).

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.local_more import contrastive_explanation_bar_static

   pertinent_positives = {
       "credit_score": 0.34, "employment_years": 0.21,
       "annual_income": 0.18, "debt_to_income": 0.12,
   }
   pertinent_negatives = {
       "late_payments": 0.27, "num_open_accounts": 0.15,
       "loan_amount": 0.09, "debt_to_income": 0.05,
   }
   ax = contrastive_explanation_bar_static(
       pertinent_positives, pertinent_negatives,
       title="Why approved vs what would flip to denial - applicant #771",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/local_more/contrastive_explanation_bar_static.png" alt="contrastive_explanation_bar_static example output"><figcaption>Example output</figcaption></figure></div>
