#!/usr/bin/env python3
#
#  type_conversion.py
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
from typing import Dict, Optional

__all__ = ["generic_type_regex", "Converter"]

generic_type_regex = re.compile(r"^([A-Za-z_.]+)(`[0-9])?\[([A-Za-z_.,]+)]$")


class Converter:
	"""
	Class to convert .NET types into Python types.
	"""

	def __init__(self, extra_mappings: Optional[Dict[str, str]] = None):
		if extra_mappings is None:
			extra_mappings = {}

		# Mapping of .NET types to Python types (all as strings)
		self.type_mapping = {
				"Boolean": "bool",
				"System.Boolean": "bool",
				"Byte": "bytes",
				"SByte": "bytes",  # TODO
				"Char": "str",
				"System.Decimal": "float",  # TODO
				"Single": "float",
				"System.Single": "float",
				"Double": "float",
				"System.Double": "float",
				"Int32": "int",
				"UInt32": "int",  # TODO: sign
				"Int64": "int",  # TODO: bit size
				"UInt64": "int",  # TODO: bit size & sign
				# UInt64
				"Int16": "int",  # TODO: bit size
				"UInt16": "int",  # TODO: bit size & sign
				"System.Object": "object",
				"System.String": "str",
				"System.Collections.Generic.IDictionary": "Dict",
				"System.Type": "Type",
				"Long": "int",
				"Void": "None",
				"System.Array": "List",
				"System.Collections.ArrayList": "List",
				"System.Collections.IList": "List",
				"System.Collections.Generic.List": "List",
				"System.Collections.Generic.IList": "List",
				"System.Enum": "Enum",
				"System.Exception": "Exception",
				"System.AggregateException": "Exception",
				"System.Data.DataRow": "List",
				"System.Data.DataColumn": "List",
				"System.Data.DataColumnChangeEventArgs": "Any",
				"System.Nullable`1[System.Int32]": "Any",
				"System.Action`1[System.Threading.Tasks.Task[]]": "Any",
				"DbDataReader": "Any",
				"ConfiguredTaskAwaiter": "Any",
				"TInput": "Any",
				"TOutput": "Any",
				"TResult": "Any",
				"IntPtr": "Any",
				"StandardValuesCollection": "Any",
				"System.Text.Encoding": "Any",
				"System.Uri": "Any",
				"System.Net.ICredentials": "Any",
				"System.Xml.XPath.XPathNavigator": "Any",
				"YieldAwaiter": "Any",
				"TypedReference": "Any",
				"MarshalByRefObject": "Any",
				"ReadOnlyCollectionBase": "Any",
				"Microsoft.Win32.SafeHandles.SafeWaitHandle": "Any",
				"EventArgs": "Any",
				"System.Threading.Tasks.Task`1[System.Int32]": "System.Threading.Tasks.Task",
				"System.Collections.Generic.IEnumerable": "List",
				"Hashtable": "Any",
				"System.Delegate": "Any",
				"System.IAsyncResult": "Any",
				"System.TypeCode": "Any",
				"System.MulticastDelegate": "Any",
				"MulticastDelegate": "Any",
				"ValueType": "Any",
				"System.EventHandler": "Any",
				"System.IFormatProvider": "Any",
				"System.AsyncCallback": "Any",
				"System.Data.Common.DbDataReader": "Any",
				"T": "Any",
				"System.Collections.Generic.IComparer": "Any",
				"IonPolarity": "Any",
				"SmoothingFunctionType": "Any",
				"SortDirection": "Any",
				"System.Runtime.Remoting.Messaging.IMessageSink": "Any",
				**extra_mappings,
				}

	def convert_type(self, csharp_type: str) -> str:
		csharp_type = re.sub(" ByRef$", '', csharp_type)

		if csharp_type in self.type_mapping:
			return self.type_mapping[csharp_type]

		elif csharp_type.endswith("[]"):
			if csharp_type[:-2] in self.type_mapping:
				return f"List[{self.type_mapping[csharp_type[:-2]]}]"
			else:
				print(f"Warning: Unknown type {csharp_type!r}")
				return f"List[{csharp_type[:-2]}]"

		elif generic_type_regex.match(csharp_type):
			m = generic_type_regex.match(csharp_type)

			container_type = self.convert_type(m.group(1))  # type: ignore

			if container_type == "Any":
				return "Any"

			inner_type = ", ".join(self.convert_type(t.strip()) for t in m.group(3).split(","))  # type: ignore

			return f"{container_type}[{inner_type}]"

		elif csharp_type.startswith("System."):
			return csharp_type

		elif csharp_type.startswith("Microsoft.Win32."):
			return "Any"

		else:
			# print(generic_type_regex.match(csharp_type))
			raise KeyError(f"Unknown type: {csharp_type}")
