# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: multiverse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import activityevent_pb2 as activityevent__pb2
import award_pb2 as award__pb2
import slots_util_pb2 as slots__util__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='multiverse.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10multiverse.proto\x12\x02pb\x1a\x13\x61\x63tivityevent.proto\x1a\x0b\x61ward.proto\x1a\x10slots_util.proto\"[\n\x0eMultiverseBuff\x12$\n\x04Type\x18\x01 \x01(\x0e\x32\x16.pb.MultiverseBuffType\x12\r\n\x05Value\x18\x02 \x01(\x05\x12\x14\n\x0c\x45ndTimeStamp\x18\x03 \x01(\x03\"\xf8\x04\n\x0eMultiverseData\x12\r\n\x05\x45ntry\x18\x01 \x01(\x05\x12\r\n\x05Level\x18\x02 \x01(\x05\x12\x12\n\nChapterIdx\x18\x03 \x01(\x05\x12\x0f\n\x07NodeIdx\x18\x04 \x01(\x05\x12,\n\nNodeStatus\x18\x05 \x01(\x0e\x32\x18.pb.MultiverseNodeStatus\x12$\n\tQuestList\x18\x06 \x03(\x0b\x32\x11.pb.ActivityEvent\x12\x38\n\x11\x43hooseLevelReward\x18\x07 \x03(\x0b\x32\x1d.pb.MultiverseData.LevelAward\x12\x36\n\rChapterReward\x18\x08 \x01(\x0b\x32\x1f.pb.MultiverseData.ChapterAward\x12!\n\nHellReward\x18\t \x03(\x0b\x32\r.pb.AwardInfo\x12 \n\x04\x42uff\x18\n \x03(\x0b\x32\x12.pb.MultiverseBuff\x12\x15\n\rChapterThemes\x18\x0b \x03(\x05\x12\x0f\n\x07GemCost\x18\x0c \x01(\x05\x12\x0e\n\x06\x42\x65Hell\x18\r \x01(\x08\x12\x17\n\x0fMaxChapterLevel\x18\x0e \x03(\x05\x1a+\n\nLevelAward\x12\x1d\n\x06\x41wards\x18\x01 \x03(\x0b\x32\r.pb.AwardInfo\x1a.\n\tNodeAward\x12!\n\nNodeAwards\x18\x01 \x03(\x0b\x32\r.pb.AwardInfo\x1aj\n\x0c\x43hapterAward\x12\x30\n\nNodeAwards\x18\x01 \x03(\x0b\x32\x1c.pb.MultiverseData.NodeAward\x12(\n\nReelReward\x18\x02 \x01(\x0b\x32\x14.pb.MultiverseReward\"\xb5\x03\n\x10MultiverseReward\x12.\n\x08Jackpots\x18\x01 \x03(\x0b\x32\x1c.pb.MultiverseReward.Section\x12(\n\x05Reels\x18\x02 \x03(\x0b\x32\x19.pb.MultiverseReward.Reel\x12\x34\n\tExtraData\x18\x03 \x03(\x0b\x32!.pb.MultiverseReward.ExtraJackpot\x1a\x41\n\x07Section\x12\'\n\x04Type\x18\x01 \x01(\x0e\x32\x19.pb.MultiverseReward.Type\x12\r\n\x05Value\x18\x02 \x01(\x03\x1aY\n\x0c\x45xtraJackpot\x12\'\n\x04Type\x18\x01 \x01(\x0e\x32\x19.pb.MultiverseReward.Type\x12 \n\x07IncData\x18\x02 \x01(\x0b\x32\x0f.pb.IncResource\x1a\x36\n\x04Reel\x12.\n\x08Sections\x18\x01 \x03(\x0b\x32\x1c.pb.MultiverseReward.Section\";\n\x04Type\x12\t\n\x05Minor\x10\x00\x12\t\n\x05Major\x10\x01\x12\t\n\x05Grand\x10\x02\x12\t\n\x05Money\x10\n\x12\x07\n\x03Key\x10\x0b*C\n\x14MultiverseNodeStatus\x12\x0c\n\x08\x43hoosing\x10\x00\x12\r\n\tInHanding\x10\x01\x12\x0e\n\nInAwarding\x10\x02*G\n\x14MultiverseDifficulty\x12\n\n\x06Normal\x10\x00\x12\r\n\tNightmare\x10\x01\x12\x08\n\x04Hell\x10\x02\x12\n\n\x06Length\x10\x03*&\n\x12MultiverseBuffType\x12\x10\n\x0cMBT_Progress\x10\x00\x42\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[activityevent__pb2.DESCRIPTOR,award__pb2.DESCRIPTOR,slots__util__pb2.DESCRIPTOR,])

_MULTIVERSENODESTATUS = _descriptor.EnumDescriptor(
  name='MultiverseNodeStatus',
  full_name='pb.MultiverseNodeStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Choosing', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InHanding', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='InAwarding', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1244,
  serialized_end=1311,
)
_sym_db.RegisterEnumDescriptor(_MULTIVERSENODESTATUS)

MultiverseNodeStatus = enum_type_wrapper.EnumTypeWrapper(_MULTIVERSENODESTATUS)
_MULTIVERSEDIFFICULTY = _descriptor.EnumDescriptor(
  name='MultiverseDifficulty',
  full_name='pb.MultiverseDifficulty',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Normal', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Nightmare', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Hell', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Length', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1313,
  serialized_end=1384,
)
_sym_db.RegisterEnumDescriptor(_MULTIVERSEDIFFICULTY)

MultiverseDifficulty = enum_type_wrapper.EnumTypeWrapper(_MULTIVERSEDIFFICULTY)
_MULTIVERSEBUFFTYPE = _descriptor.EnumDescriptor(
  name='MultiverseBuffType',
  full_name='pb.MultiverseBuffType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MBT_Progress', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1386,
  serialized_end=1424,
)
_sym_db.RegisterEnumDescriptor(_MULTIVERSEBUFFTYPE)

MultiverseBuffType = enum_type_wrapper.EnumTypeWrapper(_MULTIVERSEBUFFTYPE)
Choosing = 0
InHanding = 1
InAwarding = 2
Normal = 0
Nightmare = 1
Hell = 2
Length = 3
MBT_Progress = 0


_MULTIVERSEREWARD_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='pb.MultiverseReward.Type',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Minor', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Major', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Grand', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Money', index=3, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Key', index=4, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1183,
  serialized_end=1242,
)
_sym_db.RegisterEnumDescriptor(_MULTIVERSEREWARD_TYPE)


_MULTIVERSEBUFF = _descriptor.Descriptor(
  name='MultiverseBuff',
  full_name='pb.MultiverseBuff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.MultiverseBuff.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.MultiverseBuff.Value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='EndTimeStamp', full_name='pb.MultiverseBuff.EndTimeStamp', index=2,
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
  serialized_start=76,
  serialized_end=167,
)


_MULTIVERSEDATA_LEVELAWARD = _descriptor.Descriptor(
  name='LevelAward',
  full_name='pb.MultiverseData.LevelAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.MultiverseData.LevelAward.Awards', index=0,
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
  serialized_start=603,
  serialized_end=646,
)

_MULTIVERSEDATA_NODEAWARD = _descriptor.Descriptor(
  name='NodeAward',
  full_name='pb.MultiverseData.NodeAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='NodeAwards', full_name='pb.MultiverseData.NodeAward.NodeAwards', index=0,
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
  serialized_start=648,
  serialized_end=694,
)

_MULTIVERSEDATA_CHAPTERAWARD = _descriptor.Descriptor(
  name='ChapterAward',
  full_name='pb.MultiverseData.ChapterAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='NodeAwards', full_name='pb.MultiverseData.ChapterAward.NodeAwards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ReelReward', full_name='pb.MultiverseData.ChapterAward.ReelReward', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=696,
  serialized_end=802,
)

_MULTIVERSEDATA = _descriptor.Descriptor(
  name='MultiverseData',
  full_name='pb.MultiverseData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Entry', full_name='pb.MultiverseData.Entry', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Level', full_name='pb.MultiverseData.Level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ChapterIdx', full_name='pb.MultiverseData.ChapterIdx', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='NodeIdx', full_name='pb.MultiverseData.NodeIdx', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='NodeStatus', full_name='pb.MultiverseData.NodeStatus', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='QuestList', full_name='pb.MultiverseData.QuestList', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ChooseLevelReward', full_name='pb.MultiverseData.ChooseLevelReward', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ChapterReward', full_name='pb.MultiverseData.ChapterReward', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='HellReward', full_name='pb.MultiverseData.HellReward', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Buff', full_name='pb.MultiverseData.Buff', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ChapterThemes', full_name='pb.MultiverseData.ChapterThemes', index=10,
      number=11, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='GemCost', full_name='pb.MultiverseData.GemCost', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BeHell', full_name='pb.MultiverseData.BeHell', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MaxChapterLevel', full_name='pb.MultiverseData.MaxChapterLevel', index=13,
      number=14, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MULTIVERSEDATA_LEVELAWARD, _MULTIVERSEDATA_NODEAWARD, _MULTIVERSEDATA_CHAPTERAWARD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=170,
  serialized_end=802,
)


_MULTIVERSEREWARD_SECTION = _descriptor.Descriptor(
  name='Section',
  full_name='pb.MultiverseReward.Section',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.MultiverseReward.Section.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.MultiverseReward.Section.Value', index=1,
      number=2, type=3, cpp_type=2, label=1,
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
  serialized_start=969,
  serialized_end=1034,
)

_MULTIVERSEREWARD_EXTRAJACKPOT = _descriptor.Descriptor(
  name='ExtraJackpot',
  full_name='pb.MultiverseReward.ExtraJackpot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.MultiverseReward.ExtraJackpot.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IncData', full_name='pb.MultiverseReward.ExtraJackpot.IncData', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=1036,
  serialized_end=1125,
)

_MULTIVERSEREWARD_REEL = _descriptor.Descriptor(
  name='Reel',
  full_name='pb.MultiverseReward.Reel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Sections', full_name='pb.MultiverseReward.Reel.Sections', index=0,
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
  serialized_start=1127,
  serialized_end=1181,
)

_MULTIVERSEREWARD = _descriptor.Descriptor(
  name='MultiverseReward',
  full_name='pb.MultiverseReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Jackpots', full_name='pb.MultiverseReward.Jackpots', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Reels', full_name='pb.MultiverseReward.Reels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ExtraData', full_name='pb.MultiverseReward.ExtraData', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MULTIVERSEREWARD_SECTION, _MULTIVERSEREWARD_EXTRAJACKPOT, _MULTIVERSEREWARD_REEL, ],
  enum_types=[
    _MULTIVERSEREWARD_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=805,
  serialized_end=1242,
)

_MULTIVERSEBUFF.fields_by_name['Type'].enum_type = _MULTIVERSEBUFFTYPE
_MULTIVERSEDATA_LEVELAWARD.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
_MULTIVERSEDATA_LEVELAWARD.containing_type = _MULTIVERSEDATA
_MULTIVERSEDATA_NODEAWARD.fields_by_name['NodeAwards'].message_type = award__pb2._AWARDINFO
_MULTIVERSEDATA_NODEAWARD.containing_type = _MULTIVERSEDATA
_MULTIVERSEDATA_CHAPTERAWARD.fields_by_name['NodeAwards'].message_type = _MULTIVERSEDATA_NODEAWARD
_MULTIVERSEDATA_CHAPTERAWARD.fields_by_name['ReelReward'].message_type = _MULTIVERSEREWARD
_MULTIVERSEDATA_CHAPTERAWARD.containing_type = _MULTIVERSEDATA
_MULTIVERSEDATA.fields_by_name['NodeStatus'].enum_type = _MULTIVERSENODESTATUS
_MULTIVERSEDATA.fields_by_name['QuestList'].message_type = activityevent__pb2._ACTIVITYEVENT
_MULTIVERSEDATA.fields_by_name['ChooseLevelReward'].message_type = _MULTIVERSEDATA_LEVELAWARD
_MULTIVERSEDATA.fields_by_name['ChapterReward'].message_type = _MULTIVERSEDATA_CHAPTERAWARD
_MULTIVERSEDATA.fields_by_name['HellReward'].message_type = award__pb2._AWARDINFO
_MULTIVERSEDATA.fields_by_name['Buff'].message_type = _MULTIVERSEBUFF
_MULTIVERSEREWARD_SECTION.fields_by_name['Type'].enum_type = _MULTIVERSEREWARD_TYPE
_MULTIVERSEREWARD_SECTION.containing_type = _MULTIVERSEREWARD
_MULTIVERSEREWARD_EXTRAJACKPOT.fields_by_name['Type'].enum_type = _MULTIVERSEREWARD_TYPE
_MULTIVERSEREWARD_EXTRAJACKPOT.fields_by_name['IncData'].message_type = slots__util__pb2._INCRESOURCE
_MULTIVERSEREWARD_EXTRAJACKPOT.containing_type = _MULTIVERSEREWARD
_MULTIVERSEREWARD_REEL.fields_by_name['Sections'].message_type = _MULTIVERSEREWARD_SECTION
_MULTIVERSEREWARD_REEL.containing_type = _MULTIVERSEREWARD
_MULTIVERSEREWARD.fields_by_name['Jackpots'].message_type = _MULTIVERSEREWARD_SECTION
_MULTIVERSEREWARD.fields_by_name['Reels'].message_type = _MULTIVERSEREWARD_REEL
_MULTIVERSEREWARD.fields_by_name['ExtraData'].message_type = _MULTIVERSEREWARD_EXTRAJACKPOT
_MULTIVERSEREWARD_TYPE.containing_type = _MULTIVERSEREWARD
DESCRIPTOR.message_types_by_name['MultiverseBuff'] = _MULTIVERSEBUFF
DESCRIPTOR.message_types_by_name['MultiverseData'] = _MULTIVERSEDATA
DESCRIPTOR.message_types_by_name['MultiverseReward'] = _MULTIVERSEREWARD
DESCRIPTOR.enum_types_by_name['MultiverseNodeStatus'] = _MULTIVERSENODESTATUS
DESCRIPTOR.enum_types_by_name['MultiverseDifficulty'] = _MULTIVERSEDIFFICULTY
DESCRIPTOR.enum_types_by_name['MultiverseBuffType'] = _MULTIVERSEBUFFTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MultiverseBuff = _reflection.GeneratedProtocolMessageType('MultiverseBuff', (_message.Message,), {
  'DESCRIPTOR' : _MULTIVERSEBUFF,
  '__module__' : 'multiverse_pb2'
  # @@protoc_insertion_point(class_scope:pb.MultiverseBuff)
  })
_sym_db.RegisterMessage(MultiverseBuff)

MultiverseData = _reflection.GeneratedProtocolMessageType('MultiverseData', (_message.Message,), {

  'LevelAward' : _reflection.GeneratedProtocolMessageType('LevelAward', (_message.Message,), {
    'DESCRIPTOR' : _MULTIVERSEDATA_LEVELAWARD,
    '__module__' : 'multiverse_pb2'
    # @@protoc_insertion_point(class_scope:pb.MultiverseData.LevelAward)
    })
  ,

  'NodeAward' : _reflection.GeneratedProtocolMessageType('NodeAward', (_message.Message,), {
    'DESCRIPTOR' : _MULTIVERSEDATA_NODEAWARD,
    '__module__' : 'multiverse_pb2'
    # @@protoc_insertion_point(class_scope:pb.MultiverseData.NodeAward)
    })
  ,

  'ChapterAward' : _reflection.GeneratedProtocolMessageType('ChapterAward', (_message.Message,), {
    'DESCRIPTOR' : _MULTIVERSEDATA_CHAPTERAWARD,
    '__module__' : 'multiverse_pb2'
    # @@protoc_insertion_point(class_scope:pb.MultiverseData.ChapterAward)
    })
  ,
  'DESCRIPTOR' : _MULTIVERSEDATA,
  '__module__' : 'multiverse_pb2'
  # @@protoc_insertion_point(class_scope:pb.MultiverseData)
  })
_sym_db.RegisterMessage(MultiverseData)
_sym_db.RegisterMessage(MultiverseData.LevelAward)
_sym_db.RegisterMessage(MultiverseData.NodeAward)
_sym_db.RegisterMessage(MultiverseData.ChapterAward)

MultiverseReward = _reflection.GeneratedProtocolMessageType('MultiverseReward', (_message.Message,), {

  'Section' : _reflection.GeneratedProtocolMessageType('Section', (_message.Message,), {
    'DESCRIPTOR' : _MULTIVERSEREWARD_SECTION,
    '__module__' : 'multiverse_pb2'
    # @@protoc_insertion_point(class_scope:pb.MultiverseReward.Section)
    })
  ,

  'ExtraJackpot' : _reflection.GeneratedProtocolMessageType('ExtraJackpot', (_message.Message,), {
    'DESCRIPTOR' : _MULTIVERSEREWARD_EXTRAJACKPOT,
    '__module__' : 'multiverse_pb2'
    # @@protoc_insertion_point(class_scope:pb.MultiverseReward.ExtraJackpot)
    })
  ,

  'Reel' : _reflection.GeneratedProtocolMessageType('Reel', (_message.Message,), {
    'DESCRIPTOR' : _MULTIVERSEREWARD_REEL,
    '__module__' : 'multiverse_pb2'
    # @@protoc_insertion_point(class_scope:pb.MultiverseReward.Reel)
    })
  ,
  'DESCRIPTOR' : _MULTIVERSEREWARD,
  '__module__' : 'multiverse_pb2'
  # @@protoc_insertion_point(class_scope:pb.MultiverseReward)
  })
_sym_db.RegisterMessage(MultiverseReward)
_sym_db.RegisterMessage(MultiverseReward.Section)
_sym_db.RegisterMessage(MultiverseReward.ExtraJackpot)
_sym_db.RegisterMessage(MultiverseReward.Reel)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
