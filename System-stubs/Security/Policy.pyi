from __future__ import annotations

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
import System.Security.AccessControl
import System.Security.Cryptography
import System.Security.Cryptography.X509Certificates
import System.Threading
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization
from System.ComponentModel import MarshalByValueComponent


class Evidence:

    def __init__(self, *args, **kwargs) -> Any: ...
    def AddAssembly(self, _: object) -> None: ...
    def AddAssemblyEvidence(self, *args, **kwargs) -> Any: ...
    def AddHost(self, _: object) -> None: ...
    def AddHostEvidence(self, *args, **kwargs) -> Any: ...
    def Clear(self) -> None: ...
    def Clone(self) -> Evidence: ...
    def CopyTo(self, _: List, __: int) -> None: ...

    @property
    def Count(self): ...

    @Count.setter
    def Count(self, value): ...

    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def GetAssemblyEnumerator(self) -> System.Collections.IEnumerator: ...
    def GetAssemblyEvidence(self, *args, **kwargs) -> Any: ...
    def GetEnumerator(self) -> System.Collections.IEnumerator: ...
    def GetHashCode(self) -> int: ...
    def GetHostEnumerator(self) -> System.Collections.IEnumerator: ...
    def GetHostEvidence(self, *args, **kwargs) -> Any: ...
    def GetType(self) -> Type: ...

    @property
    def IsReadOnly(self): ...

    @IsReadOnly.setter
    def IsReadOnly(self, value): ...

    @property
    def IsSynchronized(self): ...

    @IsSynchronized.setter
    def IsSynchronized(self, value): ...

    @property
    def Locked(self): ...

    @Locked.setter
    def Locked(self, value): ...

    def MemberwiseClone(self) -> object: ...
    def Merge(self, _: Evidence) -> None: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def RemoveType(self, _: Type) -> None: ...

    @property
    def SyncRoot(self): ...

    @SyncRoot.setter
    def SyncRoot(self, value): ...

    def ToString(self) -> str: ...
    def get_Count(self) -> int: ...
    def get_IsReadOnly(self) -> bool: ...
    def get_IsSynchronized(self) -> bool: ...
    def get_Locked(self) -> bool: ...
    def get_SyncRoot(self) -> object: ...
    def set_Locked(self, _: bool) -> None: ...
