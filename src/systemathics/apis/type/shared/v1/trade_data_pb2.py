# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/type/shared/v1/trade_data.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from systemathics.apis.type.shared.v1 import trade_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_trade__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1systemathics/apis/type/shared/v1/trade_data.proto\x12 systemathics.apis.type.shared.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a,systemathics/apis/type/shared/v1/trade.proto\"\x9f\x01\n\tTradeData\x12\x18\n\x07mapping\x18\x01 \x01(\rR\x07mapping\x12\x39\n\ntime_stamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\ttimeStamp\x12=\n\x05trade\x18\x03 \x01(\x0b\x32\'.systemathics.apis.type.shared.v1.TradeR\x05tradeB\xdb\x01\n$com.systemathics.apis.type.shared.v1B\x0eTradeDataProtoP\x01\xa2\x02\x04SATS\xaa\x02 Systemathics.Apis.Type.Shared.V1\xca\x02 Systemathics\\Apis\\Type\\Shared\\V1\xe2\x02,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\xea\x02$Systemathics::Apis::Type::Shared::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.type.shared.v1.trade_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n$com.systemathics.apis.type.shared.v1B\016TradeDataProtoP\001\242\002\004SATS\252\002 Systemathics.Apis.Type.Shared.V1\312\002 Systemathics\\Apis\\Type\\Shared\\V1\342\002,Systemathics\\Apis\\Type\\Shared\\V1\\GPBMetadata\352\002$Systemathics::Apis::Type::Shared::V1'
  _globals['_TRADEDATA']._serialized_start=167
  _globals['_TRADEDATA']._serialized_end=326
# @@protoc_insertion_point(module_scope)
