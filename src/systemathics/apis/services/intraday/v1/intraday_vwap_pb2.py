# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/intraday/v1/intraday_vwap.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:systemathics/apis/services/intraday/v1/intraday_vwap.proto\x12&systemathics.apis.services.intraday.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\xa1\x02\n\x14IntradayVwapsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12S\n\rdate_interval\x18\x03 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\"a\n\x15IntradayVwapsResponse\x12H\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x34.systemathics.apis.services.intraday.v1.IntradayVwapR\x04\x64\x61ta\"\x8d\x01\n\x0cIntradayVwap\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x14\n\x05price\x18\x02 \x01(\x01R\x05price\x12\x16\n\x06volume\x18\x03 \x01(\x01R\x06volume\x12\x14\n\x05score\x18\x04 \x01(\x01R\x05score2\xc1\x01\n\x14IntradayVwapsService\x12\xa8\x01\n\rIntradayVwaps\x12<.systemathics.apis.services.intraday.v1.IntradayVwapsRequest\x1a=.systemathics.apis.services.intraday.v1.IntradayVwapsResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/intraday/vwapsB\xfc\x01\n*com.systemathics.apis.services.intraday.v1B\x11IntradayVwapProtoP\x01\xa2\x02\x04SASI\xaa\x02&Systemathics.Apis.Services.Intraday.V1\xca\x02&Systemathics\\Apis\\Services\\Intraday\\V1\xe2\x02\x32Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\xea\x02*Systemathics::Apis::Services::Intraday::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday.v1.intraday_vwap_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.systemathics.apis.services.intraday.v1B\021IntradayVwapProtoP\001\242\002\004SASI\252\002&Systemathics.Apis.Services.Intraday.V1\312\002&Systemathics\\Apis\\Services\\Intraday\\V1\342\0022Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\352\002*Systemathics::Apis::Services::Intraday::V1'
  _globals['_INTRADAYVWAPSSERVICE'].methods_by_name['IntradayVwaps']._options = None
  _globals['_INTRADAYVWAPSSERVICE'].methods_by_name['IntradayVwaps']._serialized_options = b'\202\323\344\223\002\024\022\022/v1/intraday/vwaps'
  _globals['_INTRADAYVWAPSREQUEST']._serialized_start=320
  _globals['_INTRADAYVWAPSREQUEST']._serialized_end=609
  _globals['_INTRADAYVWAPSRESPONSE']._serialized_start=611
  _globals['_INTRADAYVWAPSRESPONSE']._serialized_end=708
  _globals['_INTRADAYVWAP']._serialized_start=711
  _globals['_INTRADAYVWAP']._serialized_end=852
  _globals['_INTRADAYVWAPSSERVICE']._serialized_start=855
  _globals['_INTRADAYVWAPSSERVICE']._serialized_end=1048
# @@protoc_insertion_point(module_scope)
