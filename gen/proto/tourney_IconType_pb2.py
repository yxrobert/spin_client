# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tourney_IconType.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tourney_IconType.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16tourney_IconType.proto\x12\x02pb*)\n\x0fTourneyIconType\x12\n\n\x06\x41vatar\x10\x00\x12\n\n\x06Stream\x10\x01\x42\x06Z\x04.;pbb\x06proto3'
)

_TOURNEYICONTYPE = _descriptor.EnumDescriptor(
  name='TourneyIconType',
  full_name='pb.TourneyIconType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Avatar', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Stream', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=30,
  serialized_end=71,
)
_sym_db.RegisterEnumDescriptor(_TOURNEYICONTYPE)

TourneyIconType = enum_type_wrapper.EnumTypeWrapper(_TOURNEYICONTYPE)
Avatar = 0
Stream = 1


DESCRIPTOR.enum_types_by_name['TourneyIconType'] = _TOURNEYICONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
