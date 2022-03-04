# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: award.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='award.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x61ward.proto\x12\x02pb\"\xb4\x0b\n\tAwardInfo\x12%\n\x04Type\x18\x01 \x01(\x0e\x32\x17.pb.AwardInfo.AwardType\x12\x10\n\x08SUB_TYPE\x18\x02 \x01(\t\x12\x0e\n\x06\x41mount\x18\x03 \x01(\x04\"\xa7\x01\n\tAwardType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05\x43OINS\x10\x01\x12\n\n\x06TICKET\x10\x02\x12\x0e\n\nCOLLECTION\x10\x03\x12\x08\n\x04\x42UFF\x10\x05\x12\x0c\n\x08POWER_UP\x10\x06\x12\t\n\x05STATE\x10\x07\x12\t\n\x05TIMES\x10\x08\x12\x07\n\x03GEM\x10\t\x12\n\n\x06POINTS\x10\n\x12\x08\n\x04ITEM\x10\x0b\x12\x08\n\x04HERO\x10\x0c\x12\x0b\n\x07HERO_XP\x10\r\"\xcc\x07\n\x08\x41wardSRC\x12\x13\n\x0fUNSPECIFIED_SRC\x10\x00\x12\x0b\n\x07SRC_LUR\x10\x01\x12\x13\n\x0fSRC_LOBBY_BONUS\x10\x02\x12\x13\n\x0fSRC_DAILY_BONUS\x10\x03\x12\x12\n\x0eSRC_SHOP_BONUS\x10\x04\x12\x18\n\x14SRC_SHOP_TIMED_BONUS\x10\x05\x12\x12\n\x0eSRC_BET_TICKET\x10\x06\x12\x0f\n\x0bSRC_TOURNEY\x10\x07\x12\x15\n\x11SRC_HONEY_DO_TASK\x10\x08\x12\x18\n\x14SRC_HONEY_DO_MISSION\x10\t\x12\x1a\n\x16SRC_HONEY_DO_RETENTION\x10\n\x12\x15\n\x11SRC_SHOP_PURCHASE\x10\x0b\x12\x12\n\x0eSRC_LUR_TICKET\x10\x0c\x12\x13\n\x0fSRC_LEADERBOARD\x10\r\x12\x13\n\x0fSRC_BACK_OFFICE\x10\x0e\x12\x0c\n\x08SRC_SPIN\x10\x0f\x12\x1a\n\x16SRC_Player_Update_Info\x10\x10\x12\r\n\tSRC_DEBUG\x10\x11\x12\x0e\n\nSRC_FRIEND\x10\x12\x12\x12\n\x0eSRC_FUNKY_TOWN\x10\x13\x12\x17\n\x13SRC_NEW_PLAYER_ECON\x10\x14\x12\r\n\tSRC_QUEST\x10\x15\x12\x17\n\x13SRC_LOBBYWHEEL_FREE\x10\x16\x12\x16\n\x12SRC_LOBBYWHEEL_PAY\x10\x17\x12\x19\n\x15SRC_DAILY_BONUS_SEVEN\x10\x18\x12\x1a\n\x16SRC_DAILY_BONUS_THIRTY\x10\x19\x12\x19\n\x15SRC_DAILY_BONUS_TOTAL\x10\x1a\x12\x13\n\x0fSRC_DAILY_LOGIN\x10\x1b\x12\x0e\n\nSRC_SYSTEM\x10\x1c\x12\x0c\n\x08SRC_MAIL\x10\x1d\x12\x14\n\x10SRC_DailyMission\x10\x1e\x12\x17\n\x13SRC_LOBBYPOKER_FREE\x10\x1f\x12\x16\n\x12SRC_LOBBYPOKER_PAY\x10 \x12\x12\n\x0eSRC_LOBBYPOKER\x10!\x12\x12\n\x0eSRC_LOBBYWHEEL\x10\"\x12\x0c\n\x08SRC_HERO\x10#\x12\x15\n\x11SRC_HERO_LEVEL_UP\x10$\x12\x14\n\x10SRC_NOVICE_GUIDE\x10%\x12\x13\n\x0fSRC_HERO_ACTIVE\x10&\x12\x18\n\x14SRC_HERO_SKILL_AWARD\x10\'\x12\x19\n\x15SRC_HERO2_SKILL_AWARD\x10(\x12\x0f\n\x0bSRC_FB_BIND\x10)\x12\r\n\tSRC_PIGGY\x10*\x12\x1b\n\x17SRC_SHOP_PIGGY_PURCHASE\x10+\x12\x13\n\x0fSRC_ACT_JOURNEY\x10,\"\xe4\x01\n\x0b\x41wardSubSRC\x12\x17\n\x13SUB_UNSPECIFIED_SRC\x10\x00\x12\x1f\n\x1bSUB_SRC_DailyMission_Normal\x10\x01\x12\x1e\n\x1aSUB_SRC_DailyMission_Super\x10\x02\x12\x1e\n\x1aSUB_SRC_DailyMission_Point\x10\x03\x12\x15\n\x11SUB_SRC_Hero_Shop\x10\x04\x12!\n\x1dSUB_SRC_Hero_Skill_Award_Coin\x10\x05\x12!\n\x1dSUB_SRC_Hero_Skill_Award_Dice\x10\x06\"[\n\x05\x41ward\x12#\n\x03SRC\x18\x01 \x01(\x0e\x32\x16.pb.AwardInfo.AwardSRC\x12\x0f\n\x07SUB_SRC\x18\x02 \x01(\r\x12\x1c\n\x05Pairs\x18\x03 \x03(\x0b\x32\r.pb.AwardInfoB\x06Z\x04.;pbb\x06proto3'
)



_AWARDINFO_AWARDTYPE = _descriptor.EnumDescriptor(
  name='AwardType',
  full_name='pb.AwardInfo.AwardType',
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
      name='COINS', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TICKET', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COLLECTION', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BUFF', index=4, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POWER_UP', index=5, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='STATE', index=6, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIMES', index=7, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GEM', index=8, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='POINTS', index=9, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ITEM', index=10, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HERO', index=11, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HERO_XP', index=12, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=107,
  serialized_end=274,
)
_sym_db.RegisterEnumDescriptor(_AWARDINFO_AWARDTYPE)

_AWARDINFO_AWARDSRC = _descriptor.EnumDescriptor(
  name='AwardSRC',
  full_name='pb.AwardInfo.AwardSRC',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED_SRC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LUR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LOBBY_BONUS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_DAILY_BONUS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_SHOP_BONUS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_SHOP_TIMED_BONUS', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_BET_TICKET', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_TOURNEY', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HONEY_DO_TASK', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HONEY_DO_MISSION', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HONEY_DO_RETENTION', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_SHOP_PURCHASE', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LUR_TICKET', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LEADERBOARD', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_BACK_OFFICE', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_SPIN', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_Player_Update_Info', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_DEBUG', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_FRIEND', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_FUNKY_TOWN', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_NEW_PLAYER_ECON', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_QUEST', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LOBBYWHEEL_FREE', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LOBBYWHEEL_PAY', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_DAILY_BONUS_SEVEN', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_DAILY_BONUS_THIRTY', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_DAILY_BONUS_TOTAL', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_DAILY_LOGIN', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_SYSTEM', index=28, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_MAIL', index=29, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_DailyMission', index=30, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LOBBYPOKER_FREE', index=31, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LOBBYPOKER_PAY', index=32, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LOBBYPOKER', index=33, number=33,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_LOBBYWHEEL', index=34, number=34,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HERO', index=35, number=35,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HERO_LEVEL_UP', index=36, number=36,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_NOVICE_GUIDE', index=37, number=37,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HERO_ACTIVE', index=38, number=38,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HERO_SKILL_AWARD', index=39, number=39,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_HERO2_SKILL_AWARD', index=40, number=40,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_FB_BIND', index=41, number=41,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_PIGGY', index=42, number=42,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_SHOP_PIGGY_PURCHASE', index=43, number=43,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SRC_ACT_JOURNEY', index=44, number=44,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=277,
  serialized_end=1249,
)
_sym_db.RegisterEnumDescriptor(_AWARDINFO_AWARDSRC)

_AWARDINFO_AWARDSUBSRC = _descriptor.EnumDescriptor(
  name='AwardSubSRC',
  full_name='pb.AwardInfo.AwardSubSRC',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUB_UNSPECIFIED_SRC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUB_SRC_DailyMission_Normal', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUB_SRC_DailyMission_Super', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUB_SRC_DailyMission_Point', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUB_SRC_Hero_Shop', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUB_SRC_Hero_Skill_Award_Coin', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUB_SRC_Hero_Skill_Award_Dice', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1252,
  serialized_end=1480,
)
_sym_db.RegisterEnumDescriptor(_AWARDINFO_AWARDSUBSRC)


_AWARDINFO = _descriptor.Descriptor(
  name='AwardInfo',
  full_name='pb.AwardInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.AwardInfo.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SUB_TYPE', full_name='pb.AwardInfo.SUB_TYPE', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Amount', full_name='pb.AwardInfo.Amount', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _AWARDINFO_AWARDTYPE,
    _AWARDINFO_AWARDSRC,
    _AWARDINFO_AWARDSUBSRC,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=1480,
)


_AWARD = _descriptor.Descriptor(
  name='Award',
  full_name='pb.Award',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SRC', full_name='pb.Award.SRC', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SUB_SRC', full_name='pb.Award.SUB_SRC', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Pairs', full_name='pb.Award.Pairs', index=2,
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
  serialized_start=1482,
  serialized_end=1573,
)

_AWARDINFO.fields_by_name['Type'].enum_type = _AWARDINFO_AWARDTYPE
_AWARDINFO_AWARDTYPE.containing_type = _AWARDINFO
_AWARDINFO_AWARDSRC.containing_type = _AWARDINFO
_AWARDINFO_AWARDSUBSRC.containing_type = _AWARDINFO
_AWARD.fields_by_name['SRC'].enum_type = _AWARDINFO_AWARDSRC
_AWARD.fields_by_name['Pairs'].message_type = _AWARDINFO
DESCRIPTOR.message_types_by_name['AwardInfo'] = _AWARDINFO
DESCRIPTOR.message_types_by_name['Award'] = _AWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AwardInfo = _reflection.GeneratedProtocolMessageType('AwardInfo', (_message.Message,), {
  'DESCRIPTOR' : _AWARDINFO,
  '__module__' : 'award_pb2'
  # @@protoc_insertion_point(class_scope:pb.AwardInfo)
  })
_sym_db.RegisterMessage(AwardInfo)

Award = _reflection.GeneratedProtocolMessageType('Award', (_message.Message,), {
  'DESCRIPTOR' : _AWARD,
  '__module__' : 'award_pb2'
  # @@protoc_insertion_point(class_scope:pb.Award)
  })
_sym_db.RegisterMessage(Award)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
