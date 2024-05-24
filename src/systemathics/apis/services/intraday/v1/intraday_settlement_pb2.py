# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: systemathics/apis/services/intraday/v1/intraday_settlement.proto
# Protobuf Python Version: 5.27.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    0,
    '',
    'systemathics/apis/services/intraday/v1/intraday_settlement.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2
from systemathics.apis.type.shared.v1 import sampling_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_sampling__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@systemathics/apis/services/intraday/v1/intraday_settlement.proto\x12&systemathics.apis.services.intraday.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\xa7\x02\n\x1aIntradaySettlementsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12S\n\rdate_interval\x18\x03 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\x12\x1e\n\nadjustment\x18\x04 \x01(\x08R\nadjustment\"m\n\x1bIntradaySettlementsResponse\x12N\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32:.systemathics.apis.services.intraday.v1.IntradaySettlementR\x04\x64\x61ta\"\x93\x01\n\x12IntradaySettlement\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x16\n\x06volume\x18\x03 \x01(\x01R\x06volume\x12\x14\n\x05score\x18\x04 \x01(\x01R\x05score2\xdf\x01\n\x1aIntradaySettlementsService\x12\xc0\x01\n\x13IntradaySettlements\x12\x42.systemathics.apis.services.intraday.v1.IntradaySettlementsRequest\x1a\x43.systemathics.apis.services.intraday.v1.IntradaySettlementsResponse\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/intraday/settlementsB\x82\x02\n*com.systemathics.apis.services.intraday.v1B\x17IntradaySettlementProtoP\x01\xa2\x02\x04SASI\xaa\x02&Systemathics.Apis.Services.Intraday.V1\xca\x02&Systemathics\\Apis\\Services\\Intraday\\V1\xe2\x02\x32Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\xea\x02*Systemathics::Apis::Services::Intraday::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday.v1.intraday_settlement_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n*com.systemathics.apis.services.intraday.v1B\027IntradaySettlementProtoP\001\242\002\004SASI\252\002&Systemathics.Apis.Services.Intraday.V1\312\002&Systemathics\\Apis\\Services\\Intraday\\V1\342\0022Systemathics\\Apis\\Services\\Intraday\\V1\\GPBMetadata\352\002*Systemathics::Apis::Services::Intraday::V1'
  _globals['_INTRADAYSETTLEMENTSSERVICE'].methods_by_name['IntradaySettlements']._loaded_options = None
  _globals['_INTRADAYSETTLEMENTSSERVICE'].methods_by_name['IntradaySettlements']._serialized_options = b'\202\323\344\223\002\032\022\030/v1/intraday/settlements'
  _globals['_INTRADAYSETTLEMENTSREQUEST']._serialized_start=326
  _globals['_INTRADAYSETTLEMENTSREQUEST']._serialized_end=621
  _globals['_INTRADAYSETTLEMENTSRESPONSE']._serialized_start=623
  _globals['_INTRADAYSETTLEMENTSRESPONSE']._serialized_end=732
  _globals['_INTRADAYSETTLEMENT']._serialized_start=735
  _globals['_INTRADAYSETTLEMENT']._serialized_end=882
  _globals['_INTRADAYSETTLEMENTSSERVICE']._serialized_start=885
  _globals['_INTRADAYSETTLEMENTSSERVICE']._serialized_end=1108
# @@protoc_insertion_point(module_scope)
