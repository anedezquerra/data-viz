dataviz.univariate.profile.UnivariateProfile
============================================

.. raw:: html

   <div class="spc-api-hero"><span>Class</span><p>dataviz.univariate.profile</p></div>

.. currentmodule:: dataviz.univariate.profile

.. autoclass:: UnivariateProfile
   :members:
   :show-inheritance:

Use case
--------

Immutable result carrying the variable name, inferred kind, data quality summary, and a type-specific summary payload from auto_profile.

Complete example
----------------

The following example is self-contained and can be copied into a Python session or script.

.. code-block:: python

   from dataviz.univariate.profile import UnivariateProfile
   from dataviz.univariate.quality import DataQualitySummary

   quality = DataQualitySummary(
       count=150, missing=3, missing_rate=0.02, unique=118,
       duplicate_rate=0.19, zero_rate=0.0, negative_rate=0.0,
   )
   result = UnivariateProfile(
       name="monthly_spend",
       kind="numeric",
       quality=quality,
       summary={"count": 147, "mean": 82.4},
   )
   print(result)

Output gallery
--------------

.. raw:: html

   <div class="spc-image-grid"><figure class="spc-image-slot"><div aria-hidden="true">01</div><figcaption>Future example image 1</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">02</div><figcaption>Future example image 2</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">03</div><figcaption>Future example image 3</figcaption></figure><figure class="spc-image-slot"><div aria-hidden="true">04</div><figcaption>Future example image 4</figcaption></figure></div>
