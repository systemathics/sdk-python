# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/type/shared/v1/time_interval.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4systemathics/apis/type/shared/v1/time_interval.proto\x12 systemathics.apis.type.shared.v1\x1a\x1bgoogle/type/timeofday.proto\"x\n\x0cTimeInterval\x12\x35\n\nstart_time\x18\x01 \x01(\x0b\x32\x16.google.type.TimeOfDayR\tstartTime\x12\x31\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x16.google.type.TimeOfDayR\x07\x65ndTimeB\xde\x01\n$com.systemathics.apis.type.shared.v1B\x11TimeIntervalProtoP\x01\xa2\x02\x04SATS\xaa\x02 Systemathics.Apis.Type.Shared.V1\xca\x02 Systemathics\\Apis\\Type\\Shared\\V1\xe2\x02,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\xea\x02$Systemathics::Apis::Type::Shared::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.type.shared.v1.time_interval_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.systemathics.apis.type.shared.v1B\021TimeIntervalProtoP\001\242\002\004SATS\252\002 Systemathics.Apis.Type.Shared.V1\312\002 Systemathics\\Apis\\Type\\Shared\\V1\342\002,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\352\002$Systemathics::Apis::Type::Shared::V1'
  _globals['_TIMEINTERVAL']._serialized_start=119
  _globals['_TIMEINTERVAL']._serialized_end=239
# @@protoc_insertion_point(module_scope)
