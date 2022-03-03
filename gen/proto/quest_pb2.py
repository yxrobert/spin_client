# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: quest.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='quest.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bquest.proto\x12\x02pb\"\xee\x06\n\x06Quests\x1a\xdc\x01\n\x03Req\x12)\n\x04List\x18\n \x01(\x0b\x32\x19.pb.Quests.Req.Quest.ListH\x00\x12+\n\x05\x43heck\x18\x0b \x01(\x0b\x32\x1a.pb.Quests.Req.Quest.CheckH\x00\x12/\n\x07\x43ollect\x18\x0c \x01(\x0b\x32\x1c.pb.Quests.Req.Quest.CollectH\x00\x1a\x45\n\x05Quest\x1a\x06\n\x04List\x1a\x18\n\x05\x43heck\x12\x0f\n\x07QuestId\x18\x01 \x01(\r\x1a\x1a\n\x07\x43ollect\x12\x0f\n\x07QuestId\x18\x01 \x01(\rB\x05\n\x03one\x1a\xf8\x02\n\x03Rsp\x12&\n\x06\x43ommon\x18\n \x01(\x0b\x32\x14.pb.Quests.Rsp.ErrorH\x00\x12)\n\x04List\x18\x14 \x01(\x0b\x32\x19.pb.Quests.Rsp.Quest.ListH\x00\x12+\n\x05\x43heck\x18\x1e \x01(\x0b\x32\x1a.pb.Quests.Rsp.Quest.CheckH\x00\x12/\n\x07\x43ollect\x18( \x01(\x0b\x32\x1c.pb.Quests.Rsp.Quest.CollectH\x00\x1a\'\n\x05\x45rror\x12\x0e\n\x06\x43lient\x18\x01 \x01(\t\x12\x0e\n\x06Server\x18\x02 \x01(\t\x1a\x8f\x01\n\x05Quest\x1a,\n\x04List\x12$\n\x06Quests\x18\x01 \x03(\x0b\x32\x14.pb.Quests.QuestInfo\x1a,\n\x05\x43heck\x12#\n\x05Quest\x18\x01 \x01(\x0b\x32\x14.pb.Quests.QuestInfo\x1a*\n\x07\x43ollect\x12\x1f\n\x05\x41ward\x18\x01 \x01(\x0b\x32\x10.pb.Quests.AwardB\x05\n\x03one\x1a\x80\x01\n\tQuestInfo\x12\x0f\n\x07QuestId\x18\x01 \x01(\r\x12\x0f\n\x07ThemeId\x18\x02 \x01(\r\x12 \n\x06\x45vents\x18\x03 \x03(\x0b\x32\x10.pb.Quests.Event\x12\r\n\x05\x41ward\x18\x04 \x01(\x08\x12\x11\n\tAwardCoin\x18\x05 \x01(\x04\x12\r\n\x05Round\x18\x06 \x01(\r\x1a_\n\x05\x45vent\x12\x0f\n\x07\x45ventId\x18\x01 \x01(\t\x12\r\n\x05Index\x18\x02 \x01(\r\x12\x13\n\x0bTargetValue\x18\x03 \x01(\x04\x12\x11\n\tCurrValue\x18\x04 \x01(\x04\x12\x0e\n\x06\x46inish\x18\x05 \x01(\x08\x1a&\n\x05\x41ward\x12\x0f\n\x07QuestId\x18\x01 \x01(\r\x12\x0c\n\x04\x43oin\x18\x02 \x01(\x04\x42\x06Z\x04.;pbb\x06proto3'
)




_QUESTS_REQ_QUEST_LIST = _descriptor.Descriptor(
  name='List',
  full_name='pb.Quests.Req.Quest.List',
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
  serialized_start=38,
  serialized_end=44,
)

_QUESTS_REQ_QUEST_CHECK = _descriptor.Descriptor(
  name='Check',
  full_name='pb.Quests.Req.Quest.Check',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='QuestId', full_name='pb.Quests.Req.Quest.Check.QuestId', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=192,
  serialized_end=216,
)

_QUESTS_REQ_QUEST_COLLECT = _descriptor.Descriptor(
  name='Collect',
  full_name='pb.Quests.Req.Quest.Collect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='QuestId', full_name='pb.Quests.Req.Quest.Collect.QuestId', index=0,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=218,
  serialized_end=244,
)

_QUESTS_REQ_QUEST = _descriptor.Descriptor(
  name='Quest',
  full_name='pb.Quests.Req.Quest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_QUESTS_REQ_QUEST_LIST, _QUESTS_REQ_QUEST_CHECK, _QUESTS_REQ_QUEST_COLLECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=175,
  serialized_end=244,
)

_QUESTS_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='pb.Quests.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='List', full_name='pb.Quests.Req.List', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Check', full_name='pb.Quests.Req.Check', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Collect', full_name='pb.Quests.Req.Collect', index=2,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_QUESTS_REQ_QUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.Quests.Req.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=31,
  serialized_end=251,
)

_QUESTS_RSP_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='pb.Quests.Rsp.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Client', full_name='pb.Quests.Rsp.Error.Client', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Server', full_name='pb.Quests.Rsp.Error.Server', index=1,
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
  serialized_start=438,
  serialized_end=477,
)

_QUESTS_RSP_QUEST_LIST = _descriptor.Descriptor(
  name='List',
  full_name='pb.Quests.Rsp.Quest.List',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Quests', full_name='pb.Quests.Rsp.Quest.List.Quests', index=0,
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
  serialized_start=489,
  serialized_end=533,
)

_QUESTS_RSP_QUEST_CHECK = _descriptor.Descriptor(
  name='Check',
  full_name='pb.Quests.Rsp.Quest.Check',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Quest', full_name='pb.Quests.Rsp.Quest.Check.Quest', index=0,
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
  ],
  serialized_start=535,
  serialized_end=579,
)

_QUESTS_RSP_QUEST_COLLECT = _descriptor.Descriptor(
  name='Collect',
  full_name='pb.Quests.Rsp.Quest.Collect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Award', full_name='pb.Quests.Rsp.Quest.Collect.Award', index=0,
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
  ],
  serialized_start=581,
  serialized_end=623,
)

_QUESTS_RSP_QUEST = _descriptor.Descriptor(
  name='Quest',
  full_name='pb.Quests.Rsp.Quest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_QUESTS_RSP_QUEST_LIST, _QUESTS_RSP_QUEST_CHECK, _QUESTS_RSP_QUEST_COLLECT, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=623,
)

_QUESTS_RSP = _descriptor.Descriptor(
  name='Rsp',
  full_name='pb.Quests.Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Common', full_name='pb.Quests.Rsp.Common', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='List', full_name='pb.Quests.Rsp.List', index=1,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Check', full_name='pb.Quests.Rsp.Check', index=2,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Collect', full_name='pb.Quests.Rsp.Collect', index=3,
      number=40, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_QUESTS_RSP_ERROR, _QUESTS_RSP_QUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.Quests.Rsp.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=254,
  serialized_end=630,
)

_QUESTS_QUESTINFO = _descriptor.Descriptor(
  name='QuestInfo',
  full_name='pb.Quests.QuestInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='QuestId', full_name='pb.Quests.QuestInfo.QuestId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ThemeId', full_name='pb.Quests.QuestInfo.ThemeId', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Events', full_name='pb.Quests.QuestInfo.Events', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Award', full_name='pb.Quests.QuestInfo.Award', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AwardCoin', full_name='pb.Quests.QuestInfo.AwardCoin', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Round', full_name='pb.Quests.QuestInfo.Round', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=633,
  serialized_end=761,
)

_QUESTS_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='pb.Quests.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='EventId', full_name='pb.Quests.Event.EventId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Index', full_name='pb.Quests.Event.Index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TargetValue', full_name='pb.Quests.Event.TargetValue', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CurrValue', full_name='pb.Quests.Event.CurrValue', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Finish', full_name='pb.Quests.Event.Finish', index=4,
      number=5, type=8, cpp_type=7, label=1,
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
  serialized_start=763,
  serialized_end=858,
)

_QUESTS_AWARD = _descriptor.Descriptor(
  name='Award',
  full_name='pb.Quests.Award',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='QuestId', full_name='pb.Quests.Award.QuestId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Coin', full_name='pb.Quests.Award.Coin', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=860,
  serialized_end=898,
)

_QUESTS = _descriptor.Descriptor(
  name='Quests',
  full_name='pb.Quests',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_QUESTS_REQ, _QUESTS_RSP, _QUESTS_QUESTINFO, _QUESTS_EVENT, _QUESTS_AWARD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=898,
)

_QUESTS_REQ_QUEST_LIST.containing_type = _QUESTS_REQ_QUEST
_QUESTS_REQ_QUEST_CHECK.containing_type = _QUESTS_REQ_QUEST
_QUESTS_REQ_QUEST_COLLECT.containing_type = _QUESTS_REQ_QUEST
_QUESTS_REQ_QUEST.containing_type = _QUESTS_REQ
_QUESTS_REQ.fields_by_name['List'].message_type = _QUESTS_REQ_QUEST_LIST
_QUESTS_REQ.fields_by_name['Check'].message_type = _QUESTS_REQ_QUEST_CHECK
_QUESTS_REQ.fields_by_name['Collect'].message_type = _QUESTS_REQ_QUEST_COLLECT
_QUESTS_REQ.containing_type = _QUESTS
_QUESTS_REQ.oneofs_by_name['one'].fields.append(
  _QUESTS_REQ.fields_by_name['List'])
_QUESTS_REQ.fields_by_name['List'].containing_oneof = _QUESTS_REQ.oneofs_by_name['one']
_QUESTS_REQ.oneofs_by_name['one'].fields.append(
  _QUESTS_REQ.fields_by_name['Check'])
_QUESTS_REQ.fields_by_name['Check'].containing_oneof = _QUESTS_REQ.oneofs_by_name['one']
_QUESTS_REQ.oneofs_by_name['one'].fields.append(
  _QUESTS_REQ.fields_by_name['Collect'])
_QUESTS_REQ.fields_by_name['Collect'].containing_oneof = _QUESTS_REQ.oneofs_by_name['one']
_QUESTS_RSP_ERROR.containing_type = _QUESTS_RSP
_QUESTS_RSP_QUEST_LIST.fields_by_name['Quests'].message_type = _QUESTS_QUESTINFO
_QUESTS_RSP_QUEST_LIST.containing_type = _QUESTS_RSP_QUEST
_QUESTS_RSP_QUEST_CHECK.fields_by_name['Quest'].message_type = _QUESTS_QUESTINFO
_QUESTS_RSP_QUEST_CHECK.containing_type = _QUESTS_RSP_QUEST
_QUESTS_RSP_QUEST_COLLECT.fields_by_name['Award'].message_type = _QUESTS_AWARD
_QUESTS_RSP_QUEST_COLLECT.containing_type = _QUESTS_RSP_QUEST
_QUESTS_RSP_QUEST.containing_type = _QUESTS_RSP
_QUESTS_RSP.fields_by_name['Common'].message_type = _QUESTS_RSP_ERROR
_QUESTS_RSP.fields_by_name['List'].message_type = _QUESTS_RSP_QUEST_LIST
_QUESTS_RSP.fields_by_name['Check'].message_type = _QUESTS_RSP_QUEST_CHECK
_QUESTS_RSP.fields_by_name['Collect'].message_type = _QUESTS_RSP_QUEST_COLLECT
_QUESTS_RSP.containing_type = _QUESTS
_QUESTS_RSP.oneofs_by_name['one'].fields.append(
  _QUESTS_RSP.fields_by_name['Common'])
_QUESTS_RSP.fields_by_name['Common'].containing_oneof = _QUESTS_RSP.oneofs_by_name['one']
_QUESTS_RSP.oneofs_by_name['one'].fields.append(
  _QUESTS_RSP.fields_by_name['List'])
_QUESTS_RSP.fields_by_name['List'].containing_oneof = _QUESTS_RSP.oneofs_by_name['one']
_QUESTS_RSP.oneofs_by_name['one'].fields.append(
  _QUESTS_RSP.fields_by_name['Check'])
_QUESTS_RSP.fields_by_name['Check'].containing_oneof = _QUESTS_RSP.oneofs_by_name['one']
_QUESTS_RSP.oneofs_by_name['one'].fields.append(
  _QUESTS_RSP.fields_by_name['Collect'])
_QUESTS_RSP.fields_by_name['Collect'].containing_oneof = _QUESTS_RSP.oneofs_by_name['one']
_QUESTS_QUESTINFO.fields_by_name['Events'].message_type = _QUESTS_EVENT
_QUESTS_QUESTINFO.containing_type = _QUESTS
_QUESTS_EVENT.containing_type = _QUESTS
_QUESTS_AWARD.containing_type = _QUESTS
DESCRIPTOR.message_types_by_name['Quests'] = _QUESTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Quests = _reflection.GeneratedProtocolMessageType('Quests', (_message.Message,), {

  'Req' : _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), {

    'Quest' : _reflection.GeneratedProtocolMessageType('Quest', (_message.Message,), {

      'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
        'DESCRIPTOR' : _QUESTS_REQ_QUEST_LIST,
        '__module__' : 'quest_pb2'
        # @@protoc_insertion_point(class_scope:pb.Quests.Req.Quest.List)
        })
      ,

      'Check' : _reflection.GeneratedProtocolMessageType('Check', (_message.Message,), {
        'DESCRIPTOR' : _QUESTS_REQ_QUEST_CHECK,
        '__module__' : 'quest_pb2'
        # @@protoc_insertion_point(class_scope:pb.Quests.Req.Quest.Check)
        })
      ,

      'Collect' : _reflection.GeneratedProtocolMessageType('Collect', (_message.Message,), {
        'DESCRIPTOR' : _QUESTS_REQ_QUEST_COLLECT,
        '__module__' : 'quest_pb2'
        # @@protoc_insertion_point(class_scope:pb.Quests.Req.Quest.Collect)
        })
      ,
      'DESCRIPTOR' : _QUESTS_REQ_QUEST,
      '__module__' : 'quest_pb2'
      # @@protoc_insertion_point(class_scope:pb.Quests.Req.Quest)
      })
    ,
    'DESCRIPTOR' : _QUESTS_REQ,
    '__module__' : 'quest_pb2'
    # @@protoc_insertion_point(class_scope:pb.Quests.Req)
    })
  ,

  'Rsp' : _reflection.GeneratedProtocolMessageType('Rsp', (_message.Message,), {

    'Error' : _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
      'DESCRIPTOR' : _QUESTS_RSP_ERROR,
      '__module__' : 'quest_pb2'
      # @@protoc_insertion_point(class_scope:pb.Quests.Rsp.Error)
      })
    ,

    'Quest' : _reflection.GeneratedProtocolMessageType('Quest', (_message.Message,), {

      'List' : _reflection.GeneratedProtocolMessageType('List', (_message.Message,), {
        'DESCRIPTOR' : _QUESTS_RSP_QUEST_LIST,
        '__module__' : 'quest_pb2'
        # @@protoc_insertion_point(class_scope:pb.Quests.Rsp.Quest.List)
        })
      ,

      'Check' : _reflection.GeneratedProtocolMessageType('Check', (_message.Message,), {
        'DESCRIPTOR' : _QUESTS_RSP_QUEST_CHECK,
        '__module__' : 'quest_pb2'
        # @@protoc_insertion_point(class_scope:pb.Quests.Rsp.Quest.Check)
        })
      ,

      'Collect' : _reflection.GeneratedProtocolMessageType('Collect', (_message.Message,), {
        'DESCRIPTOR' : _QUESTS_RSP_QUEST_COLLECT,
        '__module__' : 'quest_pb2'
        # @@protoc_insertion_point(class_scope:pb.Quests.Rsp.Quest.Collect)
        })
      ,
      'DESCRIPTOR' : _QUESTS_RSP_QUEST,
      '__module__' : 'quest_pb2'
      # @@protoc_insertion_point(class_scope:pb.Quests.Rsp.Quest)
      })
    ,
    'DESCRIPTOR' : _QUESTS_RSP,
    '__module__' : 'quest_pb2'
    # @@protoc_insertion_point(class_scope:pb.Quests.Rsp)
    })
  ,

  'QuestInfo' : _reflection.GeneratedProtocolMessageType('QuestInfo', (_message.Message,), {
    'DESCRIPTOR' : _QUESTS_QUESTINFO,
    '__module__' : 'quest_pb2'
    # @@protoc_insertion_point(class_scope:pb.Quests.QuestInfo)
    })
  ,

  'Event' : _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {
    'DESCRIPTOR' : _QUESTS_EVENT,
    '__module__' : 'quest_pb2'
    # @@protoc_insertion_point(class_scope:pb.Quests.Event)
    })
  ,

  'Award' : _reflection.GeneratedProtocolMessageType('Award', (_message.Message,), {
    'DESCRIPTOR' : _QUESTS_AWARD,
    '__module__' : 'quest_pb2'
    # @@protoc_insertion_point(class_scope:pb.Quests.Award)
    })
  ,
  'DESCRIPTOR' : _QUESTS,
  '__module__' : 'quest_pb2'
  # @@protoc_insertion_point(class_scope:pb.Quests)
  })
_sym_db.RegisterMessage(Quests)
_sym_db.RegisterMessage(Quests.Req)
_sym_db.RegisterMessage(Quests.Req.Quest)
_sym_db.RegisterMessage(Quests.Req.Quest.List)
_sym_db.RegisterMessage(Quests.Req.Quest.Check)
_sym_db.RegisterMessage(Quests.Req.Quest.Collect)
_sym_db.RegisterMessage(Quests.Rsp)
_sym_db.RegisterMessage(Quests.Rsp.Error)
_sym_db.RegisterMessage(Quests.Rsp.Quest)
_sym_db.RegisterMessage(Quests.Rsp.Quest.List)
_sym_db.RegisterMessage(Quests.Rsp.Quest.Check)
_sym_db.RegisterMessage(Quests.Rsp.Quest.Collect)
_sym_db.RegisterMessage(Quests.QuestInfo)
_sym_db.RegisterMessage(Quests.Event)
_sym_db.RegisterMessage(Quests.Award)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
