# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick_analytics/v1/tick_trade_condition_statistics.proto
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
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nRsystemathics/apis/services/tick_analytics/v1/tick_trade_condition_statistics.proto\x12,systemathics.apis.services.tick_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\"\xc4\x01\n#TickTradeConditionStatisticsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12O\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\"\xf0\x01\n$TickTradeConditionStatisticsResponse\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value\x12\x14\n\x05\x63ount\x18\x02 \x01(\x03R\x05\x63ount\x12\x14\n\x05total\x18\x03 \x01(\x03R\x05total\x12\x1e\n\npercentage\x18\x04 \x01(\x01R\npercentage\x12\x16\n\x06volume\x18\x05 \x01(\x03R\x06volume\x12!\n\x0ctotal_volume\x18\x06 \x01(\x03R\x0btotalVolume\x12+\n\x11volume_percentage\x18\x07 \x01(\x01R\x10volumePercentage2\xa6\x02\n#TickTradeConditionStatisticsService\x12\xfe\x01\n\x1cTickTradeConditionStatistics\x12Q.systemathics.apis.services.tick_analytics.v1.TickTradeConditionStatisticsRequest\x1aR.systemathics.apis.services.tick_analytics.v1.TickTradeConditionStatisticsResponse\"5\x82\xd3\xe4\x93\x02/\x12-/v1/tick-analytics/trade-condition-statistics0\x01\x42\xa6\x02\n0com.systemathics.apis.services.tick_analytics.v1B!TickTradeConditionStatisticsProtoP\x01\xa2\x02\x04SAST\xaa\x02+Systemathics.Apis.Services.TickAnalytics.V1\xca\x02+Systemathics\\Apis\\Services\\TickAnalytics\\V1\xe2\x02\x37Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\xea\x02/Systemathics::Apis::Services::TickAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick_analytics.v1.tick_trade_condition_statistics_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.systemathics.apis.services.tick_analytics.v1B!TickTradeConditionStatisticsProtoP\001\242\002\004SAST\252\002+Systemathics.Apis.Services.TickAnalytics.V1\312\002+Systemathics\\Apis\\Services\\TickAnalytics\\V1\342\0027Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\352\002/Systemathics::Apis::Services::TickAnalytics::V1'
  _globals['_TICKTRADECONDITIONSTATISTICSSERVICE'].methods_by_name['TickTradeConditionStatistics']._options = None
  _globals['_TICKTRADECONDITIONSTATISTICSSERVICE'].methods_by_name['TickTradeConditionStatistics']._serialized_options = b'\202\323\344\223\002/\022-/v1/tick-analytics/trade-condition-statistics'
  _globals['_TICKTRADECONDITIONSTATISTICSREQUEST']._serialized_start=266
  _globals['_TICKTRADECONDITIONSTATISTICSREQUEST']._serialized_end=462
  _globals['_TICKTRADECONDITIONSTATISTICSRESPONSE']._serialized_start=465
  _globals['_TICKTRADECONDITIONSTATISTICSRESPONSE']._serialized_end=705
  _globals['_TICKTRADECONDITIONSTATISTICSSERVICE']._serialized_start=708
  _globals['_TICKTRADECONDITIONSTATISTICSSERVICE']._serialized_end=1002
# @@protoc_insertion_point(module_scope)
