# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/static_data/v1/sector.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6systemathics/apis/services/static_data/v1/sector.proto\x12)systemathics.apis.services.static_data.v1\x1a\x1cgoogle/api/annotations.proto\"b\n\rSectorRequest\x12\x1a\n\x08provider\x18\x01 \x01(\tR\x08provider\x12\x14\n\x04\x63ode\x18\x02 \x01(\tH\x00R\x04\x63ode\x12\x16\n\x05level\x18\x03 \x01(\x05H\x00R\x05levelB\x07\n\x05value\"\x94\x01\n\x0eSectorResponse\x12J\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x36.systemathics.apis.services.static_data.v1.SectorLevelR\x04\x64\x61ta\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x14\n\x05\x63ount\x18\x03 \x01(\x05R\x05\x63ount\"\x81\x01\n\x0bSectorLevel\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12\x14\n\x05index\x18\x02 \x01(\x05R\x05index\x12\x12\n\x04\x63ode\x18\x03 \x01(\tR\x04\x63ode\x12\x1e\n\ndefinition\x18\x04 \x01(\tR\ndefinition\x12\x14\n\x05label\x18\x05 \x01(\tR\x05label2\xae\x01\n\rSectorService\x12\x9c\x01\n\x06Sector\x12\x38.systemathics.apis.services.static_data.v1.SectorRequest\x1a\x39.systemathics.apis.services.static_data.v1.SectorResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\x12\x15/v1/staticdata/sectorB\x81\x02\n-com.systemathics.apis.services.static_data.v1B\x0bSectorProtoP\x01\xa2\x02\x04SASS\xaa\x02(Systemathics.Apis.Services.StaticData.V1\xca\x02(Systemathics\\Apis\\Services\\StaticData\\V1\xe2\x02\x34Systemathics\\Apis\\Services\\StaticData\\V1\\GPBMetadata\xea\x02,Systemathics::Apis::Services::StaticData::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.static_data.v1.sector_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n-com.systemathics.apis.services.static_data.v1B\013SectorProtoP\001\242\002\004SASS\252\002(Systemathics.Apis.Services.StaticData.V1\312\002(Systemathics\\Apis\\Services\\StaticData\\V1\342\0024Systemathics\\Apis\\Services\\StaticData\\V1\\GPBMetadata\352\002,Systemathics::Apis::Services::StaticData::V1'
  _globals['_SECTORSERVICE'].methods_by_name['Sector']._options = None
  _globals['_SECTORSERVICE'].methods_by_name['Sector']._serialized_options = b'\202\323\344\223\002\027\022\025/v1/staticdata/sector'
  _globals['_SECTORREQUEST']._serialized_start=131
  _globals['_SECTORREQUEST']._serialized_end=229
  _globals['_SECTORRESPONSE']._serialized_start=232
  _globals['_SECTORRESPONSE']._serialized_end=380
  _globals['_SECTORLEVEL']._serialized_start=383
  _globals['_SECTORLEVEL']._serialized_end=512
  _globals['_SECTORSERVICE']._serialized_start=515
  _globals['_SECTORSERVICE']._serialized_end=689
# @@protoc_insertion_point(module_scope)
