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
  serialized_pb=b'\n\x0copcode.proto\x12\x02pb*\xe7\x01\n\x06OpCode\x12\x0f\n\x0bOpResult_OK\x10\x00\x12\x10\n\x0cOpResult_Err\x10\x01\x12\x1e\n\x1aOpResult_Request_Param_Err\x10\x02\x12\x1b\n\x17OpResult_NotEnough_Coin\x10\x14\x12\x1b\n\x17OpResult_NotEnough_Dice\x10\x15\x12 \n\x1cOpResult_NotEnough_BingoBall\x10\x16\x12\x1f\n\x1bOpResult_Activity_Not_Exist\x10\x64\x12\x1d\n\x19OpResult_Activity_Req_Err\x10\x65\x42\x06Z\x04.;pbb\x06proto3'
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
      name='OpResult_NotEnough_Coin', index=3, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_Dice', index=4, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_NotEnough_BingoBall', index=5, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Activity_Not_Exist', index=6, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OpResult_Activity_Req_Err', index=7, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=21,
  serialized_end=252,
)
_sym_db.RegisterEnumDescriptor(_OPCODE)

OpCode = enum_type_wrapper.EnumTypeWrapper(_OPCODE)
OpResult_OK = 0
OpResult_Err = 1
OpResult_Request_Param_Err = 2
OpResult_NotEnough_Coin = 20
OpResult_NotEnough_Dice = 21
OpResult_NotEnough_BingoBall = 22
OpResult_Activity_Not_Exist = 100
OpResult_Activity_Req_Err = 101


DESCRIPTOR.enum_types_by_name['OpCode'] = _OPCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
