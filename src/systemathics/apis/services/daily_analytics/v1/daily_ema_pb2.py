# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_ema.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=systemathics/apis/services/daily_analytics/v1/daily_ema.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xec\x01\n\x0f\x44\x61ilyEmaRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x16\n\x06length\x18\x03 \x01(\x05R\x06length\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\"c\n\x10\x44\x61ilyEmaResponse\x12O\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32;.systemathics.apis.services.daily_analytics.v1.DailyEmaDataR\x04\x64\x61ta\"e\n\x0c\x44\x61ilyEmaData\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x18\n\x07\x61verage\x18\x03 \x01(\x01R\x07\x61verage2\xc0\x01\n\x0f\x44\x61ilyEmaService\x12\xac\x01\n\x08\x44\x61ilyEma\x12>.systemathics.apis.services.daily_analytics.v1.DailyEmaRequest\x1a?.systemathics.apis.services.daily_analytics.v1.DailyEmaResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/daily-analytics/emaB\x97\x02\n1com.systemathics.apis.services.daily_analytics.v1B\rDailyEmaProtoP\x01\xa2\x02\x04SASD\xaa\x02,Systemathics.Apis.Services.DailyAnalytics.V1\xca\x02,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\xe2\x02\x38Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\xea\x02\x30Systemathics::Apis::Services::DailyAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily_analytics.v1.daily_ema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1com.systemathics.apis.services.daily_analytics.v1B\rDailyEmaProtoP\001\242\002\004SASD\252\002,Systemathics.Apis.Services.DailyAnalytics.V1\312\002,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\342\0028Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\352\0020Systemathics::Apis::Services::DailyAnalytics::V1'
  _globals['_DAILYEMASERVICE'].methods_by_name['DailyEma']._options = None
  _globals['_DAILYEMASERVICE'].methods_by_name['DailyEma']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/daily-analytics/ema'
  _globals['_DAILYEMAREQUEST']._serialized_start=272
  _globals['_DAILYEMAREQUEST']._serialized_end=508
  _globals['_DAILYEMARESPONSE']._serialized_start=510
  _globals['_DAILYEMARESPONSE']._serialized_end=609
  _globals['_DAILYEMADATA']._serialized_start=611
  _globals['_DAILYEMADATA']._serialized_end=712
  _globals['_DAILYEMASERVICE']._serialized_start=715
  _globals['_DAILYEMASERVICE']._serialized_end=907
# @@protoc_insertion_point(module_scope)
