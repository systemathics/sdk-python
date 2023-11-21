# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_volatility.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDsystemathics/apis/services/daily_analytics/v1/daily_volatility.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xdb\x01\n\x16\x44\x61ilyVolatilityRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x1e\n\nadjustment\x18\x03 \x01(\x08R\nadjustment\"/\n\x17\x44\x61ilyVolatilityResponse\x12\x14\n\x05value\x18\x01 \x01(\x01R\x05value2\xe3\x01\n\x16\x44\x61ilyVolatilityService\x12\xc8\x01\n\x0f\x44\x61ilyVolatility\x12\x45.systemathics.apis.services.daily_analytics.v1.DailyVolatilityRequest\x1a\x46.systemathics.apis.services.daily_analytics.v1.DailyVolatilityResponse\"&\x82\xd3\xe4\x93\x02 \x12\x1e/v1/daily-analytics/volatilityB\x9e\x02\n1com.systemathics.apis.services.daily_analytics.v1B\x14\x44\x61ilyVolatilityProtoP\x01\xa2\x02\x04SASD\xaa\x02,Systemathics.Apis.Services.DailyAnalytics.V1\xca\x02,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\xe2\x02\x38Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\xea\x02\x30Systemathics::Apis::Services::DailyAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily_analytics.v1.daily_volatility_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1com.systemathics.apis.services.daily_analytics.v1B\024DailyVolatilityProtoP\001\242\002\004SASD\252\002,Systemathics.Apis.Services.DailyAnalytics.V1\312\002,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\342\0028Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\352\0020Systemathics::Apis::Services::DailyAnalytics::V1'
  _globals['_DAILYVOLATILITYSERVICE'].methods_by_name['DailyVolatility']._options = None
  _globals['_DAILYVOLATILITYSERVICE'].methods_by_name['DailyVolatility']._serialized_options = b'\202\323\344\223\002 \022\036/v1/daily-analytics/volatility'
  _globals['_DAILYVOLATILITYREQUEST']._serialized_start=255
  _globals['_DAILYVOLATILITYREQUEST']._serialized_end=474
  _globals['_DAILYVOLATILITYRESPONSE']._serialized_start=476
  _globals['_DAILYVOLATILITYRESPONSE']._serialized_end=523
  _globals['_DAILYVOLATILITYSERVICE']._serialized_start=526
  _globals['_DAILYVOLATILITYSERVICE']._serialized_end=753
# @@protoc_insertion_point(module_scope)
