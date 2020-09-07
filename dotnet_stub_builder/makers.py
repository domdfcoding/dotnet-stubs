#!/usr/bin/env python3
#
#  makers.py
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
from types import FunctionType, ModuleType
from typing import Any, Iterable, List

# 3rd party
import clr  # type: ignore
import isort  # type: ignore
from autoflake import fix_code  # type: ignore
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.stringlist import StringList

# this package
from dotnet_stub_builder.type_conversion import Converter
from dotnet_stub_builder.utils import (
		SYSTEM_MODULES, dedup, get_child_attrs, get_signature, is_dunder, isort_config, make_property
		)

clr.AddReference("System")

# 3rd party
import System  # type: ignore

__all__ = ["make_imports", "make_module", "make_package", "walk_attrs"]


def make_imports(current_module_name: str) -> List[str]:
	"""
	Create the imports for the top of a stub file.

	:param current_module_name: The name of the current module.

	:return:
	"""

	imports = [
			"from __future__ import annotations",
			'',
			"from enum import Enum",
			"from typing import Any, Dict, List, Type",
			'',
			]

	for m in SYSTEM_MODULES:
		if m != current_module_name:
			imports.append(f"import {m}")

	return imports


def make_module(
		name: str,
		module: ModuleType,
		attr_list: Iterable[str] = (),
		first_party_imports: Iterable[str] = (),
		converter=Converter()
		) -> bool:
	"""
	Create type stubs for a module.

	:param name: The name of the module.
	:param module: The module object.
	:param attr_list: A list of attributes to create stubs for.
	:param first_party_imports: A list of first-party imports to include at the top of the file.
	"""

	buf = StringList()
	path = name.split(".")

	stubs_dir = PathPlus(f"{path[0]}-stubs")
	stubs_dir.maybe_make()
	(stubs_dir / "/".join(x for x in path[1:-1])).maybe_make(parents=True)
	stub_file = stubs_dir / "/".join(x for x in path[1:-1]) / f"{path[-1]}.pyi"

	import_name = name.replace(".__init__", '')

	for imp in (*make_imports(name), *first_party_imports):
		imp = re.sub(
				fr"import {import_name}\.([A-Za-z_]+)\.([A-Za-z_]+)\.([A-Za-z_]+)", r"from .\1.\2 import \3", imp
				)
		imp = re.sub(fr"import {import_name}\.([A-Za-z_]+)\.([A-Za-z_]+)", r"from .\1 import \2", imp)
		imp = re.sub(fr"import {import_name}\.([A-Za-z_]+)", r"from . import \1", imp)
		imp = re.sub(fr"import {import_name}$", "", imp)
		buf.append(imp)

	if import_name != "System.ComponentModel":
		if import_name == "System":
			buf.append("from .ComponentModel import MarshalByValueComponent")
		else:
			buf.append("from System.ComponentModel import MarshalByValueComponent")

	for attr_name in dedup(attr_list):
		stub_code = walk_attrs(module, attr_name, converter=converter)
		stub_code = stub_code.replace(f": {import_name}.", ': ')
		stub_code = stub_code.replace(f" -> {import_name}.", ' -> ')
		stub_code = stub_code.replace(f"[{import_name}.", '[')
		stub_code.replace("System.Collections.Generic.IDictionary[System.String,System.String]", "Any")

		buf.blankline(ensure_single=True)
		buf.blankline()

		buf.append(stub_code)

	sorted_code = isort.code(str(buf), config=isort_config)
	sans_unneeded_imports = fix_code(
			sorted_code,
			additional_imports=None,
			expand_star_imports=False,
			remove_all_unused_imports=False,
			remove_duplicate_keys=False,
			remove_unused_variables=False,
			ignore_init_module_imports=False,
			)

	stub_file.write_text(sans_unneeded_imports)

	return True


def make_package(
		name: str,
		module: ModuleType,
		attr_list: Iterable[str] = (),
		converter=Converter(),
		) -> bool:
	"""
	Create type stubs for a module.

	:param name: The name of the module.
	:param module: The module object.
	:param attr_list: A list of attributes to create stubs for.
	"""

	path = name.split(".")

	stubs_dir = PathPlus(f"{path[0]}-stubs")
	(stubs_dir / "/".join(x for x in path[1:])).maybe_make(parents=True)

	return make_module(f"{name}.__init__", module, attr_list, converter=converter)


def walk_attrs(module: ModuleType, attr_name, converter=Converter()) -> str:
	"""
	Create stubs for given class, including all attributes.

	:param module:
	:param attr_name:
	:param converter:

	:return:
	"""

	buf = StringList(convert_indents=True)
	buf.indent_type = "    "

	if not is_dunder(attr_name):
		obj = getattr(module, attr_name)

		# TODO: case where obj is not a class
		if not isinstance(obj, FunctionType):
			bases = []
			for base in obj.__bases__:
				if base not in {System.Object, object}:
					if base.__name__ in converter.type_mapping:
						bases.append(converter.type_mapping[base.__name__])
					else:
						bases.append(base.__name__)

			bases = list(filter(lambda x: x is Any, bases))

			if bases:
				buf.append(f"class {attr_name}({', '.join(bases)}):\n")
			else:
				buf.append(f"class {attr_name}:\n")

			for child_attr_name in get_child_attrs(obj):
				try:
					child_obj = getattr(obj, child_attr_name)
				except TypeError as e:
					if str(e) in {
							"instance property must be accessed through a class instance",
							"property cannot be read",
							}:

						make_property(buf, child_attr_name)
						continue

					elif str(e) == "instance attribute must be accessed through a class instance":
						print(f"{e.__class__.__name__}: '{e}' occurred for {attr_name}.{child_attr_name}")
						continue

					else:
						raise e

				# TODO: if isinstance(child_obj, FunctionType):

				return_type, arguments = get_signature(child_obj, child_attr_name, converter)

				with buf.with_indent_size(buf.indent_size + 1):

					if arguments is not None and arguments:
						signature = []

						for idx, argument in enumerate(arguments.split(", ")):
							signature.append(f"{'_' * (idx + 1)}: {converter.convert_type(argument)}")

						line = f"def {child_attr_name}(self, {', '.join(signature)}) -> {return_type}: ..."

						if len(line) > 88:
							buf.blankline(ensure_single=True)
							buf.append(f"def {child_attr_name}(")

							with buf.with_indent_size(buf.indent_size + 2):
								buf.append("self,")
								for line in signature:
									buf.append(f"{line},")
								buf.append(f") -> {return_type}: ...\n")
						else:
							buf.append(line)

					elif arguments is None:
						buf.append(f"def {child_attr_name}(self, *args, **kwargs) -> {return_type}: ...")

					elif not arguments:
						# i.e. takes no arguments
						buf.append(f"def {child_attr_name}(self) -> {return_type}: ...")

		buf.blankline(ensure_single=True)
		return str(buf)

	return ''
