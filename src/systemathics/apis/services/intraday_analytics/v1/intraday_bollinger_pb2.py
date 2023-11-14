# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/intraday_analytics/v1/intraday_bollinger.proto
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
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import sampling_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_sampling__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIsystemathics/apis/services/intraday_analytics/v1/intraday_bollinger.proto\x12\x30systemathics.apis.services.intraday_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a/systemathics/apis/type/shared/v1/sampling.proto\"\xd7\x02\n\x18IntradayBollingerRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12\x46\n\x08sampling\x18\x02 \x01(\x0e\x32*.systemathics.apis.type.shared.v1.SamplingR\x08sampling\x12O\n\x0b\x63onstraints\x18\x03 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\x12\x16\n\x06length\x18\x04 \x01(\x05R\x06length\x12\x1c\n\tdeviation\x18\x05 \x01(\x01R\tdeviation\x12\x1e\n\nadjustment\x18\x06 \x01(\x08R\nadjustment\"x\n\x19IntradayBollingerResponse\x12[\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32G.systemathics.apis.services.intraday_analytics.v1.IntradayBollingerDataR\x04\x64\x61ta\"\x86\x02\n\x15IntradayBollingerData\x12\x39\n\ntime_stamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12\x14\n\x05value\x18\x02 \x01(\x01R\x05value\x12\x32\n\x05lower\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x05lower\x12\x32\n\x05upper\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x05upper\x12\x34\n\x06middle\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueR\x06middle2\xe9\x01\n\x18IntradayBollingerService\x12\xcc\x01\n\x11IntradayBollinger\x12J.systemathics.apis.services.intraday_analytics.v1.IntradayBollingerRequest\x1aK.systemathics.apis.services.intraday_analytics.v1.IntradayBollingerResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/intraday/bollingerB\xaf\x02\n4com.systemathics.apis.services.intraday_analytics.v1B\x16IntradayBollingerProtoP\x01\xa2\x02\x04SASI\xaa\x02/Systemathics.Apis.Services.IntradayAnalytics.V1\xca\x02/Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\xe2\x02;Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\\GPBMetadata\xea\x02\x33Systemathics::Apis::Services::IntradayAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.intraday_analytics.v1.intraday_bollinger_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n4com.systemathics.apis.services.intraday_analytics.v1B\026IntradayBollingerProtoP\001\242\002\004SASI\252\002/Systemathics.Apis.Services.IntradayAnalytics.V1\312\002/Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\342\002;Systemathics\\Apis\\Services\\IntradayAnalytics\\V1\\GPBMetadata\352\0023Systemathics::Apis::Services::IntradayAnalytics::V1'
  _globals['_INTRADAYBOLLINGERSERVICE'].methods_by_name['IntradayBollinger']._options = None
  _globals['_INTRADAYBOLLINGERSERVICE'].methods_by_name['IntradayBollinger']._serialized_options = b'\202\323\344\223\002\030\022\026/v1/intraday/bollinger'
  _globals['_INTRADAYBOLLINGERREQUEST']._serialized_start=375
  _globals['_INTRADAYBOLLINGERREQUEST']._serialized_end=718
  _globals['_INTRADAYBOLLINGERRESPONSE']._serialized_start=720
  _globals['_INTRADAYBOLLINGERRESPONSE']._serialized_end=840
  _globals['_INTRADAYBOLLINGERDATA']._serialized_start=843
  _globals['_INTRADAYBOLLINGERDATA']._serialized_end=1105
  _globals['_INTRADAYBOLLINGERSERVICE']._serialized_start=1108
  _globals['_INTRADAYBOLLINGERSERVICE']._serialized_end=1341
# @@protoc_insertion_point(module_scope)