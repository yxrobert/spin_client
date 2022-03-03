# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: slots_jackpot.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='slots_jackpot.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13slots_jackpot.proto\x12\x02pb\"K\n\x07Jackpot\x12\x0b\n\x03\x42\x65t\x18\x01 \x01(\x04\x12\r\n\x05Level\x18\x02 \x01(\x05\x12\x0f\n\x07Startup\x18\x03 \x01(\x04\x12\x13\n\x0bProgressive\x18\x04 \x01(\x04\"u\n\x0eJackpotSyncing\x1a\'\n\x07Request\x12\x0f\n\x07ThemeID\x18\x01 \x01(\x05\x12\x0b\n\x03\x42\x65t\x18\x02 \x01(\x04\x1a:\n\x08Response\x12\x0f\n\x07ThemeID\x18\x01 \x01(\x05\x12\x1d\n\x08Jackpots\x18\x65 \x03(\x0b\x32\x0b.pb.Jackpot\"-\n\x0cJPVisionData\x12\x0b\n\x03\x42\x65t\x18\x01 \x01(\x04\x12\x10\n\x08JPLevels\x18\x02 \x03(\x05\x42\x06Z\x04.;pbb\x06proto3'
)




_JACKPOT = _descriptor.Descriptor(
  name='Jackpot',
  full_name='pb.Jackpot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Bet', full_name='pb.Jackpot.Bet', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Level', full_name='pb.Jackpot.Level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Startup', full_name='pb.Jackpot.Startup', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Progressive', full_name='pb.Jackpot.Progressive', index=3,
      number=4, type=4, cpp_type=4, label=1,
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
  serialized_end=102,
)


_JACKPOTSYNCING_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='pb.JackpotSyncing.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ThemeID', full_name='pb.JackpotSyncing.Request.ThemeID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Bet', full_name='pb.JackpotSyncing.Request.Bet', index=1,
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
  serialized_start=122,
  serialized_end=161,
)

_JACKPOTSYNCING_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='pb.JackpotSyncing.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ThemeID', full_name='pb.JackpotSyncing.Response.ThemeID', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Jackpots', full_name='pb.JackpotSyncing.Response.Jackpots', index=1,
      number=101, type=11, cpp_type=10, label=3,
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
  serialized_start=163,
  serialized_end=221,
)

_JACKPOTSYNCING = _descriptor.Descriptor(
  name='JackpotSyncing',
  full_name='pb.JackpotSyncing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_JACKPOTSYNCING_REQUEST, _JACKPOTSYNCING_RESPONSE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=221,
)


_JPVISIONDATA = _descriptor.Descriptor(
  name='JPVisionData',
  full_name='pb.JPVisionData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Bet', full_name='pb.JPVisionData.Bet', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='JPLevels', full_name='pb.JPVisionData.JPLevels', index=1,
      number=2, type=5, cpp_type=1, label=3,
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
  serialized_start=223,
  serialized_end=268,
)

_JACKPOTSYNCING_REQUEST.containing_type = _JACKPOTSYNCING
_JACKPOTSYNCING_RESPONSE.fields_by_name['Jackpots'].message_type = _JACKPOT
_JACKPOTSYNCING_RESPONSE.containing_type = _JACKPOTSYNCING
DESCRIPTOR.message_types_by_name['Jackpot'] = _JACKPOT
DESCRIPTOR.message_types_by_name['JackpotSyncing'] = _JACKPOTSYNCING
DESCRIPTOR.message_types_by_name['JPVisionData'] = _JPVISIONDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Jackpot = _reflection.GeneratedProtocolMessageType('Jackpot', (_message.Message,), {
  'DESCRIPTOR' : _JACKPOT,
  '__module__' : 'slots_jackpot_pb2'
  # @@protoc_insertion_point(class_scope:pb.Jackpot)
  })
_sym_db.RegisterMessage(Jackpot)

JackpotSyncing = _reflection.GeneratedProtocolMessageType('JackpotSyncing', (_message.Message,), {

  'Request' : _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
    'DESCRIPTOR' : _JACKPOTSYNCING_REQUEST,
    '__module__' : 'slots_jackpot_pb2'
    # @@protoc_insertion_point(class_scope:pb.JackpotSyncing.Request)
    })
  ,

  'Response' : _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
    'DESCRIPTOR' : _JACKPOTSYNCING_RESPONSE,
    '__module__' : 'slots_jackpot_pb2'
    # @@protoc_insertion_point(class_scope:pb.JackpotSyncing.Response)
    })
  ,
  'DESCRIPTOR' : _JACKPOTSYNCING,
  '__module__' : 'slots_jackpot_pb2'
  # @@protoc_insertion_point(class_scope:pb.JackpotSyncing)
  })
_sym_db.RegisterMessage(JackpotSyncing)
_sym_db.RegisterMessage(JackpotSyncing.Request)
_sym_db.RegisterMessage(JackpotSyncing.Response)

JPVisionData = _reflection.GeneratedProtocolMessageType('JPVisionData', (_message.Message,), {
  'DESCRIPTOR' : _JPVISIONDATA,
  '__module__' : 'slots_jackpot_pb2'
  # @@protoc_insertion_point(class_scope:pb.JPVisionData)
  })
_sym_db.RegisterMessage(JPVisionData)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
