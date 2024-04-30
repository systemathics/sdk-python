# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/intraday_analytics/v1/intraday_cma.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2
from systemathics.apis.type.shared.v1 import sampling_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_sampling__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCsystemathics/apis/services/intraday_analytics/v1/intraday_cma.proto\x12\x30systemathics.apis.services.intraday_analytics.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\x9f\x02\n\x12IntradayCmaRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12S\n\rdate_interval\x18\x03 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\"l\n\x13IntradayCmaResponse\x12U\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x41.systemathics.apis.services.intraday_analytics.v1.IntradayCmaDataR\x04\x64\x61ta\"|\n\x0fIntradayCmaData\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x18\n\x07\x61verage\x18\x03 \x01(\x01R\x07\x61verage2\xb1\x01\n\x12IntradayCmaService\x12\x9a\x01\n\x0bIntradayCma\x12\x44.systemathics.apis.services.intraday_analytics.v1.IntradayCmaRequest\x1a\x45.systemathics.apis.services.intraday_analytics.v1.IntradayCmaResponseB\xa9\x02\n4com.systemathics.apis.services.intraday_analytics.v1B\x10IntradayCmaProtoP\x01\xa2\x02\x04SASI\xaa\x02/Systemathics.Apis.Services.IntradayAnalytics.V1\xca\x02/Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\xe2\x02;Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\\GPBMetadata\xea\x02\x33Systemathics::Apis::Services::IntradayAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday_analytics.v1.intraday_cma_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n4com.systemathics.apis.services.intraday_analytics.v1B\020IntradayCmaProtoP\001\242\002\004SASI\252\002/Systemathics.Apis.Services.IntradayAnalytics.V1\312\002/Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\342\002;Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\\GPBMetadata\352\0023Systemathics::Apis::Services::IntradayAnalytics::V1'
  _globals['_INTRADAYCMAREQUEST']._serialized_start=309
  _globals['_INTRADAYCMAREQUEST']._serialized_end=596
  _globals['_INTRADAYCMARESPONSE']._serialized_start=598
  _globals['_INTRADAYCMARESPONSE']._serialized_end=706
  _globals['_INTRADAYCMADATA']._serialized_start=708
  _globals['_INTRADAYCMADATA']._serialized_end=832
  _globals['_INTRADAYCMASERVICE']._serialized_start=835
  _globals['_INTRADAYCMASERVICE']._serialized_end=1012
# @@protoc_insertion_point(module_scope)
