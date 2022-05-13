# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login_reward.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='login_reward.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12login_reward.proto\x12\x02pb\"F\n\x0eReqLoginReward\x12-\n\rCliVerUpAward\x18\x01 \x01(\x0b\x32\x14.pb.CliVerUpAwardReqH\x00\x42\x05\n\x03one\"F\n\x0eRspLoginReward\x12-\n\rCliVerUpAward\x18\x01 \x01(\x0b\x32\x14.pb.CliVerUpAwardRspH\x00\x42\x05\n\x03one\"\x12\n\x10\x43liVerUpAwardReq\"\x12\n\x10\x43liVerUpAwardRspB\x06Z\x04.;pbb\x06proto3'
)




_REQLOGINREWARD = _descriptor.Descriptor(
  name='ReqLoginReward',
  full_name='pb.ReqLoginReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='CliVerUpAward', full_name='pb.ReqLoginReward.CliVerUpAward', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.ReqLoginReward.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=26,
  serialized_end=96,
)


_RSPLOGINREWARD = _descriptor.Descriptor(
  name='RspLoginReward',
  full_name='pb.RspLoginReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='CliVerUpAward', full_name='pb.RspLoginReward.CliVerUpAward', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.RspLoginReward.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=98,
  serialized_end=168,
)


_CLIVERUPAWARDREQ = _descriptor.Descriptor(
  name='CliVerUpAwardReq',
  full_name='pb.CliVerUpAwardReq',
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
  serialized_start=170,
  serialized_end=188,
)


_CLIVERUPAWARDRSP = _descriptor.Descriptor(
  name='CliVerUpAwardRsp',
  full_name='pb.CliVerUpAwardRsp',
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
  serialized_start=190,
  serialized_end=208,
)

_REQLOGINREWARD.fields_by_name['CliVerUpAward'].message_type = _CLIVERUPAWARDREQ
_REQLOGINREWARD.oneofs_by_name['one'].fields.append(
  _REQLOGINREWARD.fields_by_name['CliVerUpAward'])
_REQLOGINREWARD.fields_by_name['CliVerUpAward'].containing_oneof = _REQLOGINREWARD.oneofs_by_name['one']
_RSPLOGINREWARD.fields_by_name['CliVerUpAward'].message_type = _CLIVERUPAWARDRSP
_RSPLOGINREWARD.oneofs_by_name['one'].fields.append(
  _RSPLOGINREWARD.fields_by_name['CliVerUpAward'])
_RSPLOGINREWARD.fields_by_name['CliVerUpAward'].containing_oneof = _RSPLOGINREWARD.oneofs_by_name['one']
DESCRIPTOR.message_types_by_name['ReqLoginReward'] = _REQLOGINREWARD
DESCRIPTOR.message_types_by_name['RspLoginReward'] = _RSPLOGINREWARD
DESCRIPTOR.message_types_by_name['CliVerUpAwardReq'] = _CLIVERUPAWARDREQ
DESCRIPTOR.message_types_by_name['CliVerUpAwardRsp'] = _CLIVERUPAWARDRSP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqLoginReward = _reflection.GeneratedProtocolMessageType('ReqLoginReward', (_message.Message,), {
  'DESCRIPTOR' : _REQLOGINREWARD,
  '__module__' : 'login_reward_pb2'
  # @@protoc_insertion_point(class_scope:pb.ReqLoginReward)
  })
_sym_db.RegisterMessage(ReqLoginReward)

RspLoginReward = _reflection.GeneratedProtocolMessageType('RspLoginReward', (_message.Message,), {
  'DESCRIPTOR' : _RSPLOGINREWARD,
  '__module__' : 'login_reward_pb2'
  # @@protoc_insertion_point(class_scope:pb.RspLoginReward)
  })
_sym_db.RegisterMessage(RspLoginReward)

CliVerUpAwardReq = _reflection.GeneratedProtocolMessageType('CliVerUpAwardReq', (_message.Message,), {
  'DESCRIPTOR' : _CLIVERUPAWARDREQ,
  '__module__' : 'login_reward_pb2'
  # @@protoc_insertion_point(class_scope:pb.CliVerUpAwardReq)
  })
_sym_db.RegisterMessage(CliVerUpAwardReq)

CliVerUpAwardRsp = _reflection.GeneratedProtocolMessageType('CliVerUpAwardRsp', (_message.Message,), {
  'DESCRIPTOR' : _CLIVERUPAWARDRSP,
  '__module__' : 'login_reward_pb2'
  # @@protoc_insertion_point(class_scope:pb.CliVerUpAwardRsp)
  })
_sym_db.RegisterMessage(CliVerUpAwardRsp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
