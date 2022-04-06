# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bingo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import award_pb2 as award__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='bingo.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0b\x62ingo.proto\x12\x02pb\x1a\x0b\x61ward.proto\"\xf3\x04\n\x05\x42ingo\x1a\xce\x01\n\x04\x44\x61ta\x12\x11\n\tBingoBall\x18\x01 \x01(\x05\x12\x10\n\x08StageIdx\x18\x02 \x01(\x05\x12\x10\n\x08\x42oardIdx\x18\x03 \x01(\x05\x12\x10\n\x08Progress\x18\x04 \x01(\x05\x12!\n\x08\x43urBoard\x18\x05 \x01(\x0b\x32\x0f.pb.Bingo.Board\x12)\n\x0bStageReward\x18\x06 \x03(\x0b\x32\x14.pb.Bingo.StageAward\x12/\n\x0eProgressReward\x18\x07 \x03(\x0b\x32\x17.pb.Bingo.ProgressAward\x1a\x66\n\x05\x42oard\x12\x1f\n\x07\x43urCard\x18\x01 \x01(\x0b\x32\x0e.pb.Bingo.Card\x12\'\n\x0cPopBallQueue\x18\x02 \x03(\x0b\x32\x11.pb.Bingo.PopBall\x12\x13\n\x0bLeftBallNum\x18\x03 \x01(\x05\x1a\x44\n\x07PopBall\x12\r\n\x05Value\x18\x01 \x01(\x05\x12\x13\n\x0b\x41\x64\x64Progress\x18\x02 \x01(\x05\x12\x15\n\rAfterProgress\x18\x03 \x01(\x05\x1a\x8d\x01\n\x04\x43\x61rd\x12 \n\x04Rows\x18\x01 \x03(\x0b\x32\x12.pb.Bingo.Card.Row\x1a\x63\n\x03Row\x12\r\n\x05Items\x18\x01 \x03(\x05\x1aM\n\x04Item\x12\r\n\x05Value\x18\x01 \x01(\x05\x12\x11\n\tIsPainted\x18\x02 \x01(\x08\x12\x11\n\tHasReward\x18\x03 \x01(\x08\x12\x10\n\x08IsPicked\x18\x04 \x01(\x08\x1a+\n\nStageAward\x12\x1d\n\x06\x41wards\x18\x01 \x03(\x0b\x32\r.pb.AwardInfo\x1a.\n\rProgressAward\x12\x1d\n\x06\x41wards\x18\x01 \x03(\x0b\x32\r.pb.AwardInfoB\x06Z\x04.;pbb\x06proto3'
  ,
  dependencies=[award__pb2.DESCRIPTOR,])




_BINGO_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='pb.Bingo.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='BingoBall', full_name='pb.Bingo.Data.BingoBall', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StageIdx', full_name='pb.Bingo.Data.StageIdx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='BoardIdx', full_name='pb.Bingo.Data.BoardIdx', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Progress', full_name='pb.Bingo.Data.Progress', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='CurBoard', full_name='pb.Bingo.Data.CurBoard', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='StageReward', full_name='pb.Bingo.Data.StageReward', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ProgressReward', full_name='pb.Bingo.Data.ProgressReward', index=6,
      number=7, type=11, cpp_type=10, label=3,
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
  serialized_start=43,
  serialized_end=249,
)

_BINGO_BOARD = _descriptor.Descriptor(
  name='Board',
  full_name='pb.Bingo.Board',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='CurCard', full_name='pb.Bingo.Board.CurCard', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='PopBallQueue', full_name='pb.Bingo.Board.PopBallQueue', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='LeftBallNum', full_name='pb.Bingo.Board.LeftBallNum', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=251,
  serialized_end=353,
)

_BINGO_POPBALL = _descriptor.Descriptor(
  name='PopBall',
  full_name='pb.Bingo.PopBall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.Bingo.PopBall.Value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AddProgress', full_name='pb.Bingo.PopBall.AddProgress', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='AfterProgress', full_name='pb.Bingo.PopBall.AfterProgress', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=355,
  serialized_end=423,
)

_BINGO_CARD_ROW_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='pb.Bingo.Card.Row.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Value', full_name='pb.Bingo.Card.Row.Item.Value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IsPainted', full_name='pb.Bingo.Card.Row.Item.IsPainted', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='HasReward', full_name='pb.Bingo.Card.Row.Item.HasReward', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='IsPicked', full_name='pb.Bingo.Card.Row.Item.IsPicked', index=3,
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
  serialized_start=490,
  serialized_end=567,
)

_BINGO_CARD_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='pb.Bingo.Card.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Items', full_name='pb.Bingo.Card.Row.Items', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BINGO_CARD_ROW_ITEM, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=468,
  serialized_end=567,
)

_BINGO_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='pb.Bingo.Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Rows', full_name='pb.Bingo.Card.Rows', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BINGO_CARD_ROW, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=567,
)

_BINGO_STAGEAWARD = _descriptor.Descriptor(
  name='StageAward',
  full_name='pb.Bingo.StageAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.Bingo.StageAward.Awards', index=0,
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
  serialized_start=569,
  serialized_end=612,
)

_BINGO_PROGRESSAWARD = _descriptor.Descriptor(
  name='ProgressAward',
  full_name='pb.Bingo.ProgressAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Awards', full_name='pb.Bingo.ProgressAward.Awards', index=0,
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
  serialized_start=614,
  serialized_end=660,
)

_BINGO = _descriptor.Descriptor(
  name='Bingo',
  full_name='pb.Bingo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_BINGO_DATA, _BINGO_BOARD, _BINGO_POPBALL, _BINGO_CARD, _BINGO_STAGEAWARD, _BINGO_PROGRESSAWARD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=660,
)

_BINGO_DATA.fields_by_name['CurBoard'].message_type = _BINGO_BOARD
_BINGO_DATA.fields_by_name['StageReward'].message_type = _BINGO_STAGEAWARD
_BINGO_DATA.fields_by_name['ProgressReward'].message_type = _BINGO_PROGRESSAWARD
_BINGO_DATA.containing_type = _BINGO
_BINGO_BOARD.fields_by_name['CurCard'].message_type = _BINGO_CARD
_BINGO_BOARD.fields_by_name['PopBallQueue'].message_type = _BINGO_POPBALL
_BINGO_BOARD.containing_type = _BINGO
_BINGO_POPBALL.containing_type = _BINGO
_BINGO_CARD_ROW_ITEM.containing_type = _BINGO_CARD_ROW
_BINGO_CARD_ROW.containing_type = _BINGO_CARD
_BINGO_CARD.fields_by_name['Rows'].message_type = _BINGO_CARD_ROW
_BINGO_CARD.containing_type = _BINGO
_BINGO_STAGEAWARD.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
_BINGO_STAGEAWARD.containing_type = _BINGO
_BINGO_PROGRESSAWARD.fields_by_name['Awards'].message_type = award__pb2._AWARDINFO
_BINGO_PROGRESSAWARD.containing_type = _BINGO
DESCRIPTOR.message_types_by_name['Bingo'] = _BINGO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Bingo = _reflection.GeneratedProtocolMessageType('Bingo', (_message.Message,), {

  'Data' : _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
    'DESCRIPTOR' : _BINGO_DATA,
    '__module__' : 'bingo_pb2'
    # @@protoc_insertion_point(class_scope:pb.Bingo.Data)
    })
  ,

  'Board' : _reflection.GeneratedProtocolMessageType('Board', (_message.Message,), {
    'DESCRIPTOR' : _BINGO_BOARD,
    '__module__' : 'bingo_pb2'
    # @@protoc_insertion_point(class_scope:pb.Bingo.Board)
    })
  ,

  'PopBall' : _reflection.GeneratedProtocolMessageType('PopBall', (_message.Message,), {
    'DESCRIPTOR' : _BINGO_POPBALL,
    '__module__' : 'bingo_pb2'
    # @@protoc_insertion_point(class_scope:pb.Bingo.PopBall)
    })
  ,

  'Card' : _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {

    'Row' : _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), {

      'Item' : _reflection.GeneratedProtocolMessageType('Item', (_message.Message,), {
        'DESCRIPTOR' : _BINGO_CARD_ROW_ITEM,
        '__module__' : 'bingo_pb2'
        # @@protoc_insertion_point(class_scope:pb.Bingo.Card.Row.Item)
        })
      ,
      'DESCRIPTOR' : _BINGO_CARD_ROW,
      '__module__' : 'bingo_pb2'
      # @@protoc_insertion_point(class_scope:pb.Bingo.Card.Row)
      })
    ,
    'DESCRIPTOR' : _BINGO_CARD,
    '__module__' : 'bingo_pb2'
    # @@protoc_insertion_point(class_scope:pb.Bingo.Card)
    })
  ,

  'StageAward' : _reflection.GeneratedProtocolMessageType('StageAward', (_message.Message,), {
    'DESCRIPTOR' : _BINGO_STAGEAWARD,
    '__module__' : 'bingo_pb2'
    # @@protoc_insertion_point(class_scope:pb.Bingo.StageAward)
    })
  ,

  'ProgressAward' : _reflection.GeneratedProtocolMessageType('ProgressAward', (_message.Message,), {
    'DESCRIPTOR' : _BINGO_PROGRESSAWARD,
    '__module__' : 'bingo_pb2'
    # @@protoc_insertion_point(class_scope:pb.Bingo.ProgressAward)
    })
  ,
  'DESCRIPTOR' : _BINGO,
  '__module__' : 'bingo_pb2'
  # @@protoc_insertion_point(class_scope:pb.Bingo)
  })
_sym_db.RegisterMessage(Bingo)
_sym_db.RegisterMessage(Bingo.Data)
_sym_db.RegisterMessage(Bingo.Board)
_sym_db.RegisterMessage(Bingo.PopBall)
_sym_db.RegisterMessage(Bingo.Card)
_sym_db.RegisterMessage(Bingo.Card.Row)
_sym_db.RegisterMessage(Bingo.Card.Row.Item)
_sym_db.RegisterMessage(Bingo.StageAward)
_sym_db.RegisterMessage(Bingo.ProgressAward)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
