# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_bollinger.proto
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
from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCsystemathics/apis/services/daily_analytics/v1/daily_bollinger.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\x90\x02\n\x15\x44\x61ilyBollingerRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x16\n\x06length\x18\x03 \x01(\x05R\x06length\x12\x1c\n\tdeviation\x18\x04 \x01(\x01R\tdeviation\x12\x1e\n\nadjustment\x18\x05 \x01(\x08R\nadjustment\"o\n\x16\x44\x61ilyBollingerResponse\x12U\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x41.systemathics.apis.services.daily_analytics.v1.DailyBollingerDataR\x04\x64\x61ta\"\xef\x01\n\x12\x44\x61ilyBollingerData\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x32\n\x05lower\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x05lower\x12\x32\n\x05upper\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x05upper\x12\x34\n\x06middle\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x06middle2\xde\x01\n\x15\x44\x61ilyBollingerService\x12\xc4\x01\n\x0e\x44\x61ilyBollinger\x12\x44.systemathics.apis.services.daily_analytics.v1.DailyBollingerRequest\x1a\x45.systemathics.apis.services.daily_analytics.v1.DailyBollingerResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/daily-analytics/bollingerB\x9d\x02\n1com.systemathics.apis.services.daily_analytics.v1B\x13\x44\x61ilyBollingerProtoP\x01\xa2\x02\x04SASD\xaa\x02,Systemathics.Apis.Services.DailyAnalytics.V1\xca\x02,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\xe2\x02\x38Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\xea\x02\x30Systemathics::Apis::Services::DailyAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily_analytics.v1.daily_bollinger_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1com.systemathics.apis.services.daily_analytics.v1B\023DailyBollingerProtoP\001\242\002\004SASD\252\002,Systemathics.Apis.Services.DailyAnalytics.V1\312\002,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\342\0028Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\352\0020Systemathics::Apis::Services::DailyAnalytics::V1'
  _globals['_DAILYBOLLINGERSERVICE'].methods_by_name['DailyBollinger']._options = None
  _globals['_DAILYBOLLINGERSERVICE'].methods_by_name['DailyBollinger']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/daily-analytics/bollinger'
  _globals['_DAILYBOLLINGERREQUEST']._serialized_start=310
  _globals['_DAILYBOLLINGERREQUEST']._serialized_end=582
  _globals['_DAILYBOLLINGERRESPONSE']._serialized_start=584
  _globals['_DAILYBOLLINGERRESPONSE']._serialized_end=695
  _globals['_DAILYBOLLINGERDATA']._serialized_start=698
  _globals['_DAILYBOLLINGERDATA']._serialized_end=937
  _globals['_DAILYBOLLINGERSERVICE']._serialized_start=940
  _globals['_DAILYBOLLINGERSERVICE']._serialized_end=1162
# @@protoc_insertion_point(module_scope)