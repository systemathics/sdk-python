# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily_analytics/v1/daily_sma.proto
# Protobuf Python Version: 4.25.2
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=systemathics/apis/services/daily_analytics/v1/daily_sma.proto\x12-systemathics.apis.services.daily_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xec\x01\n\x0f\x44\x61ilySmaRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x16\n\x06length\x18\x03 \x01(\x05R\x06length\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\"c\n\x10\x44\x61ilySmaResponse\x12O\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32;.systemathics.apis.services.daily_analytics.v1.DailySmaDataR\x04\x64\x61ta\"\x83\x01\n\x0c\x44\x61ilySmaData\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x36\n\x07\x61verage\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x07\x61verage2\xc0\x01\n\x0f\x44\x61ilySmaService\x12\xac\x01\n\x08\x44\x61ilySma\x12>.systemathics.apis.services.daily_analytics.v1.DailySmaRequest\x1a?.systemathics.apis.services.daily_analytics.v1.DailySmaResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/daily-analytics/smaB\x97\x02\n1com.systemathics.apis.services.daily_analytics.v1B\rDailySmaProtoP\x01\xa2\x02\x04SASD\xaa\x02,Systemathics.Apis.Services.DailyAnalytics.V1\xca\x02,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\xe2\x02\x38Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\xea\x02\x30Systemathics::Apis::Services::DailyAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily_analytics.v1.daily_sma_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n1com.systemathics.apis.services.daily_analytics.v1B\rDailySmaProtoP\001\242\002\004SASD\252\002,Systemathics.Apis.Services.DailyAnalytics.V1\312\002,Systemathics\\Apis\\Services\\DailyAnalytics\\V1\342\0028Systemathics\\Apis\\Services\\DailyAnalytics\\V1\\GPBMetadata\352\0020Systemathics::Apis::Services::DailyAnalytics::V1'
  _globals['_DAILYSMASERVICE'].methods_by_name['DailySma']._options = None
  _globals['_DAILYSMASERVICE'].methods_by_name['DailySma']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/daily-analytics/sma'
  _globals['_DAILYSMAREQUEST']._serialized_start=304
  _globals['_DAILYSMAREQUEST']._serialized_end=540
  _globals['_DAILYSMARESPONSE']._serialized_start=542
  _globals['_DAILYSMARESPONSE']._serialized_end=641
  _globals['_DAILYSMADATA']._serialized_start=644
  _globals['_DAILYSMADATA']._serialized_end=775
  _globals['_DAILYSMASERVICE']._serialized_start=778
  _globals['_DAILYSMASERVICE']._serialized_end=970
# @@protoc_insertion_point(module_scope)
