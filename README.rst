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
	  - |travis| |actions_windows| |actions_macos| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|



.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/dotnet-stubs/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/dotnet-stubs
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/dotnet-stubs/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/dotnet-stubs/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/dotnet-stubs/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/dotnet-stubs/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/dotnet-stubs/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/dotnet-stubs/requirements/?branch=master
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

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/dotnet-stubs/v0.0.10
	:target: https://github.com/domdfcoding/dotnet-stubs/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/dotnet-stubs
	:target: https://github.com/domdfcoding/dotnet-stubs/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

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
