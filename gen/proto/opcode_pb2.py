# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: opcode.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='opcode.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0copcode.proto\x12\x02pb\"7\n\x08OpResult\x12\x1a\n\x06OpCode\x18\x01 \x01(\x0e\x32\n.pb.OpCode\x12\x0f\n\x07\x43ontent\x18\x02 \x01(\t*\xb3\x06\n\x06OpCode\x12\x0f\n\x0bOpResult_OK\x10\x00\x12\x10\n\x0cOpResult_Err\x10\x01\x12\x1e\n\x1aOpResult_Request_Param_Err\x10\x02\x12\x1a\n\x16OpResult_Data_Outdated\x10\x03\x12\x16\n\x12OpResult_InvalidID\x10\x04\x12\x19\n\x15OpResult_Repeated_Req\x10\x05\x12\x1b\n\x17OpResult_NotEnough_Coin\x10\x14\x12\x1b\n\x17OpResult_NotEnough_Dice\x10\x15\x12 \n\x1cOpResult_NotEnough_BingoBall\x10\x16\x12\x1a\n\x16OpResult_NotEnough_Gem\x10\x17\x12\x1c\n\x18OpResult_NotEnough_Candy\x10\x18\x12\x1b\n\x17OpResult_NotEnough_Time\x10\x19\x12\x1c\n\x18OpResult_NotEnough_Level\x10\x1a\x12\x1c\n\x18OpResult_NotEnough_Times\x10\x1b\x12\x1f\n\x1bOpResult_Activity_Not_Exist\x10\x64\x12\x1d\n\x19OpResult_Activity_Req_Err\x10\x65\x12\x1c\n\x17OpResult_Card_Not_Exist\x10\xc8\x01\x12!\n\x1cOpResult_ExchangeCard_Failed\x10\xc9\x01\x12 \n\x1bOpResult_LevelSprint_InGame\x10\xac\x02\x12#\n\x1eOpResult_LevelSprint_NotInGame\x10\xad\x02\x12#\n\x1eOpResult_LevelSprint_ErrStatus\x10\xae\x02\x12\x30\n+OpResult_LevelSprint_NotEnough_BuyBuffTimes\x10\xaf\x02\x12\x30\n+OpResult_LevelSprint_NotEnough_BuyTimeTimes\x10\xb0\x02\x12(\n#OpResult_LevelSprint_Have_DrawTimes\x10\xb1\x02\x12-\n(OpResult_LevelSprint_NotEnough_DrawTimes\x10\xb2\x02\x42\x06Z\x04.;pbb\x06proto3'
)

_OPCODE = _descriptor.EnumDescriptor(
  name='OpCode',
  full_name='pb.OpCode',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OpResult_OK', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Err', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Request_Param_Err', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Data_Outdated', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_InvalidID', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Repeated_Req', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Coin', index=6, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Dice', index=7, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_BingoBall', index=8, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Gem', index=9, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Candy', index=10, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Time', index=11, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Level', index=12, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Times', index=13, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Activity_Not_Exist', index=14, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Activity_Req_Err', index=15, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Card_Not_Exist', index=16, number=200,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_ExchangeCard_Failed', index=17, number=201,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_LevelSprint_InGame', index=18, number=300,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_LevelSprint_NotInGame', index=19, number=301,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_LevelSprint_ErrStatus', index=20, number=302,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_LevelSprint_NotEnough_BuyBuffTimes', index=21, number=303,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_LevelSprint_NotEnough_BuyTimeTimes', index=22, number=304,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_LevelSprint_Have_DrawTimes', index=23, number=305,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_LevelSprint_NotEnough_DrawTimes', index=24, number=306,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=78,
  serialized_end=897,
)
_sym_db.RegisterEnumDescriptor(_OPCODE)

OpCode = enum_type_wrapper.EnumTypeWrapper(_OPCODE)
OpResult_OK = 0
OpResult_Err = 1
OpResult_Request_Param_Err = 2
OpResult_Data_Outdated = 3
OpResult_InvalidID = 4
OpResult_Repeated_Req = 5
OpResult_NotEnough_Coin = 20
OpResult_NotEnough_Dice = 21
OpResult_NotEnough_BingoBall = 22
OpResult_NotEnough_Gem = 23
OpResult_NotEnough_Candy = 24
OpResult_NotEnough_Time = 25
OpResult_NotEnough_Level = 26
OpResult_NotEnough_Times = 27
OpResult_Activity_Not_Exist = 100
OpResult_Activity_Req_Err = 101
OpResult_Card_Not_Exist = 200
OpResult_ExchangeCard_Failed = 201
OpResult_LevelSprint_InGame = 300
OpResult_LevelSprint_NotInGame = 301
OpResult_LevelSprint_ErrStatus = 302
OpResult_LevelSprint_NotEnough_BuyBuffTimes = 303
OpResult_LevelSprint_NotEnough_BuyTimeTimes = 304
OpResult_LevelSprint_Have_DrawTimes = 305
OpResult_LevelSprint_NotEnough_DrawTimes = 306



_OPRESULT = _descriptor.Descriptor(
  name='OpResult',
  full_name='pb.OpResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='OpCode', full_name='pb.OpResult.OpCode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Content', full_name='pb.OpResult.Content', index=1,
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
  serialized_start=20,
  serialized_end=75,
)

_OPRESULT.fields_by_name['OpCode'].enum_type = _OPCODE
DESCRIPTOR.message_types_by_name['OpResult'] = _OPRESULT
DESCRIPTOR.enum_types_by_name['OpCode'] = _OPCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpResult = _reflection.GeneratedProtocolMessageType('OpResult', (_message.Message,), {
  'DESCRIPTOR' : _OPRESULT,
  '__module__' : 'opcode_pb2'
  # @@protoc_insertion_point(class_scope:pb.OpResult)
  })
_sym_db.RegisterMessage(OpResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
