# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: slots_stage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='slots_stage.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11slots_stage.proto\x12\x02pb\"\x8d\x01\n\x04Slot\"\x84\x01\n\x05Stage\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x08\n\x04\x42\x41SE\x10\x01\x12\x0c\n\x08\x46REESPIN\x10\x02\x12\t\n\x05\x42ONUS\x10\x03\x12\n\n\x06PICKER\x10\x04\x12\x0b\n\x07RE_SPIN\x10\x05\x12\x13\n\x0f\x43OllECTION_SPIN\x10\x06\x12\n\n\x06GAMING\x10\x07\x12\r\n\tMAX_STAGE\x10\x08\x42\x06Z\x04.;pbb\x06proto3'
)



_SLOT_STAGE = _descriptor.EnumDescriptor(
  name='Stage',
  full_name='pb.Slot.Stage',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BASE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FREESPIN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BONUS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PICKER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RE_SPIN', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COllECTION_SPIN', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAMING', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAX_STAGE', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=35,
  serialized_end=167,
)
_sym_db.RegisterEnumDescriptor(_SLOT_STAGE)


_SLOT = _descriptor.Descriptor(
  name='Slot',
  full_name='pb.Slot',
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
    _SLOT_STAGE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=167,
)

_SLOT_STAGE.containing_type = _SLOT
DESCRIPTOR.message_types_by_name['Slot'] = _SLOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Slot = _reflection.GeneratedProtocolMessageType('Slot', (_message.Message,), {
  'DESCRIPTOR' : _SLOT,
  '__module__' : 'slots_stage_pb2'
  # @@protoc_insertion_point(class_scope:pb.Slot)
  })
_sym_db.RegisterMessage(Slot)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
