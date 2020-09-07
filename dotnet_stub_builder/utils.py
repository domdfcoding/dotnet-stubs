#!/usr/bin/env python3
#
#  utils.py
"""
General utility functions.
"""
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# stdlib
import re
import string
from typing import Iterable, Iterator, List, Optional, Tuple, Type

# 3rd party
from domdf_python_tools.stringlist import StringList
from domdf_python_tools.words import alpha_sort, ascii_digits
from isort import Config  # type: ignore
from orderedset import OrderedSet  # type: ignore

# this package
from dotnet_stub_builder.type_conversion import Converter

__all__ = [
		"dedup",
		"is_dunder",
		"get_signature",
		"make_property",
		"get_child_attrs",
		"method_alphabet",
		"SKIP_ATTRS",
		"isort_config",
		"SYSTEM_MODULES",
		]


def dedup(iterable: Iterable[str]) -> List:
	"""
	Return the given iterable sans duplicates.

	:param iterable:
	"""

	return list(OrderedSet(iterable))


def is_dunder(attr_name: str) -> bool:
	"""
	Retuns whether the given attr is a magic/dunder method.

	:param attr_name:
	"""

	return attr_name.startswith("__") and attr_name.endswith("__")


def get_signature(
		obj: Type,
		obj_name: str,
		converter: Converter,
		) -> Tuple[str, Optional[str]]:
	"""

	:param obj:
	:param obj_name:
	:param converter:

	:return:
	"""

	return_type: str = "Any"
	arguments: Optional[str] = None

	doc: Optional[str] = obj.__doc__
	if doc in {int.__doc__, str.__doc__}:
		doc = None

	if doc:
		for line in doc.splitlines():
			m = re.match(fr"^(.*) {obj_name}\((.*)\)", line.strip())
			if m:
				csharp_return_type = m.group(1)
				return_type = converter.convert_type(csharp_return_type)
				arguments = m.group(2)

	return return_type, arguments


def make_property(buf: StringList, name: str) -> None:
	"""
	Add the signature of a property to the given
	:class:`domdf_python_tools.stringlist.StringList`.

	:param buf:
	:param name:
	"""

	with buf.with_indent_size(buf.indent_size + 1):
		buf.blankline(ensure_single=True)
		buf.append(f"@property\ndef {name}(self): ...")
		buf.blankline(ensure_single=True)

	with buf.with_indent_size(buf.indent_size + 1):
		buf.blankline(ensure_single=True)
		buf.append(f"@{name}.setter\ndef {name}(self, value): ...")
		buf.blankline(ensure_single=True)


def get_child_attrs(obj: Type) -> Iterator[str]:
	"""
	Returns a list of child attributes for the given object.

	:param obj:
	"""

	child_attrs = dir(obj)
	if "__init__" not in child_attrs:
		child_attrs.append("__init__")

	for child_attr_name in alpha_sort(child_attrs, alphabet=method_alphabet):
		if not is_dunder(child_attr_name) or child_attr_name == "__init__":
			if child_attr_name not in SKIP_ATTRS:
				yield child_attr_name


isort_config = Config(force_single_line=True)
method_alphabet = f"_{string.ascii_uppercase}{string.ascii_lowercase}{ascii_digits}"

SYSTEM_MODULES = [
		"System",
		"System.Collections",
		"System.ComponentModel",
		"System.Configuration",
		"System.Configuration.Assemblies",
		"System.Data",
		"System.Globalization",
		"System.IO",
		"System.Reflection",
		"System.Runtime",
		"System.Runtime.CompilerServices",
		"System.Runtime.InteropServices",
		"System.Runtime.Remoting",
		"System.Runtime.Serialization",
		"System.Security",
		"System.Security.AccessControl",
		"System.Security.Cryptography",
		"System.Security.Cryptography.X509Certificates",
		"System.Security.Policy",
		"System.Security.Principal",
		"System.Threading",
		"System.Threading.Tasks",
		"System.Xml",
		"System.Xml.Schema",
		"System.Xml.Serialization",
		]

SKIP_ATTRS = {
		"None",
		"value__",
		"AttrsImpl",
		"ClassImpl",
		"DefaultValueImpl",
		"MemberImpl",
		"NameImpl",
		"PositionImpl",
		}
