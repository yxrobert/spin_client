# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: slots_theme_status.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='slots_theme_status.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18slots_theme_status.proto\x12\x02pb\"\x1b\n\x0cNumberStatus\x12\x0b\n\x03Num\x18\x01 \x01(\x04\"7\n\x10UserChoiceStatus\x12\x10\n\x08\x43hoiceID\x18\x01 \x01(\r\x12\x11\n\tLeftTimes\x18\x02 \x01(\r\"\x19\n\nCellStatus\x12\x0b\n\x03IDS\x18\x01 \x03(\rB\x06Z\x04.;pbb\x06proto3'
)




_NUMBERSTATUS = _descriptor.Descriptor(
  name='NumberStatus',
  full_name='pb.NumberStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Num', full_name='pb.NumberStatus.Num', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=32,
  serialized_end=59,
)


_USERCHOICESTATUS = _descriptor.Descriptor(
  name='UserChoiceStatus',
  full_name='pb.UserChoiceStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ChoiceID', full_name='pb.UserChoiceStatus.ChoiceID', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LeftTimes', full_name='pb.UserChoiceStatus.LeftTimes', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=61,
  serialized_end=116,
)


_CELLSTATUS = _descriptor.Descriptor(
  name='CellStatus',
  full_name='pb.CellStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='IDS', full_name='pb.CellStatus.IDS', index=0,
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
  serialized_start=118,
  serialized_end=143,
)

DESCRIPTOR.message_types_by_name['NumberStatus'] = _NUMBERSTATUS
DESCRIPTOR.message_types_by_name['UserChoiceStatus'] = _USERCHOICESTATUS
DESCRIPTOR.message_types_by_name['CellStatus'] = _CELLSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NumberStatus = _reflection.GeneratedProtocolMessageType('NumberStatus', (_message.Message,), {
  'DESCRIPTOR' : _NUMBERSTATUS,
  '__module__' : 'slots_theme_status_pb2'
  # @@protoc_insertion_point(class_scope:pb.NumberStatus)
  })
_sym_db.RegisterMessage(NumberStatus)

UserChoiceStatus = _reflection.GeneratedProtocolMessageType('UserChoiceStatus', (_message.Message,), {
  'DESCRIPTOR' : _USERCHOICESTATUS,
  '__module__' : 'slots_theme_status_pb2'
  # @@protoc_insertion_point(class_scope:pb.UserChoiceStatus)
  })
_sym_db.RegisterMessage(UserChoiceStatus)

CellStatus = _reflection.GeneratedProtocolMessageType('CellStatus', (_message.Message,), {
  'DESCRIPTOR' : _CELLSTATUS,
  '__module__' : 'slots_theme_status_pb2'
  # @@protoc_insertion_point(class_scope:pb.CellStatus)
  })
_sym_db.RegisterMessage(CellStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
