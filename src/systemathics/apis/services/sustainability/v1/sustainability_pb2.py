# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/sustainability/v1/sustainability.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAsystemathics/apis/services/sustainability/v1/sustainability.proto\x12,systemathics.apis.services.sustainability.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\"e\n\x15SustainabilityRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\"j\n\x16SustainabilityResponse\x12P\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32<.systemathics.apis.services.sustainability.v1.SustainabilityR\x04\x64\x61ta\"\xc4\x01\n\x0eSustainability\x12\x1a\n\x08provider\x18\x01 \x01(\tR\x08provider\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12\x0e\n\x02id\x18\x03 \x01(\tR\x02id\x12\x16\n\x06parent\x18\x04 \x01(\tR\x06parent\x12\x14\n\x05value\x18\x05 \x01(\x01R\x05value\x12\x10\n\x03min\x18\x06 \x01(\x01R\x03min\x12\x10\n\x03max\x18\x07 \x01(\x01R\x03max\x12 \n\x0b\x64\x65scription\x18\x08 \x01(\tR\x0b\x64\x65scription2\xd1\x01\n\x15SustainabilityService\x12\xb7\x01\n\x0eSustainability\x12\x43.systemathics.apis.services.sustainability.v1.SustainabilityRequest\x1a\x44.systemathics.apis.services.sustainability.v1.SustainabilityResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/sustainabilityB\x9c\x02\n0com.systemathics.apis.services.sustainability.v1B\x13SustainabilityProtoP\x01\xa2\x02\x04SASS\xaa\x02,Systemathics.Apis.Services.Sustainability.V1\xca\x02,Systemathics\\Apis\\Services\\Sustainability\\V1\xe2\x02\x38Systemathics\\Apis\\Services\\Sustainability\\V1\\GPBMetadata\xea\x02\x30Systemathics::Apis::Services::Sustainability::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.sustainability.v1.sustainability_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.systemathics.apis.services.sustainability.v1B\023SustainabilityProtoP\001\242\002\004SASS\252\002,Systemathics.Apis.Services.Sustainability.V1\312\002,Systemathics\\Apis\\Services\\Sustainability\\V1\342\0028Systemathics\\Apis\\Services\\Sustainability\\V1\\GPBMetadata\352\0020Systemathics::Apis::Services::Sustainability::V1'
  _globals['_SUSTAINABILITYSERVICE'].methods_by_name['Sustainability']._options = None
  _globals['_SUSTAINABILITYSERVICE'].methods_by_name['Sustainability']._serialized_options = b'\202\323\344\223\002\024\022\022/v1/sustainability'
  _globals['_SUSTAINABILITYREQUEST']._serialized_start=196
  _globals['_SUSTAINABILITYREQUEST']._serialized_end=297
  _globals['_SUSTAINABILITYRESPONSE']._serialized_start=299
  _globals['_SUSTAINABILITYRESPONSE']._serialized_end=405
  _globals['_SUSTAINABILITY']._serialized_start=408
  _globals['_SUSTAINABILITY']._serialized_end=604
  _globals['_SUSTAINABILITYSERVICE']._serialized_start=607
  _globals['_SUSTAINABILITYSERVICE']._serialized_end=816
# @@protoc_insertion_point(module_scope)
