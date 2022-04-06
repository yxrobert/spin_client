# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: piggy.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import shop_pb2 as shop__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='piggy.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bpiggy.proto\x12\x02pb\x1a\nshop.proto\"\xf1\x04\n\x05Piggy\x1a|\n\x08PiggyReq\x12!\n\x04Info\x18\x01 \x01(\x0b\x32\x11.pb.Piggy.InfoReqH\x00\x12#\n\x05\x41ward\x18\x02 \x01(\x0b\x32\x12.pb.Piggy.AwardReqH\x00\x12!\n\x04List\x18\x03 \x01(\x0b\x32\x11.pb.Piggy.ListReqH\x00\x42\x05\n\x03one\x1a|\n\x08PiggyRsp\x12!\n\x04Info\x18\x01 \x01(\x0b\x32\x11.pb.Piggy.InfoRspH\x00\x12#\n\x05\x41ward\x18\x02 \x01(\x0b\x32\x12.pb.Piggy.AwardRspH\x00\x12!\n\x04List\x18\x03 \x01(\x0b\x32\x11.pb.Piggy.ListRspH\x00\x42\x05\n\x03one\x1a\t\n\x07InfoReq\x1a)\n\x07InfoRsp\x12\x0e\n\x06IsFull\x18\x01 \x01(\x08\x12\x0e\n\x06IsLock\x18\x02 \x01(\x08\x1a\n\n\x08\x41wardReq\x1a(\n\x08\x41wardRsp\x12\x1c\n\x05Piggy\x18\x01 \x01(\x0b\x32\r.pb.Piggy.Rsp\x1a\t\n\x07ListReq\x1a\'\n\x07ListRsp\x12\x1c\n\x05Piggy\x18\x01 \x01(\x0b\x32\r.pb.Piggy.Rsp\x1at\n\x03Rsp\x12\x0e\n\x06IsFull\x18\x01 \x01(\x08\x12\x11\n\tcoinAward\x18\x02 \x01(\x04\x12\x10\n\x08payCount\x18\x03 \x01(\r\x12\x11\n\tproductId\x18\x04 \x01(\t\x12%\n\tRoyalSeal\x18\x05 \x01(\x0b\x32\x12.pb.Shop.RoyalSeal\x1aV\n\x07Updated\x12\x0e\n\x06IsFull\x18\x01 \x01(\x05\x12\x11\n\tFirstFull\x18\x02 \x01(\x08\x12\x10\n\x08\x43urrFull\x18\x03 \x01(\x08\x12\n\n\x02\x43V\x18\x04 \x01(\x04\x12\n\n\x02TV\x18\x05 \x01(\x04\x42\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[shop__pb2.DESCRIPTOR,])




_PIGGY_PIGGYREQ = _descriptor.Descriptor(
  name='PiggyReq',
  full_name='pb.Piggy.PiggyReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Info', full_name='pb.Piggy.PiggyReq.Info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Award', full_name='pb.Piggy.PiggyReq.Award', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='List', full_name='pb.Piggy.PiggyReq.List', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='one', full_name='pb.Piggy.PiggyReq.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=41,
  serialized_end=165,
)

_PIGGY_PIGGYRSP = _descriptor.Descriptor(
  name='PiggyRsp',
  full_name='pb.Piggy.PiggyRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Info', full_name='pb.Piggy.PiggyRsp.Info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Award', full_name='pb.Piggy.PiggyRsp.Award', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='List', full_name='pb.Piggy.PiggyRsp.List', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
      name='one', full_name='pb.Piggy.PiggyRsp.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=167,
  serialized_end=291,
)

_PIGGY_INFOREQ = _descriptor.Descriptor(
  name='InfoReq',
  full_name='pb.Piggy.InfoReq',
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
  serialized_start=293,
  serialized_end=302,
)

_PIGGY_INFORSP = _descriptor.Descriptor(
  name='InfoRsp',
  full_name='pb.Piggy.InfoRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='IsFull', full_name='pb.Piggy.InfoRsp.IsFull', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IsLock', full_name='pb.Piggy.InfoRsp.IsLock', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  serialized_start=304,
  serialized_end=345,
)

_PIGGY_AWARDREQ = _descriptor.Descriptor(
  name='AwardReq',
  full_name='pb.Piggy.AwardReq',
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
  serialized_start=347,
  serialized_end=357,
)

_PIGGY_AWARDRSP = _descriptor.Descriptor(
  name='AwardRsp',
  full_name='pb.Piggy.AwardRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Piggy', full_name='pb.Piggy.AwardRsp.Piggy', index=0,
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
  serialized_start=359,
  serialized_end=399,
)

_PIGGY_LISTREQ = _descriptor.Descriptor(
  name='ListReq',
  full_name='pb.Piggy.ListReq',
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
  serialized_start=401,
  serialized_end=410,
)

_PIGGY_LISTRSP = _descriptor.Descriptor(
  name='ListRsp',
  full_name='pb.Piggy.ListRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Piggy', full_name='pb.Piggy.ListRsp.Piggy', index=0,
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
  serialized_start=412,
  serialized_end=451,
)

_PIGGY_RSP = _descriptor.Descriptor(
  name='Rsp',
  full_name='pb.Piggy.Rsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='IsFull', full_name='pb.Piggy.Rsp.IsFull', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='coinAward', full_name='pb.Piggy.Rsp.coinAward', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payCount', full_name='pb.Piggy.Rsp.payCount', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='productId', full_name='pb.Piggy.Rsp.productId', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RoyalSeal', full_name='pb.Piggy.Rsp.RoyalSeal', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=453,
  serialized_end=569,
)

_PIGGY_UPDATED = _descriptor.Descriptor(
  name='Updated',
  full_name='pb.Piggy.Updated',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='IsFull', full_name='pb.Piggy.Updated.IsFull', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='FirstFull', full_name='pb.Piggy.Updated.FirstFull', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CurrFull', full_name='pb.Piggy.Updated.CurrFull', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CV', full_name='pb.Piggy.Updated.CV', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='TV', full_name='pb.Piggy.Updated.TV', index=4,
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
  serialized_start=571,
  serialized_end=657,
)

_PIGGY = _descriptor.Descriptor(
  name='Piggy',
  full_name='pb.Piggy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_PIGGY_PIGGYREQ, _PIGGY_PIGGYRSP, _PIGGY_INFOREQ, _PIGGY_INFORSP, _PIGGY_AWARDREQ, _PIGGY_AWARDRSP, _PIGGY_LISTREQ, _PIGGY_LISTRSP, _PIGGY_RSP, _PIGGY_UPDATED, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=32,
  serialized_end=657,
)

_PIGGY_PIGGYREQ.fields_by_name['Info'].message_type = _PIGGY_INFOREQ
_PIGGY_PIGGYREQ.fields_by_name['Award'].message_type = _PIGGY_AWARDREQ
_PIGGY_PIGGYREQ.fields_by_name['List'].message_type = _PIGGY_LISTREQ
_PIGGY_PIGGYREQ.containing_type = _PIGGY
_PIGGY_PIGGYREQ.oneofs_by_name['one'].fields.append(
  _PIGGY_PIGGYREQ.fields_by_name['Info'])
_PIGGY_PIGGYREQ.fields_by_name['Info'].containing_oneof = _PIGGY_PIGGYREQ.oneofs_by_name['one']
_PIGGY_PIGGYREQ.oneofs_by_name['one'].fields.append(
  _PIGGY_PIGGYREQ.fields_by_name['Award'])
_PIGGY_PIGGYREQ.fields_by_name['Award'].containing_oneof = _PIGGY_PIGGYREQ.oneofs_by_name['one']
_PIGGY_PIGGYREQ.oneofs_by_name['one'].fields.append(
  _PIGGY_PIGGYREQ.fields_by_name['List'])
_PIGGY_PIGGYREQ.fields_by_name['List'].containing_oneof = _PIGGY_PIGGYREQ.oneofs_by_name['one']
_PIGGY_PIGGYRSP.fields_by_name['Info'].message_type = _PIGGY_INFORSP
_PIGGY_PIGGYRSP.fields_by_name['Award'].message_type = _PIGGY_AWARDRSP
_PIGGY_PIGGYRSP.fields_by_name['List'].message_type = _PIGGY_LISTRSP
_PIGGY_PIGGYRSP.containing_type = _PIGGY
_PIGGY_PIGGYRSP.oneofs_by_name['one'].fields.append(
  _PIGGY_PIGGYRSP.fields_by_name['Info'])
_PIGGY_PIGGYRSP.fields_by_name['Info'].containing_oneof = _PIGGY_PIGGYRSP.oneofs_by_name['one']
_PIGGY_PIGGYRSP.oneofs_by_name['one'].fields.append(
  _PIGGY_PIGGYRSP.fields_by_name['Award'])
_PIGGY_PIGGYRSP.fields_by_name['Award'].containing_oneof = _PIGGY_PIGGYRSP.oneofs_by_name['one']
_PIGGY_PIGGYRSP.oneofs_by_name['one'].fields.append(
  _PIGGY_PIGGYRSP.fields_by_name['List'])
_PIGGY_PIGGYRSP.fields_by_name['List'].containing_oneof = _PIGGY_PIGGYRSP.oneofs_by_name['one']
_PIGGY_INFOREQ.containing_type = _PIGGY
_PIGGY_INFORSP.containing_type = _PIGGY
_PIGGY_AWARDREQ.containing_type = _PIGGY
_PIGGY_AWARDRSP.fields_by_name['Piggy'].message_type = _PIGGY_RSP
_PIGGY_AWARDRSP.containing_type = _PIGGY
_PIGGY_LISTREQ.containing_type = _PIGGY
_PIGGY_LISTRSP.fields_by_name['Piggy'].message_type = _PIGGY_RSP
_PIGGY_LISTRSP.containing_type = _PIGGY
_PIGGY_RSP.fields_by_name['RoyalSeal'].message_type = shop__pb2._SHOP_ROYALSEAL
_PIGGY_RSP.containing_type = _PIGGY
_PIGGY_UPDATED.containing_type = _PIGGY
DESCRIPTOR.message_types_by_name['Piggy'] = _PIGGY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Piggy = _reflection.GeneratedProtocolMessageType('Piggy', (_message.Message,), {

  'PiggyReq' : _reflection.GeneratedProtocolMessageType('PiggyReq', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_PIGGYREQ,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.PiggyReq)
    })
  ,

  'PiggyRsp' : _reflection.GeneratedProtocolMessageType('PiggyRsp', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_PIGGYRSP,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.PiggyRsp)
    })
  ,

  'InfoReq' : _reflection.GeneratedProtocolMessageType('InfoReq', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_INFOREQ,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.InfoReq)
    })
  ,

  'InfoRsp' : _reflection.GeneratedProtocolMessageType('InfoRsp', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_INFORSP,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.InfoRsp)
    })
  ,

  'AwardReq' : _reflection.GeneratedProtocolMessageType('AwardReq', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_AWARDREQ,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.AwardReq)
    })
  ,

  'AwardRsp' : _reflection.GeneratedProtocolMessageType('AwardRsp', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_AWARDRSP,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.AwardRsp)
    })
  ,

  'ListReq' : _reflection.GeneratedProtocolMessageType('ListReq', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_LISTREQ,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.ListReq)
    })
  ,

  'ListRsp' : _reflection.GeneratedProtocolMessageType('ListRsp', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_LISTRSP,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.ListRsp)
    })
  ,

  'Rsp' : _reflection.GeneratedProtocolMessageType('Rsp', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_RSP,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.Rsp)
    })
  ,

  'Updated' : _reflection.GeneratedProtocolMessageType('Updated', (_message.Message,), {
    'DESCRIPTOR' : _PIGGY_UPDATED,
    '__module__' : 'piggy_pb2'
    # @@protoc_insertion_point(class_scope:pb.Piggy.Updated)
    })
  ,
  'DESCRIPTOR' : _PIGGY,
  '__module__' : 'piggy_pb2'
  # @@protoc_insertion_point(class_scope:pb.Piggy)
  })
_sym_db.RegisterMessage(Piggy)
_sym_db.RegisterMessage(Piggy.PiggyReq)
_sym_db.RegisterMessage(Piggy.PiggyRsp)
_sym_db.RegisterMessage(Piggy.InfoReq)
_sym_db.RegisterMessage(Piggy.InfoRsp)
_sym_db.RegisterMessage(Piggy.AwardReq)
_sym_db.RegisterMessage(Piggy.AwardRsp)
_sym_db.RegisterMessage(Piggy.ListReq)
_sym_db.RegisterMessage(Piggy.ListRsp)
_sym_db.RegisterMessage(Piggy.Rsp)
_sym_db.RegisterMessage(Piggy.Updated)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
