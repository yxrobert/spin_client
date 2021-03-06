# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lobbywheel.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import shop_pb2 as shop__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='lobbywheel.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10lobbywheel.proto\x12\x02pb\x1a\nshop.proto\"\xe2\x01\n\nLobbyWheel\x12 \n\x05Wheel\x18\x01 \x01(\x0b\x32\x11.pb.LobbyWheelRsp\x1a\xb1\x01\n\x03Req\x12&\n\x04Info\x18\x01 \x01(\x0b\x32\x16.pb.LobbyWheelInfotReqH\x00\x12\'\n\x05Start\x18\x02 \x01(\x0b\x32\x16.pb.LobbyWheelStartReqH\x00\x12%\n\x04Spin\x18\x03 \x01(\x0b\x32\x15.pb.LobbyWheelSpinReqH\x00\x12+\n\x07\x43ollect\x18\x04 \x01(\x0b\x32\x18.pb.LobbyWheelCollectReqH\x00\x42\x05\n\x03one\"\x14\n\x12LobbyWheelInfotReq\"4\n\x12LobbyWheelStartReq\x12\x1e\n\x03SRC\x18\x01 \x01(\x0e\x32\x11.pb.LobbyWheelSRC\"\x1f\n\x11LobbyWheelSpinReq\x12\n\n\x02id\x18\x01 \x01(\t\"\"\n\x14LobbyWheelCollectReq\x12\n\n\x02id\x18\x01 \x01(\t\"\xfa\x01\n\rLobbyWheelRsp\x12\n\n\x02id\x18\x01 \x01(\t\x12!\n\x05grids\x18\x02 \x03(\x0b\x32\x12.pb.LobbyWheelGrid\x12\x0e\n\x06vipBuf\x18\x03 \x01(\x01\x12\x12\n\nboosterBuf\x18\x04 \x01(\r\x12\x1e\n\x03pay\x18\x05 \x01(\x0b\x32\x11.pb.LobbyWheelPay\x12\r\n\x05state\x18\x06 \x01(\r\x12\x13\n\x0bhandlerType\x18\x07 \x01(\x05\x12\x1e\n\x03SRC\x18\x08 \x01(\x0e\x32\x11.pb.LobbyWheelSRC\x12\x0b\n\x03Vip\x18\t \x01(\r\x12%\n\tRoyalSeal\x18\n \x01(\x0b\x32\x12.pb.Shop.RoyalSeal\"T\n\x0eLobbyWheelGrid\x12\r\n\x05index\x18\x01 \x01(\r\x12\x10\n\x08\x62\x61seCoin\x18\x02 \x01(\x04\x12\x12\n\nisBackGrid\x18\x03 \x01(\x08\x12\r\n\x05isHit\x18\x04 \x01(\x08\"4\n\rLobbyWheelPay\x12\x10\n\x08payCount\x18\x01 \x01(\r\x12\x11\n\tproductId\x18\x02 \x01(\t*@\n\rLobbyWheelSRC\x12\r\n\tLOBBY_SRC\x10\x00\x12\x0c\n\x08MAIL_SRC\x10\x01\x12\x12\n\x0eROYAL_PASS_SRC\x10\x02*c\n\x15LobbyWheelHandlerType\x12\x10\n\x0cHANDLER_INFO\x10\x00\x12\x11\n\rHANDLER_START\x10\x01\x12\x10\n\x0cHANDLER_SPIN\x10\x02\x12\x13\n\x0fHANDLER_COLLECT\x10\x03\x42\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[shop__pb2.DESCRIPTOR,])

_LOBBYWHEELSRC = _descriptor.EnumDescriptor(
  name='LobbyWheelSRC',
  full_name='pb.LobbyWheelSRC',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='LOBBY_SRC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MAIL_SRC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROYAL_PASS_SRC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=803,
  serialized_end=867,
)
_sym_db.RegisterEnumDescriptor(_LOBBYWHEELSRC)

LobbyWheelSRC = enum_type_wrapper.EnumTypeWrapper(_LOBBYWHEELSRC)
_LOBBYWHEELHANDLERTYPE = _descriptor.EnumDescriptor(
  name='LobbyWheelHandlerType',
  full_name='pb.LobbyWheelHandlerType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='HANDLER_INFO', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HANDLER_START', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HANDLER_SPIN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HANDLER_COLLECT', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=869,
  serialized_end=968,
)
_sym_db.RegisterEnumDescriptor(_LOBBYWHEELHANDLERTYPE)

LobbyWheelHandlerType = enum_type_wrapper.EnumTypeWrapper(_LOBBYWHEELHANDLERTYPE)
LOBBY_SRC = 0
MAIL_SRC = 1
ROYAL_PASS_SRC = 2
HANDLER_INFO = 0
HANDLER_START = 1
HANDLER_SPIN = 2
HANDLER_COLLECT = 3



_LOBBYWHEEL_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='pb.LobbyWheel.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Info', full_name='pb.LobbyWheel.Req.Info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Start', full_name='pb.LobbyWheel.Req.Start', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Spin', full_name='pb.LobbyWheel.Req.Spin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Collect', full_name='pb.LobbyWheel.Req.Collect', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
      name='one', full_name='pb.LobbyWheel.Req.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=86,
  serialized_end=263,
)

_LOBBYWHEEL = _descriptor.Descriptor(
  name='LobbyWheel',
  full_name='pb.LobbyWheel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Wheel', full_name='pb.LobbyWheel.Wheel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LOBBYWHEEL_REQ, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=263,
)


_LOBBYWHEELINFOTREQ = _descriptor.Descriptor(
  name='LobbyWheelInfotReq',
  full_name='pb.LobbyWheelInfotReq',
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
  serialized_start=265,
  serialized_end=285,
)


_LOBBYWHEELSTARTREQ = _descriptor.Descriptor(
  name='LobbyWheelStartReq',
  full_name='pb.LobbyWheelStartReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='SRC', full_name='pb.LobbyWheelStartReq.SRC', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=287,
  serialized_end=339,
)


_LOBBYWHEELSPINREQ = _descriptor.Descriptor(
  name='LobbyWheelSpinReq',
  full_name='pb.LobbyWheelSpinReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.LobbyWheelSpinReq.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=341,
  serialized_end=372,
)


_LOBBYWHEELCOLLECTREQ = _descriptor.Descriptor(
  name='LobbyWheelCollectReq',
  full_name='pb.LobbyWheelCollectReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.LobbyWheelCollectReq.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=374,
  serialized_end=408,
)


_LOBBYWHEELRSP = _descriptor.Descriptor(
  name='LobbyWheelRsp',
  full_name='pb.LobbyWheelRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='pb.LobbyWheelRsp.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grids', full_name='pb.LobbyWheelRsp.grids', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vipBuf', full_name='pb.LobbyWheelRsp.vipBuf', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='boosterBuf', full_name='pb.LobbyWheelRsp.boosterBuf', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pay', full_name='pb.LobbyWheelRsp.pay', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='pb.LobbyWheelRsp.state', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='handlerType', full_name='pb.LobbyWheelRsp.handlerType', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='SRC', full_name='pb.LobbyWheelRsp.SRC', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Vip', full_name='pb.LobbyWheelRsp.Vip', index=8,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RoyalSeal', full_name='pb.LobbyWheelRsp.RoyalSeal', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=411,
  serialized_end=661,
)


_LOBBYWHEELGRID = _descriptor.Descriptor(
  name='LobbyWheelGrid',
  full_name='pb.LobbyWheelGrid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='pb.LobbyWheelGrid.index', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='baseCoin', full_name='pb.LobbyWheelGrid.baseCoin', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isBackGrid', full_name='pb.LobbyWheelGrid.isBackGrid', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isHit', full_name='pb.LobbyWheelGrid.isHit', index=3,
      number=4, type=8, cpp_type=7, label=1,
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
  serialized_start=663,
  serialized_end=747,
)


_LOBBYWHEELPAY = _descriptor.Descriptor(
  name='LobbyWheelPay',
  full_name='pb.LobbyWheelPay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='payCount', full_name='pb.LobbyWheelPay.payCount', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productId', full_name='pb.LobbyWheelPay.productId', index=1,
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
  serialized_start=749,
  serialized_end=801,
)

_LOBBYWHEEL_REQ.fields_by_name['Info'].message_type = _LOBBYWHEELINFOTREQ
_LOBBYWHEEL_REQ.fields_by_name['Start'].message_type = _LOBBYWHEELSTARTREQ
_LOBBYWHEEL_REQ.fields_by_name['Spin'].message_type = _LOBBYWHEELSPINREQ
_LOBBYWHEEL_REQ.fields_by_name['Collect'].message_type = _LOBBYWHEELCOLLECTREQ
_LOBBYWHEEL_REQ.containing_type = _LOBBYWHEEL
_LOBBYWHEEL_REQ.oneofs_by_name['one'].fields.append(
  _LOBBYWHEEL_REQ.fields_by_name['Info'])
_LOBBYWHEEL_REQ.fields_by_name['Info'].containing_oneof = _LOBBYWHEEL_REQ.oneofs_by_name['one']
_LOBBYWHEEL_REQ.oneofs_by_name['one'].fields.append(
  _LOBBYWHEEL_REQ.fields_by_name['Start'])
_LOBBYWHEEL_REQ.fields_by_name['Start'].containing_oneof = _LOBBYWHEEL_REQ.oneofs_by_name['one']
_LOBBYWHEEL_REQ.oneofs_by_name['one'].fields.append(
  _LOBBYWHEEL_REQ.fields_by_name['Spin'])
_LOBBYWHEEL_REQ.fields_by_name['Spin'].containing_oneof = _LOBBYWHEEL_REQ.oneofs_by_name['one']
_LOBBYWHEEL_REQ.oneofs_by_name['one'].fields.append(
  _LOBBYWHEEL_REQ.fields_by_name['Collect'])
_LOBBYWHEEL_REQ.fields_by_name['Collect'].containing_oneof = _LOBBYWHEEL_REQ.oneofs_by_name['one']
_LOBBYWHEEL.fields_by_name['Wheel'].message_type = _LOBBYWHEELRSP
_LOBBYWHEELSTARTREQ.fields_by_name['SRC'].enum_type = _LOBBYWHEELSRC
_LOBBYWHEELRSP.fields_by_name['grids'].message_type = _LOBBYWHEELGRID
_LOBBYWHEELRSP.fields_by_name['pay'].message_type = _LOBBYWHEELPAY
_LOBBYWHEELRSP.fields_by_name['SRC'].enum_type = _LOBBYWHEELSRC
_LOBBYWHEELRSP.fields_by_name['RoyalSeal'].message_type = shop__pb2._SHOP_ROYALSEAL
DESCRIPTOR.message_types_by_name['LobbyWheel'] = _LOBBYWHEEL
DESCRIPTOR.message_types_by_name['LobbyWheelInfotReq'] = _LOBBYWHEELINFOTREQ
DESCRIPTOR.message_types_by_name['LobbyWheelStartReq'] = _LOBBYWHEELSTARTREQ
DESCRIPTOR.message_types_by_name['LobbyWheelSpinReq'] = _LOBBYWHEELSPINREQ
DESCRIPTOR.message_types_by_name['LobbyWheelCollectReq'] = _LOBBYWHEELCOLLECTREQ
DESCRIPTOR.message_types_by_name['LobbyWheelRsp'] = _LOBBYWHEELRSP
DESCRIPTOR.message_types_by_name['LobbyWheelGrid'] = _LOBBYWHEELGRID
DESCRIPTOR.message_types_by_name['LobbyWheelPay'] = _LOBBYWHEELPAY
DESCRIPTOR.enum_types_by_name['LobbyWheelSRC'] = _LOBBYWHEELSRC
DESCRIPTOR.enum_types_by_name['LobbyWheelHandlerType'] = _LOBBYWHEELHANDLERTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LobbyWheel = _reflection.GeneratedProtocolMessageType('LobbyWheel', (_message.Message,), {

  'Req' : _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), {
    'DESCRIPTOR' : _LOBBYWHEEL_REQ,
    '__module__' : 'lobbywheel_pb2'
    # @@protoc_insertion_point(class_scope:pb.LobbyWheel.Req)
    })
  ,
  'DESCRIPTOR' : _LOBBYWHEEL,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheel)
  })
_sym_db.RegisterMessage(LobbyWheel)
_sym_db.RegisterMessage(LobbyWheel.Req)

LobbyWheelInfotReq = _reflection.GeneratedProtocolMessageType('LobbyWheelInfotReq', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYWHEELINFOTREQ,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheelInfotReq)
  })
_sym_db.RegisterMessage(LobbyWheelInfotReq)

LobbyWheelStartReq = _reflection.GeneratedProtocolMessageType('LobbyWheelStartReq', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYWHEELSTARTREQ,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheelStartReq)
  })
_sym_db.RegisterMessage(LobbyWheelStartReq)

LobbyWheelSpinReq = _reflection.GeneratedProtocolMessageType('LobbyWheelSpinReq', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYWHEELSPINREQ,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheelSpinReq)
  })
_sym_db.RegisterMessage(LobbyWheelSpinReq)

LobbyWheelCollectReq = _reflection.GeneratedProtocolMessageType('LobbyWheelCollectReq', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYWHEELCOLLECTREQ,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheelCollectReq)
  })
_sym_db.RegisterMessage(LobbyWheelCollectReq)

LobbyWheelRsp = _reflection.GeneratedProtocolMessageType('LobbyWheelRsp', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYWHEELRSP,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheelRsp)
  })
_sym_db.RegisterMessage(LobbyWheelRsp)

LobbyWheelGrid = _reflection.GeneratedProtocolMessageType('LobbyWheelGrid', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYWHEELGRID,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheelGrid)
  })
_sym_db.RegisterMessage(LobbyWheelGrid)

LobbyWheelPay = _reflection.GeneratedProtocolMessageType('LobbyWheelPay', (_message.Message,), {
  'DESCRIPTOR' : _LOBBYWHEELPAY,
  '__module__' : 'lobbywheel_pb2'
  # @@protoc_insertion_point(class_scope:pb.LobbyWheelPay)
  })
_sym_db.RegisterMessage(LobbyWheelPay)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
