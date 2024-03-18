# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/corporate_actions/v1/splits.proto
# Protobuf Python Version: 5.26.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import date_interval_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_date__interval__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<systemathics/apis/services/corporate_actions/v1/splits.proto\x12/systemathics.apis.services.corporate_actions.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xb2\x01\n\rSplitsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\"\\\n\x0eSplitsResponse\x12J\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x36.systemathics.apis.services.corporate_actions.v1.SplitR\x04\x64\x61ta\"\x82\x01\n\x05Split\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x1d\n\nnew_shares\x18\x02 \x01(\x01R\tnewShares\x12\x1d\n\nold_shares\x18\x03 \x01(\x01R\toldShares\x12\x14\n\x05score\x18\x04 \x01(\x01R\x05score2\xc1\x01\n\rSplitsService\x12\xaf\x01\n\x06Splits\x12>.systemathics.apis.services.corporate_actions.v1.SplitsRequest\x1a?.systemathics.apis.services.corporate_actions.v1.SplitsResponse\"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/corporate-actions/splitsB\x9f\x02\n3com.systemathics.apis.services.corporate_actions.v1B\x0bSplitsProtoP\x01\xa2\x02\x04SASC\xaa\x02.Systemathics.Apis.Services.CorporateActions.V1\xca\x02.Systemathics\\Apis\\Services\\CorporateActions\\V1\xe2\x02:Systemathics\\Apis\\Services\\CorporateActions\\V1\\GPBMetadata\xea\x02\x32Systemathics::Apis::Services::CorporateActions::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.corporate_actions.v1.splits_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n3com.systemathics.apis.services.corporate_actions.v1B\013SplitsProtoP\001\242\002\004SASC\252\002.Systemathics.Apis.Services.CorporateActions.V1\312\002.Systemathics\\Apis\\Services\\CorporateActions\\V1\342\002:Systemathics\\Apis\\Services\\CorporateActions\\V1\\GPBMetadata\352\0022Systemathics::Apis::Services::CorporateActions::V1'
  _globals['_SPLITSSERVICE'].methods_by_name['Splits']._loaded_options = None
  _globals['_SPLITSSERVICE'].methods_by_name['Splits']._serialized_options = b'\202\323\344\223\002\036\022\034/v1/corporate-actions/splits'
  _globals['_SPLITSREQUEST']._serialized_start=273
  _globals['_SPLITSREQUEST']._serialized_end=451
  _globals['_SPLITSRESPONSE']._serialized_start=453
  _globals['_SPLITSRESPONSE']._serialized_end=545
  _globals['_SPLIT']._serialized_start=548
  _globals['_SPLIT']._serialized_end=678
  _globals['_SPLITSSERVICE']._serialized_start=681
  _globals['_SPLITSSERVICE']._serialized_end=874
# @@protoc_insertion_point(module_scope)
