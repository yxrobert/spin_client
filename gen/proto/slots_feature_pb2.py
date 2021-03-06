# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: slots_feature.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='slots_feature.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13slots_feature.proto\x12\x02pb\"8\n\x08JPSymbol\x12\x1d\n\x04Type\x18\x01 \x01(\x0e\x32\x0f.pb.JackpotType\x12\r\n\x05Value\x18\x02 \x01(\x04\"8\n\x0fStepperProgress\x12\x10\n\x08Progress\x18\x01 \x01(\r\x12\x13\n\x0bMaxProgress\x18\x02 \x01(\r\">\n\x0cUnlockJPData\x12\r\n\x05Level\x18\x01 \x01(\r\x12\x0e\n\x06\x42\x65tIdx\x18\x02 \x01(\r\x12\x0f\n\x07JPLevel\x18\x03 \x01(\r\"\\\n\x0bGorillaItem\x12!\n\x04Type\x18\x01 \x01(\x0e\x32\x13.pb.GorillaItemType\x12\r\n\x05Value\x18\x02 \x01(\r\x12\x0c\n\x04\x43ost\x18\x03 \x01(\r\x12\r\n\x05Index\x18\x04 \x01(\x05\"X\n\x0fGorillaPageData\x12\x1e\n\x05Items\x18\x01 \x03(\x0b\x32\x0f.pb.GorillaItem\x12\x10\n\x08IsLocked\x18\x02 \x01(\x08\x12\x13\n\x0bNextPayFree\x18\x03 \x01(\x08\"0\n\x0bGorillaShop\x12!\n\x04\x44\x61ta\x18\x01 \x03(\x0b\x32\x13.pb.GorillaPageData*N\n\x13\x42ingoMooFeatureType\x12\x08\n\x04\x42\x61se\x10\x00\x12\x08\n\x04\x46ree\x10\x01\x12\x08\n\x04Mega\x10\x02\x12\t\n\x05Super\x10\x03\x12\x0e\n\nPickReward\x10\x04*O\n\x0bJackpotType\x12\x0b\n\x07\x45Symbol\x10\x00\x12\t\n\x05GRAND\x10\x01\x12\t\n\x05MAJOR\x10\x02\x12\x08\n\x04MAXI\x10\x03\x12\t\n\x05MINOR\x10\x04\x12\x08\n\x04MINI\x10\x05*j\n\x14PiggyBankFeatureType\x12\x12\n\x0ePiggyBank_Base\x10\x00\x12\x15\n\x11PiggyBank_Stepper\x10\x01\x12\x12\n\x0ePiggyBank_Free\x10\x02\x12\x13\n\x0fPiggyBank_Super\x10\x03*]\n\x0fGorillaItemType\x12\x11\n\rGorilla_Close\x10\x00\x12\x10\n\x0cGorilla_Coin\x10\x01\x12\x12\n\x0eGorilla_Double\x10\x02\x12\x11\n\rGorilla_Bonus\x10\x03\x42\x06Z\x04.;pbb\x06proto3'
)

_BINGOMOOFEATURETYPE = _descriptor.EnumDescriptor(
  name='BingoMooFeatureType',
  full_name='pb.BingoMooFeatureType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Base', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Free', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Mega', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Super', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PickReward', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=441,
  serialized_end=519,
)
_sym_db.RegisterEnumDescriptor(_BINGOMOOFEATURETYPE)

BingoMooFeatureType = enum_type_wrapper.EnumTypeWrapper(_BINGOMOOFEATURETYPE)
_JACKPOTTYPE = _descriptor.EnumDescriptor(
  name='JackpotType',
  full_name='pb.JackpotType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ESymbol', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GRAND', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAJOR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAXI', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MINOR', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MINI', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=521,
  serialized_end=600,
)
_sym_db.RegisterEnumDescriptor(_JACKPOTTYPE)

JackpotType = enum_type_wrapper.EnumTypeWrapper(_JACKPOTTYPE)
_PIGGYBANKFEATURETYPE = _descriptor.EnumDescriptor(
  name='PiggyBankFeatureType',
  full_name='pb.PiggyBankFeatureType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PiggyBank_Base', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PiggyBank_Stepper', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PiggyBank_Free', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PiggyBank_Super', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=602,
  serialized_end=708,
)
_sym_db.RegisterEnumDescriptor(_PIGGYBANKFEATURETYPE)

PiggyBankFeatureType = enum_type_wrapper.EnumTypeWrapper(_PIGGYBANKFEATURETYPE)
_GORILLAITEMTYPE = _descriptor.EnumDescriptor(
  name='GorillaItemType',
  full_name='pb.GorillaItemType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Gorilla_Close', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Gorilla_Coin', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Gorilla_Double', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Gorilla_Bonus', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=710,
  serialized_end=803,
)
_sym_db.RegisterEnumDescriptor(_GORILLAITEMTYPE)

GorillaItemType = enum_type_wrapper.EnumTypeWrapper(_GORILLAITEMTYPE)
Base = 0
Free = 1
Mega = 2
Super = 3
PickReward = 4
ESymbol = 0
GRAND = 1
MAJOR = 2
MAXI = 3
MINOR = 4
MINI = 5
PiggyBank_Base = 0
PiggyBank_Stepper = 1
PiggyBank_Free = 2
PiggyBank_Super = 3
Gorilla_Close = 0
Gorilla_Coin = 1
Gorilla_Double = 2
Gorilla_Bonus = 3



_JPSYMBOL = _descriptor.Descriptor(
  name='JPSymbol',
  full_name='pb.JPSymbol',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.JPSymbol.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.JPSymbol.Value', index=1,
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
  serialized_start=27,
  serialized_end=83,
)


_STEPPERPROGRESS = _descriptor.Descriptor(
  name='StepperProgress',
  full_name='pb.StepperProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Progress', full_name='pb.StepperProgress.Progress', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='MaxProgress', full_name='pb.StepperProgress.MaxProgress', index=1,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=85,
  serialized_end=141,
)


_UNLOCKJPDATA = _descriptor.Descriptor(
  name='UnlockJPData',
  full_name='pb.UnlockJPData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Level', full_name='pb.UnlockJPData.Level', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BetIdx', full_name='pb.UnlockJPData.BetIdx', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='JPLevel', full_name='pb.UnlockJPData.JPLevel', index=2,
      number=3, type=13, cpp_type=3, label=1,
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
  serialized_start=143,
  serialized_end=205,
)


_GORILLAITEM = _descriptor.Descriptor(
  name='GorillaItem',
  full_name='pb.GorillaItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Type', full_name='pb.GorillaItem.Type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.GorillaItem.Value', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Cost', full_name='pb.GorillaItem.Cost', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Index', full_name='pb.GorillaItem.Index', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=207,
  serialized_end=299,
)


_GORILLAPAGEDATA = _descriptor.Descriptor(
  name='GorillaPageData',
  full_name='pb.GorillaPageData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Items', full_name='pb.GorillaPageData.Items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IsLocked', full_name='pb.GorillaPageData.IsLocked', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='NextPayFree', full_name='pb.GorillaPageData.NextPayFree', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=301,
  serialized_end=389,
)


_GORILLASHOP = _descriptor.Descriptor(
  name='GorillaShop',
  full_name='pb.GorillaShop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Data', full_name='pb.GorillaShop.Data', index=0,
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
  serialized_start=391,
  serialized_end=439,
)

_JPSYMBOL.fields_by_name['Type'].enum_type = _JACKPOTTYPE
_GORILLAITEM.fields_by_name['Type'].enum_type = _GORILLAITEMTYPE
_GORILLAPAGEDATA.fields_by_name['Items'].message_type = _GORILLAITEM
_GORILLASHOP.fields_by_name['Data'].message_type = _GORILLAPAGEDATA
DESCRIPTOR.message_types_by_name['JPSymbol'] = _JPSYMBOL
DESCRIPTOR.message_types_by_name['StepperProgress'] = _STEPPERPROGRESS
DESCRIPTOR.message_types_by_name['UnlockJPData'] = _UNLOCKJPDATA
DESCRIPTOR.message_types_by_name['GorillaItem'] = _GORILLAITEM
DESCRIPTOR.message_types_by_name['GorillaPageData'] = _GORILLAPAGEDATA
DESCRIPTOR.message_types_by_name['GorillaShop'] = _GORILLASHOP
DESCRIPTOR.enum_types_by_name['BingoMooFeatureType'] = _BINGOMOOFEATURETYPE
DESCRIPTOR.enum_types_by_name['JackpotType'] = _JACKPOTTYPE
DESCRIPTOR.enum_types_by_name['PiggyBankFeatureType'] = _PIGGYBANKFEATURETYPE
DESCRIPTOR.enum_types_by_name['GorillaItemType'] = _GORILLAITEMTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JPSymbol = _reflection.GeneratedProtocolMessageType('JPSymbol', (_message.Message,), {
  'DESCRIPTOR' : _JPSYMBOL,
  '__module__' : 'slots_feature_pb2'
  # @@protoc_insertion_point(class_scope:pb.JPSymbol)
  })
_sym_db.RegisterMessage(JPSymbol)

StepperProgress = _reflection.GeneratedProtocolMessageType('StepperProgress', (_message.Message,), {
  'DESCRIPTOR' : _STEPPERPROGRESS,
  '__module__' : 'slots_feature_pb2'
  # @@protoc_insertion_point(class_scope:pb.StepperProgress)
  })
_sym_db.RegisterMessage(StepperProgress)

UnlockJPData = _reflection.GeneratedProtocolMessageType('UnlockJPData', (_message.Message,), {
  'DESCRIPTOR' : _UNLOCKJPDATA,
  '__module__' : 'slots_feature_pb2'
  # @@protoc_insertion_point(class_scope:pb.UnlockJPData)
  })
_sym_db.RegisterMessage(UnlockJPData)

GorillaItem = _reflection.GeneratedProtocolMessageType('GorillaItem', (_message.Message,), {
  'DESCRIPTOR' : _GORILLAITEM,
  '__module__' : 'slots_feature_pb2'
  # @@protoc_insertion_point(class_scope:pb.GorillaItem)
  })
_sym_db.RegisterMessage(GorillaItem)

GorillaPageData = _reflection.GeneratedProtocolMessageType('GorillaPageData', (_message.Message,), {
  'DESCRIPTOR' : _GORILLAPAGEDATA,
  '__module__' : 'slots_feature_pb2'
  # @@protoc_insertion_point(class_scope:pb.GorillaPageData)
  })
_sym_db.RegisterMessage(GorillaPageData)

GorillaShop = _reflection.GeneratedProtocolMessageType('GorillaShop', (_message.Message,), {
  'DESCRIPTOR' : _GORILLASHOP,
  '__module__' : 'slots_feature_pb2'
  # @@protoc_insertion_point(class_scope:pb.GorillaShop)
  })
_sym_db.RegisterMessage(GorillaShop)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
