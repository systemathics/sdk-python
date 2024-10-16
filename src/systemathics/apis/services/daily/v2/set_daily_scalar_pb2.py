# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v2/set_daily_scalar.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from systemathics.apis.type.shared.v1 import asset_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_asset__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2
from systemathics.apis.type.shared.v2 import set_data_mode_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v2_dot_set__data__mode__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:systemathics/apis/services/daily/v2/set_daily_scalar.proto\x12#systemathics.apis.services.daily.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a,systemathics/apis/type/shared/v1/asset.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a\x34systemathics/apis/type/shared/v2/set_data_mode.proto\"\xc0\x01\n\x15SetDailyScalarRequest\x12M\n\x04info\x18\x01 \x01(\x0b\x32\x37.systemathics.apis.services.daily.v2.SetDailyScalarInfoH\x00R\x04info\x12M\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x37.systemathics.apis.services.daily.v2.SetDailyScalarDataH\x00R\x04\x64\x61taB\t\n\x07payload\"\x7f\n\x17\x43learDailyScalarRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x16\n\x06\x66ields\x18\x02 \x03(\tR\x06\x66ields\"\xbd\x01\n\x12SetDailyScalarInfo\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x16\n\x06\x66ields\x18\x02 \x03(\tR\x06\x66ields\x12\x41\n\x04mode\x18\x03 \x01(\x0e\x32-.systemathics.apis.type.shared.v2.SetDataModeR\x04mode\"O\n\x12SetDailyScalarData\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x12\n\x04\x64\x61ta\x18\x02 \x03(\x01R\x04\x64\x61ta2\x8f\x02\n\x15SetDailyScalarService\x12y\n\x0eSetDailyScalar\x12:.systemathics.apis.services.daily.v2.SetDailyScalarRequest\x1a\x16.google.protobuf.Empty\"\x11\x82\xd3\xe4\x93\x02\x0b\"\t/v2/daily(\x01\x12{\n\x10\x43learDailyScalar\x12<.systemathics.apis.services.daily.v2.ClearDailyScalarRequest\x1a\x16.google.protobuf.Empty\"\x11\x82\xd3\xe4\x93\x02\x0b*\t/v2/dailyB\xef\x01\n\'com.systemathics.apis.services.daily.v2B\x13SetDailyScalarProtoP\x01\xa2\x02\x04SASD\xaa\x02#Systemathics.Apis.Services.Daily.V2\xca\x02#Systemathics\\Apis\\Services\\Daily\\V2\xe2\x02/Systemathics\\Apis\\Services\\Daily\\V2\\GPBMetadata\xea\x02\'Systemathics::Apis::Services::Daily::V2b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily.v2.set_daily_scalar_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.systemathics.apis.services.daily.v2B\023SetDailyScalarProtoP\001\242\002\004SASD\252\002#Systemathics.Apis.Services.Daily.V2\312\002#Systemathics\\Apis\\Services\\Daily\\V2\342\002/Systemathics\\Apis\\Services\\Daily\\V2\\GPBMetadata\352\002\'Systemathics::Apis::Services::Daily::V2'
  _globals['_SETDAILYSCALARSERVICE'].methods_by_name['SetDailyScalar']._options = None
  _globals['_SETDAILYSCALARSERVICE'].methods_by_name['SetDailyScalar']._serialized_options = b'\202\323\344\223\002\013\"\t/v2/daily'
  _globals['_SETDAILYSCALARSERVICE'].methods_by_name['ClearDailyScalar']._options = None
  _globals['_SETDAILYSCALARSERVICE'].methods_by_name['ClearDailyScalar']._serialized_options = b'\202\323\344\223\002\013*\t/v2/daily'
  _globals['_SETDAILYSCALARREQUEST']._serialized_start=418
  _globals['_SETDAILYSCALARREQUEST']._serialized_end=610
  _globals['_CLEARDAILYSCALARREQUEST']._serialized_start=612
  _globals['_CLEARDAILYSCALARREQUEST']._serialized_end=739
  _globals['_SETDAILYSCALARINFO']._serialized_start=742
  _globals['_SETDAILYSCALARINFO']._serialized_end=931
  _globals['_SETDAILYSCALARDATA']._serialized_start=933
  _globals['_SETDAILYSCALARDATA']._serialized_end=1012
  _globals['_SETDAILYSCALARSERVICE']._serialized_start=1015
  _globals['_SETDAILYSCALARSERVICE']._serialized_end=1286
# @@protoc_insertion_point(module_scope)
