# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick_conditions/v1/tick_conditions.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import condition_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_condition__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCsystemathics/apis/services/tick_conditions/v1/tick_conditions.proto\x12-systemathics.apis.services.tick_conditions.v1\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x30systemathics/apis/type/shared/v1/condition.proto\"\xa8\x01\n\x15TickConditionsRequest\x12N\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierH\x00R\nidentifier\x12\x1c\n\x08\x65xchange\x18\x02 \x01(\tH\x00R\x08\x65xchange\x12\x18\n\x06source\x18\x03 \x01(\x05H\x00R\x06sourceB\x07\n\x05value\"Y\n\x16TickConditionsResponse\x12?\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32+.systemathics.apis.type.shared.v1.ConditionR\x04\x64\x61ta2\xb7\x01\n\x15TickConditionsService\x12\x9d\x01\n\x0eTickConditions\x12\x44.systemathics.apis.services.tick_conditions.v1.TickConditionsRequest\x1a\x45.systemathics.apis.services.tick_conditions.v1.TickConditionsResponseB\x9d\x02\n1com.systemathics.apis.services.tick_conditions.v1B\x13TickConditionsProtoP\x01\xa2\x02\x04SAST\xaa\x02,Systemathics.Apis.Services.TickConditions.V1\xca\x02,Systemathics\\Apis\\Services\\TickConditions\\V1\xe2\x02\x38Systemathics\\Apis\\Services\\TickConditions\\V1\\GPBMetadata\xea\x02\x30Systemathics::Apis::Services::TickConditions::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick_conditions.v1.tick_conditions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1com.systemathics.apis.services.tick_conditions.v1B\023TickConditionsProtoP\001\242\002\004SAST\252\002,Systemathics.Apis.Services.TickConditions.V1\312\002,Systemathics\\Apis\\Services\\TickConditions\\V1\342\0028Systemathics\\Apis\\Services\\TickConditions\\V1\\GPBMetadata\352\0020Systemathics::Apis::Services::TickConditions::V1'
  _globals['_TICKCONDITIONSREQUEST']._serialized_start=220
  _globals['_TICKCONDITIONSREQUEST']._serialized_end=388
  _globals['_TICKCONDITIONSRESPONSE']._serialized_start=390
  _globals['_TICKCONDITIONSRESPONSE']._serialized_end=479
  _globals['_TICKCONDITIONSSERVICE']._serialized_start=482
  _globals['_TICKCONDITIONSSERVICE']._serialized_end=665
# @@protoc_insertion_point(module_scope)
