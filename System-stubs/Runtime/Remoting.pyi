from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Type

import System
import System.Collections
import System.Configuration
import System.Configuration.Assemblies
import System.Data
import System.Globalization
import System.IO
import System.Reflection
import System.Runtime
import System.Runtime.CompilerServices
import System.Runtime.InteropServices
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


class ObjRef:

    @property
    def ChannelInfo(self): ...

    @ChannelInfo.setter
    def ChannelInfo(self): ...

    @property
    def EnvoyInfo(self): ...

    @EnvoyInfo.setter
    def EnvoyInfo(self): ...

    def Equals(self, _: object, __: object) -> bool: ...

    def Finalize(self) -> None: ...

    def GetHashCode(self) -> int: ...

    def GetObjectData(self,
            _: System.Runtime.Serialization.SerializationInfo,
            __: System.Runtime.Serialization.StreamingContext,
            ) -> None: ...

    def GetRealObject(self,
            _: System.Runtime.Serialization.StreamingContext,
            ) -> object: ...

    def GetType(self) -> Type: ...

    def IsFromThisAppDomain(self) -> bool: ...

    def IsFromThisProcess(self) -> bool: ...

    def MemberwiseClone(self) -> object: ...

    def Overloads(self, *args, **kwargs) -> Any: ...

    def ReferenceEquals(self, _: object, __: object) -> bool: ...

    def ToString(self) -> str: ...

    @property
    def TypeInfo(self): ...

    @TypeInfo.setter
    def TypeInfo(self): ...

    @property
    def URI(self): ...

    @URI.setter
    def URI(self): ...

    def __init__(self, *args, **kwargs) -> Any: ...

    def get_ChannelInfo(self) -> IChannelInfo: ...

    def get_EnvoyInfo(self) -> IEnvoyInfo: ...

    def get_TypeInfo(self) -> IRemotingTypeInfo: ...

    def get_URI(self) -> str: ...

    def set_ChannelInfo(self, _: IChannelInfo) -> None: ...

    def set_EnvoyInfo(self, _: IEnvoyInfo) -> None: ...

    def set_TypeInfo(self, _: IRemotingTypeInfo) -> None: ...

    def set_URI(self, _: str) -> None: ...
