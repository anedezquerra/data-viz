dataviz.univariate.text.top_terms_bar_interactive
=================================================

.. raw:: html

   <div class="spc-api-hero"><span>Function</span><p>dataviz.univariate.text</p></div>

.. currentmodule:: dataviz.univariate.text

.. autofunction:: top_terms_bar_interactive

Use case
--------

Use to chart the most common terms in a text column for quick exploratory profiling.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   import numpy as np
   import pandas as pd
   from dataviz.univariate.text import top_terms_bar_interactive

   rng = np.random.default_rng(42)
   vocab = ["battery", "screen", "delivery", "quality", "support", "price", "design", "fast"]
   reviews = pd.Series(
       [" ".join(rng.choice(vocab, size=rng.integers(3, 9))) for _ in range(60)],
       name="review",
   )
   fig = top_terms_bar_interactive(
       reviews,
       top_n=8,
       title="Most Common Terms in Product Reviews",
       color="coral",
       height=500,
   )
   fig.update_traces(showlegend=True, selector=lambda trace: bool(trace.name))
   fig.update_layout(legend=dict(orientation='h', yanchor='top', y=-0.2, xanchor='center', x=0.5), margin=dict(b=110))
   fig.show()

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot spc-image-real"><img src="../../../../../_static/api/dataviz/univariate/text/top_terms_bar_interactive.png" alt="top_terms_bar_interactive example output"><figcaption>Example output</figcaption></figure></div>
