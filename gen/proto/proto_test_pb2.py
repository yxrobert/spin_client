# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto_test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto_test.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10proto_test.proto\x12\x02pb\"\x1f\n\rStructFixed32\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x07\" \n\x0eStructSFixed32\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x0f\"\x1e\n\x0cStructUint32\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\r\"\x1d\n\x0bStructInt32\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x05\"\x1e\n\x0cStructSint32\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x11\"\x1f\n\rStructFixed64\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x06\" \n\x0eStructSFixed64\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x10\"\x1e\n\x0cStructUint64\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x04\"\x1d\n\x0bStructInt64\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x03\"\x1e\n\x0cStructSint64\x12\x0e\n\x06\x41rrays\x18\x01 \x03(\x12\x42\x06Z\x04.;pbb\x06proto3'
)




_STRUCTFIXED32 = _descriptor.Descriptor(
  name='StructFixed32',
  full_name='pb.StructFixed32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructFixed32.Arrays', index=0,
      number=1, type=7, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=24,
  serialized_end=55,
)


_STRUCTSFIXED32 = _descriptor.Descriptor(
  name='StructSFixed32',
  full_name='pb.StructSFixed32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructSFixed32.Arrays', index=0,
      number=1, type=15, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=57,
  serialized_end=89,
)


_STRUCTUINT32 = _descriptor.Descriptor(
  name='StructUint32',
  full_name='pb.StructUint32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructUint32.Arrays', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=91,
  serialized_end=121,
)


_STRUCTINT32 = _descriptor.Descriptor(
  name='StructInt32',
  full_name='pb.StructInt32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructInt32.Arrays', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=123,
  serialized_end=152,
)


_STRUCTSINT32 = _descriptor.Descriptor(
  name='StructSint32',
  full_name='pb.StructSint32',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructSint32.Arrays', index=0,
      number=1, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=154,
  serialized_end=184,
)


_STRUCTFIXED64 = _descriptor.Descriptor(
  name='StructFixed64',
  full_name='pb.StructFixed64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructFixed64.Arrays', index=0,
      number=1, type=6, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=186,
  serialized_end=217,
)


_STRUCTSFIXED64 = _descriptor.Descriptor(
  name='StructSFixed64',
  full_name='pb.StructSFixed64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructSFixed64.Arrays', index=0,
      number=1, type=16, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=219,
  serialized_end=251,
)


_STRUCTUINT64 = _descriptor.Descriptor(
  name='StructUint64',
  full_name='pb.StructUint64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructUint64.Arrays', index=0,
      number=1, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=253,
  serialized_end=283,
)


_STRUCTINT64 = _descriptor.Descriptor(
  name='StructInt64',
  full_name='pb.StructInt64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructInt64.Arrays', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=285,
  serialized_end=314,
)


_STRUCTSINT64 = _descriptor.Descriptor(
  name='StructSint64',
  full_name='pb.StructSint64',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Arrays', full_name='pb.StructSint64.Arrays', index=0,
      number=1, type=18, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=316,
  serialized_end=346,
)

DESCRIPTOR.message_types_by_name['StructFixed32'] = _STRUCTFIXED32
DESCRIPTOR.message_types_by_name['StructSFixed32'] = _STRUCTSFIXED32
DESCRIPTOR.message_types_by_name['StructUint32'] = _STRUCTUINT32
DESCRIPTOR.message_types_by_name['StructInt32'] = _STRUCTINT32
DESCRIPTOR.message_types_by_name['StructSint32'] = _STRUCTSINT32
DESCRIPTOR.message_types_by_name['StructFixed64'] = _STRUCTFIXED64
DESCRIPTOR.message_types_by_name['StructSFixed64'] = _STRUCTSFIXED64
DESCRIPTOR.message_types_by_name['StructUint64'] = _STRUCTUINT64
DESCRIPTOR.message_types_by_name['StructInt64'] = _STRUCTINT64
DESCRIPTOR.message_types_by_name['StructSint64'] = _STRUCTSINT64
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StructFixed32 = _reflection.GeneratedProtocolMessageType('StructFixed32', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTFIXED32,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructFixed32)
  })
_sym_db.RegisterMessage(StructFixed32)

StructSFixed32 = _reflection.GeneratedProtocolMessageType('StructSFixed32', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTSFIXED32,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructSFixed32)
  })
_sym_db.RegisterMessage(StructSFixed32)

StructUint32 = _reflection.GeneratedProtocolMessageType('StructUint32', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTUINT32,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructUint32)
  })
_sym_db.RegisterMessage(StructUint32)

StructInt32 = _reflection.GeneratedProtocolMessageType('StructInt32', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTINT32,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructInt32)
  })
_sym_db.RegisterMessage(StructInt32)

StructSint32 = _reflection.GeneratedProtocolMessageType('StructSint32', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTSINT32,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructSint32)
  })
_sym_db.RegisterMessage(StructSint32)

StructFixed64 = _reflection.GeneratedProtocolMessageType('StructFixed64', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTFIXED64,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructFixed64)
  })
_sym_db.RegisterMessage(StructFixed64)

StructSFixed64 = _reflection.GeneratedProtocolMessageType('StructSFixed64', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTSFIXED64,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructSFixed64)
  })
_sym_db.RegisterMessage(StructSFixed64)

StructUint64 = _reflection.GeneratedProtocolMessageType('StructUint64', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTUINT64,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructUint64)
  })
_sym_db.RegisterMessage(StructUint64)

StructInt64 = _reflection.GeneratedProtocolMessageType('StructInt64', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTINT64,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructInt64)
  })
_sym_db.RegisterMessage(StructInt64)

StructSint64 = _reflection.GeneratedProtocolMessageType('StructSint64', (_message.Message,), {
  'DESCRIPTOR' : _STRUCTSINT64,
  '__module__' : 'proto_test_pb2'
  # @@protoc_insertion_point(class_scope:pb.StructSint64)
  })
_sym_db.RegisterMessage(StructSint64)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
