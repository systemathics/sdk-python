# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick_analytics/v1/tick_trade_conditions.proto
# Protobuf Python Version: 5.26.1
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
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import condition_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_condition__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHsystemathics/apis/services/tick_analytics/v1/tick_trade_conditions.proto\x12,systemathics.apis.services.tick_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x30systemathics/apis/type/shared/v1/condition.proto\"\xd8\x02\n\x1aTickTradeConditionsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12O\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\x12\x35\n\x08sampling\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x08sampling\x12\x31\n\x06period\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06period\x12\x31\n\x06offset\x18\x05 \x01(\x0b\x32\x19.google.protobuf.DurationR\x06offset\"\xaf\x02\n\x1bTickTradeConditionsResponse\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x16\n\x06volume\x18\x02 \x01(\x03R\x06volume\x12\x14\n\x05\x63ount\x18\x03 \x01(\x03R\x05\x63ount\x12M\n\x0b\x64\x65scription\x18\x04 \x03(\x0b\x32+.systemathics.apis.type.shared.v1.ConditionR\x0b\x64\x65scription\x12X\n\x04\x64\x61ta\x18\x05 \x03(\x0b\x32\x44.systemathics.apis.services.tick_analytics.v1.TickTradeConditionDataR\x04\x64\x61ta\"\xa9\x01\n\x16TickTradeConditionData\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x14\n\x05\x63ount\x18\x02 \x01(\x03R\x05\x63ount\x12\x1e\n\npercentage\x18\x03 \x01(\x01R\npercentage\x12\x16\n\x06volume\x18\x04 \x01(\x03R\x06volume\x12+\n\x11volume_percentage\x18\x05 \x01(\x01R\x10volumePercentage2\xf8\x01\n\x1aTickTradeConditionsService\x12\xd9\x01\n\x13TickTradeConditions\x12H.systemathics.apis.services.tick_analytics.v1.TickTradeConditionsRequest\x1aI.systemathics.apis.services.tick_analytics.v1.TickTradeConditionsResponse\"+\x82\xd3\xe4\x93\x02%\x12#/v1/tick-analytics/trade-conditions0\x01\x42\x9d\x02\n0com.systemathics.apis.services.tick_analytics.v1B\x18TickTradeConditionsProtoP\x01\xa2\x02\x04SAST\xaa\x02+Systemathics.Apis.Services.TickAnalytics.V1\xca\x02+Systemathics\\Apis\\Services\\TickAnalytics\\V1\xe2\x02\x37Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\xea\x02/Systemathics::Apis::Services::TickAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick_analytics.v1.tick_trade_conditions_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.systemathics.apis.services.tick_analytics.v1B\030TickTradeConditionsProtoP\001\242\002\004SAST\252\002+Systemathics.Apis.Services.TickAnalytics.V1\312\002+Systemathics\\Apis\\Services\\TickAnalytics\\V1\342\0027Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\352\002/Systemathics::Apis::Services::TickAnalytics::V1'
  _globals['_TICKTRADECONDITIONSSERVICE'].methods_by_name['TickTradeConditions']._loaded_options = None
  _globals['_TICKTRADECONDITIONSSERVICE'].methods_by_name['TickTradeConditions']._serialized_options = b'\202\323\344\223\002%\022#/v1/tick-analytics/trade-conditions'
  _globals['_TICKTRADECONDITIONSREQUEST']._serialized_start=371
  _globals['_TICKTRADECONDITIONSREQUEST']._serialized_end=715
  _globals['_TICKTRADECONDITIONSRESPONSE']._serialized_start=718
  _globals['_TICKTRADECONDITIONSRESPONSE']._serialized_end=1021
  _globals['_TICKTRADECONDITIONDATA']._serialized_start=1024
  _globals['_TICKTRADECONDITIONDATA']._serialized_end=1193
  _globals['_TICKTRADECONDITIONSSERVICE']._serialized_start=1196
  _globals['_TICKTRADECONDITIONSSERVICE']._serialized_end=1444
# @@protoc_insertion_point(module_scope)
