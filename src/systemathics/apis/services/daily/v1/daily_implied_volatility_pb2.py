# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_implied_volatility.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBsystemathics/apis/services/daily/v1/daily_implied_volatility.proto\x12#systemathics.apis.services.daily.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xc4\x01\n\x1f\x44\x61ilyImpliedVolatilitiesRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\"s\n DailyImpliedVolatilitiesResponse\x12O\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32;.systemathics.apis.services.daily.v1.DailyImpliedVolatilityR\x04\x64\x61ta\"\xb3\x0c\n\x16\x44\x61ilyImpliedVolatility\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12-\n\x12implied_volatility\x18\x02 \x01(\x01R\x11impliedVolatility\x12\x14\n\x05score\x18\x03 \x01(\x01R\x05score\x12;\n\x1aimplied_volatility_30_call\x18\x04 \x01(\x01R\x17impliedVolatility30Call\x12\x39\n\x19implied_volatility_30_put\x18\x05 \x01(\x01R\x16impliedVolatility30Put\x12;\n\x1aimplied_volatility_30_mean\x18\x06 \x01(\x01R\x17impliedVolatility30Mean\x12;\n\x1aimplied_volatility_60_call\x18\x07 \x01(\x01R\x17impliedVolatility60Call\x12\x39\n\x19implied_volatility_60_put\x18\x08 \x01(\x01R\x16impliedVolatility60Put\x12;\n\x1aimplied_volatility_60_mean\x18\t \x01(\x01R\x17impliedVolatility60Mean\x12;\n\x1aimplied_volatility_90_call\x18\n \x01(\x01R\x17impliedVolatility90Call\x12\x39\n\x19implied_volatility_90_put\x18\x0b \x01(\x01R\x16impliedVolatility90Put\x12;\n\x1aimplied_volatility_90_mean\x18\x0c \x01(\x01R\x17impliedVolatility90Mean\x12=\n\x1bimplied_volatility_120_call\x18\r \x01(\x01R\x18impliedVolatility120Call\x12;\n\x1aimplied_volatility_120_put\x18\x0e \x01(\x01R\x17impliedVolatility120Put\x12=\n\x1bimplied_volatility_120_mean\x18\x0f \x01(\x01R\x18impliedVolatility120Mean\x12=\n\x1bimplied_volatility_150_call\x18\x10 \x01(\x01R\x18impliedVolatility150Call\x12;\n\x1aimplied_volatility_150_put\x18\x11 \x01(\x01R\x17impliedVolatility150Put\x12=\n\x1bimplied_volatility_150_mean\x18\x12 \x01(\x01R\x18impliedVolatility150Mean\x12=\n\x1bimplied_volatility_180_call\x18\x13 \x01(\x01R\x18impliedVolatility180Call\x12;\n\x1aimplied_volatility_180_put\x18\x14 \x01(\x01R\x17impliedVolatility180Put\x12=\n\x1bimplied_volatility_180_mean\x18\x15 \x01(\x01R\x18impliedVolatility180Mean\x12=\n\x1bimplied_volatility_360_call\x18\x16 \x01(\x01R\x18impliedVolatility360Call\x12;\n\x1aimplied_volatility_360_put\x18\x17 \x01(\x01R\x17impliedVolatility360Put\x12=\n\x1bimplied_volatility_360_mean\x18\x18 \x01(\x01R\x18impliedVolatility360Mean\x12\x34\n\x16implied_volatility_bid\x18\x19 \x01(\x01R\x14impliedVolatilityBid\x12\x34\n\x16implied_volatility_ask\x18\x1a \x01(\x01R\x14impliedVolatilityAsk\x12\x36\n\x17implied_volatility_mean\x18\x1b \x01(\x01R\x15impliedVolatilityMean2\xf2\x01\n\x1f\x44\x61ilyImpliedVolatilitiesService\x12\xce\x01\n\x18\x44\x61ilyImpliedVolatilities\x12\x44.systemathics.apis.services.daily.v1.DailyImpliedVolatilitiesRequest\x1a\x45.systemathics.apis.services.daily.v1.DailyImpliedVolatilitiesResponse\"%\x82\xd3\xe4\x93\x02\x1f\x12\x1d/v1/daily/impliedvolatilitiesB\xf7\x01\n\'com.systemathics.apis.services.daily.v1B\x1b\x44\x61ilyImpliedVolatilityProtoP\x01\xa2\x02\x04SASD\xaa\x02#Systemathics.Apis.Services.Daily.V1\xca\x02#Systemathics\\Apis\\Services\\Daily\\V1\xe2\x02/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\xea\x02\'Systemathics::Apis::Services::Daily::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily.v1.daily_implied_volatility_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.systemathics.apis.services.daily.v1B\033DailyImpliedVolatilityProtoP\001\242\002\004SASD\252\002#Systemathics.Apis.Services.Daily.V1\312\002#Systemathics\\Apis\\Services\\Daily\\V1\342\002/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\352\002\'Systemathics::Apis::Services::Daily::V1'
  _globals['_DAILYIMPLIEDVOLATILITIESSERVICE'].methods_by_name['DailyImpliedVolatilities']._options = None
  _globals['_DAILYIMPLIEDVOLATILITIESSERVICE'].methods_by_name['DailyImpliedVolatilities']._serialized_options = b'\202\323\344\223\002\037\022\035/v1/daily/impliedvolatilities'
  _globals['_DAILYIMPLIEDVOLATILITIESREQUEST']._serialized_start=267
  _globals['_DAILYIMPLIEDVOLATILITIESREQUEST']._serialized_end=463
  _globals['_DAILYIMPLIEDVOLATILITIESRESPONSE']._serialized_start=465
  _globals['_DAILYIMPLIEDVOLATILITIESRESPONSE']._serialized_end=580
  _globals['_DAILYIMPLIEDVOLATILITY']._serialized_start=583
  _globals['_DAILYIMPLIEDVOLATILITY']._serialized_end=2170
  _globals['_DAILYIMPLIEDVOLATILITIESSERVICE']._serialized_start=2173
  _globals['_DAILYIMPLIEDVOLATILITIESSERVICE']._serialized_end=2415
# @@protoc_insertion_point(module_scope)
