# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick_analytics/v1/tick_ema.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;systemathics/apis/services/tick_analytics/v1/tick_ema.proto\x12,systemathics.apis.services.tick_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\"\x82\x04\n\x0eTickEmaRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12O\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\x12L\n\x05\x66ield\x18\x03 \x01(\x0e\x32\x36.systemathics.apis.services.tick_analytics.v1.EmaPriceR\x05\x66ield\x12\x16\n\x06length\x18\x04 \x01(\x05R\x06length\x12\x31\n\x06period\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06period\x12\x31\n\x06offset\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06offset\x12\x35\n\x08sampling\x18\x07 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08sampling\x12\x1e\n\nadjustment\x18\x08 \x01(\x08R\nadjustment\x12\x16\n\x06\x61\x63\x63\x65pt\x18\t \x03(\tR\x06\x61\x63\x63\x65pt\x12\x16\n\x06reject\x18\n \x03(\tR\x06reject\"\x9a\x01\n\x0fTickEmaResponse\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x36\n\x07\x61verage\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x07\x61verage*`\n\x08\x45maPrice\x12\x19\n\x15\x45MA_PRICE_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x45MA_PRICE_TRADE\x10\x01\x12\x11\n\rEMA_PRICE_BID\x10\x02\x12\x11\n\rEMA_PRICE_ASK\x10\x03\x32\xbb\x01\n\x0eTickEmaService\x12\xa8\x01\n\x07TickEma\x12<.systemathics.apis.services.tick_analytics.v1.TickEmaRequest\x1a=.systemathics.apis.services.tick_analytics.v1.TickEmaResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/tick-analytics/ema0\x01\x42\x91\x02\n0com.systemathics.apis.services.tick_analytics.v1B\x0cTickEmaProtoP\x01\xa2\x02\x04SAST\xaa\x02+Systemathics.Apis.Services.TickAnalytics.V1\xca\x02+Systemathics\\Apis\\Services\\TickAnalytics\\V1\xe2\x02\x37Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\xea\x02/Systemathics::Apis::Services::TickAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick_analytics.v1.tick_ema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.systemathics.apis.services.tick_analytics.v1B\014TickEmaProtoP\001\242\002\004SAST\252\002+Systemathics.Apis.Services.TickAnalytics.V1\312\002+Systemathics\\Apis\\Services\\TickAnalytics\\V1\342\0027Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\352\002/Systemathics::Apis::Services::TickAnalytics::V1'
  _globals['_TICKEMASERVICE'].methods_by_name['TickEma']._options = None
  _globals['_TICKEMASERVICE'].methods_by_name['TickEma']._serialized_options = b'\202\323\344\223\002\030\022\026/v1/tick-analytics/ema'
  _globals['_EMAPRICE']._serialized_start=1013
  _globals['_EMAPRICE']._serialized_end=1109
  _globals['_TICKEMAREQUEST']._serialized_start=340
  _globals['_TICKEMAREQUEST']._serialized_end=854
  _globals['_TICKEMARESPONSE']._serialized_start=857
  _globals['_TICKEMARESPONSE']._serialized_end=1011
  _globals['_TICKEMASERVICE']._serialized_start=1112
  _globals['_TICKEMASERVICE']._serialized_end=1299
# @@protoc_insertion_point(module_scope)