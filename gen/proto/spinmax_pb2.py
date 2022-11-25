# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spinmax.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import shop_pb2 as shop__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='spinmax.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rspinmax.proto\x12\x02pb\x1a\nshop.proto\"\xda\x01\n\x07SpinMax\x1a\x80\x01\n\x04\x44\x61ta\x12 \n\x05State\x18\x01 \x01(\x0e\x32\x11.pb.SpinMax.State\x12\x0f\n\x07Symbols\x18\x02 \x03(\r\x12\x10\n\x08Multiple\x18\x03 \x01(\x01\x12%\n\tRoyalSeal\x18\x04 \x01(\x0b\x32\x12.pb.Shop.RoyalSeal\x12\x0c\n\x04\x63oin\x18\x05 \x01(\x04\"L\n\x05State\x12\x14\n\x10State_InitFinish\x10\x00\x12\x14\n\x10State_SpinFinish\x10\x01\x12\x17\n\x13State_CollectFinish\x10\x02\x42\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[shop__pb2.DESCRIPTOR,])



_SPINMAX_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='pb.SpinMax.State',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='State_InitFinish', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='State_SpinFinish', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='State_CollectFinish', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=176,
  serialized_end=252,
)
_sym_db.RegisterEnumDescriptor(_SPINMAX_STATE)


_SPINMAX_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='pb.SpinMax.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='State', full_name='pb.SpinMax.Data.State', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Symbols', full_name='pb.SpinMax.Data.Symbols', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Multiple', full_name='pb.SpinMax.Data.Multiple', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RoyalSeal', full_name='pb.SpinMax.Data.RoyalSeal', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coin', full_name='pb.SpinMax.Data.coin', index=4,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_start=46,
  serialized_end=174,
)

_SPINMAX = _descriptor.Descriptor(
  name='SpinMax',
  full_name='pb.SpinMax',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_SPINMAX_DATA, ],
  enum_types=[
    _SPINMAX_STATE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=252,
)

_SPINMAX_DATA.fields_by_name['State'].enum_type = _SPINMAX_STATE
_SPINMAX_DATA.fields_by_name['RoyalSeal'].message_type = shop__pb2._SHOP_ROYALSEAL
_SPINMAX_DATA.containing_type = _SPINMAX
_SPINMAX_STATE.containing_type = _SPINMAX
DESCRIPTOR.message_types_by_name['SpinMax'] = _SPINMAX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SpinMax = _reflection.GeneratedProtocolMessageType('SpinMax', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _SPINMAX_DATA,
    '__module__' : 'spinmax_pb2'
    # @@protoc_insertion_point(class_scope:pb.SpinMax.Data)
    })
  ,
  'DESCRIPTOR' : _SPINMAX,
  '__module__' : 'spinmax_pb2'
  # @@protoc_insertion_point(class_scope:pb.SpinMax)
  })
_sym_db.RegisterMessage(SpinMax)
_sym_db.RegisterMessage(SpinMax.Data)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
