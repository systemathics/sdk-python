# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_open_interest.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=systemathics/apis/services/daily/v1/daily_open_interest.proto\x12#systemathics.apis.services.daily.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xbe\x01\n\x19\x44\x61ilyOpenInterestsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\"h\n\x1a\x44\x61ilyOpenInterestsResponse\x12J\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x36.systemathics.apis.services.daily.v1.DailyOpenInterestR\x04\x64\x61ta\"\xa9\x02\n\x11\x44\x61ilyOpenInterest\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12#\n\ropen_interest\x18\x02 \x01(\x01R\x0copenInterest\x12\x14\n\x05score\x18\x03 \x01(\x01R\x05score\x12,\n\x12\x63\x61ll_open_interest\x18\x04 \x01(\x01R\x10\x63\x61llOpenInterest\x12*\n\x11put_open_interest\x18\x05 \x01(\x01R\x0fputOpenInterest\x12.\n\x13total_open_interest\x18\x06 \x01(\x01R\x11totalOpenInterest\x12(\n\x10t1_open_interest\x18\x07 \x01(\x01R\x0et1OpenInterest2\xd4\x01\n\x19\x44\x61ilyOpenInterestsService\x12\xb6\x01\n\x12\x44\x61ilyOpenInterests\x12>.systemathics.apis.services.daily.v1.DailyOpenInterestsRequest\x1a?.systemathics.apis.services.daily.v1.DailyOpenInterestsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/daily/openinterestsB\xf2\x01\n\'com.systemathics.apis.services.daily.v1B\x16\x44\x61ilyOpenInterestProtoP\x01\xa2\x02\x04SASD\xaa\x02#Systemathics.Apis.Services.Daily.V1\xca\x02#Systemathics\\Apis\\Services\\Daily\\V1\xe2\x02/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\xea\x02\'Systemathics::Apis::Services::Daily::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily.v1.daily_open_interest_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.systemathics.apis.services.daily.v1B\026DailyOpenInterestProtoP\001\242\002\004SASD\252\002#Systemathics.Apis.Services.Daily.V1\312\002#Systemathics\\Apis\\Services\\Daily\\V1\342\002/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\352\002\'Systemathics::Apis::Services::Daily::V1'
  _globals['_DAILYOPENINTERESTSSERVICE'].methods_by_name['DailyOpenInterests']._options = None
  _globals['_DAILYOPENINTERESTSSERVICE'].methods_by_name['DailyOpenInterests']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/daily/openinterests'
  _globals['_DAILYOPENINTERESTSREQUEST']._serialized_start=262
  _globals['_DAILYOPENINTERESTSREQUEST']._serialized_end=452
  _globals['_DAILYOPENINTERESTSRESPONSE']._serialized_start=454
  _globals['_DAILYOPENINTERESTSRESPONSE']._serialized_end=558
  _globals['_DAILYOPENINTEREST']._serialized_start=561
  _globals['_DAILYOPENINTEREST']._serialized_end=858
  _globals['_DAILYOPENINTERESTSSERVICE']._serialized_start=861
  _globals['_DAILYOPENINTERESTSSERVICE']._serialized_end=1073
# @@protoc_insertion_point(module_scope)
