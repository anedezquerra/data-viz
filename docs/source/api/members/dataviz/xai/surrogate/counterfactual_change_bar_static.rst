dataviz.xai.surrogate.counterfactual_change_bar_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.surrogate</p></div>

.. currentmodule:: dataviz.xai.surrogate

.. autofunction:: counterfactual_change_bar_static

Use case
--------

Use to show the smallest per-feature changes needed to flip a prediction, annotated with original to counterfactual values.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.surrogate import counterfactual_change_bar_static

   original = {
       "credit_score": 598.0, "debt_to_income": 0.46,
       "loan_amount": 22000.0, "annual_income": 48000.0,
       "employment_years": 1.0, "late_payments": 2.0,
   }
   counterfactual = {
       "credit_score": 645.0, "debt_to_income": 0.38,
       "loan_amount": 18000.0, "annual_income": 48000.0,
       "employment_years": 1.0, "late_payments": 0.0,
   }
   ax = counterfactual_change_bar_static(
       original, counterfactual, top_n=6,
       title="Smallest changes to flip applicant #2048 to approval",
   )
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/surrogate/counterfactual_change_bar_static.png" alt="counterfactual_change_bar_static example output"><figcaption>Example output</figcaption></figure></div>
