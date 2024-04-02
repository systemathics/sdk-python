# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/intraday/v1/intraday_best_limit.proto
# Protobuf Python Version: 5.26.1
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@systemathics/apis/services/intraday/v1/intraday_best_limit.proto\x12&systemathics.apis.services.intraday.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\xa6\x02\n\x19IntradayBestLimitsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12S\n\rdate_interval\x18\x03 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\"k\n\x1aIntradayBestLimitsResponse\x12M\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x39.systemathics.apis.services.intraday.v1.IntradayBestLimitR\x04\x64\x61ta\"\xd0\x01\n\x11IntradayBestLimit\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x1a\n\x08\x42idPrice\x18\x02 \x01(\x01R\x08\x42idPrice\x12\x18\n\x07\x42idSize\x18\x03 \x01(\x01R\x07\x42idSize\x12\x1a\n\x08\x41skPrice\x18\x04 \x01(\x01R\x08\x41skPrice\x12\x18\n\x07\x41skSize\x18\x05 \x01(\x01R\x07\x41skSize\x12\x14\n\x05score\x18\x06 \x01(\x01R\x05score2\xda\x01\n\x19IntradayBestLimitsService\x12\xbc\x01\n\x12IntradayBestLimits\x12\x41.systemathics.apis.services.intraday.v1.IntradayBestLimitsRequest\x1a\x42.systemathics.apis.services.intraday.v1.IntradayBestLimitsResponse\"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v1/intraday/bestlimitsB\x81\x02\n*com.systemathics.apis.services.intraday.v1B\x16IntradayBestLimitProtoP\x01\xa2\x02\x04SASI\xaa\x02&Systemathics.Apis.Services.Intraday.V1\xca\x02&Systemathics\\Apis\\Services\\Intraday\\V1\xe2\x02\x32Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\xea\x02*Systemathics::Apis::Services::Intraday::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday.v1.intraday_best_limit_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.systemathics.apis.services.intraday.v1B\026IntradayBestLimitProtoP\001\242\002\004SASI\252\002&Systemathics.Apis.Services.Intraday.V1\312\002&Systemathics\\Apis\\Services\\Intraday\\V1\342\0022Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\352\002*Systemathics::Apis::Services::Intraday::V1'
  _globals['_INTRADAYBESTLIMITSSERVICE'].methods_by_name['IntradayBestLimits']._loaded_options = None
  _globals['_INTRADAYBESTLIMITSSERVICE'].methods_by_name['IntradayBestLimits']._serialized_options = b'\202\323\344\223\002\031\022\027/v1/intraday/bestlimits'
  _globals['_INTRADAYBESTLIMITSREQUEST']._serialized_start=326
  _globals['_INTRADAYBESTLIMITSREQUEST']._serialized_end=620
  _globals['_INTRADAYBESTLIMITSRESPONSE']._serialized_start=622
  _globals['_INTRADAYBESTLIMITSRESPONSE']._serialized_end=729
  _globals['_INTRADAYBESTLIMIT']._serialized_start=732
  _globals['_INTRADAYBESTLIMIT']._serialized_end=940
  _globals['_INTRADAYBESTLIMITSSERVICE']._serialized_start=943
  _globals['_INTRADAYBESTLIMITSSERVICE']._serialized_end=1161
# @@protoc_insertion_point(module_scope)
