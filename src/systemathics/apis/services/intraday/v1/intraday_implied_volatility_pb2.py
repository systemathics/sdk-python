# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/intraday/v1/intraday_implied_volatility.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2
from systemathics.apis.type.shared.v1 import sampling_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_sampling__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHsystemathics/apis/services/intraday/v1/intraday_implied_volatility.proto\x12&systemathics.apis.services.intraday.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\x8f\x02\n\"IntradayImpliedVolatilitiesRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12S\n\rdate_interval\x18\x03 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\"|\n#IntradayImpliedVolatilitiesResponse\x12U\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x41.systemathics.apis.services.intraday.v1.IntradayImpliedVolatilityR\x04\x64\x61ta\"\x82\x01\n\x19IntradayImpliedVolatility\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x14\n\x05score\x18\x03 \x01(\x01R\x05score2\x87\x02\n\"IntradayImpliedVolatilitiesService\x12\xe0\x01\n\x1bIntradayImpliedVolatilities\x12J.systemathics.apis.services.intraday.v1.IntradayImpliedVolatilitiesRequest\x1aK.systemathics.apis.services.intraday.v1.IntradayImpliedVolatilitiesResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/intraday/impliedvolatilitiesB\x89\x02\n*com.systemathics.apis.services.intraday.v1B\x1eIntradayImpliedVolatilityProtoP\x01\xa2\x02\x04SASI\xaa\x02&Systemathics.Apis.Services.Intraday.V1\xca\x02&Systemathics\\Apis\\Services\\Intraday\\V1\xe2\x02\x32Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\xea\x02*Systemathics::Apis::Services::Intraday::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday.v1.intraday_implied_volatility_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.systemathics.apis.services.intraday.v1B\036IntradayImpliedVolatilityProtoP\001\242\002\004SASI\252\002&Systemathics.Apis.Services.Intraday.V1\312\002&Systemathics\\Apis\\Services\\Intraday\\V1\342\0022Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\352\002*Systemathics::Apis::Services::Intraday::V1'
  _globals['_INTRADAYIMPLIEDVOLATILITIESSERVICE'].methods_by_name['IntradayImpliedVolatilities']._options = None
  _globals['_INTRADAYIMPLIEDVOLATILITIESSERVICE'].methods_by_name['IntradayImpliedVolatilities']._serialized_options = b'\202\323\344\223\002\"\022 /v1/intraday/impliedvolatilities'
  _globals['_INTRADAYIMPLIEDVOLATILITIESREQUEST']._serialized_start=334
  _globals['_INTRADAYIMPLIEDVOLATILITIESREQUEST']._serialized_end=605
  _globals['_INTRADAYIMPLIEDVOLATILITIESRESPONSE']._serialized_start=607
  _globals['_INTRADAYIMPLIEDVOLATILITIESRESPONSE']._serialized_end=731
  _globals['_INTRADAYIMPLIEDVOLATILITY']._serialized_start=734
  _globals['_INTRADAYIMPLIEDVOLATILITY']._serialized_end=864
  _globals['_INTRADAYIMPLIEDVOLATILITIESSERVICE']._serialized_start=867
  _globals['_INTRADAYIMPLIEDVOLATILITIESSERVICE']._serialized_end=1130
# @@protoc_insertion_point(module_scope)
