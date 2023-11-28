# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/screener_data/v1/screener_data.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.type import date_pb2 as google_dot_type_dot_date__pb2
from systemathics.apis.type.shared.v1 import identifier_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_identifier__pb2
from systemathics.apis.type.shared.v1 import constraints_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_constraints__pb2
from systemathics.apis.services.static_data.v1 import static_data_pb2 as systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?systemathics/apis/services/screener_data/v1/screener_data.proto\x12+systemathics.apis.services.screener_data.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x32systemathics/apis/type/shared/v1/constraints.proto\x1a;systemathics/apis/services/static_data/v1/static_data.proto\"\x9c\x07\n\x0fScreenerRequest\x12\x31\n\x05start\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x05start\x12\x31\n\x05\x63ount\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.Int32ValueR\x05\x63ount\x12\x41\n\rbase_currency\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x0c\x62\x61seCurrency\x12\x38\n\x08\x65xchange\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueR\x08\x65xchange\x12h\n\x0e\x63\x61pitalization\x18\x05 \x01(\x0b\x32@.systemathics.apis.services.static_data.v1.StaticDataDoubleRangeR\x0e\x63\x61pitalization\x12V\n\x06\x65xpiry\x18\x06 \x01(\x0b\x32>.systemathics.apis.services.static_data.v1.StaticDataDateRangeR\x06\x65xpiry\x12V\n\x0boption_type\x18\x07 \x01(\x0e\x32\x35.systemathics.apis.services.static_data.v1.OptionTypeR\noptionType\x12\\\n\rexercise_type\x18\x08 \x01(\x0e\x32\x37.systemathics.apis.services.static_data.v1.ExerciseTypeR\x0c\x65xerciseType\x12V\n\x05\x64\x65lta\x18\t \x01(\x0b\x32@.systemathics.apis.services.static_data.v1.StaticDataDoubleRangeR\x05\x64\x65lta\x12o\n\x12implied_volatility\x18\n \x01(\x0b\x32@.systemathics.apis.services.static_data.v1.StaticDataDoubleRangeR\x11impliedVolatility\x12\x65\n\ropen_interest\x18\x0b \x01(\x0b\x32@.systemathics.apis.services.static_data.v1.StaticDataDoubleRangeR\x0copenInterest\"e\n\x10ScreenerResponse\x12Q\n\x06\x65quity\x18\x01 \x01(\x0b\x32\x39.systemathics.apis.services.static_data.v1.EquityResponseR\x06\x65quity2\xb5\x01\n\x0fScreenerService\x12\xa1\x01\n\x08Screener\x12<.systemathics.apis.services.screener_data.v1.ScreenerRequest\x1a=.systemathics.apis.services.screener_data.v1.ScreenerResponse\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/screenerdataB\x91\x02\n/com.systemathics.apis.services.screener_data.v1B\x11ScreenerDataProtoP\x01\xa2\x02\x04SASS\xaa\x02*Systemathics.Apis.Services.ScreenerData.V1\xca\x02*Systemathics\\Apis\\Services\\ScreenerData\\V1\xe2\x02\x36Systemathics\\Apis\\Services\\ScreenerData\\V1\\GPBMetadata\xea\x02.Systemathics::Apis::Services::ScreenerData::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.screener_data.v1.screener_data_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n/com.systemathics.apis.services.screener_data.v1B\021ScreenerDataProtoP\001\242\002\004SASS\252\002*Systemathics.Apis.Services.ScreenerData.V1\312\002*Systemathics\\Apis\\Services\\ScreenerData\\V1\342\0026Systemathics\\Apis\\Services\\ScreenerData\\V1\\GPBMetadata\352\002.Systemathics::Apis::Services::ScreenerData::V1'
  _globals['_SCREENERSERVICE'].methods_by_name['Screener']._options = None
  _globals['_SCREENERSERVICE'].methods_by_name['Screener']._serialized_options = b'\202\323\344\223\002\022\022\020/v1/screenerdata'
  _globals['_SCREENERREQUEST']._serialized_start=395
  _globals['_SCREENERREQUEST']._serialized_end=1319
  _globals['_SCREENERRESPONSE']._serialized_start=1321
  _globals['_SCREENERRESPONSE']._serialized_end=1422
  _globals['_SCREENERSERVICE']._serialized_start=1425
  _globals['_SCREENERSERVICE']._serialized_end=1606
# @@protoc_insertion_point(module_scope)
