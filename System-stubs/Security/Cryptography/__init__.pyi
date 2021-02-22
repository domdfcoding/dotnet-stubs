from __future__ import annotations

# stdlib
from typing import Any, Type

# 3rd party
import System
import System.Collections
import System.ComponentModel
import System.Configuration
import System.Configuration.Assemblies
import System.Data
import System.Globalization
import System.IO
import System.Reflection
import System.Runtime
import System.Runtime.CompilerServices
import System.Runtime.InteropServices
import System.Runtime.Remoting
import System.Runtime.Serialization
import System.Security
import System.Security.AccessControl
import System.Security.Policy
import System.Security.Principal
import System.Threading
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization
from System.ComponentModel import MarshalByValueComponent

# this package
from . import X509Certificates

class HashAlgorithmName:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MD5(self, *args, **kwargs) -> Any: ...
	def MemberwiseClone(self) -> object: ...

	@property
	def Name(self): ...

	@Name.setter
	def Name(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def SHA1(self, *args, **kwargs) -> Any: ...
	def SHA256(self, *args, **kwargs) -> Any: ...
	def SHA384(self, *args, **kwargs) -> Any: ...
	def SHA512(self, *args, **kwargs) -> Any: ...
	def ToString(self) -> str: ...
	def get_MD5(self) -> HashAlgorithmName: ...
	def get_Name(self) -> str: ...
	def get_SHA1(self) -> HashAlgorithmName: ...
	def get_SHA256(self) -> HashAlgorithmName: ...
	def get_SHA384(self) -> HashAlgorithmName: ...
	def get_SHA512(self) -> HashAlgorithmName: ...

	def op_Equality(
			self,
			_: HashAlgorithmName,
			__: HashAlgorithmName,
			) -> bool: ...

	def op_Inequality(
			self,
			_: HashAlgorithmName,
			__: HashAlgorithmName,
			) -> bool: ...
