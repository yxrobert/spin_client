# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: post_office.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='post_office.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11post_office.proto\x12\x02pb\"\xfe\x01\n\nPostOffice\x1a:\n\x03Req\x12,\n\x07\x41\x64\x64Push\x18\x01 \x01(\x0b\x32\x19.pb.PostOffice.ReqAddPushH\x00\x42\x05\n\x03one\x1a<\n\x04Resp\x12-\n\x07\x41\x64\x64Push\x18\x01 \x01(\x0b\x32\x1a.pb.PostOffice.RespAddPushH\x00\x42\x05\n\x03one\x1a[\n\nReqAddPush\x12\x11\n\tAccountID\x18\x01 \x01(\t\x12\x0b\n\x03UID\x18\x02 \x01(\x03\x12\r\n\x05Title\x18\x03 \x01(\t\x12\x0b\n\x03Msg\x18\x04 \x01(\t\x12\x11\n\tTimestamp\x18\x05 \x01(\x03\x1a\x19\n\x0bRespAddPush\x12\n\n\x02ID\x18\x01 \x01(\x03\x42\x06Z\x04.;pbb\x06proto3'
)




_POSTOFFICE_REQ = _descriptor.Descriptor(
  name='Req',
  full_name='pb.PostOffice.Req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='AddPush', full_name='pb.PostOffice.Req.AddPush', index=0,
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
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.PostOffice.Req.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=40,
  serialized_end=98,
)

_POSTOFFICE_RESP = _descriptor.Descriptor(
  name='Resp',
  full_name='pb.PostOffice.Resp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='AddPush', full_name='pb.PostOffice.Resp.AddPush', index=0,
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
    _descriptor.OneofDescriptor(
      name='one', full_name='pb.PostOffice.Resp.one',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=100,
  serialized_end=160,
)

_POSTOFFICE_REQADDPUSH = _descriptor.Descriptor(
  name='ReqAddPush',
  full_name='pb.PostOffice.ReqAddPush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='AccountID', full_name='pb.PostOffice.ReqAddPush.AccountID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='UID', full_name='pb.PostOffice.ReqAddPush.UID', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Title', full_name='pb.PostOffice.ReqAddPush.Title', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Msg', full_name='pb.PostOffice.ReqAddPush.Msg', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Timestamp', full_name='pb.PostOffice.ReqAddPush.Timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
  serialized_start=162,
  serialized_end=253,
)

_POSTOFFICE_RESPADDPUSH = _descriptor.Descriptor(
  name='RespAddPush',
  full_name='pb.PostOffice.RespAddPush',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ID', full_name='pb.PostOffice.RespAddPush.ID', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=255,
  serialized_end=280,
)

_POSTOFFICE = _descriptor.Descriptor(
  name='PostOffice',
  full_name='pb.PostOffice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_POSTOFFICE_REQ, _POSTOFFICE_RESP, _POSTOFFICE_REQADDPUSH, _POSTOFFICE_RESPADDPUSH, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=280,
)

_POSTOFFICE_REQ.fields_by_name['AddPush'].message_type = _POSTOFFICE_REQADDPUSH
_POSTOFFICE_REQ.containing_type = _POSTOFFICE
_POSTOFFICE_REQ.oneofs_by_name['one'].fields.append(
  _POSTOFFICE_REQ.fields_by_name['AddPush'])
_POSTOFFICE_REQ.fields_by_name['AddPush'].containing_oneof = _POSTOFFICE_REQ.oneofs_by_name['one']
_POSTOFFICE_RESP.fields_by_name['AddPush'].message_type = _POSTOFFICE_RESPADDPUSH
_POSTOFFICE_RESP.containing_type = _POSTOFFICE
_POSTOFFICE_RESP.oneofs_by_name['one'].fields.append(
  _POSTOFFICE_RESP.fields_by_name['AddPush'])
_POSTOFFICE_RESP.fields_by_name['AddPush'].containing_oneof = _POSTOFFICE_RESP.oneofs_by_name['one']
_POSTOFFICE_REQADDPUSH.containing_type = _POSTOFFICE
_POSTOFFICE_RESPADDPUSH.containing_type = _POSTOFFICE
DESCRIPTOR.message_types_by_name['PostOffice'] = _POSTOFFICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostOffice = _reflection.GeneratedProtocolMessageType('PostOffice', (_message.Message,), {

  'Req' : _reflection.GeneratedProtocolMessageType('Req', (_message.Message,), {
    'DESCRIPTOR' : _POSTOFFICE_REQ,
    '__module__' : 'post_office_pb2'
    # @@protoc_insertion_point(class_scope:pb.PostOffice.Req)
    })
  ,

  'Resp' : _reflection.GeneratedProtocolMessageType('Resp', (_message.Message,), {
    'DESCRIPTOR' : _POSTOFFICE_RESP,
    '__module__' : 'post_office_pb2'
    # @@protoc_insertion_point(class_scope:pb.PostOffice.Resp)
    })
  ,

  'ReqAddPush' : _reflection.GeneratedProtocolMessageType('ReqAddPush', (_message.Message,), {
    'DESCRIPTOR' : _POSTOFFICE_REQADDPUSH,
    '__module__' : 'post_office_pb2'
    # @@protoc_insertion_point(class_scope:pb.PostOffice.ReqAddPush)
    })
  ,

  'RespAddPush' : _reflection.GeneratedProtocolMessageType('RespAddPush', (_message.Message,), {
    'DESCRIPTOR' : _POSTOFFICE_RESPADDPUSH,
    '__module__' : 'post_office_pb2'
    # @@protoc_insertion_point(class_scope:pb.PostOffice.RespAddPush)
    })
  ,
  'DESCRIPTOR' : _POSTOFFICE,
  '__module__' : 'post_office_pb2'
  # @@protoc_insertion_point(class_scope:pb.PostOffice)
  })
_sym_db.RegisterMessage(PostOffice)
_sym_db.RegisterMessage(PostOffice.Req)
_sym_db.RegisterMessage(PostOffice.Resp)
_sym_db.RegisterMessage(PostOffice.ReqAddPush)
_sym_db.RegisterMessage(PostOffice.RespAddPush)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
