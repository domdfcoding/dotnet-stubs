#############
dotnet-stubs
#############

.. start short_desc

**Incomplete, and probably incorrect, stubs for .NET**

.. end short_desc


.. start shields

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |actions_linux| image:: https://github.com/domdfcoding/dotnet-stubs/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/dotnet-stubs/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/dotnet-stubs/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/dotnet-stubs/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/dotnet-stubs/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/dotnet-stubs/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/dotnet-stubs/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/dotnet-stubs/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/dotnet-stubs/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/dotnet-stubs/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/dotnet-stubs/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/dotnet-stubs/
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/dotnet-stubs?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/dotnet-stubs
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/dotnet-stubs
	:target: https://pypi.org/project/dotnet-stubs/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/dotnet-stubs?logo=python&logoColor=white
	:target: https://pypi.org/project/dotnet-stubs/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/dotnet-stubs
	:target: https://pypi.org/project/dotnet-stubs/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/dotnet-stubs
	:target: https://pypi.org/project/dotnet-stubs/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/dotnet-stubs
	:target: https://github.com/domdfcoding/dotnet-stubs/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/dotnet-stubs
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/dotnet-stubs/v0.0.12
	:target: https://github.com/domdfcoding/dotnet-stubs/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/dotnet-stubs
	:target: https://github.com/domdfcoding/dotnet-stubs/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2024
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/dotnet-stubs
	:target: https://pypi.org/project/dotnet-stubs/
	:alt: PyPI - Downloads

.. end shields

|

Installation
--------------

.. start installation

``dotnet-stubs`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install dotnet-stubs

.. end installation


Stubs are build using the ``dotnet_stub_builder`` that ships alongside these stubs. Is has additional dependencies, which can be installed using the ``builder`` extra:

.. code-block:: bash

	$ python -m pip install dotnet-stubs[builder]
