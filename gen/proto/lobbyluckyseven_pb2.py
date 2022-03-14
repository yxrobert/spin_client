# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lobbyluckyseven.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lobbyluckyseven.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15lobbyluckyseven.proto\x12\x02pb\"\xaa\x01\n\x0eLobbLuckySeven\x1a\x43\n\rLuckySevenReq\x12+\n\x05\x41ward\x18\x01 \x01(\x0b\x32\x1a.pb.LobbLuckySevenAwardReqH\x00\x42\x05\n\x03one\x1aS\n\rLuckySevenRsp\x12\x10\n\x08\x62\x61seCoin\x18\x01 \x01(\x04\x12\x10\n\x08multiple\x18\x02 \x01(\r\x12\x0e\n\x06point1\x18\x03 \x01(\r\x12\x0e\n\x06point2\x18\x04 \x01(\r\"\x18\n\x16LobbLuckySevenAwardReqB\x06Z\x04.;pbb\x06proto3'
)




_LOBBLUCKYSEVEN_LUCKYSEVENREQ = _descriptor.Descriptor(
  name='LuckySevenReq',
  full_name='pb.LobbLuckySeven.LuckySevenReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Award', full_name='pb.LobbLuckySeven.LuckySevenReq.Award', index=0,
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
      name='one', full_name='pb.LobbLuckySeven.LuckySevenReq.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=48,
  serialized_end=115,
)

_LOBBLUCKYSEVEN_LUCKYSEVENRSP = _descriptor.Descriptor(
  name='LuckySevenRsp',
  full_name='pb.LobbLuckySeven.LuckySevenRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='baseCoin', full_name='pb.LobbLuckySeven.LuckySevenRsp.baseCoin', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='multiple', full_name='pb.LobbLuckySeven.LuckySevenRsp.multiple', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point1', full_name='pb.LobbLuckySeven.LuckySevenRsp.point1', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='point2', full_name='pb.LobbLuckySeven.LuckySevenRsp.point2', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=117,
  serialized_end=200,
)

_LOBBLUCKYSEVEN = _descriptor.Descriptor(
  name='LobbLuckySeven',
  full_name='pb.LobbLuckySeven',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_LOBBLUCKYSEVEN_LUCKYSEVENREQ, _LOBBLUCKYSEVEN_LUCKYSEVENRSP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=200,
)


_LOBBLUCKYSEVENAWARDREQ = _descriptor.Descriptor(
  name='LobbLuckySevenAwardReq',
  full_name='pb.LobbLuckySevenAwardReq',
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
  serialized_start=202,
  serialized_end=226,
)

_LOBBLUCKYSEVEN_LUCKYSEVENREQ.fields_by_name['Award'].message_type = _LOBBLUCKYSEVENAWARDREQ
_LOBBLUCKYSEVEN_LUCKYSEVENREQ.containing_type = _LOBBLUCKYSEVEN
_LOBBLUCKYSEVEN_LUCKYSEVENREQ.oneofs_by_name['one'].fields.append(
  _LOBBLUCKYSEVEN_LUCKYSEVENREQ.fields_by_name['Award'])
_LOBBLUCKYSEVEN_LUCKYSEVENREQ.fields_by_name['Award'].containing_oneof = _LOBBLUCKYSEVEN_LUCKYSEVENREQ.oneofs_by_name['one']
_LOBBLUCKYSEVEN_LUCKYSEVENRSP.containing_type = _LOBBLUCKYSEVEN
DESCRIPTOR.message_types_by_name['LobbLuckySeven'] = _LOBBLUCKYSEVEN
DESCRIPTOR.message_types_by_name['LobbLuckySevenAwardReq'] = _LOBBLUCKYSEVENAWARDREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LobbLuckySeven = _reflection.GeneratedProtocolMessageType('LobbLuckySeven', (_message.Message,), {

  'LuckySevenReq' : _reflection.GeneratedProtocolMessageType('LuckySevenReq', (_message.Message,), {
    'DESCRIPTOR' : _LOBBLUCKYSEVEN_LUCKYSEVENREQ,
    '__module__' : 'lobbyluckyseven_pb2'
    # @@protoc_insertion_point(class_scope:pb.LobbLuckySeven.LuckySevenReq)
    })
  ,

  'LuckySevenRsp' : _reflection.GeneratedProtocolMessageType('LuckySevenRsp', (_message.Message,), {
    'DESCRIPTOR' : _LOBBLUCKYSEVEN_LUCKYSEVENRSP,
    '__module__' : 'lobbyluckyseven_pb2'
    # @@protoc_insertion_point(class_scope:pb.LobbLuckySeven.LuckySevenRsp)
    })
  ,
  'DESCRIPTOR' : _LOBBLUCKYSEVEN,
  '__module__' : 'lobbyluckyseven_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbLuckySeven)
  })
_sym_db.RegisterMessage(LobbLuckySeven)
_sym_db.RegisterMessage(LobbLuckySeven.LuckySevenReq)
_sym_db.RegisterMessage(LobbLuckySeven.LuckySevenRsp)

LobbLuckySevenAwardReq = _reflection.GeneratedProtocolMessageType('LobbLuckySevenAwardReq', (_message.Message,), {
  'DESCRIPTOR' : _LOBBLUCKYSEVENAWARDREQ,
  '__module__' : 'lobbyluckyseven_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbLuckySevenAwardReq)
  })
_sym_db.RegisterMessage(LobbLuckySevenAwardReq)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
