#!/usr/bin/env python3
#
#  __main__.py
#
#  Copyright © 2020 Dominic Davis-Foster <dominic@davis-foster.co.uk>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#  DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#  OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.
#

# 3rd party
import clr  # type: ignore
from domdf_python_tools.paths import PathPlus

# this package
from dotnet_stub_builder.makers import make_module, make_package

clr.AddReference("System")
clr.AddReference("System.Collections")
clr.AddReference("System.Configuration")
clr.AddReference("System.Data")
clr.AddReference("System.Globalization")
clr.AddReference("System.IO")
clr.AddReference("System.Reflection")
clr.AddReference("System.Runtime")
clr.AddReference("System.Runtime.InteropServices")
clr.AddReference("System.Runtime.Remoting")
clr.AddReference("System.Runtime.Serialization")
clr.AddReference("System.Security")
clr.AddReference("System.Threading")
clr.AddReference("System.Threading.Tasks")
clr.AddReference("System.Xml")
clr.AddReference("System.Xml.Serialization")

# 3rd party
import System  # type: ignore
import System.Collections  # type: ignore
import System.Configuration  # type: ignore
import System.Configuration.Assemblies  # type: ignore
import System.Data  # type: ignore
import System.Globalization  # type: ignore
import System.IO  # type: ignore
import System.Reflection  # type: ignore
import System.Runtime  # type: ignore
import System.Runtime.CompilerServices  # type: ignore
import System.Runtime.InteropServices  # type: ignore
import System.Runtime.Remoting  # type: ignore
import System.Runtime.Serialization  # type: ignore
import System.Security  # type: ignore
import System.Security.AccessControl  # type: ignore
import System.Security.Cryptography  # type: ignore
import System.Security.Cryptography.X509Certificates  # type: ignore
import System.Security.Policy  # type: ignore
import System.Threading  # type: ignore
import System.Threading.Tasks  # type: ignore
import System.Xml  # type: ignore
import System.Xml.Schema  # type: ignore
import System.Xml.Serialization  # type: ignore

__all__ = ["build_stubs"]


def build_stubs():
	# System
	system_stubs_dir = PathPlus("System-stubs")
	system_stubs_dir.maybe_make()

	make_package(
			"System",
			System,
			[
					"TypeCode",
					"Predicate",
					"TimeSpan",
					"ModuleHandle",
					"Delegate",
					"IAsyncResult",
					"MulticastDelegate",
					"EventHandler",
					"IFormatProvider",
					"AsyncCallback",
					"EventArgs",
					"DateTime",
					"Guid",
					"Converter",
					"RuntimeMethodHandle",
					"RuntimeTypeHandle",
					"DateTimeKind",
					"RuntimeFieldHandle",
					"Version",
					"ResolveEventArgs",
					"Action",
					"Object",
					"Func",
					"Attribute",
					"DayOfWeek",
					"DateTimeOffset",
					]
			)

	# System.Data
	make_module(
			"System.Data",
			System.Data,
			[
					"InternalDataCollectionBase",
					"AcceptRejectRule",
					"DataTable",
					"DataTableReader",
					"DataRowState",
					"DataRow",
					"DataSet",
					"DataColumn",
					"IDataReader",
					"LoadOption",
					"FillErrorEventHandler",
					"MissingSchemaAction",
					"DataRowBuilder",
					"DataRowChangeEventArgs",
					"DataTableNewRowEventArgs",
					"DataTableNewRowEventHandler",
					"XmlReadMode",
					"XmlWriteMode",
					"DataViewRowState",
					"DataColumnChangeEventHandler",
					"DataRowChangeEventHandler",
					"DataView",
					"DataColumnCollection",
					"DataRowCollection",
					"DataRelationCollection",
					"PropertyCollection",
					"SerializationFormat",
					"DataTableClearEventArgs",
					"DataTableClearEventHandler",
					"ConstraintCollection",
					"DataRowVersion",
					"DataRelation",
					"MappingType",
					"DataSetDateTime",
					"FillErrorEventArgs",
					"DataRowAction",
					"MergeFailedEventHandler",
					"DataViewManager",
					"DataTableCollection",
					"DataRowView",
					"MergeFailedEventArgs",
					"DataViewSettingCollection",
					"DataViewSetting",
					"Constraint",
					"ForeignKeyConstraint",
					"UniqueConstraint",
					"Rule",
					"SchemaSerializationMode",
					]
			)

	# System.Xml
	make_package(
			"System.Xml",
			System.Xml,
			[
					"XmlReader",
					"XmlWriter",
					"XmlReaderSettings",
					"XmlNodeType",
					"IXmlNamespaceResolver",
					"XmlNameTable",
					"XmlWriterSettings",
					"XmlResolver",
					"XmlQualifiedName",
					"XmlAttribute",
					"XmlTokenizedType",
					"XmlOutputMethod",
					"XmlNode",
					"XmlNodeList",
					"XmlNamespaceManager",
					"XmlAttributeCollection",
					"XmlElement",
					"XmlNamespaceScope",
					"XmlDocument",
					"XmlEntityReference",
					"XmlSignificantWhitespace",
					"XmlDocumentFragment",
					"XmlText",
					"XmlWhitespace",
					"XmlDeclaration",
					"ReadState",
					"XmlSpace",
					"NewLineHandling",
					"NamespaceHandling",
					"XmlCDataSection",
					"XmlComment",
					"XmlDocumentType",
					"XmlProcessingInstruction",
					"XmlNodeChangedEventHandler",
					"ValidationType",
					"ConformanceLevel",
					"DtdProcessing",
					"WriteState",
					"XmlNamedNodeMap",
					"XmlImplementation",
					"XmlNodeChangedEventArgs",
					"XmlNodeChangedAction",
					]
			)

	# System.Xml.Schema
	make_module(
			"System.Xml.Schema",
			System.Xml.Schema,
			[
					"XmlSchema",
					"XmlTypeCode",
					"XmlSchemaSimpleType",
					"XmlSchemaSet",
					"XmlSchemaForm",
					"XmlSchemaType",
					"XmlSchemaObject",
					"XmlSchemaContentModel",
					"XmlSchemaDatatype",
					"XmlSchemaObjectTable",
					"XmlSchemaAnyAttribute",
					"XmlSchemaComplexType",
					"XmlSchemaParticle",
					"XmlSchemaCompilationSettings",
					"XmlSchemaObjectCollection",
					"XmlSchemaDerivationMethod",
					"ValidationEventHandler",
					"XmlSchemaAnnotation",
					"ValidationEventArgs",
					"XmlSchemaSimpleTypeContent",
					"XmlSchemaContent",
					"XmlSchemaContentType",
					"XmlSchemaException",
					"XmlSeverityType",
					"XmlSchemaContentProcessing",
					"XmlSchemaDatatypeVariety",
					"IXmlSchemaInfo",
					"XmlSchemaValidationFlags",
					"XmlSchemaValidity",
					"XmlSchemaElement",
					"XmlSchemaAttribute",
					"XmlSchemaUse",
					]
			)

	# System.Xml.Serialization
	make_module(
			"System.Xml.Serialization",
			System.Xml.Serialization,
			["XmlSerializerNamespaces"],
			)

	# System.Runtime
	make_package("System.Runtime", System.Runtime, [])

	# System.Runtime.Serialization
	make_module(
			"System.Runtime.Serialization",
			System.Runtime.Serialization,
			[
					"StreamingContextStates",
					"SerializationEntry",
					"SerializationInfo",
					"StreamingContext",
					"SerializationInfoEnumerator",
					"SafeSerializationEventArgs",
					"ISafeSerializationData",
					]
			)

	# System.Runtime.CompilerServices
	make_module(
			"System.Runtime.CompilerServices",
			System.Runtime.CompilerServices, ["ConfiguredTaskAwaitable", "TaskAwaiter", "YieldAwaitable"]
			)

	# System.Runtime.Remoting
	make_module(
			"System.Runtime.Remoting",
			System.Runtime.Remoting, [
					"ObjRef",
					"IChannelInfo",
					"IEnvoyInfo",
					"IRemotingTypeInfo",
					]
			)

	# System.Runtime.InteropServices
	make_module(
			"System.Runtime.InteropServices",
			System.Runtime.InteropServices, [
					"StructLayoutAttribute",
					"LayoutKind",
					]
			)

	# System.Collections
	make_module(
			"System.Collections",
			System.Collections,
			[
					"IEnumerator",
					"IDictionary",
					"ArrayList",
					"IDictionaryEnumerator",
					"IEqualityComparer",
					"ICollection",
					"IHashCodeProvider",
					"IComparer",
					"Hashtable",
					"DictionaryEntry",
					"IList",
					]
			)

	# System.Globalization
	make_module(
			"System.Globalization",
			System.Globalization,
			[
					"CultureInfo",
					"DateTimeFormatInfo",
					"NumberFormatInfo",
					"DateTimeStyles",
					"DigitShapes",
					"TimeSpanStyles",
					]
			)

	# System.ComponentModel
	make_module(
			"System.ComponentModel",
			System.ComponentModel,
			[
					"ITypeDescriptorContext",
					"PropertyDescriptor",
					"AttributeCollection",
					"PropertyDescriptorCollection",
					"TypeConverter",
					"DesignerSerializationVisibility",
					"MarshalByValueComponent",
					"PropertyChangedEventArgs",
					"PropertyChangedEventHandler",
					"CollectionChangeEventArgs",
					"CollectionChangeEventHandler",
					"ListChangedEventArgs",
					"ListChangedEventHandler",
					"IContainer",
					"EventHandlerList",
					"ISite",
					"CollectionChangeAction",
					"IComponent",
					"ComponentCollection",
					"ListChangedType",
					]
			)

	# System.IO
	make_module("System.IO", System.IO, [
			"Stream",
			"TextReader",
			"SeekOrigin",
			"FileStream",
			"TextWriter",
			])

	# System.Threading
	make_package(
			"System.Threading",
			System.Threading,
			["CancellationToken", "WaitHandle", "CancellationTokenRegistration"],
			)

	# System.Threading.Tasks
	make_module(
			"System.Threading.Tasks",
			System.Threading.Tasks,
			[
					"Task",
					"TaskScheduler",
					"TaskFactory",
					"TaskCreationOptions",
					"TaskStatus",
					"UnobservedTaskExceptionEventArgs",
					"TaskContinuationOptions",
					],
			)

	# System.Reflection
	make_module(
			"System.Reflection",
			System.Reflection,
			[
					"MemberInfo",
					"MethodBase",
					"MethodInfo",
					"Module",
					"TypeInfo",
					"TypeFilter",
					"Assembly",
					"EventAttributes",
					"AssemblyContentType",
					"ExceptionHandlingClauseOptions",
					"PropertyAttributes",
					"PortableExecutableKinds",
					"ImageFileMachine",
					"CustomAttributeNamedArgument",
					"ConstructorInfo",
					"CustomAttributeTypedArgument",
					"ExceptionHandlingClause",
					"LocalVariableInfo",
					"MethodAttributes",
					"CallingConventions",
					"CustomAttributeData",
					"MethodBody",
					"ParameterInfo",
					"MethodImplAttributes",
					"BindingFlags",
					"Binder",
					"FieldAttributes",
					"ModuleResolveEventHandler",
					"MemberTypes",
					"MemberFilter",
					"TypeAttributes",
					"EventInfo",
					"InterfaceMapping",
					"ICustomAttributeProvider",
					"ParameterModifier",
					"PropertyInfo",
					"ParameterAttributes",
					"FieldInfo",
					"ManifestResourceInfo",
					"AssemblyName",
					"AssemblyNameFlags",
					"StrongNameKeyPair",
					]
			)

	# System.Security
	make_package(
			"System.Security",
			System.Security,
			["PermissionSet", "SecurityRuleSet", "IPermission", "SecurityElement"],
			)

	# System.Security.Policy
	make_module("System.Security.Policy", System.Security.Policy, ["Evidence"])

	# System.Security.Cryptography
	make_package("System.Security.Cryptography", System.Security.Cryptography, ["HashAlgorithmName"])

	# System.Security.AccessControl
	make_package(
			"System.Security.AccessControl",
			System.Security.AccessControl,
			["FileSecurity", "InheritanceFlags", "PropagationFlags", "AccessControlType", "AccessRule"],
			)

	# System.Security.Cryptography.X509Certificates
	make_package(
			"System.Security.Cryptography.X509Certificates",
			System.Security.Cryptography.X509Certificates,
			["X509Certificate", "X509ContentType", "X509KeyStorageFlags"],
			)

	# System.Configuration
	make_package("System.Configuration", System.Configuration, [])

	# System.Configuration.Assemblies
	make_module(
			"System.Configuration.Assemblies",
			System.Configuration.Assemblies,
			["AssemblyHashAlgorithm", "AssemblyVersionCompatibility"],
			)


if __name__ == '__main__':
	build_stubs()
