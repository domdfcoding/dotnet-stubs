from __future__ import annotations

# stdlib
from enum import Enum
from typing import Any, List, Type

# 3rd party
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
import System.Security.Principal
import System.Threading
import System.Threading.Tasks
import System.Xml
import System.Xml.Schema
import System.Xml.Serialization

class ITypeDescriptorContext:

	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Container(self): ...

	@Container.setter
	def Container(self, value): ...

	def GetService(self, _: Type) -> object: ...

	@property
	def Instance(self): ...

	@Instance.setter
	def Instance(self, value): ...

	def OnComponentChanged(self) -> None: ...
	def OnComponentChanging(self) -> bool: ...

	@property
	def PropertyDescriptor(self): ...

	@PropertyDescriptor.setter
	def PropertyDescriptor(self, value): ...

	def get_Container(self) -> IContainer: ...
	def get_Instance(self) -> object: ...
	def get_PropertyDescriptor(self) -> PropertyDescriptor: ...

class PropertyDescriptor:

	def __init__(self, *args, **kwargs) -> Any: ...
	def AddValueChanged(self, _: object, __: Any) -> None: ...

	@property
	def AttributeArray(self): ...

	@AttributeArray.setter
	def AttributeArray(self, value): ...

	@property
	def Attributes(self): ...

	@Attributes.setter
	def Attributes(self, value): ...

	def CanResetValue(self, _: object) -> bool: ...

	@property
	def Category(self): ...

	@Category.setter
	def Category(self, value): ...

	@property
	def ComponentType(self): ...

	@ComponentType.setter
	def ComponentType(self, value): ...

	@property
	def Converter(self): ...

	@Converter.setter
	def Converter(self, value): ...

	def CreateAttributeCollection(self) -> AttributeCollection: ...
	def CreateInstance(self, _: Type) -> object: ...

	@property
	def Description(self): ...

	@Description.setter
	def Description(self, value): ...

	@property
	def DesignTimeOnly(self): ...

	@DesignTimeOnly.setter
	def DesignTimeOnly(self, value): ...

	@property
	def DisplayName(self): ...

	@DisplayName.setter
	def DisplayName(self, value): ...

	def Equals(self, _: object) -> bool: ...
	def FillAttributes(self, _: List) -> None: ...
	def Finalize(self) -> None: ...
	def FindMethod(
			self,
			_: Type,
			__: str,
			___: List[Type],
			____: Type,
			_____: bool,
			) -> System.Reflection.MethodInfo: ...

	def GetChildProperties(
			self,
			_: object,
			__: List[System.Attribute],
			) -> PropertyDescriptorCollection: ...

	def GetEditor(self, _: Type) -> object: ...
	def GetHashCode(self) -> int: ...
	def GetInvocationTarget(self, _: Type, __: object) -> object: ...
	def GetInvokee(self, _: Type, __: object) -> object: ...
	def GetSite(self, _: object) -> ISite: ...
	def GetType(self) -> Type: ...
	def GetTypeFromName(self, _: str) -> Type: ...

	def GetValue(self, _: object) -> object: ...
	def GetValueChangedHandler(self, _: object) -> Any: ...

	@property
	def IsBrowsable(self): ...

	@IsBrowsable.setter
	def IsBrowsable(self, value): ...

	@property
	def IsLocalizable(self): ...

	@IsLocalizable.setter
	def IsLocalizable(self, value): ...

	@property
	def IsReadOnly(self): ...

	@IsReadOnly.setter
	def IsReadOnly(self, value): ...

	def MemberwiseClone(self) -> object: ...

	@property
	def Name(self): ...

	@Name.setter
	def Name(self, value): ...

	@property
	def NameHashCode(self): ...

	@NameHashCode.setter
	def NameHashCode(self, value): ...

	def OnValueChanged(self, _: object, __: System.EventArgs) -> None: ...
	def Overloads(self, *args, **kwargs) -> Any: ...

	@property
	def PropertyType(self): ...

	@PropertyType.setter
	def PropertyType(self, value): ...

	def ReferenceEquals(self, _: object, __: object) -> bool: ...

	def RemoveValueChanged(self, _: object, __: Any) -> None: ...
	def ResetValue(self, _: object) -> None: ...

	@property
	def SerializationVisibility(self): ...

	@SerializationVisibility.setter
	def SerializationVisibility(self, value): ...

	def SetValue(self, _: object, __: object) -> None: ...
	def ShouldSerializeValue(self, _: object) -> bool: ...

	@property
	def SupportsChangeEvents(self): ...

	@SupportsChangeEvents.setter
	def SupportsChangeEvents(self, value): ...

	def ToString(self) -> str: ...
	def get_AttributeArray(self) -> List[System.Attribute]: ...
	def get_Attributes(self) -> AttributeCollection: ...
	def get_Category(self) -> str: ...
	def get_ComponentType(self) -> Type: ...
	def get_Converter(self) -> TypeConverter: ...
	def get_Description(self) -> str: ...
	def get_DesignTimeOnly(self) -> bool: ...
	def get_DisplayName(self) -> str: ...
	def get_IsBrowsable(self) -> bool: ...
	def get_IsLocalizable(self) -> bool: ...
	def get_IsReadOnly(self) -> bool: ...
	def get_Name(self) -> str: ...
	def get_NameHashCode(self) -> int: ...
	def get_PropertyType(self) -> Type: ...
	def get_SerializationVisibility(self) -> DesignerSerializationVisibility: ...
	def get_SupportsChangeEvents(self) -> bool: ...
	def set_AttributeArray(self, _: List[System.Attribute]) -> None: ...

class AttributeCollection:

	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Attributes(self): ...

	@Attributes.setter
	def Attributes(self, value): ...

	def Contains(self, _: System.Attribute) -> bool: ...
	def CopyTo(self, _: List, __: int) -> None: ...

	@property
	def Count(self): ...

	@Count.setter
	def Count(self, value): ...

	def Empty(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def FromExisting(
			self,
			_: AttributeCollection,
			__: List[System.Attribute],
			) -> AttributeCollection: ...

	def GetDefaultAttribute(self, _: Type) -> System.Attribute: ...
	def GetEnumerator(self) -> System.Collections.IEnumerator: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def Matches(self, _: System.Attribute) -> bool: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToString(self) -> str: ...
	def get_Attributes(self) -> List[System.Attribute]: ...
	def get_Count(self) -> int: ...
	def get_Item(self, _: int) -> System.Attribute: ...

class PropertyDescriptorCollection:

	def __init__(self, *args, **kwargs) -> Any: ...
	def Add(self, _: PropertyDescriptor) -> int: ...
	def Clear(self) -> None: ...

	def Contains(self, _: PropertyDescriptor) -> bool: ...
	def CopyTo(self, _: List, __: int) -> None: ...

	@property
	def Count(self): ...

	@Count.setter
	def Count(self, value): ...

	def Empty(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def Find(self, _: str, __: bool) -> PropertyDescriptor: ...
	def GetEnumerator(self) -> System.Collections.IEnumerator: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def IndexOf(self, _: PropertyDescriptor) -> int: ...
	def Insert(self, _: int, __: PropertyDescriptor) -> None: ...
	def InternalSort(self, _: List[str]) -> None: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Remove(self, _: PropertyDescriptor) -> None: ...
	def RemoveAt(self, _: int) -> None: ...
	def Sort(
			self,
			_: List[str],
			__: System.Collections.IComparer,
			) -> PropertyDescriptorCollection: ...

	def ToString(self) -> str: ...
	def get_Count(self) -> int: ...
	def get_Item(self, _: str) -> PropertyDescriptor: ...

class TypeConverter:

	def __init__(self, *args, **kwargs) -> Any: ...
	def CanConvertFrom(
			self,
			_: ITypeDescriptorContext,
			__: Type,
			) -> bool: ...

	def CanConvertTo(
			self,
			_: ITypeDescriptorContext,
			__: Type,
			) -> bool: ...

	def ConvertFrom(
			self,
			_: ITypeDescriptorContext,
			__: System.Globalization.CultureInfo,
			___: object,
			) -> object: ...

	def ConvertFromInvariantString(
			self,
			_: ITypeDescriptorContext,
			__: str,
			) -> object: ...

	def ConvertFromString(
			self,
			_: ITypeDescriptorContext,
			__: System.Globalization.CultureInfo,
			___: str,
			) -> object: ...

	def ConvertTo(
			self,
			_: ITypeDescriptorContext,
			__: System.Globalization.CultureInfo,
			___: object,
			____: Type,
			) -> object: ...

	def ConvertToInvariantString(
			self,
			_: ITypeDescriptorContext,
			__: object,
			) -> str: ...

	def ConvertToString(
			self,
			_: ITypeDescriptorContext,
			__: System.Globalization.CultureInfo,
			___: object,
			) -> str: ...

	def CreateInstance(
			self,
			_: ITypeDescriptorContext,
			__: System.Collections.IDictionary,
			) -> object: ...

	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetConvertFromException(self, _: object) -> Exception: ...
	def GetConvertToException(self, _: object, __: Type) -> Exception: ...
	def GetCreateInstanceSupported(
			self,
			_: ITypeDescriptorContext,
			) -> bool: ...

	def GetHashCode(self) -> int: ...
	def GetProperties(
			self,
			_: ITypeDescriptorContext,
			__: object,
			___: List[System.Attribute],
			) -> PropertyDescriptorCollection: ...

	def GetPropertiesSupported(
			self,
			_: ITypeDescriptorContext,
			) -> bool: ...

	def GetStandardValues(self, _: ITypeDescriptorContext) -> Any: ...
	def GetStandardValuesExclusive(
			self,
			_: ITypeDescriptorContext,
			) -> bool: ...

	def GetStandardValuesSupported(
			self,
			_: ITypeDescriptorContext,
			) -> bool: ...

	def GetType(self) -> Type: ...
	def IsValid(
			self,
			_: ITypeDescriptorContext,
			__: object,
			) -> bool: ...

	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def SimplePropertyDescriptor(self, *args, **kwargs) -> Any: ...
	def SortProperties(
			self,
			_: PropertyDescriptorCollection,
			__: List[str],
			) -> PropertyDescriptorCollection: ...

	def StandardValuesCollection(self, *args, **kwargs) -> Any: ...
	def ToString(self) -> str: ...

class DesignerSerializationVisibility:

	def __init__(self, *args, **kwargs) -> Any: ...
	def CompareTo(self, _: object) -> int: ...
	def Content(self, *args, **kwargs) -> Any: ...
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
	def Hidden(self, *args, **kwargs) -> Any: ...
	def IsDefined(self, _: Type, __: object) -> bool: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def Parse(self, _: Type, __: str, ___: bool) -> object: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToObject(self, _: Type, __: object) -> object: ...
	def ToString(self, _: str, __: Any) -> str: ...
	def TryParse(self, *args, **kwargs) -> Any: ...
	def Visible(self, *args, **kwargs) -> Any: ...

class MarshalByValueComponent:

	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Container(self): ...

	@Container.setter
	def Container(self, value): ...

	@property
	def DesignMode(self): ...

	@DesignMode.setter
	def DesignMode(self, value): ...

	def Dispose(self, _: bool) -> None: ...

	def Disposed(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...

	@property
	def Events(self): ...

	@Events.setter
	def Events(self, value): ...

	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetService(self, _: Type) -> object: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...

	@property
	def Site(self): ...

	@Site.setter
	def Site(self, value): ...

	def ToString(self) -> str: ...
	def add_Disposed(self, _: Any) -> None: ...
	def get_Container(self) -> IContainer: ...
	def get_DesignMode(self) -> bool: ...
	def get_Events(self) -> EventHandlerList: ...
	def get_Site(self) -> ISite: ...
	def remove_Disposed(self, _: Any) -> None: ...
	def set_Site(self, _: ISite) -> None: ...

class PropertyChangedEventArgs:

	def __init__(self, *args, **kwargs) -> Any: ...
	def Empty(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...

	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...

	@property
	def PropertyName(self): ...

	@PropertyName.setter
	def PropertyName(self, value): ...

	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToString(self) -> str: ...
	def get_PropertyName(self) -> str: ...

class PropertyChangedEventHandler:

	def __init__(self, *args, **kwargs) -> Any: ...
	def BeginInvoke(
			self,
			_: object,
			__: PropertyChangedEventArgs,
			___: Any,
			____: object,
			) -> Any: ...

	def Clone(self) -> object: ...
	def Combine(self, _: Any, __: Any) -> Any: ...
	def CombineImpl(self, _: Any) -> Any: ...
	def CreateDelegate(
			self,
			_: Type,
			__: object,
			___: str,
			____: bool,
			_____: bool,
			) -> Any: ...

	def DynamicInvoke(self, _: List[object]) -> object: ...
	def DynamicInvokeImpl(self, _: List[object]) -> object: ...
	def EndInvoke(self, _: Any) -> None: ...
	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetInvocationList(self) -> List[Any]: ...
	def GetMethodImpl(self) -> System.Reflection.MethodInfo: ...
	def GetObjectData(
			self,
			_: System.Runtime.Serialization.SerializationInfo,
			__: System.Runtime.Serialization.StreamingContext,
			) -> None: ...

	def GetType(self) -> Type: ...
	def Invoke(
			self,
			_: object,
			__: PropertyChangedEventArgs,
			) -> None: ...

	def MemberwiseClone(self) -> object: ...

	@property
	def Method(self): ...

	@Method.setter
	def Method(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Remove(self, _: Any, __: Any) -> Any: ...

	def RemoveAll(self, _: Any, __: Any) -> Any: ...
	def RemoveImpl(self, _: Any) -> Any: ...

	@property
	def Target(self): ...

	@Target.setter
	def Target(self, value): ...

	def ToString(self) -> str: ...
	def get_Method(self) -> System.Reflection.MethodInfo: ...
	def get_Target(self) -> object: ...
	def op_Equality(self, _: Any, __: Any) -> bool: ...
	def op_Inequality(self, _: Any, __: Any) -> bool: ...

class CollectionChangeEventArgs:

	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Action(self): ...

	@Action.setter
	def Action(self, value): ...

	@property
	def Element(self): ...

	@Element.setter
	def Element(self, value): ...

	def Empty(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToString(self) -> str: ...
	def get_Action(self) -> CollectionChangeAction: ...
	def get_Element(self) -> object: ...

class CollectionChangeEventHandler:

	def __init__(self, *args, **kwargs) -> Any: ...
	def BeginInvoke(
			self,
			_: object,
			__: CollectionChangeEventArgs,
			___: Any,
			____: object,
			) -> Any: ...

	def Clone(self) -> object: ...
	def Combine(self, _: Any, __: Any) -> Any: ...
	def CombineImpl(self, _: Any) -> Any: ...
	def CreateDelegate(
			self,
			_: Type,
			__: object,
			___: str,
			____: bool,
			_____: bool,
			) -> Any: ...

	def DynamicInvoke(self, _: List[object]) -> object: ...
	def DynamicInvokeImpl(self, _: List[object]) -> object: ...
	def EndInvoke(self, _: Any) -> None: ...
	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetInvocationList(self) -> List[Any]: ...
	def GetMethodImpl(self) -> System.Reflection.MethodInfo: ...
	def GetObjectData(
			self,
			_: System.Runtime.Serialization.SerializationInfo,
			__: System.Runtime.Serialization.StreamingContext,
			) -> None: ...

	def GetType(self) -> Type: ...
	def Invoke(
			self,
			_: object,
			__: CollectionChangeEventArgs,
			) -> None: ...

	def MemberwiseClone(self) -> object: ...

	@property
	def Method(self): ...

	@Method.setter
	def Method(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Remove(self, _: Any, __: Any) -> Any: ...

	def RemoveAll(self, _: Any, __: Any) -> Any: ...
	def RemoveImpl(self, _: Any) -> Any: ...

	@property
	def Target(self): ...

	@Target.setter
	def Target(self, value): ...

	def ToString(self) -> str: ...
	def get_Method(self) -> System.Reflection.MethodInfo: ...
	def get_Target(self) -> object: ...
	def op_Equality(self, _: Any, __: Any) -> bool: ...
	def op_Inequality(self, _: Any, __: Any) -> bool: ...

class ListChangedEventArgs:

	def __init__(self, *args, **kwargs) -> Any: ...
	def Empty(self, *args, **kwargs) -> Any: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...

	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...

	@property
	def ListChangedType(self): ...

	@ListChangedType.setter
	def ListChangedType(self, value): ...

	def MemberwiseClone(self) -> object: ...

	@property
	def NewIndex(self): ...

	@NewIndex.setter
	def NewIndex(self, value): ...

	@property
	def OldIndex(self): ...

	@OldIndex.setter
	def OldIndex(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...

	@property
	def PropertyDescriptor(self): ...

	@PropertyDescriptor.setter
	def PropertyDescriptor(self, value): ...

	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def ToString(self) -> str: ...
	def get_ListChangedType(self) -> ListChangedType: ...
	def get_NewIndex(self) -> int: ...
	def get_OldIndex(self) -> int: ...
	def get_PropertyDescriptor(self) -> PropertyDescriptor: ...

class ListChangedEventHandler:

	def __init__(self, *args, **kwargs) -> Any: ...
	def BeginInvoke(
			self,
			_: object,
			__: ListChangedEventArgs,
			___: Any,
			____: object,
			) -> Any: ...

	def Clone(self) -> object: ...
	def Combine(self, _: Any, __: Any) -> Any: ...
	def CombineImpl(self, _: Any) -> Any: ...
	def CreateDelegate(
			self,
			_: Type,
			__: object,
			___: str,
			____: bool,
			_____: bool,
			) -> Any: ...

	def DynamicInvoke(self, _: List[object]) -> object: ...
	def DynamicInvokeImpl(self, _: List[object]) -> object: ...
	def EndInvoke(self, _: Any) -> None: ...
	def Equals(self, _: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetInvocationList(self) -> List[Any]: ...
	def GetMethodImpl(self) -> System.Reflection.MethodInfo: ...
	def GetObjectData(
			self,
			_: System.Runtime.Serialization.SerializationInfo,
			__: System.Runtime.Serialization.StreamingContext,
			) -> None: ...

	def GetType(self) -> Type: ...

	def Invoke(self, _: object, __: ListChangedEventArgs) -> None: ...
	def MemberwiseClone(self) -> object: ...

	@property
	def Method(self): ...

	@Method.setter
	def Method(self, value): ...

	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Remove(self, _: Any, __: Any) -> Any: ...

	def RemoveAll(self, _: Any, __: Any) -> Any: ...
	def RemoveImpl(self, _: Any) -> Any: ...

	@property
	def Target(self): ...

	@Target.setter
	def Target(self, value): ...

	def ToString(self) -> str: ...
	def get_Method(self) -> System.Reflection.MethodInfo: ...
	def get_Target(self) -> object: ...
	def op_Equality(self, _: Any, __: Any) -> bool: ...
	def op_Inequality(self, _: Any, __: Any) -> bool: ...

class IContainer:

	def __init__(self, *args, **kwargs) -> Any: ...
	def Add(self, _: IComponent, __: str) -> None: ...

	@property
	def Components(self): ...

	@Components.setter
	def Components(self, value): ...

	def Dispose(self) -> None: ...
	def Remove(self, _: IComponent) -> None: ...
	def get_Components(self) -> ComponentCollection: ...

class EventHandlerList:

	def __init__(self, *args, **kwargs) -> Any: ...
	def AddHandler(self, _: object, __: Any) -> None: ...
	def AddHandlers(self, _: EventHandlerList) -> None: ...
	def Dispose(self) -> None: ...
	def Equals(self, _: object, __: object) -> bool: ...
	def Finalize(self) -> None: ...
	def GetHashCode(self) -> int: ...
	def GetType(self) -> Type: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def RemoveHandler(self, _: object, __: Any) -> None: ...
	def ToString(self) -> str: ...
	def get_Item(self, _: object) -> Any: ...
	def set_Item(self, _: object, __: Any) -> None: ...

class ISite:

	def __init__(self, *args, **kwargs) -> Any: ...

	@property
	def Component(self): ...

	@Component.setter
	def Component(self, value): ...

	@property
	def Container(self): ...

	@Container.setter
	def Container(self, value): ...

	@property
	def DesignMode(self): ...

	@DesignMode.setter
	def DesignMode(self, value): ...

	def GetService(self, _: Type) -> object: ...

	@property
	def Name(self): ...

	@Name.setter
	def Name(self, value): ...

	def get_Component(self) -> IComponent: ...
	def get_Container(self) -> IContainer: ...
	def get_DesignMode(self) -> bool: ...
	def get_Name(self) -> str: ...
	def set_Name(self, _: str) -> None: ...

class CollectionChangeAction:

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
	def Refresh(self, *args, **kwargs) -> Any: ...
	def Remove(self, *args, **kwargs) -> Any: ...
	def ToObject(self, _: Type, __: object) -> object: ...
	def ToString(self, _: str, __: Any) -> str: ...
	def TryParse(self, *args, **kwargs) -> Any: ...

class IComponent:

	def __init__(self, *args, **kwargs) -> Any: ...

	def Dispose(self) -> None: ...
	def Disposed(self, *args, **kwargs) -> Any: ...

	@property
	def Site(self): ...

	@Site.setter
	def Site(self, value): ...

	def add_Disposed(self, _: Any) -> None: ...
	def get_Site(self) -> ISite: ...
	def remove_Disposed(self, _: Any) -> None: ...
	def set_Site(self, _: ISite) -> None: ...

class ComponentCollection:

	def __init__(self, *args, **kwargs) -> Any: ...
	def CopyTo(self, _: List[IComponent], __: int) -> None: ...

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
	def get_Item(self, _: str) -> IComponent: ...

class ListChangedType:

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
	def ItemAdded(self, *args, **kwargs) -> Any: ...
	def ItemChanged(self, *args, **kwargs) -> Any: ...
	def ItemDeleted(self, *args, **kwargs) -> Any: ...
	def ItemMoved(self, *args, **kwargs) -> Any: ...
	def MemberwiseClone(self) -> object: ...
	def Overloads(self, *args, **kwargs) -> Any: ...
	def Parse(self, _: Type, __: str, ___: bool) -> object: ...
	def PropertyDescriptorAdded(self, *args, **kwargs) -> Any: ...
	def PropertyDescriptorChanged(self, *args, **kwargs) -> Any: ...
	def PropertyDescriptorDeleted(self, *args, **kwargs) -> Any: ...
	def ReferenceEquals(self, _: object, __: object) -> bool: ...
	def Reset(self, *args, **kwargs) -> Any: ...
	def ToObject(self, _: Type, __: object) -> object: ...
	def ToString(self, _: str, __: Any) -> str: ...
	def TryParse(self, *args, **kwargs) -> Any: ...
