# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: activityevent.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import award_pb2 as award__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='activityevent.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13\x61\x63tivityevent.proto\x12\x02pb\x1a\x0b\x61ward.proto\"i\n\rActivityEvent\x12\r\n\x05\x45ntry\x18\x01 \x01(\x05\x12\x10\n\x08progress\x18\x02 \x01(\x03\x12\x0e\n\x06target\x18\x03 \x01(\x03\x12\'\n\x06Status\x18\x04 \x01(\x0e\x32\x17.pb.ActivityEventStatus\"@\n\rProgressAward\x12\x10\n\x08Progress\x18\x01 \x01(\x05\x12\x1d\n\x06\x41wards\x18\x02 \x03(\x0b\x32\r.pb.AwardInfo*]\n\x13\x41\x63tivityEventStatus\x12\x0f\n\x0b\x41\x45S_NotOpen\x10\x00\x12\x11\n\rAES_InHanding\x10\x01\x12\x10\n\x0c\x41\x45S_InReward\x10\x02\x12\x10\n\x0c\x41\x45S_Finished\x10\x03\x42\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[award__pb2.DESCRIPTOR,])

_ACTIVITYEVENTSTATUS = _descriptor.EnumDescriptor(
  name='ActivityEventStatus',
  full_name='pb.ActivityEventStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='AES_NotOpen', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AES_InHanding', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AES_InReward', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AES_Finished', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=213,
  serialized_end=306,
)
_sym_db.RegisterEnumDescriptor(_ACTIVITYEVENTSTATUS)

ActivityEventStatus = enum_type_wrapper.EnumTypeWrapper(_ACTIVITYEVENTSTATUS)
AES_NotOpen = 0
AES_InHanding = 1
AES_InReward = 2
AES_Finished = 3



_ACTIVITYEVENT = _descriptor.Descriptor(
  name='ActivityEvent',
  full_name='pb.ActivityEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Entry', full_name='pb.ActivityEvent.Entry', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='progress', full_name='pb.ActivityEvent.progress', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target', full_name='pb.ActivityEvent.target', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Status', full_name='pb.ActivityEvent.Status', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  serialized_start=40,
  serialized_end=145,
)


_PROGRESSAWARD = _descriptor.Descriptor(
  name='ProgressAward',
  full_name='pb.ProgressAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Progress', full_name='pb.ProgressAward.Progress', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.ProgressAward.Awards', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=147,
  serialized_end=211,
)

_ACTIVITYEVENT.fields_by_name['Status'].enum_type = _ACTIVITYEVENTSTATUS
_PROGRESSAWARD.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
DESCRIPTOR.message_types_by_name['ActivityEvent'] = _ACTIVITYEVENT
DESCRIPTOR.message_types_by_name['ProgressAward'] = _PROGRESSAWARD
DESCRIPTOR.enum_types_by_name['ActivityEventStatus'] = _ACTIVITYEVENTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActivityEvent = _reflection.GeneratedProtocolMessageType('ActivityEvent', (_message.Message,), {
  'DESCRIPTOR' : _ACTIVITYEVENT,
  '__module__' : 'activityevent_pb2'
  # @@protoc_insertion_point(class_scope:pb.ActivityEvent)
  })
_sym_db.RegisterMessage(ActivityEvent)

ProgressAward = _reflection.GeneratedProtocolMessageType('ProgressAward', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSAWARD,
  '__module__' : 'activityevent_pb2'
  # @@protoc_insertion_point(class_scope:pb.ProgressAward)
  })
_sym_db.RegisterMessage(ProgressAward)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
