=============
Release notes
=============

.. current developments

0.3.0
=====

**Added:**

* Latest release checklist containing steps for `twine check dist/*` and `python -m build`
* Added support for Python 3.14

**Changed:**

* Modify `.github` directory and `.pre-commit-config.yaml` to comply with renaming of package maintainer.

**Fixed:**

* Added Sphinx imports to fix documentation rendering.
* Update copyright to 2022-2025.
* Format code to comply with group standards.
* API docstrings rendered with Linux GitHub CI by installing xvfb
* Support ``scikit-package`` Level 5 standard (https://scikit-package.github.io/scikit-package/).

**Removed:**

* Removed support for Python 3.11


0.2.0
=====

**Added:**

* tutorial added to documentation
* Add tutorial to documentation
* Added api documentation
* Add GitHub release workflow
* add docstrings to functions without docstrings
* Added `codespell` for spell check on all files.
* Added longer description to README along with proper citation for `diffpy.fourigui`

**Changed:**

* support for python < 3.13

**Fixed:**

* test warning applycutoff test
* added [project.scripts] to pyproject.toml
* Fixed deprecation warning presented by numpy2
* Suppress the `RuntimeWarning` in tests for the `applycutoff` function
* cookiecut to group's Python package standard
* add pip packages under pip.txt
* Recut to group's package standard, fix installation
* remove time dependency in pip, conda.txt
* qmin/qmax limits in reciprocal space grid so qmin and qmax are not excluded

**Removed:**

* debug.py file for running tests
* Removed support for python `<3.11`
