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
import System.Security
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


class FileSecurity:

    def __init__(self, *args, **kwargs) -> Any: ...

    @property
    def AccessRightType(self): ...

    @AccessRightType.setter
    def AccessRightType(self, value): ...

    def AccessRuleFactory(self,
            _: System.Security.Principal.IdentityReference,
            __: int,
            ___: bool,
            ____: InheritanceFlags,
            _____: PropagationFlags,
            ______: AccessControlType,
            ) -> AccessRule: ...

    @property
    def AccessRuleType(self): ...

    @AccessRuleType.setter
    def AccessRuleType(self, value): ...

    @property
    def AccessRulesModified(self): ...

    @AccessRulesModified.setter
    def AccessRulesModified(self, value): ...

    def AddAccessRule(self, _: AccessRule) -> None: ...
    def AddAuditRule(self, _: AuditRule) -> None: ...

    @property
    def AreAccessRulesCanonical(self): ...

    @AreAccessRulesCanonical.setter
    def AreAccessRulesCanonical(self, value): ...

    @property
    def AreAccessRulesProtected(self): ...

    @AreAccessRulesProtected.setter
    def AreAccessRulesProtected(self, value): ...

    @property
    def AreAuditRulesCanonical(self): ...

    @AreAuditRulesCanonical.setter
    def AreAuditRulesCanonical(self, value): ...

    @property
    def AreAuditRulesProtected(self): ...

    @AreAuditRulesProtected.setter
    def AreAuditRulesProtected(self, value): ...

    def AuditRuleFactory(self,
            _: System.Security.Principal.IdentityReference,
            __: int,
            ___: bool,
            ____: InheritanceFlags,
            _____: PropagationFlags,
            ______: AuditFlags,
            ) -> AuditRule: ...

    @property
    def AuditRuleType(self): ...

    @AuditRuleType.setter
    def AuditRuleType(self, value): ...

    @property
    def AuditRulesModified(self): ...

    @AuditRulesModified.setter
    def AuditRulesModified(self, value): ...

    def Equals(self, _: object, __: object) -> bool: ...
    def ExceptionFromErrorCode(self, *args, **kwargs) -> Any: ...
    def Finalize(self) -> None: ...

    def GetAccessRules(self,
            _: bool,
            __: bool,
            ___: Type,
            ) -> AuthorizationRuleCollection: ...

    def GetAuditRules(self,
            _: bool,
            __: bool,
            ___: Type,
            ) -> AuthorizationRuleCollection: ...

    def GetGroup(self, _: Type) -> System.Security.Principal.IdentityReference: ...
    def GetHashCode(self) -> int: ...
    def GetOwner(self, _: Type) -> System.Security.Principal.IdentityReference: ...
    def GetSecurityDescriptorBinaryForm(self) -> List[bytes]: ...

    def GetSecurityDescriptorSddlForm(self,
            _: AccessControlSections,
            ) -> str: ...

    def GetType(self) -> Type: ...

    @property
    def GroupModified(self): ...

    @GroupModified.setter
    def GroupModified(self, value): ...

    @property
    def IsContainer(self): ...

    @IsContainer.setter
    def IsContainer(self, value): ...

    @property
    def IsDS(self): ...

    @IsDS.setter
    def IsDS(self, value): ...

    def IsSddlConversionSupported(self) -> bool: ...
    def MemberwiseClone(self) -> object: ...

    def ModifyAccess(self,
            _: AccessControlModification,
            __: AccessRule,
            ___: bool,
            ) -> bool: ...

    def ModifyAccessRule(self,
            _: AccessControlModification,
            __: AccessRule,
            ___: bool,
            ) -> bool: ...

    def ModifyAudit(self,
            _: AccessControlModification,
            __: AuditRule,
            ___: bool,
            ) -> bool: ...

    def ModifyAuditRule(self,
            _: AccessControlModification,
            __: AuditRule,
            ___: bool,
            ) -> bool: ...

    def Overloads(self, *args, **kwargs) -> Any: ...

    @property
    def OwnerModified(self): ...

    @OwnerModified.setter
    def OwnerModified(self, value): ...

    def Persist(self,
            _: bool,
            __: str,
            ___: AccessControlSections,
            ) -> None: ...

    def PurgeAccessRules(self, _: System.Security.Principal.IdentityReference) -> None: ...
    def PurgeAuditRules(self, _: System.Security.Principal.IdentityReference) -> None: ...
    def ReadLock(self) -> None: ...
    def ReadUnlock(self) -> None: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def RemoveAccessRule(self, _: AccessRule) -> bool: ...
    def RemoveAccessRuleAll(self, _: AccessRule) -> None: ...

    def RemoveAccessRuleSpecific(self,
            _: AccessRule,
            ) -> None: ...

    def RemoveAuditRule(self, _: AuditRule) -> bool: ...
    def RemoveAuditRuleAll(self, _: AuditRule) -> None: ...

    def RemoveAuditRuleSpecific(self,
            _: AuditRule,
            ) -> None: ...

    def ResetAccessRule(self, _: AccessRule) -> None: ...
    def SetAccessRule(self, _: AccessRule) -> None: ...
    def SetAccessRuleProtection(self, _: bool, __: bool) -> None: ...
    def SetAuditRule(self, _: AuditRule) -> None: ...
    def SetAuditRuleProtection(self, _: bool, __: bool) -> None: ...
    def SetGroup(self, _: System.Security.Principal.IdentityReference) -> None: ...
    def SetOwner(self, _: System.Security.Principal.IdentityReference) -> None: ...

    def SetSecurityDescriptorBinaryForm(self,
            _: List[bytes],
            __: AccessControlSections,
            ) -> None: ...

    def SetSecurityDescriptorSddlForm(self,
            _: str,
            __: AccessControlSections,
            ) -> None: ...

    def ToString(self) -> str: ...
    def WriteLock(self) -> None: ...
    def WriteUnlock(self) -> None: ...
    def get_AccessRightType(self) -> Type: ...
    def get_AccessRuleType(self) -> Type: ...
    def get_AccessRulesModified(self) -> bool: ...
    def get_AreAccessRulesCanonical(self) -> bool: ...
    def get_AreAccessRulesProtected(self) -> bool: ...
    def get_AreAuditRulesCanonical(self) -> bool: ...
    def get_AreAuditRulesProtected(self) -> bool: ...
    def get_AuditRuleType(self) -> Type: ...
    def get_AuditRulesModified(self) -> bool: ...
    def get_GroupModified(self) -> bool: ...
    def get_IsContainer(self) -> bool: ...
    def get_IsDS(self) -> bool: ...
    def get_OwnerModified(self) -> bool: ...
    def set_AccessRulesModified(self, _: bool) -> None: ...
    def set_AuditRulesModified(self, _: bool) -> None: ...
    def set_GroupModified(self, _: bool) -> None: ...
    def set_OwnerModified(self, _: bool) -> None: ...


class InheritanceFlags:

    def __init__(self, *args, **kwargs) -> Any: ...
    def CompareTo(self, _: object) -> int: ...
    def ContainerInherit(self, *args, **kwargs) -> Any: ...
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
    def MemberwiseClone(self) -> object: ...
    def ObjectInherit(self, *args, **kwargs) -> Any: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Parse(self, _: Type, __: str, ___: bool) -> object: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...


class PropagationFlags:

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
    def InheritOnly(self, *args, **kwargs) -> Any: ...
    def IsDefined(self, _: Type, __: object) -> bool: ...
    def MemberwiseClone(self) -> object: ...
    def NoPropagateInherit(self, *args, **kwargs) -> Any: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Parse(self, _: Type, __: str, ___: bool) -> object: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...


class AccessControlType:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Allow(self, *args, **kwargs) -> Any: ...
    def CompareTo(self, _: object) -> int: ...
    def Deny(self, *args, **kwargs) -> Any: ...
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
    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Parse(self, _: Type, __: str, ___: bool) -> object: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...


class AccessRule:

    def __init__(self, *args, **kwargs) -> Any: ...

    @property
    def AccessControlType(self): ...

    @AccessControlType.setter
    def AccessControlType(self, value): ...

    @property
    def AccessMask(self): ...

    @AccessMask.setter
    def AccessMask(self, value): ...

    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def GetType(self) -> Type: ...

    @property
    def IdentityReference(self): ...

    @IdentityReference.setter
    def IdentityReference(self, value): ...

    @property
    def InheritanceFlags(self): ...

    @InheritanceFlags.setter
    def InheritanceFlags(self, value): ...

    @property
    def IsInherited(self): ...

    @IsInherited.setter
    def IsInherited(self, value): ...

    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...

    @property
    def PropagationFlags(self): ...

    @PropagationFlags.setter
    def PropagationFlags(self, value): ...

    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToString(self) -> str: ...
    def get_AccessControlType(self) -> AccessControlType: ...
    def get_AccessMask(self) -> int: ...
    def get_IdentityReference(self) -> System.Security.Principal.IdentityReference: ...
    def get_InheritanceFlags(self) -> InheritanceFlags: ...
    def get_IsInherited(self) -> bool: ...
    def get_PropagationFlags(self) -> PropagationFlags: ...


class AuditRule:

    def __init__(self, *args, **kwargs) -> Any: ...

    @property
    def AccessMask(self): ...

    @AccessMask.setter
    def AccessMask(self, value): ...

    @property
    def AuditFlags(self): ...

    @AuditFlags.setter
    def AuditFlags(self, value): ...

    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def GetType(self) -> Type: ...

    @property
    def IdentityReference(self): ...

    @IdentityReference.setter
    def IdentityReference(self, value): ...

    @property
    def InheritanceFlags(self): ...

    @InheritanceFlags.setter
    def InheritanceFlags(self, value): ...

    @property
    def IsInherited(self): ...

    @IsInherited.setter
    def IsInherited(self, value): ...

    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...

    @property
    def PropagationFlags(self): ...

    @PropagationFlags.setter
    def PropagationFlags(self, value): ...

    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToString(self) -> str: ...
    def get_AccessMask(self) -> int: ...
    def get_AuditFlags(self) -> AuditFlags: ...
    def get_IdentityReference(self) -> System.Security.Principal.IdentityReference: ...
    def get_InheritanceFlags(self) -> InheritanceFlags: ...
    def get_IsInherited(self) -> bool: ...
    def get_PropagationFlags(self) -> PropagationFlags: ...


class AuditFlags:

    def __init__(self, *args, **kwargs) -> Any: ...
    def CompareTo(self, _: object) -> int: ...
    def Equals(self, _: object) -> bool: ...
    def Failure(self, *args, **kwargs) -> Any: ...
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
    def Success(self, *args, **kwargs) -> Any: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...


class AccessControlSections:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Access(self, *args, **kwargs) -> Any: ...
    def All(self, *args, **kwargs) -> Any: ...
    def Audit(self, *args, **kwargs) -> Any: ...
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
    def Group(self, *args, **kwargs) -> Any: ...
    def HasFlag(self, _: Enum) -> bool: ...
    def IsDefined(self, _: Type, __: object) -> bool: ...
    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Owner(self, *args, **kwargs) -> Any: ...
    def Parse(self, _: Type, __: str, ___: bool) -> object: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...


class AuthorizationRuleCollection:

    def __init__(self, *args, **kwargs) -> Any: ...
    def AddRule(self, _: AuthorizationRule) -> None: ...

    def CopyTo(self,
            _: List[AuthorizationRule],
            __: int,
            ) -> None: ...

    @property
    def Count(self): ...

    @Count.setter
    def Count(self, value): ...

    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def GetEnumerator(self) -> System.Collections.IEnumerator: ...
    def GetHashCode(self) -> int: ...
    def GetType(self) -> Type: ...

    @property
    def InnerList(self): ...

    @InnerList.setter
    def InnerList(self, value): ...

    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToString(self) -> str: ...
    def get_Count(self) -> int: ...
    def get_InnerList(self) -> List: ...
    def get_Item(self, _: int) -> AuthorizationRule: ...


class AccessControlModification:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Add(self, *args, **kwargs) -> Any: ...
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
    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Parse(self, _: Type, __: str, ___: bool) -> object: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def Remove(self, *args, **kwargs) -> Any: ...
    def RemoveAll(self, *args, **kwargs) -> Any: ...
    def RemoveSpecific(self, *args, **kwargs) -> Any: ...
    def Reset(self, *args, **kwargs) -> Any: ...
    def Set(self, *args, **kwargs) -> Any: ...
    def ToObject(self, _: Type, __: object) -> object: ...
    def ToString(self, _: str, __: Any) -> str: ...
    def TryParse(self, *args, **kwargs) -> Any: ...


class AuthorizationRule:

    def __init__(self, *args, **kwargs) -> Any: ...

    @property
    def AccessMask(self): ...

    @AccessMask.setter
    def AccessMask(self, value): ...

    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def GetType(self) -> Type: ...

    @property
    def IdentityReference(self): ...

    @IdentityReference.setter
    def IdentityReference(self, value): ...

    @property
    def InheritanceFlags(self): ...

    @InheritanceFlags.setter
    def InheritanceFlags(self, value): ...

    @property
    def IsInherited(self): ...

    @IsInherited.setter
    def IsInherited(self, value): ...

    def MemberwiseClone(self) -> object: ...
    def Overloads(self, *args, **kwargs) -> Any: ...

    @property
    def PropagationFlags(self): ...

    @PropagationFlags.setter
    def PropagationFlags(self, value): ...

    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def ToString(self) -> str: ...
    def get_AccessMask(self) -> int: ...
    def get_IdentityReference(self) -> System.Security.Principal.IdentityReference: ...
    def get_InheritanceFlags(self) -> InheritanceFlags: ...
    def get_IsInherited(self) -> bool: ...
    def get_PropagationFlags(self) -> PropagationFlags: ...
