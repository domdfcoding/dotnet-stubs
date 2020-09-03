from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Type

import System
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
import System.Threading
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization
from System.ComponentModel import MarshalByValueComponent


class IEnumerator:

    @property
    def Current(self): ...

    @Current.setter
    def Current(self): ...

    def MoveNext(self) -> bool: ...

    def Reset(self) -> None: ...

    def __init__(self, *args, **kwargs) -> Any: ...

    def get_Current(self) -> object: ...


class IDictionary:

    def Add(self, _: object, __: object) -> None: ...

    def Clear(self) -> None: ...

    def Contains(self, _: object) -> bool: ...

    def CopyTo(self, _: List, __: int) -> None: ...

    @property
    def Count(self): ...

    @Count.setter
    def Count(self): ...

    def GetEnumerator(self) -> IDictionaryEnumerator: ...

    @property
    def IsFixedSize(self): ...

    @IsFixedSize.setter
    def IsFixedSize(self): ...

    @property
    def IsReadOnly(self): ...

    @IsReadOnly.setter
    def IsReadOnly(self): ...

    @property
    def IsSynchronized(self): ...

    @IsSynchronized.setter
    def IsSynchronized(self): ...

    @property
    def Keys(self): ...

    @Keys.setter
    def Keys(self): ...

    def Remove(self, _: object) -> None: ...

    @property
    def SyncRoot(self): ...

    @SyncRoot.setter
    def SyncRoot(self): ...

    @property
    def Values(self): ...

    @Values.setter
    def Values(self): ...

    def __init__(self, *args, **kwargs) -> Any: ...

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

    def Adapter(self, _: List) -> List: ...

    def Add(self, _: object) -> int: ...

    def AddRange(self, _: ICollection) -> None: ...

    def BinarySearch(self,
            _: int,
            __: int,
            ___: object,
            ____: IComparer,
            ) -> int: ...

    @property
    def Capacity(self): ...

    @Capacity.setter
    def Capacity(self): ...

    def Clear(self) -> None: ...

    def Clone(self) -> object: ...

    def Contains(self, _: object) -> bool: ...

    def CopyTo(self, _: int, __: List, ___: int, ____: int) -> None: ...

    @property
    def Count(self): ...

    @Count.setter
    def Count(self): ...

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
    def IsFixedSize(self): ...

    @property
    def IsReadOnly(self): ...

    @IsReadOnly.setter
    def IsReadOnly(self): ...

    @property
    def IsSynchronized(self): ...

    @IsSynchronized.setter
    def IsSynchronized(self): ...

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
    def SyncRoot(self): ...

    def Synchronized(self, _: List) -> List: ...

    def ToArray(self, _: Type) -> List: ...

    def ToString(self) -> str: ...

    def TrimToSize(self) -> None: ...

    def __init__(self, *args, **kwargs) -> Any: ...

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

    @property
    def Current(self): ...

    @Current.setter
    def Current(self): ...

    @property
    def Entry(self): ...

    @Entry.setter
    def Entry(self): ...

    @property
    def Key(self): ...

    @Key.setter
    def Key(self): ...

    def MoveNext(self) -> bool: ...

    def Reset(self) -> None: ...

    @property
    def Value(self): ...

    @Value.setter
    def Value(self): ...

    def __init__(self, *args, **kwargs) -> Any: ...

    def get_Current(self) -> object: ...

    def get_Entry(self) -> DictionaryEntry: ...

    def get_Key(self) -> object: ...

    def get_Value(self) -> object: ...


class IEqualityComparer:

    def Equals(self, _: object, __: object) -> bool: ...

    def GetHashCode(self, _: object) -> int: ...

    def __init__(self, *args, **kwargs) -> Any: ...


class ICollection:

    def CopyTo(self, _: List, __: int) -> None: ...

    @property
    def Count(self): ...

    @Count.setter
    def Count(self): ...

    def GetEnumerator(self) -> IEnumerator: ...

    @property
    def IsSynchronized(self): ...

    @IsSynchronized.setter
    def IsSynchronized(self): ...

    @property
    def SyncRoot(self): ...

    @SyncRoot.setter
    def SyncRoot(self): ...

    def __init__(self, *args, **kwargs) -> Any: ...

    def get_Count(self) -> int: ...

    def get_IsSynchronized(self) -> bool: ...

    def get_SyncRoot(self) -> object: ...


class IHashCodeProvider:

    def GetHashCode(self, _: object) -> int: ...

    def __init__(self, *args, **kwargs) -> Any: ...


class IComparer:

    def Compare(self, _: object, __: object) -> int: ...

    def __init__(self, *args, **kwargs) -> Any: ...


class Hashtable:

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
    def Count(self): ...

    @property
    def EqualityComparer(self): ...

    @EqualityComparer.setter
    def EqualityComparer(self): ...

    def Equals(self, _: object, __: object) -> bool: ...

    def Finalize(self) -> None: ...

    def GetEnumerator(self) -> IDictionaryEnumerator: ...

    def GetHash(self, _: object) -> int: ...

    def GetHashCode(self) -> int: ...

    def GetObjectData(self,
            _: System.Runtime.Serialization.SerializationInfo,
            __: System.Runtime.Serialization.StreamingContext,
            ) -> None: ...

    def GetType(self) -> Type: ...

    @property
    def IsFixedSize(self): ...

    @IsFixedSize.setter
    def IsFixedSize(self): ...

    @property
    def IsReadOnly(self): ...

    @IsReadOnly.setter
    def IsReadOnly(self): ...

    @property
    def IsSynchronized(self): ...

    @IsSynchronized.setter
    def IsSynchronized(self): ...

    def KeyEquals(self, _: object, __: object) -> bool: ...

    @property
    def Keys(self): ...

    @Keys.setter
    def Keys(self): ...

    def MemberwiseClone(self) -> object: ...

    def OnDeserialization(self, _: object) -> None: ...

    def Overloads(self, *args, **kwargs) -> Any: ...

    def ReferenceEquals(self, _: object, __: object) -> bool: ...

    def Remove(self, _: object) -> None: ...

    @property
    def SyncRoot(self): ...

    @SyncRoot.setter
    def SyncRoot(self): ...

    def Synchronized(self,
            _: Hashtable,
            ) -> Hashtable: ...

    def ToString(self) -> str: ...

    @property
    def Values(self): ...

    @Values.setter
    def Values(self): ...

    def __init__(self, *args, **kwargs) -> Any: ...

    @property
    def comparer(self): ...

    @comparer.setter
    def comparer(self): ...

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
    def hcp(self): ...

    def set_Item(self, _: object, __: object) -> None: ...

    def set_comparer(self, _: IComparer) -> None: ...

    def set_hcp(self, _: IHashCodeProvider) -> None: ...


class DictionaryEntry:

    def Equals(self, _: object) -> bool: ...

    def Finalize(self) -> None: ...

    def GetHashCode(self) -> int: ...

    def GetType(self) -> Type: ...

    @property
    def Key(self): ...

    @Key.setter
    def Key(self): ...

    def MemberwiseClone(self) -> object: ...

    def Overloads(self, *args, **kwargs) -> Any: ...

    def ReferenceEquals(self, _: object, __: object) -> bool: ...

    def ToString(self) -> str: ...

    @property
    def Value(self): ...

    @Value.setter
    def Value(self): ...

    def __init__(self, *args, **kwargs) -> Any: ...

    def get_Key(self) -> object: ...

    def get_Value(self) -> object: ...

    def set_Key(self, _: object) -> None: ...

    def set_Value(self, _: object) -> None: ...


class IList:

    def Add(self, _: object) -> int: ...

    def Clear(self) -> None: ...

    def Contains(self, _: object) -> bool: ...

    def CopyTo(self, _: List, __: int) -> None: ...

    @property
    def Count(self): ...

    @Count.setter
    def Count(self): ...

    def GetEnumerator(self) -> IEnumerator: ...

    def IndexOf(self, _: object) -> int: ...

    def Insert(self, _: int, __: object) -> None: ...

    @property
    def IsFixedSize(self): ...

    @IsFixedSize.setter
    def IsFixedSize(self): ...

    @property
    def IsReadOnly(self): ...

    @IsReadOnly.setter
    def IsReadOnly(self): ...

    @property
    def IsSynchronized(self): ...

    @IsSynchronized.setter
    def IsSynchronized(self): ...

    def Remove(self, _: object) -> None: ...

    def RemoveAt(self, _: int) -> None: ...

    @property
    def SyncRoot(self): ...

    @SyncRoot.setter
    def SyncRoot(self): ...

    def __init__(self, *args, **kwargs) -> Any: ...

    def get_Count(self) -> int: ...

    def get_IsFixedSize(self) -> bool: ...

    def get_IsReadOnly(self) -> bool: ...

    def get_IsSynchronized(self) -> bool: ...

    def get_Item(self, _: int) -> object: ...

    def get_SyncRoot(self) -> object: ...

    def set_Item(self, _: int, __: object) -> None: ...
