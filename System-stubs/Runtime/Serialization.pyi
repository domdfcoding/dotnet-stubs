from __future__ import annotations

# stdlib
from enum import Enum
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
import System.Security
import System.Security.AccessControl
import System.Security.Cryptography
import System.Security.Cryptography.X509Certificates
import System.Security.Policy
import System.Security.Principal
import System.Threading
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization
from System.ComponentModel import MarshalByValueComponent

class StreamingContextStates:
	def __init__(self, *args, **kwargs) -> Any: ...
	def All(self, *args, **kwargs) -> Any: ...
	def Clone(self, *args, **kwargs) -> Any: ...
	def CompareTo(self, _: object) -> int: ...
	def CrossAppDomain(self, *args, **kwargs) -> Any: ...
	def CrossMachine(self, *args, **kwargs) -> Any: ...
	def CrossProcess(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object) -> bool: ...
	def File(self, *args, **kwargs) -> Any: ...
	def Finalize(self) -> None: ...
	def Format(self, _: Type, __: object, ___: str) -> str: ...
	def GetHashCode(self) -> int: ...
	def GetName(self, _: Type, __: object) -> str: ...
	def GetNames(self, _: Type) -> List[str]: ...
	def GetType(self) -> Type: ...
	def GetTypeCode(self) -> Any: ...
	def GetUnderlyingType(self, _: Type) -> Type: ...
	def GetValues(self, _: Type) -> List: ...
	def HasFlag(self, _: Enum) -> bool: ...
	def IsDefined(self, _: Type, __: object) -> bool: ...
	def MemberwiseClone(self) -> object: ...
	def Other(self, *args, **kwargs) -> Any: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def Parse(self, _: Type, __: str, ___: bool) -> object: ...
	def Persistence(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Remoting(self, *args, **kwargs) -> Any: ...
	def ToObject(self, _: Type, __: object) -> object: ...
	def ToString(self, _: str, __: Any) -> str: ...
	def TryParse(self, *args, **kwargs) -> Any: ...

class SerializationEntry:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...

	@property
	def Name(self): ...

	@Name.setter
	def Name(self, value): ...

	@property
	def ObjectType(self): ...

	@ObjectType.setter
	def ObjectType(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToString(self) -> str: ...

	@property
	def Value(self): ...

	@Value.setter
	def Value(self, value): ...

	def get_Name(self) -> str: ...
	def get_ObjectType(self) -> Type: ...
	def get_Value(self) -> object: ...

class SerializationInfo:
	def __init__(self, *args, **kwargs) -> Any: ...
	def AddValue(self, _: str, __: object, ___: Type) -> None: ...

	@property
	def AssemblyName(self): ...

	@AssemblyName.setter
	def AssemblyName(self, value): ...

	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...

	@property
	def FullTypeName(self): ...

	@FullTypeName.setter
	def FullTypeName(self, value): ...

	def GetBoolean(self, _: str) -> bool: ...
	def GetByte(self, _: str) -> bytes: ...
	def GetChar(self, _: str) -> str: ...
	def GetDateTime(self, _: str) -> System.DateTime: ...
	def GetDecimal(self, _: str) -> float: ...
	def GetDouble(self, _: str) -> float: ...
	def GetEnumerator(self) -> SerializationInfoEnumerator: ...
	def GetHashCode(self) -> int: ...
	def GetInt16(self, _: str) -> int: ...
	def GetInt32(self, _: str) -> int: ...
	def GetInt64(self, _: str) -> int: ...
	def GetSByte(self, _: str) -> bytes: ...
	def GetSingle(self, _: str) -> float: ...
	def GetString(self, _: str) -> str: ...
	def GetType(self) -> Type: ...
	def GetUInt16(self, _: str) -> int: ...
	def GetUInt32(self, _: str) -> int: ...
	def GetUInt64(self, _: str) -> int: ...
	def GetValue(self, _: str, __: Type) -> object: ...

	@property
	def IsAssemblyNameSetExplicit(self): ...

	@IsAssemblyNameSetExplicit.setter
	def IsAssemblyNameSetExplicit(self, value): ...

	@property
	def IsFullTypeNameSetExplicit(self): ...

	@IsFullTypeNameSetExplicit.setter
	def IsFullTypeNameSetExplicit(self, value): ...

	@property
	def MemberCount(self): ...

	@MemberCount.setter
	def MemberCount(self, value): ...

	def MemberwiseClone(self) -> object: ...

	@property
	def ObjectType(self): ...

	@ObjectType.setter
	def ObjectType(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def SetType(self, _: Type) -> None: ...
	def ToString(self) -> str: ...
	def get_AssemblyName(self) -> str: ...
	def get_FullTypeName(self) -> str: ...
	def get_IsAssemblyNameSetExplicit(self) -> bool: ...
	def get_IsFullTypeNameSetExplicit(self) -> bool: ...
	def get_MemberCount(self) -> int: ...
	def get_ObjectType(self) -> Type: ...
	def set_AssemblyName(self, _: str) -> None: ...
	def set_FullTypeName(self, _: str) -> None: ...

class StreamingContext:
	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Context(self): ...

	@Context.setter
	def Context(self, value): ...

	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...

	@property
	def State(self): ...

	@State.setter
	def State(self, value): ...

	def ToString(self) -> str: ...
	def get_Context(self) -> object: ...
	def get_State(self) -> StreamingContextStates: ...

class SerializationInfoEnumerator:
	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Current(self): ...

	@Current.setter
	def Current(self, value): ...

	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...
	def MoveNext(self) -> bool: ...

	@property
	def Name(self): ...

	@Name.setter
	def Name(self, value): ...

	@property
	def ObjectType(self): ...

	@ObjectType.setter
	def ObjectType(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Reset(self) -> None: ...
	def ToString(self) -> str: ...

	@property
	def Value(self): ...

	@Value.setter
	def Value(self, value): ...

	def get_Current(self) -> SerializationEntry: ...
	def get_Name(self) -> str: ...
	def get_ObjectType(self) -> Type: ...
	def get_Value(self) -> object: ...

class SafeSerializationEventArgs:
	def __init__(self, *args, **kwargs) -> Any: ...

	def AddSerializedState(
			self,
			_: ISafeSerializationData,
			) -> None: ...

	def Empty(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...

	@property
	def StreamingContext(self): ...

	@StreamingContext.setter
	def StreamingContext(self, value): ...

	def ToString(self) -> str: ...
	def get_StreamingContext(self) -> StreamingContext: ...

class ISafeSerializationData:
	def __init__(self, *args, **kwargs) -> Any: ...
	def CompleteDeserialization(self, _: object) -> None: ...
