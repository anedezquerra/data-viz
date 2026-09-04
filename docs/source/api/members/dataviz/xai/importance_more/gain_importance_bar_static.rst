dataviz.xai.importance_more.gain_importance_bar_static
======================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.xai.importance_more</p></div>

.. currentmodule:: dataviz.xai.importance_more

.. autofunction:: gain_importance_bar_static

Use case
--------

Use to rank features by gradient-boosting gain, optionally overlaying split counts on a second axis to spot overused weak splits.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import matplotlib.pyplot as plt
   from dataviz.xai.importance_more import gain_importance_bar_static

   gain = {
       "credit_score": 42.7, "debt_to_income": 31.4, "loan_amount": 24.9,
       "employment_years": 18.2, "annual_income": 15.6,
       "num_open_accounts": 9.8, "age": 7.3, "num_credit_cards": 5.1,
   }
   split_count = {
       "credit_score": 184, "debt_to_income": 152, "loan_amount": 131,
       "employment_years": 98, "annual_income": 87, "num_open_accounts": 54,
       "age": 41, "num_credit_cards": 26,
   }
   ax = gain_importance_bar_static(
       gain, split_count=split_count, top_n=8,
       title="XGBoost gain importance - credit default model",
   )
   ax.set_xlabel("Total gain (bars) vs split count (line)")
   plt.gca().legend(loc="upper center", bbox_to_anchor=(0.5, -0.12), ncols=3, frameon=False)
   plt.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/xai/importance_more/gain_importance_bar_static.png" alt="gain_importance_bar_static example output"><figcaption>Example output</figcaption></figure></div>
