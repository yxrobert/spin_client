# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fb.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fb.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\004.;pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x08\x66\x62.proto\x12\x02pb\"L\n\x02\x46\x42\x1a\x07\n\x05\x46\x42Req\x1a\x07\n\x05\x46\x42Rsp\x1a\x0b\n\tFBBindReq\x1a\'\n\tFBBindRsp\x12\x0c\n\x04\x63oin\x18\x01 \x01(\x04\x12\x0c\n\x04\x62ind\x18\x02 \x01(\rB\x06Z\x04.;pbb\x06proto3'
)




_FB_FBREQ = _descriptor.Descriptor(
  name='FBReq',
  full_name='pb.FB.FBReq',
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
  serialized_start=22,
  serialized_end=29,
)

_FB_FBRSP = _descriptor.Descriptor(
  name='FBRsp',
  full_name='pb.FB.FBRsp',
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
  serialized_start=31,
  serialized_end=38,
)

_FB_FBBINDREQ = _descriptor.Descriptor(
  name='FBBindReq',
  full_name='pb.FB.FBBindReq',
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
  serialized_start=40,
  serialized_end=51,
)

_FB_FBBINDRSP = _descriptor.Descriptor(
  name='FBBindRsp',
  full_name='pb.FB.FBBindRsp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='coin', full_name='pb.FB.FBBindRsp.coin', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bind', full_name='pb.FB.FBBindRsp.bind', index=1,
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
  serialized_start=53,
  serialized_end=92,
)

_FB = _descriptor.Descriptor(
  name='FB',
  full_name='pb.FB',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[_FB_FBREQ, _FB_FBRSP, _FB_FBBINDREQ, _FB_FBBINDRSP, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=92,
)

_FB_FBREQ.containing_type = _FB
_FB_FBRSP.containing_type = _FB
_FB_FBBINDREQ.containing_type = _FB
_FB_FBBINDRSP.containing_type = _FB
DESCRIPTOR.message_types_by_name['FB'] = _FB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FB = _reflection.GeneratedProtocolMessageType('FB', (_message.Message,), {

  'FBReq' : _reflection.GeneratedProtocolMessageType('FBReq', (_message.Message,), {
    'DESCRIPTOR' : _FB_FBREQ,
    '__module__' : 'fb_pb2'
    # @@protoc_insertion_point(class_scope:pb.FB.FBReq)
    })
  ,

  'FBRsp' : _reflection.GeneratedProtocolMessageType('FBRsp', (_message.Message,), {
    'DESCRIPTOR' : _FB_FBRSP,
    '__module__' : 'fb_pb2'
    # @@protoc_insertion_point(class_scope:pb.FB.FBRsp)
    })
  ,

  'FBBindReq' : _reflection.GeneratedProtocolMessageType('FBBindReq', (_message.Message,), {
    'DESCRIPTOR' : _FB_FBBINDREQ,
    '__module__' : 'fb_pb2'
    # @@protoc_insertion_point(class_scope:pb.FB.FBBindReq)
    })
  ,

  'FBBindRsp' : _reflection.GeneratedProtocolMessageType('FBBindRsp', (_message.Message,), {
    'DESCRIPTOR' : _FB_FBBINDRSP,
    '__module__' : 'fb_pb2'
    # @@protoc_insertion_point(class_scope:pb.FB.FBBindRsp)
    })
  ,
  'DESCRIPTOR' : _FB,
  '__module__' : 'fb_pb2'
  # @@protoc_insertion_point(class_scope:pb.FB)
  })
_sym_db.RegisterMessage(FB)
_sym_db.RegisterMessage(FB.FBReq)
_sym_db.RegisterMessage(FB.FBRsp)
_sym_db.RegisterMessage(FB.FBBindReq)
_sym_db.RegisterMessage(FB.FBBindRsp)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
