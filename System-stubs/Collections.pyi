from __future__ import annotations

# stdlib
from typing import Any, List, Type

# 3rd party
import System
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
import System.Threading
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization
from System.ComponentModel import MarshalByValueComponent

class IEnumerator:
	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Current(self): ...

	@Current.setter
	def Current(self, value): ...

	def MoveNext(self) -> bool: ...
	def Reset(self) -> None: ...
	def get_Current(self) -> object: ...

class IDictionary:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Add(self, _: object, __: object) -> None: ...
	def Clear(self) -> None: ...
	def Contains(self, _: object) -> bool: ...
	def CopyTo(self, _: List, __: int) -> None: ...

	@property
	def Count(self): ...

	@Count.setter
	def Count(self, value): ...

	def GetEnumerator(self) -> IDictionaryEnumerator: ...

	@property
	def IsFixedSize(self): ...

	@IsFixedSize.setter
	def IsFixedSize(self, value): ...

	@property
	def IsReadOnly(self): ...

	@IsReadOnly.setter
	def IsReadOnly(self, value): ...

	@property
	def IsSynchronized(self): ...

	@IsSynchronized.setter
	def IsSynchronized(self, value): ...

	@property
	def Keys(self): ...

	@Keys.setter
	def Keys(self, value): ...

	def Remove(self, _: object) -> None: ...

	@property
	def SyncRoot(self): ...

	@SyncRoot.setter
	def SyncRoot(self, value): ...

	@property
	def Values(self): ...

	@Values.setter
	def Values(self, value): ...

	def get_Count(self) -> int: ...
	def get_IsFixedSize(self) -> bool: ...
	def get_IsReadOnly(self) -> bool: ...
	def get_IsSynchronized(self) -> bool: ...
	def get_Item(self, _: object) -> object: ...
	def get_Keys(self) -> ICollection: ...
	def get_SyncRoot(self) -> object: ...
	def get_Values(self) -> ICollection: ...
	def set_Item(self, _: object, __: object) -> None: ...

class ArrayList:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Adapter(self, _: List) -> List: ...
	def Add(self, _: object) -> int: ...
	def AddRange(self, _: ICollection) -> None: ...

	def BinarySearch(
			self,
			_: int,
			__: int,
			___: object,
			____: IComparer,
			) -> int: ...

	@property
	def Capacity(self): ...

	@Capacity.setter
	def Capacity(self, value): ...

	def Clear(self) -> None: ...
	def Clone(self) -> object: ...
	def Contains(self, _: object) -> bool: ...
	def CopyTo(self, _: int, __: List, ___: int, ____: int) -> None: ...

	@property
	def Count(self): ...

	@Count.setter
	def Count(self, value): ...

	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def FixedSize(self, _: List) -> List: ...
	def GetEnumerator(self, _: int, __: int) -> IEnumerator: ...
	def GetHashCode(self) -> int: ...
	def GetRange(self, _: int, __: int) -> List: ...
	def GetType(self) -> Type: ...
	def IndexOf(self, _: object, __: int, ___: int) -> int: ...
	def Insert(self, _: int, __: object) -> None: ...
	def InsertRange(self, _: int, __: ICollection) -> None: ...

	@property
	def IsFixedSize(self): ...

	@IsFixedSize.setter
	def IsFixedSize(self, value): ...

	@property
	def IsReadOnly(self): ...

	@IsReadOnly.setter
	def IsReadOnly(self, value): ...

	@property
	def IsSynchronized(self): ...

	@IsSynchronized.setter
	def IsSynchronized(self, value): ...

	def LastIndexOf(self, _: object, __: int, ___: int) -> int: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReadOnly(self, _: List) -> List: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Remove(self, _: object) -> None: ...
	def RemoveAt(self, _: int) -> None: ...
	def RemoveRange(self, _: int, __: int) -> None: ...
	def Repeat(self, _: object, __: int) -> List: ...
	def Reverse(self, _: int, __: int) -> None: ...
	def SetRange(self, _: int, __: ICollection) -> None: ...
	def Sort(self, _: int, __: int, ___: IComparer) -> None: ...

	@property
	def SyncRoot(self): ...

	@SyncRoot.setter
	def SyncRoot(self, value): ...

	def Synchronized(self, _: List) -> List: ...
	def ToArray(self, _: Type) -> List: ...
	def ToString(self) -> str: ...
	def TrimToSize(self) -> None: ...
	def get_Capacity(self) -> int: ...
	def get_Count(self) -> int: ...
	def get_IsFixedSize(self) -> bool: ...
	def get_IsReadOnly(self) -> bool: ...
	def get_IsSynchronized(self) -> bool: ...
	def get_Item(self, _: int) -> object: ...
	def get_SyncRoot(self) -> object: ...
	def set_Capacity(self, _: int) -> None: ...
	def set_Item(self, _: int, __: object) -> None: ...

class IDictionaryEnumerator:
	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Current(self): ...

	@Current.setter
	def Current(self, value): ...

	@property
	def Entry(self): ...

	@Entry.setter
	def Entry(self, value): ...

	@property
	def Key(self): ...

	@Key.setter
	def Key(self, value): ...

	def MoveNext(self) -> bool: ...
	def Reset(self) -> None: ...

	@property
	def Value(self): ...

	@Value.setter
	def Value(self, value): ...

	def get_Current(self) -> object: ...
	def get_Entry(self) -> DictionaryEntry: ...
	def get_Key(self) -> object: ...
	def get_Value(self) -> object: ...

class IEqualityComparer:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def GetHashCode(self, _: object) -> int: ...

class ICollection:
	def __init__(self, *args, **kwargs) -> Any: ...
	def CopyTo(self, _: List, __: int) -> None: ...

	@property
	def Count(self): ...

	@Count.setter
	def Count(self, value): ...

	def GetEnumerator(self) -> IEnumerator: ...

	@property
	def IsSynchronized(self): ...

	@IsSynchronized.setter
	def IsSynchronized(self, value): ...

	@property
	def SyncRoot(self): ...

	@SyncRoot.setter
	def SyncRoot(self, value): ...

	def get_Count(self) -> int: ...
	def get_IsSynchronized(self) -> bool: ...
	def get_SyncRoot(self) -> object: ...

class IHashCodeProvider:
	def __init__(self, *args, **kwargs) -> Any: ...
	def GetHashCode(self, _: object) -> int: ...

class IComparer:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Compare(self, _: object, __: object) -> int: ...

class Hashtable:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Add(self, _: object, __: object) -> None: ...
	def Clear(self) -> None: ...
	def Clone(self) -> object: ...
	def Contains(self, _: object) -> bool: ...
	def ContainsKey(self, _: object) -> bool: ...
	def ContainsValue(self, _: object) -> bool: ...
	def CopyTo(self, _: List, __: int) -> None: ...

	@property
	def Count(self): ...

	@Count.setter
	def Count(self, value): ...

	@property
	def EqualityComparer(self): ...

	@EqualityComparer.setter
	def EqualityComparer(self, value): ...

	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetEnumerator(self) -> IDictionaryEnumerator: ...
	def GetHash(self, _: object) -> int: ...
	def GetHashCode(self) -> int: ...

	def GetObjectData(
			self,
			_: System.Runtime.Serialization.SerializationInfo,
			__: System.Runtime.Serialization.StreamingContext,
			) -> None: ...

	def GetType(self) -> Type: ...

	@property
	def IsFixedSize(self): ...

	@IsFixedSize.setter
	def IsFixedSize(self, value): ...

	@property
	def IsReadOnly(self): ...

	@IsReadOnly.setter
	def IsReadOnly(self, value): ...

	@property
	def IsSynchronized(self): ...

	@IsSynchronized.setter
	def IsSynchronized(self, value): ...

	def KeyEquals(self, _: object, __: object) -> bool: ...

	@property
	def Keys(self): ...

	@Keys.setter
	def Keys(self, value): ...

	def MemberwiseClone(self) -> object: ...
	def OnDeserialization(self, _: object) -> None: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Remove(self, _: object) -> None: ...

	@property
	def SyncRoot(self): ...

	@SyncRoot.setter
	def SyncRoot(self, value): ...

	def Synchronized(
			self,
			_: Hashtable,
			) -> Hashtable: ...

	def ToString(self) -> str: ...

	@property
	def Values(self): ...

	@Values.setter
	def Values(self, value): ...

	@property
	def comparer(self): ...

	@comparer.setter
	def comparer(self, value): ...

	def get_Count(self) -> int: ...
	def get_EqualityComparer(self) -> IEqualityComparer: ...
	def get_IsFixedSize(self) -> bool: ...
	def get_IsReadOnly(self) -> bool: ...
	def get_IsSynchronized(self) -> bool: ...
	def get_Item(self, _: object) -> object: ...
	def get_Keys(self) -> ICollection: ...
	def get_SyncRoot(self) -> object: ...
	def get_Values(self) -> ICollection: ...
	def get_comparer(self) -> IComparer: ...
	def get_hcp(self) -> IHashCodeProvider: ...

	@property
	def hcp(self): ...

	@hcp.setter
	def hcp(self, value): ...

	def set_Item(self, _: object, __: object) -> None: ...
	def set_comparer(self, _: IComparer) -> None: ...
	def set_hcp(self, _: IHashCodeProvider) -> None: ...

class DictionaryEntry:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...

	@property
	def Key(self): ...

	@Key.setter
	def Key(self, value): ...

	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToString(self) -> str: ...

	@property
	def Value(self): ...

	@Value.setter
	def Value(self, value): ...

	def get_Key(self) -> object: ...
	def get_Value(self) -> object: ...
	def set_Key(self, _: object) -> None: ...
	def set_Value(self, _: object) -> None: ...

class IList:
	def __init__(self, *args, **kwargs) -> Any: ...
	def Add(self, _: object) -> int: ...
	def Clear(self) -> None: ...
	def Contains(self, _: object) -> bool: ...
	def CopyTo(self, _: List, __: int) -> None: ...

	@property
	def Count(self): ...

	@Count.setter
	def Count(self, value): ...

	def GetEnumerator(self) -> IEnumerator: ...
	def IndexOf(self, _: object) -> int: ...
	def Insert(self, _: int, __: object) -> None: ...

	@property
	def IsFixedSize(self): ...

	@IsFixedSize.setter
	def IsFixedSize(self, value): ...

	@property
	def IsReadOnly(self): ...

	@IsReadOnly.setter
	def IsReadOnly(self, value): ...

	@property
	def IsSynchronized(self): ...

	@IsSynchronized.setter
	def IsSynchronized(self, value): ...

	def Remove(self, _: object) -> None: ...
	def RemoveAt(self, _: int) -> None: ...

	@property
	def SyncRoot(self): ...

	@SyncRoot.setter
	def SyncRoot(self, value): ...

	def get_Count(self) -> int: ...
	def get_IsFixedSize(self) -> bool: ...
	def get_IsReadOnly(self) -> bool: ...
	def get_IsSynchronized(self) -> bool: ...
	def get_Item(self, _: int) -> object: ...
	def get_SyncRoot(self) -> object: ...
	def set_Item(self, _: int, __: object) -> None: ...
