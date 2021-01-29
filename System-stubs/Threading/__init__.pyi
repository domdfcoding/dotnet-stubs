from __future__ import annotations

# stdlib
from typing import Any, List, Type

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
import System.Security.Cryptography
import System.Security.Cryptography.X509Certificates
import System.Security.Policy
import System.Security.Principal
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization
from System.ComponentModel import MarshalByValueComponent

# this package
from . import Tasks

class CancellationToken:

	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def CanBeCanceled(self): ...

	@CanBeCanceled.setter
	def CanBeCanceled(self, value): ...

	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...

	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...

	@property
	def IsCancellationRequested(self): ...

	@IsCancellationRequested.setter
	def IsCancellationRequested(self, value): ...

	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Register(
			self,
			_: System.Action[object],
			__: object,
			___: bool,
			) -> CancellationTokenRegistration: ...

	def ThrowIfCancellationRequested(self) -> None: ...
	def ToString(self) -> str: ...

	@property
	def WaitHandle(self): ...

	@WaitHandle.setter
	def WaitHandle(self, value): ...

	def get_CanBeCanceled(self) -> bool: ...
	def get_IsCancellationRequested(self) -> bool: ...
	def get_None(self) -> CancellationToken: ...
	def get_WaitHandle(self) -> WaitHandle: ...
	def op_Equality(
			self,
			_: CancellationToken,
			__: CancellationToken,
			) -> bool: ...

	def op_Inequality(
			self,
			_: CancellationToken,
			__: CancellationToken,
			) -> bool: ...

class WaitHandle:

	def __init__(self, *args, **kwargs) -> Any: ...
	def Close(self) -> None: ...
	def CreateObjRef(self, _: Type) -> System.Runtime.Remoting.ObjRef: ...
	def Dispose(self, _: bool) -> None: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...

	def GetLifetimeService(self) -> object: ...
	def GetType(self) -> Type: ...

	@property
	def Handle(self): ...

	@Handle.setter
	def Handle(self, value): ...

	def InitializeLifetimeService(self) -> object: ...
	def InvalidHandle(self, *args, **kwargs) -> Any: ...
	def MemberwiseClone(self) -> object: ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...

	@property
	def SafeWaitHandle(self): ...

	@SafeWaitHandle.setter
	def SafeWaitHandle(self, value): ...

	def SignalAndWait(
			self,
			_: WaitHandle,
			__: WaitHandle,
			___: int,
			____: bool,
			) -> bool: ...

	def ToString(self) -> str: ...
	def WaitAll(self, _: List[WaitHandle], __: int, ___: bool) -> bool: ...
	def WaitAny(self, _: List[WaitHandle], __: int, ___: bool) -> int: ...
	def WaitOne(self, _: int, __: bool) -> bool: ...
	def WaitTimeout(self, *args, **kwargs) -> Any: ...
	def get_Handle(self) -> Any: ...
	def get_SafeWaitHandle(self) -> Any: ...
	def set_Handle(self, _: Any) -> None: ...
	def set_SafeWaitHandle(self, _: Any) -> None: ...

class CancellationTokenRegistration:

	def __init__(self, *args, **kwargs) -> Any: ...
	def Dispose(self) -> None: ...
	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToString(self) -> str: ...
	def op_Equality(
			self,
			_: CancellationTokenRegistration,
			__: CancellationTokenRegistration,
			) -> bool: ...

	def op_Inequality(
			self,
			_: CancellationTokenRegistration,
			__: CancellationTokenRegistration,
			) -> bool: ...
