# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/type/shared/v1/mappings.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import memo_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_memo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/systemathics/apis/type/shared/v1/mappings.proto\x12 systemathics.apis.type.shared.v1\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a+systemathics/apis/type/shared/v1/memo.proto\"\xb6\x01\n\x07Mapping\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12:\n\x04memo\x18\x02 \x01(\x0b\x32&.systemathics.apis.type.shared.v1.MemoR\x04memo\x12!\n\x0c\x65vent_source\x18\x03 \x01(\rR\x0b\x65ventSource\"K\n\x08Mappings\x12?\n\x05table\x18\x01 \x03(\x0b\x32).systemathics.apis.type.shared.v1.MappingR\x05tableB\xda\x01\n$com.systemathics.apis.type.shared.v1B\rMappingsProtoP\x01\xa2\x02\x04SATS\xaa\x02 Systemathics.Apis.Type.Shared.V1\xca\x02 Systemathics\\Apis\\Type\\Shared\\V1\xe2\x02,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\xea\x02$Systemathics::Apis::Type::Shared::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.type.shared.v1.mappings_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.systemathics.apis.type.shared.v1B\rMappingsProtoP\001\242\002\004SATS\252\002 Systemathics.Apis.Type.Shared.V1\312\002 Systemathics\\Apis\\Type\\Shared\\V1\342\002,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\352\002$Systemathics::Apis::Type::Shared::V1'
  _globals['_MAPPING']._serialized_start=182
  _globals['_MAPPING']._serialized_end=364
  _globals['_MAPPINGS']._serialized_start=366
  _globals['_MAPPINGS']._serialized_end=441
# @@protoc_insertion_point(module_scope)
