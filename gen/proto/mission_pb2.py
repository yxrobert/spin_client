# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mission.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import award_pb2 as award__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mission.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmission.proto\x12\x02pb\x1a\x0b\x61ward.proto\"\xe0\t\n\x07HoneyDo\x1a\xff\x02\n\x03Req\x12\x35\n\x0cMissionCheck\x18\n \x01(\x0b\x32\x1d.pb.HoneyDo.Req.Mission.CheckH\x00\x12\x39\n\x0eMissionCollect\x18\x0b \x01(\x0b\x32\x1f.pb.HoneyDo.Req.Mission.CollectH\x00\x12\x39\n\x0eRetentionCheck\x18\x14 \x01(\x0b\x32\x1f.pb.HoneyDo.Req.Retention.CheckH\x00\x12=\n\x10RetentionCollect\x18\x15 \x01(\x0b\x32!.pb.HoneyDo.Req.Retention.CollectH\x00\x1aI\n\x07Mission\x1a\x15\n\x05\x43heck\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\t\x1a\'\n\x07\x43ollect\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\t\x12\x0e\n\x06TaskID\x18\x02 \x01(\r\x1a:\n\tRetention\x1a\x07\n\x05\x43heck\x1a$\n\x07\x43ollect\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\t\x12\x0b\n\x03Idx\x18\x02 \x01(\x05\x42\x05\n\x03one\x1a\x89\x05\n\x03Rsp\x12\x11\n\tLocalTime\x18\x01 \x01(\t\x12(\n\x06\x43ommon\x18\x90N \x01(\x0b\x32\x15.pb.HoneyDo.Rsp.ErrorH\x00\x12\x35\n\x0cMissionState\x18\n \x01(\x0b\x32\x1d.pb.HoneyDo.Rsp.Mission.StateH\x00\x12\x39\n\x0eMissionCollect\x18\x0b \x01(\x0b\x32\x1f.pb.HoneyDo.Rsp.Mission.CollectH\x00\x12\x39\n\x0eRetentionState\x18\x14 \x01(\x0b\x32\x1f.pb.HoneyDo.Rsp.Retention.StateH\x00\x12=\n\x10RetentionCollect\x18\x15 \x01(\x0b\x32!.pb.HoneyDo.Rsp.Retention.CollectH\x00\x1a\'\n\x05\x45rror\x12\x0e\n\x06\x43lient\x18\x01 \x01(\t\x12\x0e\n\x06Server\x18\x02 \x01(\t\x1a\xa3\x01\n\x07Mission\x1a\x63\n\x05State\x12\x0c\n\x04\x44\x61te\x18\x01 \x01(\t\x12\x1f\n\x05Tasks\x18\x02 \x03(\x0b\x32\x10.pb.HoneyDo.Task\x12\x0c\n\x04\x44one\x18\x03 \x01(\x08\x12\x1d\n\x06\x41wards\x18\x04 \x03(\x0b\x32\r.pb.AwardInfo\x1a\x33\n\x07\x43ollect\x12\n\n\x02OK\x18\x01 \x01(\x08\x12\x0c\n\x04\x44\x61te\x18\x02 \x01(\t\x12\x0e\n\x06TaskID\x18\x03 \x01(\r\x1a\x82\x01\n\tRetention\x1a<\n\x05State\x12\x33\n\x0fRetentionAwards\x18\x02 \x03(\x0b\x32\x1a.pb.HoneyDo.RetentionAward\x1a\x37\n\x07\x43ollect\x12\x13\n\x0bMissionDate\x18\x01 \x01(\t\x12\x0b\n\x03Idx\x18\x02 \x01(\x05\x12\n\n\x02OK\x18\x03 \x01(\x08\x42\x05\n\x03one\x1al\n\x04Task\x12\x0e\n\x06TaskID\x18\x01 \x01(\x05\x12\x0c\n\x04\x46ull\x18\x02 \x01(\x05\x12\r\n\x05\x43ount\x18\x03 \x01(\x05\x12\x11\n\tDiversity\x18\x04 \x01(\t\x12\x0f\n\x07\x41warded\x18\x05 \x01(\x08\x12\x13\n\x0bRewardCoins\x18\x06 \x01(\x04\x1aY\n\x0eRetentionAward\x12\x13\n\x0bMissionDate\x18\x01 \x01(\t\x12\x0e\n\x06\x44\x61yIdx\x18\x02 \x01(\x05\x12\x11\n\tValidFrom\x18\x03 \x01(\t\x12\x0f\n\x07ValidTo\x18\x04 \x01(\tB\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[award__pb2.DESCRIPTOR,])




_HONEYDO_REQ_MISSION_CHECK = _descriptor.Descriptor(
  name='Check',
  full_name='pb.HoneyDo.Req.Mission.Check',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Date', full_name='pb.HoneyDo.Req.Mission.Check.Date', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=301,
  serialized_end=322,
)

_HONEYDO_REQ_MISSION_COLLECT = _descriptor.Descriptor(
  name='Collect',
  full_name='pb.HoneyDo.Req.Mission.Collect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Date', full_name='pb.HoneyDo.Req.Mission.Collect.Date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TaskID', full_name='pb.HoneyDo.Req.Mission.Collect.TaskID', index=1,
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
  serialized_start=324,
  serialized_end=363,
)

_HONEYDO_REQ_MISSION = _descriptor.Descriptor(
  name='Mission',
  full_name='pb.HoneyDo.Req.Mission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_HONEYDO_REQ_MISSION_CHECK, _HONEYDO_REQ_MISSION_COLLECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=290,
  serialized_end=363,
)

_HONEYDO_REQ_RETENTION_CHECK = _descriptor.Descriptor(
  name='Check',
  full_name='pb.HoneyDo.Req.Retention.Check',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=301,
  serialized_end=308,
)

_HONEYDO_REQ_RETENTION_COLLECT = _descriptor.Descriptor(
  name='Collect',
  full_name='pb.HoneyDo.Req.Retention.Collect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Date', full_name='pb.HoneyDo.Req.Retention.Collect.Date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Idx', full_name='pb.HoneyDo.Req.Retention.Collect.Idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=387,
  serialized_end=423,
)

_HONEYDO_REQ_RETENTION = _descriptor.Descriptor(
  name='Retention',
  full_name='pb.HoneyDo.Req.Retention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_HONEYDO_REQ_RETENTION_CHECK, _HONEYDO_REQ_RETENTION_COLLECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=423,
)

_HONEYDO_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='pb.HoneyDo.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MissionCheck', full_name='pb.HoneyDo.Req.MissionCheck', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MissionCollect', full_name='pb.HoneyDo.Req.MissionCollect', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RetentionCheck', full_name='pb.HoneyDo.Req.RetentionCheck', index=2,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RetentionCollect', full_name='pb.HoneyDo.Req.RetentionCollect', index=3,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HONEYDO_REQ_MISSION, _HONEYDO_REQ_RETENTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.HoneyDo.Req.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=47,
  serialized_end=430,
)

_HONEYDO_RSP_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='pb.HoneyDo.Rsp.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Client', full_name='pb.HoneyDo.Rsp.Error.Client', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Server', full_name='pb.HoneyDo.Rsp.Error.Server', index=1,
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
  serialized_start=737,
  serialized_end=776,
)

_HONEYDO_RSP_MISSION_STATE = _descriptor.Descriptor(
  name='State',
  full_name='pb.HoneyDo.Rsp.Mission.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Date', full_name='pb.HoneyDo.Rsp.Mission.State.Date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Tasks', full_name='pb.HoneyDo.Rsp.Mission.State.Tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Done', full_name='pb.HoneyDo.Rsp.Mission.State.Done', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.HoneyDo.Rsp.Mission.State.Awards', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=790,
  serialized_end=889,
)

_HONEYDO_RSP_MISSION_COLLECT = _descriptor.Descriptor(
  name='Collect',
  full_name='pb.HoneyDo.Rsp.Mission.Collect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='OK', full_name='pb.HoneyDo.Rsp.Mission.Collect.OK', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Date', full_name='pb.HoneyDo.Rsp.Mission.Collect.Date', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TaskID', full_name='pb.HoneyDo.Rsp.Mission.Collect.TaskID', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=891,
  serialized_end=942,
)

_HONEYDO_RSP_MISSION = _descriptor.Descriptor(
  name='Mission',
  full_name='pb.HoneyDo.Rsp.Mission',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_HONEYDO_RSP_MISSION_STATE, _HONEYDO_RSP_MISSION_COLLECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=779,
  serialized_end=942,
)

_HONEYDO_RSP_RETENTION_STATE = _descriptor.Descriptor(
  name='State',
  full_name='pb.HoneyDo.Rsp.Retention.State',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='RetentionAwards', full_name='pb.HoneyDo.Rsp.Retention.State.RetentionAwards', index=0,
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
  serialized_start=958,
  serialized_end=1018,
)

_HONEYDO_RSP_RETENTION_COLLECT = _descriptor.Descriptor(
  name='Collect',
  full_name='pb.HoneyDo.Rsp.Retention.Collect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MissionDate', full_name='pb.HoneyDo.Rsp.Retention.Collect.MissionDate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Idx', full_name='pb.HoneyDo.Rsp.Retention.Collect.Idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OK', full_name='pb.HoneyDo.Rsp.Retention.Collect.OK', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=1020,
  serialized_end=1075,
)

_HONEYDO_RSP_RETENTION = _descriptor.Descriptor(
  name='Retention',
  full_name='pb.HoneyDo.Rsp.Retention',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_HONEYDO_RSP_RETENTION_STATE, _HONEYDO_RSP_RETENTION_COLLECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=945,
  serialized_end=1075,
)

_HONEYDO_RSP = _descriptor.Descriptor(
  name='Rsp',
  full_name='pb.HoneyDo.Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='LocalTime', full_name='pb.HoneyDo.Rsp.LocalTime', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Common', full_name='pb.HoneyDo.Rsp.Common', index=1,
      number=10000, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MissionState', full_name='pb.HoneyDo.Rsp.MissionState', index=2,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MissionCollect', full_name='pb.HoneyDo.Rsp.MissionCollect', index=3,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RetentionState', full_name='pb.HoneyDo.Rsp.RetentionState', index=4,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RetentionCollect', full_name='pb.HoneyDo.Rsp.RetentionCollect', index=5,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_HONEYDO_RSP_ERROR, _HONEYDO_RSP_MISSION, _HONEYDO_RSP_RETENTION, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.HoneyDo.Rsp.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=433,
  serialized_end=1082,
)

_HONEYDO_TASK = _descriptor.Descriptor(
  name='Task',
  full_name='pb.HoneyDo.Task',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='TaskID', full_name='pb.HoneyDo.Task.TaskID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Full', full_name='pb.HoneyDo.Task.Full', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Count', full_name='pb.HoneyDo.Task.Count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Diversity', full_name='pb.HoneyDo.Task.Diversity', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Awarded', full_name='pb.HoneyDo.Task.Awarded', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RewardCoins', full_name='pb.HoneyDo.Task.RewardCoins', index=5,
      number=6, type=4, cpp_type=4, label=1,
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
  serialized_start=1084,
  serialized_end=1192,
)

_HONEYDO_RETENTIONAWARD = _descriptor.Descriptor(
  name='RetentionAward',
  full_name='pb.HoneyDo.RetentionAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='MissionDate', full_name='pb.HoneyDo.RetentionAward.MissionDate', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DayIdx', full_name='pb.HoneyDo.RetentionAward.DayIdx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ValidFrom', full_name='pb.HoneyDo.RetentionAward.ValidFrom', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ValidTo', full_name='pb.HoneyDo.RetentionAward.ValidTo', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1194,
  serialized_end=1283,
)

_HONEYDO = _descriptor.Descriptor(
  name='HoneyDo',
  full_name='pb.HoneyDo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_HONEYDO_REQ, _HONEYDO_RSP, _HONEYDO_TASK, _HONEYDO_RETENTIONAWARD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=1283,
)

_HONEYDO_REQ_MISSION_CHECK.containing_type = _HONEYDO_REQ_MISSION
_HONEYDO_REQ_MISSION_COLLECT.containing_type = _HONEYDO_REQ_MISSION
_HONEYDO_REQ_MISSION.containing_type = _HONEYDO_REQ
_HONEYDO_REQ_RETENTION_CHECK.containing_type = _HONEYDO_REQ_RETENTION
_HONEYDO_REQ_RETENTION_COLLECT.containing_type = _HONEYDO_REQ_RETENTION
_HONEYDO_REQ_RETENTION.containing_type = _HONEYDO_REQ
_HONEYDO_REQ.fields_by_name['MissionCheck'].message_type = _HONEYDO_REQ_MISSION_CHECK
_HONEYDO_REQ.fields_by_name['MissionCollect'].message_type = _HONEYDO_REQ_MISSION_COLLECT
_HONEYDO_REQ.fields_by_name['RetentionCheck'].message_type = _HONEYDO_REQ_RETENTION_CHECK
_HONEYDO_REQ.fields_by_name['RetentionCollect'].message_type = _HONEYDO_REQ_RETENTION_COLLECT
_HONEYDO_REQ.containing_type = _HONEYDO
_HONEYDO_REQ.oneofs_by_name['one'].fields.append(
  _HONEYDO_REQ.fields_by_name['MissionCheck'])
_HONEYDO_REQ.fields_by_name['MissionCheck'].containing_oneof = _HONEYDO_REQ.oneofs_by_name['one']
_HONEYDO_REQ.oneofs_by_name['one'].fields.append(
  _HONEYDO_REQ.fields_by_name['MissionCollect'])
_HONEYDO_REQ.fields_by_name['MissionCollect'].containing_oneof = _HONEYDO_REQ.oneofs_by_name['one']
_HONEYDO_REQ.oneofs_by_name['one'].fields.append(
  _HONEYDO_REQ.fields_by_name['RetentionCheck'])
_HONEYDO_REQ.fields_by_name['RetentionCheck'].containing_oneof = _HONEYDO_REQ.oneofs_by_name['one']
_HONEYDO_REQ.oneofs_by_name['one'].fields.append(
  _HONEYDO_REQ.fields_by_name['RetentionCollect'])
_HONEYDO_REQ.fields_by_name['RetentionCollect'].containing_oneof = _HONEYDO_REQ.oneofs_by_name['one']
_HONEYDO_RSP_ERROR.containing_type = _HONEYDO_RSP
_HONEYDO_RSP_MISSION_STATE.fields_by_name['Tasks'].message_type = _HONEYDO_TASK
_HONEYDO_RSP_MISSION_STATE.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
_HONEYDO_RSP_MISSION_STATE.containing_type = _HONEYDO_RSP_MISSION
_HONEYDO_RSP_MISSION_COLLECT.containing_type = _HONEYDO_RSP_MISSION
_HONEYDO_RSP_MISSION.containing_type = _HONEYDO_RSP
_HONEYDO_RSP_RETENTION_STATE.fields_by_name['RetentionAwards'].message_type = _HONEYDO_RETENTIONAWARD
_HONEYDO_RSP_RETENTION_STATE.containing_type = _HONEYDO_RSP_RETENTION
_HONEYDO_RSP_RETENTION_COLLECT.containing_type = _HONEYDO_RSP_RETENTION
_HONEYDO_RSP_RETENTION.containing_type = _HONEYDO_RSP
_HONEYDO_RSP.fields_by_name['Common'].message_type = _HONEYDO_RSP_ERROR
_HONEYDO_RSP.fields_by_name['MissionState'].message_type = _HONEYDO_RSP_MISSION_STATE
_HONEYDO_RSP.fields_by_name['MissionCollect'].message_type = _HONEYDO_RSP_MISSION_COLLECT
_HONEYDO_RSP.fields_by_name['RetentionState'].message_type = _HONEYDO_RSP_RETENTION_STATE
_HONEYDO_RSP.fields_by_name['RetentionCollect'].message_type = _HONEYDO_RSP_RETENTION_COLLECT
_HONEYDO_RSP.containing_type = _HONEYDO
_HONEYDO_RSP.oneofs_by_name['one'].fields.append(
  _HONEYDO_RSP.fields_by_name['Common'])
_HONEYDO_RSP.fields_by_name['Common'].containing_oneof = _HONEYDO_RSP.oneofs_by_name['one']
_HONEYDO_RSP.oneofs_by_name['one'].fields.append(
  _HONEYDO_RSP.fields_by_name['MissionState'])
_HONEYDO_RSP.fields_by_name['MissionState'].containing_oneof = _HONEYDO_RSP.oneofs_by_name['one']
_HONEYDO_RSP.oneofs_by_name['one'].fields.append(
  _HONEYDO_RSP.fields_by_name['MissionCollect'])
_HONEYDO_RSP.fields_by_name['MissionCollect'].containing_oneof = _HONEYDO_RSP.oneofs_by_name['one']
_HONEYDO_RSP.oneofs_by_name['one'].fields.append(
  _HONEYDO_RSP.fields_by_name['RetentionState'])
_HONEYDO_RSP.fields_by_name['RetentionState'].containing_oneof = _HONEYDO_RSP.oneofs_by_name['one']
_HONEYDO_RSP.oneofs_by_name['one'].fields.append(
  _HONEYDO_RSP.fields_by_name['RetentionCollect'])
_HONEYDO_RSP.fields_by_name['RetentionCollect'].containing_oneof = _HONEYDO_RSP.oneofs_by_name['one']
_HONEYDO_TASK.containing_type = _HONEYDO
_HONEYDO_RETENTIONAWARD.containing_type = _HONEYDO
DESCRIPTOR.message_types_by_name['HoneyDo'] = _HONEYDO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HoneyDo = _reflection.GeneratedProtocolMessageType('HoneyDo', (_message.Message,), {

  'Req' : _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), {

    'Mission' : _reflection.GeneratedProtocolMessageType('Mission', (_message.Message,), {

      'Check' : _reflection.GeneratedProtocolMessageType('Check', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_REQ_MISSION_CHECK,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Req.Mission.Check)
        })
      ,

      'Collect' : _reflection.GeneratedProtocolMessageType('Collect', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_REQ_MISSION_COLLECT,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Req.Mission.Collect)
        })
      ,
      'DESCRIPTOR' : _HONEYDO_REQ_MISSION,
      '__module__' : 'mission_pb2'
      # @@protoc_insertion_point(class_scope:pb.HoneyDo.Req.Mission)
      })
    ,

    'Retention' : _reflection.GeneratedProtocolMessageType('Retention', (_message.Message,), {

      'Check' : _reflection.GeneratedProtocolMessageType('Check', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_REQ_RETENTION_CHECK,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Req.Retention.Check)
        })
      ,

      'Collect' : _reflection.GeneratedProtocolMessageType('Collect', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_REQ_RETENTION_COLLECT,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Req.Retention.Collect)
        })
      ,
      'DESCRIPTOR' : _HONEYDO_REQ_RETENTION,
      '__module__' : 'mission_pb2'
      # @@protoc_insertion_point(class_scope:pb.HoneyDo.Req.Retention)
      })
    ,
    'DESCRIPTOR' : _HONEYDO_REQ,
    '__module__' : 'mission_pb2'
    # @@protoc_insertion_point(class_scope:pb.HoneyDo.Req)
    })
  ,

  'Rsp' : _reflection.GeneratedProtocolMessageType('Rsp', (_message.Message,), {

    'Error' : _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
      'DESCRIPTOR' : _HONEYDO_RSP_ERROR,
      '__module__' : 'mission_pb2'
      # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp.Error)
      })
    ,

    'Mission' : _reflection.GeneratedProtocolMessageType('Mission', (_message.Message,), {

      'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_RSP_MISSION_STATE,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp.Mission.State)
        })
      ,

      'Collect' : _reflection.GeneratedProtocolMessageType('Collect', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_RSP_MISSION_COLLECT,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp.Mission.Collect)
        })
      ,
      'DESCRIPTOR' : _HONEYDO_RSP_MISSION,
      '__module__' : 'mission_pb2'
      # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp.Mission)
      })
    ,

    'Retention' : _reflection.GeneratedProtocolMessageType('Retention', (_message.Message,), {

      'State' : _reflection.GeneratedProtocolMessageType('State', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_RSP_RETENTION_STATE,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp.Retention.State)
        })
      ,

      'Collect' : _reflection.GeneratedProtocolMessageType('Collect', (_message.Message,), {
        'DESCRIPTOR' : _HONEYDO_RSP_RETENTION_COLLECT,
        '__module__' : 'mission_pb2'
        # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp.Retention.Collect)
        })
      ,
      'DESCRIPTOR' : _HONEYDO_RSP_RETENTION,
      '__module__' : 'mission_pb2'
      # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp.Retention)
      })
    ,
    'DESCRIPTOR' : _HONEYDO_RSP,
    '__module__' : 'mission_pb2'
    # @@protoc_insertion_point(class_scope:pb.HoneyDo.Rsp)
    })
  ,

  'Task' : _reflection.GeneratedProtocolMessageType('Task', (_message.Message,), {
    'DESCRIPTOR' : _HONEYDO_TASK,
    '__module__' : 'mission_pb2'
    # @@protoc_insertion_point(class_scope:pb.HoneyDo.Task)
    })
  ,

  'RetentionAward' : _reflection.GeneratedProtocolMessageType('RetentionAward', (_message.Message,), {
    'DESCRIPTOR' : _HONEYDO_RETENTIONAWARD,
    '__module__' : 'mission_pb2'
    # @@protoc_insertion_point(class_scope:pb.HoneyDo.RetentionAward)
    })
  ,
  'DESCRIPTOR' : _HONEYDO,
  '__module__' : 'mission_pb2'
  # @@protoc_insertion_point(class_scope:pb.HoneyDo)
  })
_sym_db.RegisterMessage(HoneyDo)
_sym_db.RegisterMessage(HoneyDo.Req)
_sym_db.RegisterMessage(HoneyDo.Req.Mission)
_sym_db.RegisterMessage(HoneyDo.Req.Mission.Check)
_sym_db.RegisterMessage(HoneyDo.Req.Mission.Collect)
_sym_db.RegisterMessage(HoneyDo.Req.Retention)
_sym_db.RegisterMessage(HoneyDo.Req.Retention.Check)
_sym_db.RegisterMessage(HoneyDo.Req.Retention.Collect)
_sym_db.RegisterMessage(HoneyDo.Rsp)
_sym_db.RegisterMessage(HoneyDo.Rsp.Error)
_sym_db.RegisterMessage(HoneyDo.Rsp.Mission)
_sym_db.RegisterMessage(HoneyDo.Rsp.Mission.State)
_sym_db.RegisterMessage(HoneyDo.Rsp.Mission.Collect)
_sym_db.RegisterMessage(HoneyDo.Rsp.Retention)
_sym_db.RegisterMessage(HoneyDo.Rsp.Retention.State)
_sym_db.RegisterMessage(HoneyDo.Rsp.Retention.Collect)
_sym_db.RegisterMessage(HoneyDo.Task)
_sym_db.RegisterMessage(HoneyDo.RetentionAward)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
