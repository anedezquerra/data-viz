Documentation development
=========================

Source of truth
---------------

The publishable documentation lives in ``docs/source``. The ``website`` folder
is a legacy static prototype and is not used by the GitHub Pages workflow.

Build locally
-------------

Install the documentation dependencies and package:

.. code-block:: console

   python -m pip install -e ".[docs]"
   python -m sphinx -W --keep-going -b html docs/source docs/build/html

Open ``docs/build/html/index.html`` after a successful build. Build artifacts
are ignored by Git and should not be committed.

Validate links
--------------

.. code-block:: console

   python -m sphinx -W --keep-going -b linkcheck docs/source docs/build/linkcheck

Regenerate API pages
--------------------

The API pages are generated from the Python package layout:

.. code-block:: console

   python docs/generate_api.py

The generator creates one page per public function or class beneath its
submodule and keeps subpackage / submodule pages as navigation indexes.

Lint generated docs
-------------------

After regenerating pages, run the wording check that protects against
boilerplate creeping back into auto-generated pages (e.g. ``(this package)``
in example requirements blocks or ``<dotted.name> package`` H1 headings):

.. code-block:: console

   python docs/_tools/check_package_wording.py

The same check runs in the ``Documentation`` workflow and will fail CI if
new generator templates reintroduce the redundant wording.

GitHub Pages
------------

Pull requests run the strict Sphinx build without deploying. Pushes to
``main`` upload the HTML artifact and deploy it through GitHub's official Pages
actions. In repository settings, select **GitHub Actions** as the Pages source.
