# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/intraday/v1/intraday_bars.proto
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:systemathics/apis/services/intraday/v1/intraday_bars.proto\x12&systemathics.apis.services.intraday.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\xa0\x02\n\x13IntradayBarsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12S\n\rdate_interval\x18\x03 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\"_\n\x14IntradayBarsResponse\x12G\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x33.systemathics.apis.services.intraday.v1.IntradayBarR\x04\x64\x61ta\"\xf0\x01\n\x0bIntradayBar\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x12\n\x04open\x18\x02 \x01(\x01R\x04open\x12\x12\n\x04high\x18\x03 \x01(\x01R\x04high\x12\x10\n\x03low\x18\x04 \x01(\x01R\x03low\x12\x14\n\x05\x63lose\x18\x05 \x01(\x01R\x05\x63lose\x12\x16\n\x06volume\x18\x06 \x01(\x01R\x06volume\x12\x14\n\x05\x63ount\x18\x07 \x01(\x05R\x05\x63ount\x12\x12\n\x04vwap\x18\x08 \x01(\x01R\x04vwap\x12\x14\n\x05score\x18\t \x01(\x01R\x05score2\xbc\x01\n\x13IntradayBarsService\x12\xa4\x01\n\x0cIntradayBars\x12;.systemathics.apis.services.intraday.v1.IntradayBarsRequest\x1a<.systemathics.apis.services.intraday.v1.IntradayBarsResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/intraday/barsB\xfc\x01\n*com.systemathics.apis.services.intraday.v1B\x11IntradayBarsProtoP\x01\xa2\x02\x04SASI\xaa\x02&Systemathics.Apis.Services.Intraday.V1\xca\x02&Systemathics\\Apis\\Services\\Intraday\\V1\xe2\x02\x32Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\xea\x02*Systemathics::Apis::Services::Intraday::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday.v1.intraday_bars_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.systemathics.apis.services.intraday.v1B\021IntradayBarsProtoP\001\242\002\004SASI\252\002&Systemathics.Apis.Services.Intraday.V1\312\002&Systemathics\\Apis\\Services\\Intraday\\V1\342\0022Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\352\002*Systemathics::Apis::Services::Intraday::V1'
  _globals['_INTRADAYBARSSERVICE'].methods_by_name['IntradayBars']._options = None
  _globals['_INTRADAYBARSSERVICE'].methods_by_name['IntradayBars']._serialized_options = b'\202\323\344\223\002\023\022\021/v1/intraday/bars'
  _globals['_INTRADAYBARSREQUEST']._serialized_start=320
  _globals['_INTRADAYBARSREQUEST']._serialized_end=608
  _globals['_INTRADAYBARSRESPONSE']._serialized_start=610
  _globals['_INTRADAYBARSRESPONSE']._serialized_end=705
  _globals['_INTRADAYBAR']._serialized_start=708
  _globals['_INTRADAYBAR']._serialized_end=948
  _globals['_INTRADAYBARSSERVICE']._serialized_start=951
  _globals['_INTRADAYBARSSERVICE']._serialized_end=1139
# @@protoc_insertion_point(module_scope)
