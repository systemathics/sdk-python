# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_greeks.proto
# Protobuf Python Version: 4.25.3
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6systemathics/apis/services/daily/v1/daily_greeks.proto\x12#systemathics.apis.services.daily.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xb7\x01\n\x12\x44\x61ilyGreeksRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\"[\n\x13\x44\x61ilyGreeksResponse\x12\x44\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x30.systemathics.apis.services.daily.v1.DailyGreeksR\x04\x64\x61ta\"\xb2\x01\n\x0b\x44\x61ilyGreeks\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x14\n\x05\x64\x65lta\x18\x02 \x01(\x01R\x05\x64\x65lta\x12\x14\n\x05gamma\x18\x03 \x01(\x01R\x05gamma\x12\x14\n\x05theta\x18\x04 \x01(\x01R\x05theta\x12\x12\n\x04vega\x18\x05 \x01(\x01R\x04vega\x12\x10\n\x03rho\x18\x06 \x01(\x01R\x03rho\x12\x14\n\x05score\x18\x07 \x01(\x01R\x05score2\xb1\x01\n\x12\x44\x61ilyGreeksService\x12\x9a\x01\n\x0b\x44\x61ilyGreeks\x12\x37.systemathics.apis.services.daily.v1.DailyGreeksRequest\x1a\x38.systemathics.apis.services.daily.v1.DailyGreeksResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/daily/greeksB\xec\x01\n\'com.systemathics.apis.services.daily.v1B\x10\x44\x61ilyGreeksProtoP\x01\xa2\x02\x04SASD\xaa\x02#Systemathics.Apis.Services.Daily.V1\xca\x02#Systemathics\\Apis\\Services\\Daily\\V1\xe2\x02/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\xea\x02\'Systemathics::Apis::Services::Daily::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily.v1.daily_greeks_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.systemathics.apis.services.daily.v1B\020DailyGreeksProtoP\001\242\002\004SASD\252\002#Systemathics.Apis.Services.Daily.V1\312\002#Systemathics\\Apis\\Services\\Daily\\V1\342\002/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\352\002\'Systemathics::Apis::Services::Daily::V1'
  _globals['_DAILYGREEKSSERVICE'].methods_by_name['DailyGreeks']._options = None
  _globals['_DAILYGREEKSSERVICE'].methods_by_name['DailyGreeks']._serialized_options = b'\202\323\344\223\002\022\022\020/v1/daily/greeks'
  _globals['_DAILYGREEKSREQUEST']._serialized_start=255
  _globals['_DAILYGREEKSREQUEST']._serialized_end=438
  _globals['_DAILYGREEKSRESPONSE']._serialized_start=440
  _globals['_DAILYGREEKSRESPONSE']._serialized_end=531
  _globals['_DAILYGREEKS']._serialized_start=534
  _globals['_DAILYGREEKS']._serialized_end=712
  _globals['_DAILYGREEKSSERVICE']._serialized_start=715
  _globals['_DAILYGREEKSSERVICE']._serialized_end=892
# @@protoc_insertion_point(module_scope)
