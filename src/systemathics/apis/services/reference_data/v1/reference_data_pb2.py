# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: systemathics/apis/services/reference_data/v1/reference_data.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from systemathics.apis.type.shared.v1 import asset_pb2 as systemathics_dot_apis_dot_type_dot_shared_dot_v1_dot_asset__pb2
from systemathics.apis.services.daily.v1 import daily_bars_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__bars__pb2
from systemathics.apis.services.daily.v1 import daily_prices_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__prices__pb2
from systemathics.apis.services.daily.v1 import daily_vwap_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__vwap__pb2
from systemathics.apis.services.daily.v1 import daily_calendars_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__calendars__pb2
from systemathics.apis.services.daily.v1 import daily_open_interest_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__open__interest__pb2
from systemathics.apis.services.daily.v1 import daily_implied_volatility_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__implied__volatility__pb2
from systemathics.apis.services.daily.v1 import daily_settlement_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2
from systemathics.apis.services.daily.v1 import daily_greeks_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__greeks__pb2
from systemathics.apis.services.daily.v1 import daily_market_data_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__market__data__pb2
from systemathics.apis.services.corporate_actions.v1 import dividends_pb2 as systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2
from systemathics.apis.services.corporate_actions.v1 import splits_pb2 as systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_splits__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAsystemathics/apis/services/reference_data/v1/reference_data.proto\x12,systemathics.apis.services.reference_data.v1\x1a\x1cgoogle/api/annotations.proto\x1a,systemathics/apis/type/shared/v1/asset.proto\x1a\x34systemathics/apis/services/daily/v1/daily_bars.proto\x1a\x36systemathics/apis/services/daily/v1/daily_prices.proto\x1a\x34systemathics/apis/services/daily/v1/daily_vwap.proto\x1a\x39systemathics/apis/services/daily/v1/daily_calendars.proto\x1a=systemathics/apis/services/daily/v1/daily_open_interest.proto\x1a\x42systemathics/apis/services/daily/v1/daily_implied_volatility.proto\x1a:systemathics/apis/services/daily/v1/daily_settlement.proto\x1a\x36systemathics/apis/services/daily/v1/daily_greeks.proto\x1a;systemathics/apis/services/daily/v1/daily_market_data.proto\x1a?systemathics/apis/services/corporate_actions/v1/dividends.proto\x1a<systemathics/apis/services/corporate_actions/v1/splits.proto\"\x92\x01\n\x10ReferenceRequest\x12J\n\nasset_type\x18\x01 \x01(\x0e\x32+.systemathics.apis.type.shared.v1.AssetTypeR\tassetType\x12\x16\n\x06ticker\x18\x02 \x01(\tR\x06ticker\x12\x1a\n\x08\x65xchange\x18\x03 \x01(\tR\x08\x65xchange\"\x94\x07\n\x11ReferenceResponse\x12?\n\x03\x62\x61r\x18\x01 \x01(\x0b\x32-.systemathics.apis.services.daily.v1.DailyBarR\x03\x62\x61r\x12\x45\n\x05price\x18\x02 \x01(\x0b\x32/.systemathics.apis.services.daily.v1.DailyPriceR\x05price\x12\x42\n\x04vwap\x18\x03 \x01(\x0b\x32..systemathics.apis.services.daily.v1.DailyVwapR\x04vwap\x12N\n\x08\x63\x61lendar\x18\x04 \x01(\x0b\x32\x32.systemathics.apis.services.daily.v1.DailyCalendarR\x08\x63\x61lendar\x12T\n\nsettlement\x18\x05 \x01(\x0b\x32\x34.systemathics.apis.services.daily.v1.DailySettlementR\nsettlement\x12[\n\ropen_interest\x18\x06 \x01(\x0b\x32\x36.systemathics.apis.services.daily.v1.DailyOpenInterestR\x0copenInterest\x12j\n\x12implied_volatility\x18\x07 \x01(\x0b\x32;.systemathics.apis.services.daily.v1.DailyImpliedVolatilityR\x11impliedVolatility\x12H\n\x06greeks\x18\x08 \x01(\x0b\x32\x30.systemathics.apis.services.daily.v1.DailyGreeksR\x06greeks\x12U\n\x08\x64ividend\x18\t \x01(\x0b\x32\x39.systemathics.apis.services.corporate_actions.v1.DividendR\x08\x64ividend\x12L\n\x05split\x18\n \x01(\x0b\x32\x36.systemathics.apis.services.corporate_actions.v1.SplitR\x05split\x12U\n\x0bmarket_data\x18\x0b \x01(\x0b\x32\x34.systemathics.apis.services.daily.v1.DailyMarketDataR\nmarketData2\xbc\x01\n\x10ReferenceService\x12\xa7\x01\n\tReference\x12>.systemathics.apis.services.reference_data.v1.ReferenceRequest\x1a?.systemathics.apis.services.reference_data.v1.ReferenceResponse\"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v1/referencedataB\x97\x02\n0com.systemathics.apis.services.reference_data.v1B\x12ReferenceDataProtoP\x01\xa2\x02\x04SASR\xaa\x02+Systemathics.Apis.Services.ReferenceData.V1\xca\x02+Systemathics\\Apis\\Services\\ReferenceData\\V1\xe2\x02\x37Systemathics\\Apis\\Services\\ReferenceData\\V1\\GPBMetadata\xea\x02/Systemathics::Apis::Services::ReferenceData::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'systemathics.apis.services.reference_data.v1.reference_data_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n0com.systemathics.apis.services.reference_data.v1B\022ReferenceDataProtoP\001\242\002\004SASR\252\002+Systemathics.Apis.Services.ReferenceData.V1\312\002+Systemathics\\Apis\\Services\\ReferenceData\\V1\342\0027Systemathics\\Apis\\Services\\ReferenceData\\V1\\GPBMetadata\352\002/Systemathics::Apis::Services::ReferenceData::V1'
  _globals['_REFERENCESERVICE'].methods_by_name['Reference']._loaded_options = None
  _globals['_REFERENCESERVICE'].methods_by_name['Reference']._serialized_options = b'\202\323\344\223\002\023\022\021/v1/referencedata'
  _globals['_REFERENCEREQUEST']._serialized_start=850
  _globals['_REFERENCEREQUEST']._serialized_end=996
  _globals['_REFERENCERESPONSE']._serialized_start=999
  _globals['_REFERENCERESPONSE']._serialized_end=1915
  _globals['_REFERENCESERVICE']._serialized_start=1918
  _globals['_REFERENCESERVICE']._serialized_end=2106
# @@protoc_insertion_point(module_scope)
