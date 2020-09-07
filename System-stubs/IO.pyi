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


class Stream:

    def __init__(self, *args, **kwargs) -> Any: ...

    def BeginRead(self,
            _: List[bytes],
            __: int,
            ___: int,
            ____: Any,
            _____: object,
            ) -> Any: ...

    def BeginWrite(self,
            _: List[bytes],
            __: int,
            ___: int,
            ____: Any,
            _____: object,
            ) -> Any: ...

    @property
    def CanRead(self): ...

    @CanRead.setter
    def CanRead(self, value): ...

    @property
    def CanSeek(self): ...

    @CanSeek.setter
    def CanSeek(self, value): ...

    @property
    def CanTimeout(self): ...

    @CanTimeout.setter
    def CanTimeout(self, value): ...

    @property
    def CanWrite(self): ...

    @CanWrite.setter
    def CanWrite(self, value): ...
    def Close(self) -> None: ...
    def CopyTo(self, _: Stream, __: int) -> None: ...

    def CopyToAsync(self,
            _: Stream,
            __: int,
            ___: System.Threading.CancellationToken,
            ) -> System.Threading.Tasks.Task: ...

    def CreateObjRef(self, _: Type) -> System.Runtime.Remoting.ObjRef: ...
    def CreateWaitHandle(self) -> System.Threading.WaitHandle: ...
    def Dispose(self, _: bool) -> None: ...
    def EndRead(self, _: Any) -> int: ...
    def EndWrite(self, _: Any) -> None: ...
    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def Flush(self) -> None: ...

    def FlushAsync(self,
            _: System.Threading.CancellationToken,
            ) -> System.Threading.Tasks.Task: ...

    def GetHashCode(self) -> int: ...
    def GetLifetimeService(self) -> object: ...
    def GetType(self) -> Type: ...
    def InitializeLifetimeService(self) -> object: ...

    @property
    def Length(self): ...

    @Length.setter
    def Length(self, value): ...
    def MemberwiseClone(self) -> object: ...
    def Null(self, *args, **kwargs) -> Any: ...
    def ObjectInvariant(self) -> None: ...
    def Overloads(self, *args, **kwargs) -> Any: ...

    @property
    def Position(self): ...

    @Position.setter
    def Position(self, value): ...
    def Read(self, _: List[bytes], __: int, ___: int) -> int: ...

    def ReadAsync(self,
            _: List[bytes],
            __: int,
            ___: int,
            ____: System.Threading.CancellationToken,
            ) -> System.Threading.Tasks.Task: ...

    def ReadByte(self) -> int: ...

    @property
    def ReadTimeout(self): ...

    @ReadTimeout.setter
    def ReadTimeout(self, value): ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def Seek(self, _: int, __: SeekOrigin) -> int: ...
    def SetLength(self, _: int) -> None: ...
    def Synchronized(self, _: Stream) -> Stream: ...
    def ToString(self) -> str: ...
    def Write(self, _: List[bytes], __: int, ___: int) -> None: ...

    def WriteAsync(self,
            _: List[bytes],
            __: int,
            ___: int,
            ____: System.Threading.CancellationToken,
            ) -> System.Threading.Tasks.Task: ...

    def WriteByte(self, _: bytes) -> None: ...

    @property
    def WriteTimeout(self): ...

    @WriteTimeout.setter
    def WriteTimeout(self, value): ...
    def get_CanRead(self) -> bool: ...
    def get_CanSeek(self) -> bool: ...
    def get_CanTimeout(self) -> bool: ...
    def get_CanWrite(self) -> bool: ...
    def get_Length(self) -> int: ...
    def get_Position(self) -> int: ...
    def get_ReadTimeout(self) -> int: ...
    def get_WriteTimeout(self) -> int: ...
    def set_Position(self, _: int) -> None: ...
    def set_ReadTimeout(self, _: int) -> None: ...
    def set_WriteTimeout(self, _: int) -> None: ...


class TextReader:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Close(self) -> None: ...
    def CreateObjRef(self, _: Type) -> System.Runtime.Remoting.ObjRef: ...
    def Dispose(self, _: bool) -> None: ...
    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def GetHashCode(self) -> int: ...
    def GetLifetimeService(self) -> object: ...
    def GetType(self) -> Type: ...
    def InitializeLifetimeService(self) -> object: ...
    def MemberwiseClone(self) -> object: ...
    def Null(self, *args, **kwargs) -> Any: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def Peek(self) -> int: ...
    def Read(self, _: List[str], __: int, ___: int) -> int: ...
    def ReadAsync(self, _: List[str], __: int, ___: int) -> System.Threading.Tasks.Task: ...
    def ReadBlock(self, _: List[str], __: int, ___: int) -> int: ...

    def ReadBlockAsync(self,
            _: List[str],
            __: int,
            ___: int,
            ) -> System.Threading.Tasks.Task: ...

    def ReadLine(self) -> str: ...
    def ReadLineAsync(self) -> System.Threading.Tasks.Task[str]: ...
    def ReadToEnd(self) -> str: ...
    def ReadToEndAsync(self) -> System.Threading.Tasks.Task[str]: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def Synchronized(self, _: TextReader) -> TextReader: ...
    def ToString(self) -> str: ...


class SeekOrigin:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Begin(self, *args, **kwargs) -> Any: ...
    def CompareTo(self, _: object) -> int: ...
    def Current(self, *args, **kwargs) -> Any: ...
    def End(self, *args, **kwargs) -> Any: ...
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


class FileStream:

    def __init__(self, *args, **kwargs) -> Any: ...

    def BeginRead(self,
            _: List[bytes],
            __: int,
            ___: int,
            ____: Any,
            _____: object,
            ) -> Any: ...

    def BeginWrite(self,
            _: List[bytes],
            __: int,
            ___: int,
            ____: Any,
            _____: object,
            ) -> Any: ...

    @property
    def CanRead(self): ...

    @CanRead.setter
    def CanRead(self, value): ...

    @property
    def CanSeek(self): ...

    @CanSeek.setter
    def CanSeek(self, value): ...

    @property
    def CanTimeout(self): ...

    @CanTimeout.setter
    def CanTimeout(self, value): ...

    @property
    def CanWrite(self): ...

    @CanWrite.setter
    def CanWrite(self, value): ...
    def Close(self) -> None: ...
    def CopyTo(self, _: Stream, __: int) -> None: ...

    def CopyToAsync(self,
            _: Stream,
            __: int,
            ___: System.Threading.CancellationToken,
            ) -> System.Threading.Tasks.Task: ...

    def CreateObjRef(self, _: Type) -> System.Runtime.Remoting.ObjRef: ...
    def CreateWaitHandle(self) -> System.Threading.WaitHandle: ...
    def Dispose(self) -> None: ...
    def EndRead(self, _: Any) -> int: ...
    def EndWrite(self, _: Any) -> None: ...
    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def Flush(self, _: bool) -> None: ...
    def FlushAsync(self) -> System.Threading.Tasks.Task: ...
    def GetAccessControl(self) -> System.Security.AccessControl.FileSecurity: ...
    def GetHashCode(self) -> int: ...
    def GetLifetimeService(self) -> object: ...
    def GetType(self) -> Type: ...

    @property
    def Handle(self): ...

    @Handle.setter
    def Handle(self, value): ...
    def InitializeLifetimeService(self) -> object: ...

    @property
    def IsAsync(self): ...

    @IsAsync.setter
    def IsAsync(self, value): ...

    @property
    def Length(self): ...

    @Length.setter
    def Length(self, value): ...
    def Lock(self, _: int, __: int) -> None: ...
    def MemberwiseClone(self) -> object: ...

    @property
    def Name(self): ...

    @Name.setter
    def Name(self, value): ...
    def Null(self, *args, **kwargs) -> Any: ...
    def ObjectInvariant(self) -> None: ...
    def Overloads(self, *args, **kwargs) -> Any: ...

    @property
    def Position(self): ...

    @Position.setter
    def Position(self, value): ...
    def Read(self, _: List[bytes], __: int, ___: int) -> int: ...

    def ReadAsync(self,
            _: List[bytes],
            __: int,
            ___: int,
            ) -> System.Threading.Tasks.Task: ...

    def ReadByte(self) -> int: ...

    @property
    def ReadTimeout(self): ...

    @ReadTimeout.setter
    def ReadTimeout(self, value): ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...

    @property
    def SafeFileHandle(self): ...

    @SafeFileHandle.setter
    def SafeFileHandle(self, value): ...
    def Seek(self, _: int, __: SeekOrigin) -> int: ...
    def SetAccessControl(self, _: System.Security.AccessControl.FileSecurity) -> None: ...
    def SetLength(self, _: int) -> None: ...
    def Synchronized(self, _: Stream) -> Stream: ...
    def ToString(self) -> str: ...
    def Unlock(self, _: int, __: int) -> None: ...
    def Write(self, _: List[bytes], __: int, ___: int) -> None: ...

    def WriteAsync(self,
            _: List[bytes],
            __: int,
            ___: int,
            ) -> System.Threading.Tasks.Task: ...

    def WriteByte(self, _: bytes) -> None: ...

    @property
    def WriteTimeout(self): ...

    @WriteTimeout.setter
    def WriteTimeout(self, value): ...
    def get_CanRead(self) -> bool: ...
    def get_CanSeek(self) -> bool: ...
    def get_CanTimeout(self) -> bool: ...
    def get_CanWrite(self) -> bool: ...
    def get_Handle(self) -> Any: ...
    def get_IsAsync(self) -> bool: ...
    def get_Length(self) -> int: ...
    def get_Name(self) -> str: ...
    def get_Position(self) -> int: ...
    def get_ReadTimeout(self) -> int: ...
    def get_SafeFileHandle(self) -> Any: ...
    def get_WriteTimeout(self) -> int: ...
    def set_Position(self, _: int) -> None: ...
    def set_ReadTimeout(self, _: int) -> None: ...
    def set_WriteTimeout(self, _: int) -> None: ...


class TextWriter:

    def __init__(self, *args, **kwargs) -> Any: ...
    def Close(self) -> None: ...
    def CreateObjRef(self, _: Type) -> System.Runtime.Remoting.ObjRef: ...
    def Dispose(self, _: bool) -> None: ...

    @property
    def Encoding(self): ...

    @Encoding.setter
    def Encoding(self, value): ...
    def Equals(self, _: object, __: object) -> bool: ...
    def Finalize(self) -> None: ...
    def Flush(self) -> None: ...
    def FlushAsync(self) -> System.Threading.Tasks.Task: ...

    @property
    def FormatProvider(self): ...

    @FormatProvider.setter
    def FormatProvider(self, value): ...
    def GetHashCode(self) -> int: ...
    def GetLifetimeService(self) -> object: ...
    def GetType(self) -> Type: ...
    def InitializeLifetimeService(self) -> object: ...
    def MemberwiseClone(self) -> object: ...

    @property
    def NewLine(self): ...

    @NewLine.setter
    def NewLine(self, value): ...
    def Null(self, *args, **kwargs) -> Any: ...
    def Overloads(self, *args, **kwargs) -> Any: ...
    def ReferenceEquals(self, _: object, __: object) -> bool: ...
    def Synchronized(self, _: TextWriter) -> TextWriter: ...
    def ToString(self) -> str: ...
    def Write(self, _: str, __: object, ___: object, ____: object) -> None: ...
    def WriteAsync(self, _: str) -> System.Threading.Tasks.Task: ...
    def WriteLine(self, _: str, __: object, ___: object, ____: object) -> None: ...
    def WriteLineAsync(self, _: str) -> System.Threading.Tasks.Task: ...
    def get_Encoding(self) -> Any: ...
    def get_FormatProvider(self) -> Any: ...
    def get_NewLine(self) -> str: ...
    def set_NewLine(self, _: str) -> None: ...
