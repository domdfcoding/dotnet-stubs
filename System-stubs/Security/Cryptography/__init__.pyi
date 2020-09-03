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


class HashAlgorithmName:

    def Equals(self, _: object) -> bool: ...

    def Finalize(self) -> None: ...

    def GetHashCode(self) -> int: ...

    def GetType(self) -> Type: ...

    def MD5(self, *args, **kwargs) -> Any: ...

    def MemberwiseClone(self) -> object: ...

    @property
    def Name(self): ...

    @Name.setter
    def Name(self): ...

    def Overloads(self, *args, **kwargs) -> Any: ...

    def ReferenceEquals(self, _: object, __: object) -> bool: ...

    def SHA1(self, *args, **kwargs) -> Any: ...

    def SHA256(self, *args, **kwargs) -> Any: ...

    def SHA384(self, *args, **kwargs) -> Any: ...

    def SHA512(self, *args, **kwargs) -> Any: ...

    def ToString(self) -> str: ...

    def __init__(self, *args, **kwargs) -> Any: ...

    def get_MD5(self) -> System.Security.Cryptography.HashAlgorithmName: ...

    def get_Name(self) -> str: ...

    def get_SHA1(self) -> System.Security.Cryptography.HashAlgorithmName: ...

    def get_SHA256(self) -> System.Security.Cryptography.HashAlgorithmName: ...

    def get_SHA384(self) -> System.Security.Cryptography.HashAlgorithmName: ...

    def get_SHA512(self) -> System.Security.Cryptography.HashAlgorithmName: ...

    def op_Equality(self,
            _: System.Security.Cryptography.HashAlgorithmName,
            __: System.Security.Cryptography.HashAlgorithmName,
            ) -> bool: ...

    def op_Inequality(self,
            _: System.Security.Cryptography.HashAlgorithmName,
            __: System.Security.Cryptography.HashAlgorithmName,
            ) -> bool: ...
