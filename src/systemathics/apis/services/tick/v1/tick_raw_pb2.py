# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick/v1/tick_raw.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import identifier_and_level_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__and__level__pb2
from systemathics.apis.type.shared.v1 import keys_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2
from systemathics.apis.type.shared.v1 import raw_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_raw__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1systemathics/apis/services/tick/v1/tick_raw.proto\x12\"systemathics.apis.services.tick.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a;systemathics/apis/type/shared/v1/identifier_and_level.proto\x1a+systemathics/apis/type/shared/v1/keys.proto\x1a*systemathics/apis/type/shared/v1/raw.proto\"\xb9\x01\n\x0eTickRawRequest\x12V\n\x0bidentifiers\x18\x01 \x03(\x0b\x32\x34.systemathics.apis.type.shared.v1.IdentifierAndLevelR\x0bidentifiers\x12O\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\"\x9b\x01\n\x0fTickRawResponse\x12\x39\n\x03raw\x18\x01 \x01(\x0b\x32%.systemathics.apis.type.shared.v1.RawH\x00R\x03raw\x12\x42\n\x07mapping\x18\x02 \x01(\x0b\x32&.systemathics.apis.type.shared.v1.KeysH\x00R\x07mappingB\t\n\x07payload2\x9d\x01\n\x0eTickRawService\x12\x8a\x01\n\x07TickRaw\x12\x32.systemathics.apis.services.tick.v1.TickRawRequest\x1a\x33.systemathics.apis.services.tick.v1.TickRawResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/tick/raw0\x01\x42\xe3\x01\n&com.systemathics.apis.services.tick.v1B\x0cTickRawProtoP\x01\xa2\x02\x04SAST\xaa\x02\"Systemathics.Apis.Services.Tick.V1\xca\x02\"Systemathics\\Apis\\Services\\Tick\\V1\xe2\x02.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\xea\x02&Systemathics::Apis::Services::Tick::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick.v1.tick_raw_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.systemathics.apis.services.tick.v1B\014TickRawProtoP\001\242\002\004SAST\252\002\"Systemathics.Apis.Services.Tick.V1\312\002\"Systemathics\\Apis\\Services\\Tick\\V1\342\002.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\352\002&Systemathics::Apis::Services::Tick::V1'
  _globals['_TICKRAWSERVICE'].methods_by_name['TickRaw']._options = None
  _globals['_TICKRAWSERVICE'].methods_by_name['TickRaw']._serialized_options = b'\202\323\344\223\002\016\022\014/v1/tick/raw'
  _globals['_TICKRAWREQUEST']._serialized_start=322
  _globals['_TICKRAWREQUEST']._serialized_end=507
  _globals['_TICKRAWRESPONSE']._serialized_start=510
  _globals['_TICKRAWRESPONSE']._serialized_end=665
  _globals['_TICKRAWSERVICE']._serialized_start=668
  _globals['_TICKRAWSERVICE']._serialized_end=825
# @@protoc_insertion_point(module_scope)
