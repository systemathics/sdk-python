# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick/v1/tick_trades_and_book.proto
# Protobuf Python Version: 4.25.0
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
from systemathics.apis.type.shared.v1 import identifier_and_level_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__and__level__pb2
from systemathics.apis.type.shared.v1 import keys_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2
from systemathics.apis.type.shared.v1 import book_updates_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_book__updates__pb2
from systemathics.apis.type.shared.v1 import trade_and_book_data_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_trade__and__book__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=systemathics/apis/services/tick/v1/tick_trades_and_book.proto\x12\"systemathics.apis.services.tick.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a;systemathics/apis/type/shared/v1/identifier_and_level.proto\x1a+systemathics/apis/type/shared/v1/keys.proto\x1a\x33systemathics/apis/type/shared/v1/book_updates.proto\x1a:systemathics/apis/type/shared/v1/trade_and_book_data.proto\"\x93\x03\n\x18TickTradesAndBookRequest\x12V\n\x0bidentifiers\x18\x01 \x03(\x0b\x32\x34.systemathics.apis.type.shared.v1.IdentifierAndLevelR\x0bidentifiers\x12P\n\x0c\x62ook_updates\x18\x02 \x01(\x0e\x32-.systemathics.apis.type.shared.v1.BookUpdatesR\x0b\x62ookUpdates\x12O\n\x0b\x63onstraints\x18\x03 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\x12\x38\n\tmax_depth\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x08maxDepth\x12\"\n\x0c\x63ontributors\x18\x06 \x01(\x08R\x0c\x63ontributors\"\xb4\x01\n\x19TickTradesAndBookResponse\x12H\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x32.systemathics.apis.type.shared.v1.TradeAndBookDataH\x00R\x04\x64\x61ta\x12\x42\n\x07mapping\x18\x02 \x01(\x0b\x32&.systemathics.apis.type.shared.v1.KeysH\x00R\x07mappingB\t\n\x07payload2\xd1\x01\n\x18TickTradesAndBookService\x12\xb4\x01\n\x11TickTradesAndBook\x12<.systemathics.apis.services.tick.v1.TickTradesAndBookRequest\x1a=.systemathics.apis.services.tick.v1.TickTradesAndBookResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/tick/trades-and-book0\x01\x42\xed\x01\n&com.systemathics.apis.services.tick.v1B\x16TickTradesAndBookProtoP\x01\xa2\x02\x04SAST\xaa\x02\"Systemathics.Apis.Services.Tick.V1\xca\x02\"Systemathics\\Apis\\Services\\Tick\\V1\xe2\x02.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\xea\x02&Systemathics::Apis::Services::Tick::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick.v1.tick_trades_and_book_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.systemathics.apis.services.tick.v1B\026TickTradesAndBookProtoP\001\242\002\004SAST\252\002\"Systemathics.Apis.Services.Tick.V1\312\002\"Systemathics\\Apis\\Services\\Tick\\V1\342\002.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\352\002&Systemathics::Apis::Services::Tick::V1'
  _globals['_TICKTRADESANDBOOKSERVICE'].methods_by_name['TickTradesAndBook']._options = None
  _globals['_TICKTRADESANDBOOKSERVICE'].methods_by_name['TickTradesAndBook']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/tick/trades-and-book'
  _globals['_TICKTRADESANDBOOKREQUEST']._serialized_start=435
  _globals['_TICKTRADESANDBOOKREQUEST']._serialized_end=838
  _globals['_TICKTRADESANDBOOKRESPONSE']._serialized_start=841
  _globals['_TICKTRADESANDBOOKRESPONSE']._serialized_end=1021
  _globals['_TICKTRADESANDBOOKSERVICE']._serialized_start=1024
  _globals['_TICKTRADESANDBOOKSERVICE']._serialized_end=1233
# @@protoc_insertion_point(module_scope)