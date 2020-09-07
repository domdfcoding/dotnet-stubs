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
import System.Runtime.InteropServices
import System.Runtime.Remoting
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization
from System.ComponentModel import MarshalByValueComponent

from . import AccessControl
from . import Cryptography
from . import Policy
from . import Principal
from .Cryptography import X509Certificates


class PermissionSet:

    def __init__(self, *args, **kwargs) -> Any: ...

    def AddPermission(self,
            _: IPermission,
            ) -> IPermission: ...

    def AddPermissionImpl(self,
            _: IPermission,
            ) -> IPermission: ...

    def Assert(self) -> None: ...
    def ContainsNonCodeAccessPermissions(self) -> bool: ...
    def ConvertPermissionSet(self, _: str, __: List[bytes], ___: str) -> List[bytes]: ...
    def Copy(self) -> PermissionSet: ...
    def CopyTo(self, _: List, __: int) -> None: ...

    @property
    def Count(self): ...

    @Count.setter
    def Count(self, value): ...

    def Demand(self) -> None: ...
    def Deny(self) -> None: ...
    def Equals(self, _: object) -> bool: ...
    def Finalize(self) -> None: ...
    def FromXml(self, _: SecurityElement) -> None: ...
    def GetEnumerator(self) -> System.Collections.IEnumerator: ...
    def GetEnumeratorImpl(self) -> System.Collections.IEnumerator: ...
    def GetHashCode(self) -> int: ...
    def GetPermission(self, _: Type) -> IPermission: ...
    def GetPermissionImpl(self, _: Type) -> IPermission: ...
    def GetType(self) -> Type: ...

    def Intersect(self,
            _: PermissionSet,
            ) -> PermissionSet: ...

    def IsEmpty(self) -> bool: ...

    @property
    def IsReadOnly(self): ...

    @IsReadOnly.setter
    def IsReadOnly(self, value): ...

    def IsSubsetOf(self, _: PermissionSet) -> bool: ...

    @property
    def IsSynchronized(self): ...

    @IsSynchronized.setter
    def IsSynchronized(self, value): ...

    def IsUnrestricted(self) -> bool: ...
    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def PermitOnly(self) -> None: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def RemovePermission(self, _: Type) -> IPermission: ...
    def RemovePermissionImpl(self, _: Type) -> IPermission: ...
    def RevertAssert(self) -> None: ...

    def SetPermission(self,
            _: IPermission,
            ) -> IPermission: ...

    def SetPermissionImpl(self,
            _: IPermission,
            ) -> IPermission: ...

    @property
    def SyncRoot(self): ...

    @SyncRoot.setter
    def SyncRoot(self, value): ...

    def ToString(self) -> str: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, _: PermissionSet) -> PermissionSet: ...
    def get_Count(self) -> int: ...
    def get_IsReadOnly(self) -> bool: ...
    def get_IsSynchronized(self) -> bool: ...
    def get_SyncRoot(self) -> object: ...


class SecurityRuleSet:

    def __init__(self, *args, **kwargs) -> Any: ...
    def CompareTo(self, _: object) -> int: ...
    def Equals(self, _: object) -> bool: ...
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
    def Level1(self, *args, **kwargs) -> Any: ...
    def Level2(self, *args, **kwargs) -> Any: ...
    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Parse(self, _: Type, __: str, ___: bool) -> object: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...


class IPermission:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Copy(self) -> IPermission: ...
    def Demand(self) -> None: ...
    def FromXml(self, _: SecurityElement) -> None: ...
    def Intersect(self, _: IPermission) -> IPermission: ...
    def IsSubsetOf(self, _: IPermission) -> bool: ...
    def ToXml(self) -> SecurityElement: ...
    def Union(self, _: IPermission) -> IPermission: ...


class SecurityElement:

    def __init__(self, *args, **kwargs) -> Any: ...
    def AddAttribute(self, _: str, __: str) -> None: ...
    def AddChild(self, _: SecurityElement) -> None: ...
    def Attribute(self, _: str) -> str: ...

    @property
    def Attributes(self): ...

    @Attributes.setter
    def Attributes(self, value): ...

    @property
    def Children(self): ...

    @Children.setter
    def Children(self, value): ...

    def Copy(self) -> SecurityElement: ...
    def Equal(self, _: SecurityElement) -> bool: ...
    def Equals(self, _: object, __: object) -> bool: ...
    def Escape(self, _: str) -> str: ...
    def Finalize(self) -> None: ...
    def FromString(self, _: str) -> SecurityElement: ...
    def GetHashCode(self) -> int: ...
    def GetType(self) -> Type: ...
    def IsValidAttributeName(self, _: str) -> bool: ...
    def IsValidAttributeValue(self, _: str) -> bool: ...
    def IsValidTag(self, _: str) -> bool: ...
    def IsValidText(self, _: str) -> bool: ...
    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def SearchForChildByTag(self, _: str) -> SecurityElement: ...
    def SearchForTextOfTag(self, _: str) -> str: ...

    @property
    def Tag(self): ...

    @Tag.setter
    def Tag(self, value): ...

    @property
    def Text(self): ...

    @Text.setter
    def Text(self, value): ...

    def ToString(self) -> str: ...
    def get_Attributes(self) -> System.Collections.Hashtable: ...
    def get_Children(self) -> List: ...
    def get_Tag(self) -> str: ...
    def get_Text(self) -> str: ...
    def set_Attributes(self, _: System.Collections.Hashtable) -> None: ...
    def set_Children(self, _: List) -> None: ...
    def set_Tag(self, _: str) -> None: ...
    def set_Text(self, _: str) -> None: ...
