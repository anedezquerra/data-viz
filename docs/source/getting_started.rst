Getting started
===============

Installation
------------

Install the package from a local checkout:

.. code-block:: console

   python -m pip install -e .

For development, testing, and documentation tooling:

.. code-block:: console

   python -m pip install -e ".[dev,docs]"

Basic workflow
--------------

Static chart functions return Matplotlib axes. Interactive functions return
Plotly figures.

.. code-block:: python

   import matplotlib.pyplot as plt
   import pandas as pd
   import dataviz as dv

   values = pd.Series([12.1, 11.8, 13.0, 12.7, 14.2], name="Cycle time")

   ax = dv.histogram(values, bins=8, title="Cycle-time distribution")
   ax.figure.tight_layout()
   plt.show()

   fig = dv.histogram_interactive(values, bins=8)
   fig.show()

Import styles
-------------

The package supports both convenience imports and explicit submodule access:

.. code-block:: python

   import dataviz as dv

   ax = dv.scatter_plot(x, y)
   fig = dv.bivariate.scatter_plot_interactive(x, y)

Prefer explicit submodule access in larger applications when it makes API
ownership clearer.

Next steps
----------

* Read :doc:`user_guide` for module selection and return-value conventions.
* Try the complete snippets in :doc:`examples`.
* Browse :doc:`api/modules` for generated API documentation.
