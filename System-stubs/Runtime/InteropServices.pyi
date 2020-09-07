from __future__ import annotations

from enum import Enum
from typing import Any
from typing import List
from typing import Type

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


class StructLayoutAttribute:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Equals(self, _: object) -> bool: ...
    def Finalize(self) -> None: ...

    def GetCustomAttribute(self,
            _: System.Reflection.ParameterInfo,
            __: Type,
            ___: bool,
            ) -> System.Attribute: ...

    def GetCustomAttributes(self,
            _: System.Reflection.ParameterInfo,
            __: Type,
            ___: bool,
            ) -> List[System.Attribute]: ...

    def GetHashCode(self) -> int: ...
    def GetType(self) -> Type: ...
    def IsDefaultAttribute(self) -> bool: ...

    def IsDefined(self,
            _: System.Reflection.ParameterInfo,
            __: Type,
            ___: bool,
            ) -> bool: ...

    def Match(self, _: object) -> bool: ...
    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToString(self) -> str: ...

    @property
    def TypeId(self): ...

    @TypeId.setter
    def TypeId(self, value): ...

    @property
    def Value(self): ...

    @Value.setter
    def Value(self, value): ...
    def get_TypeId(self) -> object: ...
    def get_Value(self) -> LayoutKind: ...


class LayoutKind:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Auto(self, *args, **kwargs) -> Any: ...
    def CompareTo(self, _: object) -> int: ...
    def Equals(self, _: object) -> bool: ...
    def Explicit(self, *args, **kwargs) -> Any: ...
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
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Parse(self, _: Type, __: str, ___: bool) -> object: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def Sequential(self, *args, **kwargs) -> Any: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...
