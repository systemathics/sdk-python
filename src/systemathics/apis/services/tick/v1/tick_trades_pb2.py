# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick/v1/tick_trades.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import keys_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2
from systemathics.apis.type.shared.v1 import trade_data_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_trade__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4systemathics/apis/services/tick/v1/tick_trades.proto\x12\"systemathics.apis.services.tick.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a+systemathics/apis/type/shared/v1/keys.proto\x1a\x31systemathics/apis/type/shared/v1/trade_data.proto\"\xd4\x01\n\x11TickTradesRequest\x12N\n\x0bidentifiers\x18\x01 \x03(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\x0bidentifiers\x12O\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\x12\x1e\n\nadjustment\x18\x03 \x01(\x08R\nadjustment\"\xa6\x01\n\x12TickTradesResponse\x12\x41\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32+.systemathics.apis.type.shared.v1.TradeDataH\x00R\x04\x64\x61ta\x12\x42\n\x07mapping\x18\x02 \x01(\x0b\x32&.systemathics.apis.type.shared.v1.KeysH\x00R\x07mappingB\t\n\x07payload2\xac\x01\n\x11TickTradesService\x12\x96\x01\n\nTickTrades\x12\x35.systemathics.apis.services.tick.v1.TickTradesRequest\x1a\x36.systemathics.apis.services.tick.v1.TickTradesResponse\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0f/v1/tick/trades0\x01\x42\xe6\x01\n&com.systemathics.apis.services.tick.v1B\x0fTickTradesProtoP\x01\xa2\x02\x04SAST\xaa\x02\"Systemathics.Apis.Services.Tick.V1\xca\x02\"Systemathics\\Apis\\Services\\Tick\\V1\xe2\x02.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\xea\x02&Systemathics::Apis::Services::Tick::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick.v1.tick_trades_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.systemathics.apis.services.tick.v1B\017TickTradesProtoP\001\242\002\004SAST\252\002\"Systemathics.Apis.Services.Tick.V1\312\002\"Systemathics\\Apis\\Services\\Tick\\V1\342\002.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\352\002&Systemathics::Apis::Services::Tick::V1'
  _globals['_TICKTRADESSERVICE'].methods_by_name['TickTrades']._options = None
  _globals['_TICKTRADESSERVICE'].methods_by_name['TickTrades']._serialized_options = b'\202\323\344\223\002\021\022\017/v1/tick/trades'
  _globals['_TICKTRADESREQUEST']._serialized_start=322
  _globals['_TICKTRADESREQUEST']._serialized_end=534
  _globals['_TICKTRADESRESPONSE']._serialized_start=537
  _globals['_TICKTRADESRESPONSE']._serialized_end=703
  _globals['_TICKTRADESSERVICE']._serialized_start=706
  _globals['_TICKTRADESSERVICE']._serialized_end=878
# @@protoc_insertion_point(module_scope)
