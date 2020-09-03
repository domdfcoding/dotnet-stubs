#!/usr/bin/env python
# This file is managed by 'repo_helper'. Don't edit it directly.

# stdlib
import sys

# 3rd party
from setuptools import setup

sys.path.append('.')

# this package
from __pkginfo__ import *  # pylint: disable=wildcard-import



setup(
		description='Incomplete, and probably incorrect, stubs for .NET.',
		extras_require=extras_require,
		install_requires=install_requires,
		py_modules=[],
		version=__version__,
		packages=["System-stubs", "dotnet_stub_builder"]
		)
