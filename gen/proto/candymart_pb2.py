# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: candymart.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import award_pb2 as award__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='candymart.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0f\x63\x61ndymart.proto\x12\x02pb\x1a\x0b\x61ward.proto\"\xec\n\n\tCandyMart\x12!\n\x05\x43\x61ndy\x18\x01 \x01(\x0b\x32\x12.pb.CandyMart.Data\x1a\xc4\x04\n\x04\x44\x61ta\x12\r\n\x05\x43\x61ndy\x18\x01 \x01(\x05\x12\x10\n\x08StageIdx\x18\x02 \x01(\x05\x12\x17\n\x0fMissionProgress\x18\x03 \x01(\x05\x12\x14\n\x0c\x44ropProgress\x18\x04 \x01(\x05\x12\x12\n\nJPProgress\x18\x05 \x03(\x05\x12%\n\x08\x43urStage\x18\x06 \x01(\x0b\x32\x13.pb.CandyMart.Stage\x12)\n\tLastCandy\x18\x07 \x01(\x0b\x32\x16.pb.CandyMart.PopCandy\x12.\n\x0eProgressReward\x18\x08 \x03(\x0b\x32\x16.pb.CandyMart.Progress\x12-\n\x0bStageReward\x18\t \x03(\x0b\x32\x18.pb.CandyMart.StageAward\x12\'\n\x08JPAwards\x18\n \x03(\x0b\x32\x15.pb.CandyMart.JPAward\x12\x0f\n\x07HasDrop\x18\x0b \x01(\x08\x12\x10\n\x08\x42\x65Guided\x18\x0c \x01(\x08\x12\x30\n\x0e\x43urStageReward\x18\r \x01(\x0b\x32\x18.pb.CandyMart.StageAward\x12-\n\rMorePickCandy\x18\x0e \x01(\x0b\x32\x16.pb.CandyMart.PopCandy\x12#\n\x07\x42ooster\x18\x0f \x03(\x0b\x32\x12.pb.CandyMart.Buff\x12\x12\n\nCandyLimit\x18\x10 \x01(\x05\x12\r\n\x05Loops\x18\x11 \x01(\x05\x12\x0f\n\x07\x42\x65\x45nter\x18\x12 \x01(\x08\x12!\n\nFinalAward\x18\x13 \x01(\x0b\x32\r.pb.AwardList\x1aL\n\x04\x42uff\x12$\n\x04Type\x18\x01 \x01(\x0e\x32\x16.pb.CandyMart.BuffType\x12\r\n\x05Value\x18\x02 \x01(\x05\x12\x0f\n\x07\x45ndTime\x18\x03 \x01(\x03\x1a\x80\x01\n\x05Stage\x12+\n\x0bGroundCandy\x18\x01 \x03(\x0b\x32\x16.pb.CandyMart.PopCandy\x12(\n\x08\x42oxCandy\x18\x02 \x03(\x0b\x32\x16.pb.CandyMart.PopCandy\x12 \n\x04\x42uff\x18\x03 \x03(\x0b\x32\x12.pb.CandyMart.Buff\x1a\xd8\x01\n\x08PopCandy\x12%\n\x04Type\x18\x01 \x01(\x0e\x32\x17.pb.CandyMart.CandyType\x12\x13\n\x0b\x41\x64\x64Progress\x18\x02 \x01(\x05\x12\x15\n\rAfterProgress\x18\x03 \x01(\x05\x12.\n\x0bJPPointType\x18\x04 \x01(\x0e\x32\x19.pb.CandyMart.JPPointType\x12\x12\n\nAddJPPoint\x18\x05 \x01(\x05\x12\x14\n\x0c\x41\x66terJPPoint\x18\x06 \x01(\x05\x12\r\n\x05HitJP\x18\x07 \x01(\x08\x12\x10\n\x08Position\x18\x08 \x01(\x05\x1a(\n\x07JPAward\x12\x1d\n\x06\x41wards\x18\x01 \x03(\x0b\x32\r.pb.AwardInfo\x1a+\n\nStageAward\x12\x1d\n\x06\x41wards\x18\x01 \x03(\x0b\x32\r.pb.AwardInfo\x1a\x38\n\x08Progress\x12\r\n\x05Value\x18\x01 \x01(\x05\x12\x1d\n\x06\x41wards\x18\x02 \x03(\x0b\x32\r.pb.AwardInfo\":\n\tCandyType\x12\t\n\x05\x45mpty\x10\x00\x12\x0b\n\x07Present\x10\x01\x12\x0b\n\x07JPPoint\x10\x02\x12\x08\n\x04Pass\x10\x03\"A\n\x0bJPPointType\x12\x07\n\x03One\x10\x00\x12\x07\n\x03Two\x10\x01\x12\t\n\x05Three\x10\x02\x12\x08\n\x04\x46our\x10\x03\x12\x0b\n\x07\x42oarder\x10\x04\"9\n\x08\x42uffType\x12\x08\n\x04\x43oin\x10\x00\x12\x08\n\x04Spin\x10\x01\x12\x0f\n\x0b\x42oosterCoin\x10\x02\x12\x08\n\x04Pick\x10\x03\x42\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[award__pb2.DESCRIPTOR,])



_CANDYMART_CANDYTYPE = _descriptor.EnumDescriptor(
  name='CandyType',
  full_name='pb.CandyMart.CandyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Empty', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Present', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPPoint', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Pass', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1241,
  serialized_end=1299,
)
_sym_db.RegisterEnumDescriptor(_CANDYMART_CANDYTYPE)

_CANDYMART_JPPOINTTYPE = _descriptor.EnumDescriptor(
  name='JPPointType',
  full_name='pb.CandyMart.JPPointType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='One', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Two', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Three', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Four', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Boarder', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1301,
  serialized_end=1366,
)
_sym_db.RegisterEnumDescriptor(_CANDYMART_JPPOINTTYPE)

_CANDYMART_BUFFTYPE = _descriptor.EnumDescriptor(
  name='BuffType',
  full_name='pb.CandyMart.BuffType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Coin', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Spin', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BoosterCoin', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Pick', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1368,
  serialized_end=1425,
)
_sym_db.RegisterEnumDescriptor(_CANDYMART_BUFFTYPE)


_CANDYMART_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='pb.CandyMart.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Candy', full_name='pb.CandyMart.Data.Candy', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StageIdx', full_name='pb.CandyMart.Data.StageIdx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MissionProgress', full_name='pb.CandyMart.Data.MissionProgress', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='DropProgress', full_name='pb.CandyMart.Data.DropProgress', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='JPProgress', full_name='pb.CandyMart.Data.JPProgress', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CurStage', full_name='pb.CandyMart.Data.CurStage', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LastCandy', full_name='pb.CandyMart.Data.LastCandy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ProgressReward', full_name='pb.CandyMart.Data.ProgressReward', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StageReward', full_name='pb.CandyMart.Data.StageReward', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='JPAwards', full_name='pb.CandyMart.Data.JPAwards', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='HasDrop', full_name='pb.CandyMart.Data.HasDrop', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BeGuided', full_name='pb.CandyMart.Data.BeGuided', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CurStageReward', full_name='pb.CandyMart.Data.CurStageReward', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MorePickCandy', full_name='pb.CandyMart.Data.MorePickCandy', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Booster', full_name='pb.CandyMart.Data.Booster', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CandyLimit', full_name='pb.CandyMart.Data.CandyLimit', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Loops', full_name='pb.CandyMart.Data.Loops', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BeEnter', full_name='pb.CandyMart.Data.BeEnter', index=17,
      number=18, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FinalAward', full_name='pb.CandyMart.Data.FinalAward', index=18,
      number=19, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=86,
  serialized_end=666,
)

_CANDYMART_BUFF = _descriptor.Descriptor(
  name='Buff',
  full_name='pb.CandyMart.Buff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.CandyMart.Buff.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.CandyMart.Buff.Value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EndTime', full_name='pb.CandyMart.Buff.EndTime', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=668,
  serialized_end=744,
)

_CANDYMART_STAGE = _descriptor.Descriptor(
  name='Stage',
  full_name='pb.CandyMart.Stage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='GroundCandy', full_name='pb.CandyMart.Stage.GroundCandy', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BoxCandy', full_name='pb.CandyMart.Stage.BoxCandy', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Buff', full_name='pb.CandyMart.Stage.Buff', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=747,
  serialized_end=875,
)

_CANDYMART_POPCANDY = _descriptor.Descriptor(
  name='PopCandy',
  full_name='pb.CandyMart.PopCandy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.CandyMart.PopCandy.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AddProgress', full_name='pb.CandyMart.PopCandy.AddProgress', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AfterProgress', full_name='pb.CandyMart.PopCandy.AfterProgress', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='JPPointType', full_name='pb.CandyMart.PopCandy.JPPointType', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AddJPPoint', full_name='pb.CandyMart.PopCandy.AddJPPoint', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AfterJPPoint', full_name='pb.CandyMart.PopCandy.AfterJPPoint', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='HitJP', full_name='pb.CandyMart.PopCandy.HitJP', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Position', full_name='pb.CandyMart.PopCandy.Position', index=7,
      number=8, type=5, cpp_type=1, label=1,
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
  serialized_start=878,
  serialized_end=1094,
)

_CANDYMART_JPAWARD = _descriptor.Descriptor(
  name='JPAward',
  full_name='pb.CandyMart.JPAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.CandyMart.JPAward.Awards', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1096,
  serialized_end=1136,
)

_CANDYMART_STAGEAWARD = _descriptor.Descriptor(
  name='StageAward',
  full_name='pb.CandyMart.StageAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.CandyMart.StageAward.Awards', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=1138,
  serialized_end=1181,
)

_CANDYMART_PROGRESS = _descriptor.Descriptor(
  name='Progress',
  full_name='pb.CandyMart.Progress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.CandyMart.Progress.Value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.CandyMart.Progress.Awards', index=1,
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
  serialized_start=1183,
  serialized_end=1239,
)

_CANDYMART = _descriptor.Descriptor(
  name='CandyMart',
  full_name='pb.CandyMart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Candy', full_name='pb.CandyMart.Candy', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CANDYMART_DATA, _CANDYMART_BUFF, _CANDYMART_STAGE, _CANDYMART_POPCANDY, _CANDYMART_JPAWARD, _CANDYMART_STAGEAWARD, _CANDYMART_PROGRESS, ],
  enum_types=[
    _CANDYMART_CANDYTYPE,
    _CANDYMART_JPPOINTTYPE,
    _CANDYMART_BUFFTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=1425,
)

_CANDYMART_DATA.fields_by_name['CurStage'].message_type = _CANDYMART_STAGE
_CANDYMART_DATA.fields_by_name['LastCandy'].message_type = _CANDYMART_POPCANDY
_CANDYMART_DATA.fields_by_name['ProgressReward'].message_type = _CANDYMART_PROGRESS
_CANDYMART_DATA.fields_by_name['StageReward'].message_type = _CANDYMART_STAGEAWARD
_CANDYMART_DATA.fields_by_name['JPAwards'].message_type = _CANDYMART_JPAWARD
_CANDYMART_DATA.fields_by_name['CurStageReward'].message_type = _CANDYMART_STAGEAWARD
_CANDYMART_DATA.fields_by_name['MorePickCandy'].message_type = _CANDYMART_POPCANDY
_CANDYMART_DATA.fields_by_name['Booster'].message_type = _CANDYMART_BUFF
_CANDYMART_DATA.fields_by_name['FinalAward'].message_type = award__pb2._AWARDLIST
_CANDYMART_DATA.containing_type = _CANDYMART
_CANDYMART_BUFF.fields_by_name['Type'].enum_type = _CANDYMART_BUFFTYPE
_CANDYMART_BUFF.containing_type = _CANDYMART
_CANDYMART_STAGE.fields_by_name['GroundCandy'].message_type = _CANDYMART_POPCANDY
_CANDYMART_STAGE.fields_by_name['BoxCandy'].message_type = _CANDYMART_POPCANDY
_CANDYMART_STAGE.fields_by_name['Buff'].message_type = _CANDYMART_BUFF
_CANDYMART_STAGE.containing_type = _CANDYMART
_CANDYMART_POPCANDY.fields_by_name['Type'].enum_type = _CANDYMART_CANDYTYPE
_CANDYMART_POPCANDY.fields_by_name['JPPointType'].enum_type = _CANDYMART_JPPOINTTYPE
_CANDYMART_POPCANDY.containing_type = _CANDYMART
_CANDYMART_JPAWARD.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
_CANDYMART_JPAWARD.containing_type = _CANDYMART
_CANDYMART_STAGEAWARD.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
_CANDYMART_STAGEAWARD.containing_type = _CANDYMART
_CANDYMART_PROGRESS.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
_CANDYMART_PROGRESS.containing_type = _CANDYMART
_CANDYMART.fields_by_name['Candy'].message_type = _CANDYMART_DATA
_CANDYMART_CANDYTYPE.containing_type = _CANDYMART
_CANDYMART_JPPOINTTYPE.containing_type = _CANDYMART
_CANDYMART_BUFFTYPE.containing_type = _CANDYMART
DESCRIPTOR.message_types_by_name['CandyMart'] = _CANDYMART
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CandyMart = _reflection.GeneratedProtocolMessageType('CandyMart', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _CANDYMART_DATA,
    '__module__' : 'candymart_pb2'
    # @@protoc_insertion_point(class_scope:pb.CandyMart.Data)
    })
  ,

  'Buff' : _reflection.GeneratedProtocolMessageType('Buff', (_message.Message,), {
    'DESCRIPTOR' : _CANDYMART_BUFF,
    '__module__' : 'candymart_pb2'
    # @@protoc_insertion_point(class_scope:pb.CandyMart.Buff)
    })
  ,

  'Stage' : _reflection.GeneratedProtocolMessageType('Stage', (_message.Message,), {
    'DESCRIPTOR' : _CANDYMART_STAGE,
    '__module__' : 'candymart_pb2'
    # @@protoc_insertion_point(class_scope:pb.CandyMart.Stage)
    })
  ,

  'PopCandy' : _reflection.GeneratedProtocolMessageType('PopCandy', (_message.Message,), {
    'DESCRIPTOR' : _CANDYMART_POPCANDY,
    '__module__' : 'candymart_pb2'
    # @@protoc_insertion_point(class_scope:pb.CandyMart.PopCandy)
    })
  ,

  'JPAward' : _reflection.GeneratedProtocolMessageType('JPAward', (_message.Message,), {
    'DESCRIPTOR' : _CANDYMART_JPAWARD,
    '__module__' : 'candymart_pb2'
    # @@protoc_insertion_point(class_scope:pb.CandyMart.JPAward)
    })
  ,

  'StageAward' : _reflection.GeneratedProtocolMessageType('StageAward', (_message.Message,), {
    'DESCRIPTOR' : _CANDYMART_STAGEAWARD,
    '__module__' : 'candymart_pb2'
    # @@protoc_insertion_point(class_scope:pb.CandyMart.StageAward)
    })
  ,

  'Progress' : _reflection.GeneratedProtocolMessageType('Progress', (_message.Message,), {
    'DESCRIPTOR' : _CANDYMART_PROGRESS,
    '__module__' : 'candymart_pb2'
    # @@protoc_insertion_point(class_scope:pb.CandyMart.Progress)
    })
  ,
  'DESCRIPTOR' : _CANDYMART,
  '__module__' : 'candymart_pb2'
  # @@protoc_insertion_point(class_scope:pb.CandyMart)
  })
_sym_db.RegisterMessage(CandyMart)
_sym_db.RegisterMessage(CandyMart.Data)
_sym_db.RegisterMessage(CandyMart.Buff)
_sym_db.RegisterMessage(CandyMart.Stage)
_sym_db.RegisterMessage(CandyMart.PopCandy)
_sym_db.RegisterMessage(CandyMart.JPAward)
_sym_db.RegisterMessage(CandyMart.StageAward)
_sym_db.RegisterMessage(CandyMart.Progress)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
