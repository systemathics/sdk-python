# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/tick/v1/tick_updates.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.type.shared.v1 import keys_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_keys__pb2
from systemathics.apis.type.shared.v1 import identifier_and_level_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__and__level__pb2
from systemathics.apis.type.shared.v1 import market_fields_updates_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_market__fields__updates__pb2
from systemathics.apis.type.shared.v1 import mbl_market_book_updates_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_mbl__market__book__updates__pb2
from systemathics.apis.type.shared.v1 import mbo_market_book_updates_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_mbo__market__book__updates__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5systemathics/apis/services/tick/v1/tick_updates.proto\x12\"systemathics.apis.services.tick.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a+systemathics/apis/type/shared/v1/keys.proto\x1a;systemathics/apis/type/shared/v1/identifier_and_level.proto\x1a<systemathics/apis/type/shared/v1/market_fields_updates.proto\x1a>systemathics/apis/type/shared/v1/mbl_market_book_updates.proto\x1a>systemathics/apis/type/shared/v1/mbo_market_book_updates.proto\"\xdd\x01\n\x12TickUpdatesRequest\x12V\n\x0bidentifiers\x18\x01 \x03(\x0b\x32\x34.systemathics.apis.type.shared.v1.IdentifierAndLevelR\x0bidentifiers\x12O\n\x0b\x63onstraints\x18\x02 \x01(\x0b\x32-.systemathics.apis.type.shared.v1.ConstraintsR\x0b\x63onstraints\x12\x1e\n\nadjustment\x18\x03 \x01(\x08R\nadjustment\"\x8c\x03\n\x13TickUpdatesResponse\x12^\n\x0e\x66ields_updates\x18\x01 \x01(\x0b\x32\x35.systemathics.apis.type.shared.v1.MarketFieldsUpdatesH\x00R\rfieldsUpdates\x12\x62\n\x10mbl_book_updates\x18\x02 \x01(\x0b\x32\x36.systemathics.apis.type.shared.v1.MblMarketBookUpdatesH\x00R\x0emblBookUpdates\x12\x62\n\x10mbo_book_updates\x18\x03 \x01(\x0b\x32\x36.systemathics.apis.type.shared.v1.MboMarketBookUpdatesH\x00R\x0emboBookUpdates\x12\x42\n\x07mapping\x18\x04 \x01(\x0b\x32&.systemathics.apis.type.shared.v1.KeysH\x00R\x07mappingB\t\n\x07payload2\xb1\x01\n\x12TickUpdatesService\x12\x9a\x01\n\x0bTickUpdates\x12\x36.systemathics.apis.services.tick.v1.TickUpdatesRequest\x1a\x37.systemathics.apis.services.tick.v1.TickUpdatesResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/tick/updates0\x01\x42\xe7\x01\n&com.systemathics.apis.services.tick.v1B\x10TickUpdatesProtoP\x01\xa2\x02\x04SAST\xaa\x02\"Systemathics.Apis.Services.Tick.V1\xca\x02\"Systemathics\\Apis\\Services\\Tick\\V1\xe2\x02.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\xea\x02&Systemathics::Apis::Services::Tick::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.tick.v1.tick_updates_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n&com.systemathics.apis.services.tick.v1B\020TickUpdatesProtoP\001\242\002\004SAST\252\002\"Systemathics.Apis.Services.Tick.V1\312\002\"Systemathics\\Apis\\Services\\Tick\\V1\342\002.Systemathics\\Apis\\Services\\Tick\\V1\\GPBMetadata\352\002&Systemathics::Apis::Services::Tick::V1'
  _globals['_TICKUPDATESSERVICE'].methods_by_name['TickUpdates']._options = None
  _globals['_TICKUPDATESSERVICE'].methods_by_name['TickUpdates']._serialized_options = b'\202\323\344\223\002\022\022\020/v1/tick/updates'
  _globals['_TICKUPDATESREQUEST']._serialized_start=472
  _globals['_TICKUPDATESREQUEST']._serialized_end=693
  _globals['_TICKUPDATESRESPONSE']._serialized_start=696
  _globals['_TICKUPDATESRESPONSE']._serialized_end=1092
  _globals['_TICKUPDATESSERVICE']._serialized_start=1095
  _globals['_TICKUPDATESSERVICE']._serialized_end=1272
# @@protoc_insertion_point(module_scope)