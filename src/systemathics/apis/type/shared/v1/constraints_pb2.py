# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/type/shared/v1/constraints.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import date_pb2 as google_dot_type_dot_date__pb2
from google.type import dayofweek_pb2 as google_dot_type_dot_dayofweek__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2
from systemathics.apis.type.shared.v1 import time_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_time__interval__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2systemathics/apis/type/shared/v1/constraints.proto\x12 systemathics.apis.type.shared.v1\x1a\x16google/type/date.proto\x1a\x1bgoogle/type/dayofweek.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\x1a\x34systemathics/apis/type/shared/v1/time_interval.proto\"\xb2\x02\n\x0b\x43onstraints\x12U\n\x0e\x64\x61te_intervals\x18\x01 \x03(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\rdateIntervals\x12U\n\x0etime_intervals\x18\x02 \x03(\x0b\x32..systemathics.apis.type.shared.v1.TimeIntervalR\rtimeIntervals\x12\x38\n\x0e\x65xcluded_dates\x18\x03 \x03(\x0b\x32\x11.google.type.DateR\rexcludedDates\x12;\n\rexcluded_days\x18\x04 \x03(\x0e\x32\x16.google.type.DayOfWeekR\x0c\x65xcludedDaysB\xdd\x01\n$com.systemathics.apis.type.shared.v1B\x10\x43onstraintsProtoP\x01\xa2\x02\x04SATS\xaa\x02 Systemathics.Apis.Type.Shared.V1\xca\x02 Systemathics\\Apis\\Type\\Shared\\V1\xe2\x02,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\xea\x02$Systemathics::Apis::Type::Shared::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.type.shared.v1.constraints_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.systemathics.apis.type.shared.v1B\020ConstraintsProtoP\001\242\002\004SATS\252\002 Systemathics.Apis.Type.Shared.V1\312\002 Systemathics\\Apis\\Type\\Shared\\V1\342\002,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\352\002$Systemathics::Apis::Type::Shared::V1'
  _globals['_CONSTRAINTS']._serialized_start=250
  _globals['_CONSTRAINTS']._serialized_end=556
# @@protoc_insertion_point(module_scope)
