# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/intraday_analytics/v1/intraday_macd.proto
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
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2
from systemathics.apis.type.shared.v1 import sampling_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_sampling__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDsystemathics/apis/services/intraday_analytics/v1/intraday_macd.proto\x12\x30systemathics.apis.services.intraday_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\xca\x02\n\x13IntradayMacdRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12S\n\rdate_interval\x18\x03 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x12\n\x04long\x18\x04 \x01(\x05R\x04long\x12\x14\n\x05short\x18\x05 \x01(\x05R\x05short\x12\x1e\n\nadjustment\x18\x06 \x01(\x08R\nadjustment\"n\n\x14IntradayMacdResponse\x12V\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x42.systemathics.apis.services.intraday_analytics.v1.IntradayMacdDataR\x04\x64\x61ta\"\xa1\x01\n\x10IntradayMacdData\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x12\n\x04macd\x18\x03 \x01(\x01R\x04macd\x12\x14\n\x05short\x18\x04 \x01(\x01R\x05short\x12\x12\n\x04long\x18\x05 \x01(\x01R\x04long2\xd0\x01\n\x13IntradayMacdService\x12\xb8\x01\n\x0cIntradayMacd\x12\x45.systemathics.apis.services.intraday_analytics.v1.IntradayMacdRequest\x1a\x46.systemathics.apis.services.intraday_analytics.v1.IntradayMacdResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/intraday/macdB\xaa\x02\n4com.systemathics.apis.services.intraday_analytics.v1B\x11IntradayMacdProtoP\x01\xa2\x02\x04SASI\xaa\x02/Systemathics.Apis.Services.IntradayAnalytics.V1\xca\x02/Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\xe2\x02;Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\\GPBMetadata\xea\x02\x33Systemathics::Apis::Services::IntradayAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday_analytics.v1.intraday_macd_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n4com.systemathics.apis.services.intraday_analytics.v1B\021IntradayMacdProtoP\001\242\002\004SASI\252\002/Systemathics.Apis.Services.IntradayAnalytics.V1\312\002/Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\342\002;Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\\GPBMetadata\352\0023Systemathics::Apis::Services::IntradayAnalytics::V1'
  _globals['_INTRADAYMACDSERVICE'].methods_by_name['IntradayMacd']._options = None
  _globals['_INTRADAYMACDSERVICE'].methods_by_name['IntradayMacd']._serialized_options = b'\202\323\344\223\002\023\022\021/v1/intraday/macd'
  _globals['_INTRADAYMACDREQUEST']._serialized_start=340
  _globals['_INTRADAYMACDREQUEST']._serialized_end=670
  _globals['_INTRADAYMACDRESPONSE']._serialized_start=672
  _globals['_INTRADAYMACDRESPONSE']._serialized_end=782
  _globals['_INTRADAYMACDDATA']._serialized_start=785
  _globals['_INTRADAYMACDDATA']._serialized_end=946
  _globals['_INTRADAYMACDSERVICE']._serialized_start=949
  _globals['_INTRADAYMACDSERVICE']._serialized_end=1157
# @@protoc_insertion_point(module_scope)
