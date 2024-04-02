# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick_analytics/v1/tick_priips.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>systemathics/apis/services/tick_analytics/v1/tick_priips.proto\x12,systemathics.apis.services.tick_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1agoogle/type/datetime.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\"\x9b\x04\n\x11TickPriipsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x34\n\norder_time\x18\x02 \x01(\x0b\x32\x15.google.type.DateTimeR\torderTime\x12<\n\x0e\x65xecution_time\x18\x03 \x01(\x0b\x32\x15.google.type.DateTimeR\rexecutionTime\x12\'\n\x0f\x65xecution_price\x18\x04 \x01(\x01R\x0e\x65xecutionPrice\x12O\n\x05\x66ield\x18\x05 \x01(\x0e\x32\x39.systemathics.apis.services.tick_analytics.v1.PriipsPriceR\x05\x66ield\x12\x33\n\x07latency\x18\x06 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07latency\x12\x16\n\x06\x61\x63\x63\x65pt\x18\x07 \x03(\tR\x06\x61\x63\x63\x65pt\x12\x16\n\x06reject\x18\x08 \x03(\tR\x06reject\x12\x18\n\x07metrics\x18\t \x01(\x08R\x07metrics\x12K\n\"use_reverse_iteration_optimization\x18\n \x01(\x08R\x1fuseReverseIterationOptimization\"\xce\x0e\n\x12TickPriipsResponse\x12=\n\x0c\x61rrival_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x0b\x61rrivalTime\x12\x41\n\rarrival_price\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x0c\x61rrivalPrice\x12?\n\x0c\x61rrival_cost\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x0b\x61rrivalCost\x12\x37\n\topen_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\x08openTime\x12\x39\n\nclose_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcloseTime\x12\x39\n\norder_time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\torderTime\x12\x41\n\x0e\x65xecution_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\rexecutionTime\x12\x33\n\x07latency\x18\x08 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07latency\x12\'\n\x0f\x65xecution_price\x18\t \x01(\x01R\x0e\x65xecutionPrice\x12\x31\n\x05\x63ount\x18\n \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x05\x63ount\x12;\n\nopen_price\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\topenPrice\x12;\n\nhigh_price\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\thighPrice\x12\x39\n\tlow_price\x18\r \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x08lowPrice\x12=\n\x0b\x63lose_price\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\nclosePrice\x12\x30\n\x04vwap\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x04vwap\x12\x33\n\x06volume\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x06volume\x12\x18\n\x07message\x18\x11 \x01(\tR\x07message\x12@\n\x0e\x61rrival_period\x18\x12 \x01(\x0b\x32\x19.google.protobuf.DurationR\rarrivalPeriod\x12@\n\x0eworking_period\x18\x13 \x01(\x0b\x32\x19.google.protobuf.DurationR\rworkingPeriod\x12@\n\x0e\x63losing_period\x18\x14 \x01(\x0b\x32\x19.google.protobuf.DurationR\rclosingPeriod\x12@\n\x0eopening_period\x18\x15 \x01(\x0b\x32\x19.google.protobuf.DurationR\ropeningPeriod\x12\x39\n\ncross_time\x18\x16 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcrossTime\x12>\n\x0cupper_volume\x18\x17 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0bupperVolume\x12>\n\x0clower_volume\x18\x18 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0blowerVolume\x12>\n\x0c\x65qual_volume\x18\x19 \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\x0b\x65qualVolume\x12<\n\x0bupper_count\x18\x1a \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\nupperCount\x12<\n\x0blower_count\x18\x1b \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\nlowerCount\x12<\n\x0b\x65qual_count\x18\x1c \x01(\x0b\x32\x1b.google.protobuf.Int64ValueR\nequalCount\x12\x1e\n\nconditions\x18\x1d \x03(\tR\nconditions\x12)\n\x10upper_conditions\x18\x1e \x03(\tR\x0fupperConditions\x12)\n\x10lower_conditions\x18\x1f \x03(\tR\x0flowerConditions\x12)\n\x10\x65qual_conditions\x18  \x03(\tR\x0f\x65qualConditions\x12\x1f\n\x0bticks_count\x18! \x01(\x03R\nticksCount*o\n\x0bPriipsPrice\x12\x1c\n\x18PRIIPS_PRICE_UNSPECIFIED\x10\x00\x12\x16\n\x12PRIIPS_PRICE_TRADE\x10\x01\x12\x14\n\x10PRIIPS_PRICE_BID\x10\x02\x12\x14\n\x10PRIIPS_PRICE_ASK\x10\x03\x32\xc8\x01\n\x11TickPriipsService\x12\xb2\x01\n\nTickPriips\x12?.systemathics.apis.services.tick_analytics.v1.TickPriipsRequest\x1a@.systemathics.apis.services.tick_analytics.v1.TickPriipsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/v1/tick-analytics/priipsB\x94\x02\n0com.systemathics.apis.services.tick_analytics.v1B\x0fTickPriipsProtoP\x01\xa2\x02\x04SAST\xaa\x02+Systemathics.Apis.Services.TickAnalytics.V1\xca\x02+Systemathics\\Apis\\Services\\TickAnalytics\\V1\xe2\x02\x37Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\xea\x02/Systemathics::Apis::Services::TickAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick_analytics.v1.tick_priips_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.systemathics.apis.services.tick_analytics.v1B\017TickPriipsProtoP\001\242\002\004SAST\252\002+Systemathics.Apis.Services.TickAnalytics.V1\312\002+Systemathics\\Apis\\Services\\TickAnalytics\\V1\342\0027Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\352\002/Systemathics::Apis::Services::TickAnalytics::V1'
  _globals['_TICKPRIIPSSERVICE'].methods_by_name['TickPriips']._loaded_options = None
  _globals['_TICKPRIIPSSERVICE'].methods_by_name['TickPriips']._serialized_options = b'\202\323\344\223\002\033\022\031/v1/tick-analytics/priips'
  _globals['_PRIIPSPRICE']._serialized_start=2733
  _globals['_PRIIPSPRICE']._serialized_end=2844
  _globals['_TICKPRIIPSREQUEST']._serialized_start=319
  _globals['_TICKPRIIPSREQUEST']._serialized_end=858
  _globals['_TICKPRIIPSRESPONSE']._serialized_start=861
  _globals['_TICKPRIIPSRESPONSE']._serialized_end=2731
  _globals['_TICKPRIIPSSERVICE']._serialized_start=2847
  _globals['_TICKPRIIPSSERVICE']._serialized_end=3047
# @@protoc_insertion_point(module_scope)
