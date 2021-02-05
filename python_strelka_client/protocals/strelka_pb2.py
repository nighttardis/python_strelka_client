# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: strelka.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='strelka.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstrelka.proto\"I\n\x07Request\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x63lient\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x12\n\ngatekeeper\x18\x04 \x01(\x08\"|\n\nAttributes\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12+\n\x08metadata\x18\x02 \x03(\x0b\x32\x19.Attributes.MetadataEntry\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"[\n\x0fScanFileRequest\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x19\n\x07request\x18\x02 \x01(\x0b\x32\x08.Request\x12\x1f\n\nattributes\x18\x03 \x01(\x0b\x32\x0b.Attributes\")\n\x0cScanResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65vent\x18\x02 \x01(\t2=\n\x08\x46rontend\x12\x31\n\x08ScanFile\x12\x10.ScanFileRequest\x1a\r.ScanResponse\"\x00(\x01\x30\x01\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Request.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='client', full_name='Request.client', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='source', full_name='Request.source', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gatekeeper', full_name='Request.gatekeeper', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=90,
)


_ATTRIBUTES_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='Attributes.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Attributes.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Attributes.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=216,
)

_ATTRIBUTES = _descriptor.Descriptor(
  name='Attributes',
  full_name='Attributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='Attributes.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='Attributes.metadata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_ATTRIBUTES_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=216,
)


_SCANFILEREQUEST = _descriptor.Descriptor(
  name='ScanFileRequest',
  full_name='ScanFileRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ScanFileRequest.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request', full_name='ScanFileRequest.request', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ScanFileRequest.attributes', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=309,
)


_SCANRESPONSE = _descriptor.Descriptor(
  name='ScanResponse',
  full_name='ScanResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ScanResponse.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='event', full_name='ScanResponse.event', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=352,
)

_ATTRIBUTES_METADATAENTRY.containing_type = _ATTRIBUTES
_ATTRIBUTES.fields_by_name['metadata'].message_type = _ATTRIBUTES_METADATAENTRY
_SCANFILEREQUEST.fields_by_name['request'].message_type = _REQUEST
_SCANFILEREQUEST.fields_by_name['attributes'].message_type = _ATTRIBUTES
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Attributes'] = _ATTRIBUTES
DESCRIPTOR.message_types_by_name['ScanFileRequest'] = _SCANFILEREQUEST
DESCRIPTOR.message_types_by_name['ScanResponse'] = _SCANRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'strelka_pb2'
  # @@protoc_insertion_point(class_scope:Request)
  })
_sym_db.RegisterMessage(Request)

Attributes = _reflection.GeneratedProtocolMessageType('Attributes', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _ATTRIBUTES_METADATAENTRY,
    '__module__' : 'strelka_pb2'
    # @@protoc_insertion_point(class_scope:Attributes.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _ATTRIBUTES,
  '__module__' : 'strelka_pb2'
  # @@protoc_insertion_point(class_scope:Attributes)
  })
_sym_db.RegisterMessage(Attributes)
_sym_db.RegisterMessage(Attributes.MetadataEntry)

ScanFileRequest = _reflection.GeneratedProtocolMessageType('ScanFileRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCANFILEREQUEST,
  '__module__' : 'strelka_pb2'
  # @@protoc_insertion_point(class_scope:ScanFileRequest)
  })
_sym_db.RegisterMessage(ScanFileRequest)

ScanResponse = _reflection.GeneratedProtocolMessageType('ScanResponse', (_message.Message,), {
  'DESCRIPTOR' : _SCANRESPONSE,
  '__module__' : 'strelka_pb2'
  # @@protoc_insertion_point(class_scope:ScanResponse)
  })
_sym_db.RegisterMessage(ScanResponse)


_ATTRIBUTES_METADATAENTRY._options = None

_FRONTEND = _descriptor.ServiceDescriptor(
  name='Frontend',
  full_name='Frontend',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=354,
  serialized_end=415,
  methods=[
  _descriptor.MethodDescriptor(
    name='ScanFile',
    full_name='Frontend.ScanFile',
    index=0,
    containing_service=None,
    input_type=_SCANFILEREQUEST,
    output_type=_SCANRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_FRONTEND)

DESCRIPTOR.services_by_name['Frontend'] = _FRONTEND

# @@protoc_insertion_point(module_scope)