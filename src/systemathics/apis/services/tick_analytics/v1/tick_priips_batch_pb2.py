# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick_analytics/v1/tick_priips_batch.proto
# Protobuf Python Version: 4.25.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from systemathics.apis.services.tick_analytics.v1 import tick_priips_pb2 as systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDsystemathics/apis/services/tick_analytics/v1/tick_priips_batch.proto\x12,systemathics.apis.services.tick_analytics.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a>systemathics/apis/services/tick_analytics/v1/tick_priips.proto\"\xe9\x02\n\x16TickPriipsBatchRequest\x12\x15\n\x06\x63sv_gz\x18\x01 \x01(\x0cR\x05\x63svGz\x12O\n\x05\x66ield\x18\x02 \x01(\x0e\x32\x39.systemathics.apis.services.tick_analytics.v1.PriipsPriceR\x05\x66ield\x12\x33\n\x07latency\x18\x03 \x01(\x0b\x32\x19.google.protobuf.DurationR\x07latency\x12\x16\n\x06\x61\x63\x63\x65pt\x18\x04 \x03(\tR\x06\x61\x63\x63\x65pt\x12\x16\n\x06reject\x18\x05 \x03(\tR\x06reject\x12\x18\n\x07metrics\x18\x06 \x01(\x08R\x07metrics\x12K\n\"use_reverse_iteration_optimization\x18\x07 \x01(\x08R\x1fuseReverseIterationOptimization\x12\x1b\n\ttime_zone\x18\x08 \x01(\x0cR\x08timeZone\"T\n\x17TickPriipsBatchResponse\x12\x15\n\x06\x63sv_gz\x18\x01 \x01(\x0cR\x05\x63svGz\x12\"\n\rerrors_csv_gz\x18\x02 \x01(\x0cR\x0b\x65rrorsCsvGz2\xe2\x01\n\x16TickPriipsBatchService\x12\xc7\x01\n\x0fTickPriipsBatch\x12\x44.systemathics.apis.services.tick_analytics.v1.TickPriipsBatchRequest\x1a\x45.systemathics.apis.services.tick_analytics.v1.TickPriipsBatchResponse\"\'\x82\xd3\xe4\x93\x02!\x12\x1f/v1/tick-analytics/priips-batchB\x99\x02\n0com.systemathics.apis.services.tick_analytics.v1B\x14TickPriipsBatchProtoP\x01\xa2\x02\x04SAST\xaa\x02+Systemathics.Apis.Services.TickAnalytics.V1\xca\x02+Systemathics\\Apis\\Services\\TickAnalytics\\V1\xe2\x02\x37Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\xea\x02/Systemathics::Apis::Services::TickAnalytics::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick_analytics.v1.tick_priips_batch_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.systemathics.apis.services.tick_analytics.v1B\024TickPriipsBatchProtoP\001\242\002\004SAST\252\002+Systemathics.Apis.Services.TickAnalytics.V1\312\002+Systemathics\\Apis\\Services\\TickAnalytics\\V1\342\0027Systemathics\\Apis\\Services\\TickAnalytics\\V1\\GPBMetadata\352\002/Systemathics::Apis::Services::TickAnalytics::V1'
  _globals['_TICKPRIIPSBATCHSERVICE'].methods_by_name['TickPriipsBatch']._options = None
  _globals['_TICKPRIIPSBATCHSERVICE'].methods_by_name['TickPriipsBatch']._serialized_options = b'\202\323\344\223\002!\022\037/v1/tick-analytics/priips-batch'
  _globals['_TICKPRIIPSBATCHREQUEST']._serialized_start=245
  _globals['_TICKPRIIPSBATCHREQUEST']._serialized_end=606
  _globals['_TICKPRIIPSBATCHRESPONSE']._serialized_start=608
  _globals['_TICKPRIIPSBATCHRESPONSE']._serialized_end=692
  _globals['_TICKPRIIPSBATCHSERVICE']._serialized_start=695
  _globals['_TICKPRIIPSBATCHSERVICE']._serialized_end=921
# @@protoc_insertion_point(module_scope)
