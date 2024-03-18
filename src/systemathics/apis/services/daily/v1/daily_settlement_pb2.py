# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_settlement.proto
# Protobuf Python Version: 5.26.0
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:systemathics/apis/services/daily/v1/daily_settlement.proto\x12#systemathics.apis.services.daily.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xdc\x01\n\x17\x44\x61ilySettlementsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x1e\n\nadjustment\x18\x03 \x01(\x08R\nadjustment\"d\n\x18\x44\x61ilySettlementsResponse\x12H\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x34.systemathics.apis.services.daily.v1.DailySettlementR\x04\x64\x61ta\"|\n\x0f\x44\x61ilySettlement\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x14\n\x05price\x18\x02 \x01(\x01R\x05price\x12\x16\n\x06volume\x18\x03 \x01(\x01R\x06volume\x12\x14\n\x05score\x18\x04 \x01(\x01R\x05score2\xca\x01\n\x17\x44\x61ilySettlementsService\x12\xae\x01\n\x10\x44\x61ilySettlements\x12<.systemathics.apis.services.daily.v1.DailySettlementsRequest\x1a=.systemathics.apis.services.daily.v1.DailySettlementsResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/daily/settlementsB\xf0\x01\n\'com.systemathics.apis.services.daily.v1B\x14\x44\x61ilySettlementProtoP\x01\xa2\x02\x04SASD\xaa\x02#Systemathics.Apis.Services.Daily.V1\xca\x02#Systemathics\\Apis\\Services\\Daily\\V1\xe2\x02/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\xea\x02\'Systemathics::Apis::Services::Daily::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily.v1.daily_settlement_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.systemathics.apis.services.daily.v1B\024DailySettlementProtoP\001\242\002\004SASD\252\002#Systemathics.Apis.Services.Daily.V1\312\002#Systemathics\\Apis\\Services\\Daily\\V1\342\002/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\352\002\'Systemathics::Apis::Services::Daily::V1'
  _globals['_DAILYSETTLEMENTSSERVICE'].methods_by_name['DailySettlements']._loaded_options = None
  _globals['_DAILYSETTLEMENTSSERVICE'].methods_by_name['DailySettlements']._serialized_options = b'\202\323\344\223\002\027\022\025/v1/daily/settlements'
  _globals['_DAILYSETTLEMENTSREQUEST']._serialized_start=259
  _globals['_DAILYSETTLEMENTSREQUEST']._serialized_end=479
  _globals['_DAILYSETTLEMENTSRESPONSE']._serialized_start=481
  _globals['_DAILYSETTLEMENTSRESPONSE']._serialized_end=581
  _globals['_DAILYSETTLEMENT']._serialized_start=583
  _globals['_DAILYSETTLEMENT']._serialized_end=707
  _globals['_DAILYSETTLEMENTSSERVICE']._serialized_start=710
  _globals['_DAILYSETTLEMENTSSERVICE']._serialized_end=912
# @@protoc_insertion_point(module_scope)
