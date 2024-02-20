# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick/v1/tick_book.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import keys_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2
from systemathics.apis.type.shared.v1 import book_updates_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_book__updates__pb2
from systemathics.apis.type.shared.v1 import book_data_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_book__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2systemathics/apis/services/tick/v1/tick_book.proto\x12\"systemathics.apis.services.tick.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a+systemathics/apis/type/shared/v1/keys.proto\x1a\x33systemathics/apis/type/shared/v1/book_updates.proto\x1a\x30systemathics/apis/type/shared/v1/book_data.proto\"\x82\x03\n\x0fTickBookRequest\x12N\n\x0bidentifiers\x18\x01 \x03(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\x0bidentifiers\x12P\n\x0c\x62ook_updates\x18\x02 \x01(\x0e\x32-.systemathics.apis.type.shared.v1.BookUpdatesR\x0b\x62ookUpdates\x12O\n\x0b\x63onstraints\x18\x03 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\x12\x38\n\tmax_depth\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x08maxDepth\x12\"\n\x0c\x63ontributors\x18\x06 \x01(\x08R\x0c\x63ontributors\"\xa3\x01\n\x10TickBookResponse\x12@\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32*.systemathics.apis.type.shared.v1.BookDataH\x00R\x04\x64\x61ta\x12\x42\n\x07mapping\x18\x02 \x01(\x0b\x32&.systemathics.apis.type.shared.v1.KeysH\x00R\x07mappingB\t\n\x07payload2\xa2\x01\n\x0fTickBookService\x12\x8e\x01\n\x08TickBook\x12\x33.systemathics.apis.services.tick.v1.TickBookRequest\x1a\x34.systemathics.apis.services.tick.v1.TickBookResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/v1/tick/book0\x01\x42\xe4\x01\n&com.systemathics.apis.services.tick.v1B\rTickBookProtoP\x01\xa2\x02\x04SAST\xaa\x02\"Systemathics.Apis.Services.Tick.V1\xca\x02\"Systemathics\\Apis\\Services\\Tick\\V1\xe2\x02.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\xea\x02&Systemathics::Apis::Services::Tick::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick.v1.tick_book_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.systemathics.apis.services.tick.v1B\rTickBookProtoP\001\242\002\004SAST\252\002\"Systemathics.Apis.Services.Tick.V1\312\002\"Systemathics\\Apis\\Services\\Tick\\V1\342\002.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\352\002&Systemathics::Apis::Services::Tick::V1'
  _globals['_TICKBOOKSERVICE'].methods_by_name['TickBook']._options = None
  _globals['_TICKBOOKSERVICE'].methods_by_name['TickBook']._serialized_options = b'\202\323\344\223\002\017\022\r/v1/tick/book'
  _globals['_TICKBOOKREQUEST']._serialized_start=404
  _globals['_TICKBOOKREQUEST']._serialized_end=790
  _globals['_TICKBOOKRESPONSE']._serialized_start=793
  _globals['_TICKBOOKRESPONSE']._serialized_end=956
  _globals['_TICKBOOKSERVICE']._serialized_start=959
  _globals['_TICKBOOKSERVICE']._serialized_end=1121
# @@protoc_insertion_point(module_scope)
