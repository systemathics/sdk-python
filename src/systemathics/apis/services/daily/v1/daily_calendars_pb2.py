# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/daily/v1/daily_calendars.proto
# Protobuf Python Version: 4.25.1
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


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9systemathics/apis/services/daily/v1/daily_calendars.proto\x12#systemathics.apis.services.daily.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x16google/type/date.proto\x1a\x31systemathics/apis/type/shared/v1/identifier.proto\x1a\x34systemathics/apis/type/shared/v1/date_interval.proto\"\xba\x01\n\x15\x44\x61ilyCalendarsRequest\x12L\n\nidentifier\x18\x01 \x01(\x0b\x32,.systemathics.apis.type.shared.v1.IdentifierR\nidentifier\x12S\n\rdate_interval\x18\x02 \x01(\x0b\x32..systemathics.apis.type.shared.v1.DateIntervalR\x0c\x64\x61teInterval\"`\n\x16\x44\x61ilyCalendarsResponse\x12\x46\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x32.systemathics.apis.services.daily.v1.DailyCalendarR\x04\x64\x61ta\"\xa1\x01\n\rDailyCalendar\x12%\n\x04\x64\x61te\x18\x01 \x01(\x0b\x32\x11.google.type.DateR\x04\x64\x61te\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\x12\x1d\n\nis_holiday\x18\x04 \x01(\x08R\tisHoliday\x12\x14\n\x05score\x18\x05 \x01(\x01R\x05score2\xc0\x01\n\x15\x44\x61ilyCalendarsService\x12\xa6\x01\n\x0e\x44\x61ilyCalendars\x12:.systemathics.apis.services.daily.v1.DailyCalendarsRequest\x1a;.systemathics.apis.services.daily.v1.DailyCalendarsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/daily/calendarsB\xef\x01\n\'com.systemathics.apis.services.daily.v1B\x13\x44\x61ilyCalendarsProtoP\x01\xa2\x02\x04SASD\xaa\x02#Systemathics.Apis.Services.Daily.V1\xca\x02#Systemathics\\Apis\\Services\\Daily\\V1\xe2\x02/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\xea\x02\'Systemathics::Apis::Services::Daily::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.daily.v1.daily_calendars_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\'com.systemathics.apis.services.daily.v1B\023DailyCalendarsProtoP\001\242\002\004SASD\252\002#Systemathics.Apis.Services.Daily.V1\312\002#Systemathics\\Apis\\Services\\Daily\\V1\342\002/Systemathics\\Apis\\Services\\Daily\\V1\\GPBMetadata\352\002\'Systemathics::Apis::Services::Daily::V1'
  _globals['_DAILYCALENDARSSERVICE'].methods_by_name['DailyCalendars']._options = None
  _globals['_DAILYCALENDARSSERVICE'].methods_by_name['DailyCalendars']._serialized_options = b'\202\323\344\223\002\025\022\023/v1/daily/calendars'
  _globals['_DAILYCALENDARSREQUEST']._serialized_start=258
  _globals['_DAILYCALENDARSREQUEST']._serialized_end=444
  _globals['_DAILYCALENDARSRESPONSE']._serialized_start=446
  _globals['_DAILYCALENDARSRESPONSE']._serialized_end=542
  _globals['_DAILYCALENDAR']._serialized_start=545
  _globals['_DAILYCALENDAR']._serialized_end=706
  _globals['_DAILYCALENDARSSERVICE']._serialized_start=709
  _globals['_DAILYCALENDARSSERVICE']._serialized_end=901
# @@protoc_insertion_point(module_scope)
