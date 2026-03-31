"""Systemathics Ganymede  API Token Helpers

This module helps to create tokens to access Systemathics Ganymede authenticated API.

functions:
    get_cds_index_daily - Get CDS Index daily data as a DataFrame using Ganymede gRPC API.
    get_cds_index_intraday - Get CDS Index intraday data as a DataFrame using Ganymede gRPC API.
    get_cds_daily - Get CDS daily data as a DataFrame using Ganymede gRPC API.
    get_cds_intraday - Get CDS intraday data as a DataFrame using Ganymede gRPC API.
    get_index_tick - Get Index tick data as a DataFrame using Ganymede gRPC API.
    get_future_daily - Get future daily data as a DataFrame using Ganymede gRPC API.
    get_equity_daily - Get equity daily data as a DataFrame using Ganymede gRPC API.
    get_equity_intraday - Get equity intraday data as a DataFrame using Ganymede gRPC API.
    get_future_intraday - Get future intraday data as a DataFrame using Ganymede gRPC API.
    get_cds_index_option_daily - Get CDS Index option daily data as a DataFrame using Ganymede gRPC API.
    get_cds_index_option_by_underlier - Get CDS Index option data filtered by underlier as a DataFrame using Ganymede gRPC API.
"""


import grpc
import pandas as pd
from datetime import date,datetime
from google.type import date_pb2
import google.protobuf.wrappers_pb2 as wrappers_pb2


from systemathics.apis.type.shared.v1 import asset_pb2 as asset
from systemathics.apis.type.shared.v1 import constraints_pb2 as constraints
from systemathics.apis.type.shared.v1 import date_interval_pb2 as date_interval
from systemathics.apis.type.shared.v1 import time_interval_pb2 as time_interval
from google.type import timeofday_pb2 as timeofday
import systemathics.apis.type.shared.v1.sampling_pb2 as sampling
import systemathics.apis.type.shared.v1.identifier_pb2 as identifier
import systemathics.apis.services.daily.v1.daily_bars_pb2 as daily_bars
import systemathics.apis.services.intraday.v1.intraday_bars_pb2 as intraday_bars
import systemathics.apis.services.intraday.v1.intraday_bars_pb2_grpc as intraday_bars_service
import systemathics.apis.services.daily.v1.daily_bars_pb2_grpc as daily_bars_service
import systemathics.apis.services.daily.v2.get_daily_pb2 as get_daily
import systemathics.apis.services.daily.v2.get_daily_pb2_grpc as get_daily_service
import systemathics.apis.services.intraday.v2.get_intraday_pb2 as get_intraday
import systemathics.apis.services.intraday.v2.get_intraday_pb2_grpc as get_intraday_service
import systemathics.apis.services.tick.v2.get_tick_pb2 as get_tick
import systemathics.apis.services.tick.v2.get_tick_pb2_grpc as get_tick_service
import systemathics.apis.type.shared.v1.option_type_pb2 as OptionType
import systemathics.apis.type.shared.v1.strike_type_pb2 as StrikeType
import systemathics.apis.type.shared.v1.filter_pb2 as filter


import systemathics.apis.helpers.token_helpers as token_helpers
import systemathics.apis.helpers.channel_helpers as channel_helpers


from typing import Union, Tuple, Optional

# Type aliases for readability
StrikeInput   = Union[float, Tuple[Optional[float], Optional[float]]]
MaturityInput = Union[datetime.date, str, Tuple[Optional[Union[datetime.date, str]], Optional[Union[datetime.date, str]]]]

# ---------------------------------------------------------------------------

def get_cds_index_option_by_underlier(
    ticker: str,
    start_date=None,
    end_date=None,
    selected_fields=None,
    provider: str = "JPMorgan",
    maturity_date: Optional[MaturityInput] = None,
    strike_interval: Optional[StrikeInput] = None,
    option_type=None,
    strike_type=None,
):
    """
    Fetch CDS Index Option daily data from gRPC API for a given underlier ticker.

    Parameters
    ----------
    ticker : str
        The underlier ticker symbol, e.g. "ITXEB544".
    start_date : date | str | None
        Start of the observation date range (inclusive). No lower bound if None.
    end_date : date | str | None
        End of the observation date range (exclusive). No upper bound if None.
    selected_fields : list[str] | None
        Subset of double fields to retrieve. Retrieves all fields when None.
    provider : str
        Data provider name. Default is "JPMorgan".
    maturity_date : date | str | (start, end) tuple | None
        Filter on option maturity date.
        - Single value  → exact match,  e.g. "2025-06-20"
        - 2-tuple       → date range,   e.g. ("2025-03-01", "2025-12-31")
          Either element may be None for an open-ended bound.
    strike_interval : float | (min, max) tuple | None
        Filter on strike value.
        - Single float  → exact match,  e.g. 100.0
        - 2-tuple       → range,        e.g. (80.0, 120.0)
          Either element may be None for an open-ended bound.
    option_type : OptionType | None
        Optional filter: OPTION_TYPE_CALL, OPTION_TYPE_PUT, etc.
    strike_type : StrikeType | None
        Optional filter: STRIKE_TYPE_FIXED, STRIKE_TYPE_FLOATING_DELTA, etc.

    Returns
    -------
    pd.DataFrame
        Multi-indexed DataFrame (Date, MaturityDate, Strike, OptionType, StrikeType)
        with the requested double fields as columns. Empty DataFrame on error.
    """

    ALL_FIELDS = [
        "ImpliedVol", "Premium", "Delta", "Gamma", "Theta", "Vega",
        "StrikePrice", "StrikeDuration", "AtTheMoneyForwardSpread",
        "AtTheMoneyForwardPrice", "AtTheMoneyForwardDuration",
        "RefIndexSpread", "RefIndexPrice",
    ]

    if selected_fields is None:
        fields = ALL_FIELDS
    else:
        fields = [f for f in selected_fields if f in ALL_FIELDS]
        if not fields:
            raise ValueError(f"No valid fields. Available: {ALL_FIELDS}")

    # Identifier
    id_ = identifier.Identifier(
        asset_type=asset.AssetType.ASSET_TYPE_CDS_INDEX,
        ticker=ticker,
    )
    id_.provider.value = provider

    # Observation date interval (required by proto)
    di_kwargs = {}
    if start_date is not None:
        di_kwargs["start_date"] = _parse_date_input(start_date)
    if end_date is not None:
        di_kwargs["end_date"] = _parse_date_input(end_date)
    di = date_interval.DateInterval(**di_kwargs)

    # Build request
    request_kwargs = {
        "identifier":    id_,
        "date_interval": di,
        "double_fields": fields,
    }

    if maturity_date is not None:
        request_kwargs["maturity_date"] = _build_maturity_filter(maturity_date)
    if strike_interval is not None:
        request_kwargs["strike_interval"] = _build_strike_filter(strike_interval)
    if option_type is not None:
        request_kwargs["option_type"] = _parse_option_type(option_type)
    if strike_type is not None:
        request_kwargs["strike_type"] = _parse_strike_type(strike_type)

    request = get_daily.DailyOptionUnderlierWithStrikeTypeRequest(**request_kwargs)

    # Stream & parse
    try:
        with channel_helpers.get_grpc_channel() as channel:
            token = token_helpers.get_token()
            service = get_daily_service.DailyServiceStub(channel)

            field_names = []
            rows = []

            for msg in service.DailyOptionUnderlierWithStrikeTypeStream(
                request=request,
                metadata=[("authorization", token)],
            ):
                payload = msg.WhichOneof("payload")

                if payload == "info":
                    field_names = list(msg.info.fields)

                elif payload == "double_data":
                    item = msg.double_data
                    row = {
                        "Date": pd.Timestamp(
                            year=item.date.year,
                            month=item.date.month,
                            day=item.date.day,
                        ),
                        "MaturityDate": pd.Timestamp(
                            year=item.maturity_date.year,
                            month=item.maturity_date.month,
                            day=item.maturity_date.day,
                        ),
                        "Strike":     item.strike,
                        "OptionType": _format_option_type(item.option_type),
                        "StrikeType": _format_strike_type(item.strike_type),
                    }
                    for field, value in zip(field_names, item.data):
                        row[field] = value
                    rows.append(row)

        if not rows:
            print("No data received.")
            return pd.DataFrame()

        return (
            pd.DataFrame(rows)
            .set_index(["Date", "MaturityDate", "Strike", "OptionType", "StrikeType"])
            .sort_index()
        )

    except grpc.RpcError as e:
        print(f"gRPC Error [{e.code().name}]: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()



def get_cds_index_option_daily(ticker, start_date=None, end_date=None, selected_fields=None, provider="JPMorgan"):
    """
    Fetch CDS Index Option daily data from gRPC API for a given ticker and date range.
    
    Parameters:
    ticker (str): The ticker symbol, ex: ITXEB544-202606-100-Pay
    start_date (datetime.date or str, optional): Start date for data retrieval. 
                                                 If None, set not limits
    end_date (datetime.date or str, optional): End date for data retrieval.
                                               If None, uses today's date
    selected_fields (list, optional): List of specific fields to retrieve. If None, gets all fields.
    provider (str): Data provider, default is "JPMorgan"
    
    Returns:
    pd.DataFrame: DataFrame with Date as index and all available fields as columns
    """
    

    
    # All available fields
    all_fields = [
                    "ImpliedVol",
                    "Premium",
                    "Delta",
                    "Gamma",
                    "Theta",
                    "Vega",
                    "StrikePrice",
                    "StrikeDuration",
                    "AtTheMoneyForwardSpread",
                    "AtTheMoneyForwardPrice",
                    "AtTheMoneyForwardDuration",
                    "RefIndexSpread",
                    "RefIndexPrice"
    ]
    
    # Use all fields if none specified, otherwise validate selected fields
    if selected_fields is None:
        fields = all_fields
    else:
        fields = [f for f in selected_fields if f in all_fields]
        if not fields:
            raise ValueError("No valid fields selected")
        
    # Create identifier
    id = identifier.Identifier(
        asset_type=asset.AssetType.ASSET_TYPE_CDS_INDEX_OPTION,
        ticker=ticker
    )
    id.provider.value = provider
    
    # Build constraints only if we have at least one date
    constraints_obj = None
    if start_date is not None or end_date is not None:
        # Create DateInterval with only the dates that are provided
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)
        
        constraints_obj = constraints.Constraints(
            date_intervals=[date_interval.DateInterval(**date_interval_kwargs)]
        )

    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()
            first = True
            rows = []
            field_names = []
            # Create service stub
            service = get_daily_service.DailyServiceStub(channel)
            

            
            # Create request with or without constraints
            request_kwargs = {
                'identifier': id,
                'fields': fields
            }
            if constraints_obj is not None:
                request_kwargs['constraints'] = constraints_obj
            
            request = get_daily.DailyRequest(**request_kwargs)
            
            for data in service.DailyScalarStream(
                request=request, 
                metadata=[('authorization', token)] 
            ):
                if first:
                    field_names = list(data.info.fields)
                    first = False
                else:
                    row = {'Date': pd.Timestamp(year=data.data.date.year, month=data.data.date.month, day=data.data.date.day)}
                    for field, value in zip(field_names, data.data.data):
                        row[field] = value
                    rows.append(row)

    
        # Process the response
        if not rows or not field_names:
            print("No data received")
            return pd.DataFrame()

        # Sort by date for better readability
        df = pd.DataFrame(rows).set_index('Date').sort_index()

        return df
        
    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()



def get_cds_index_daily(ticker, start_date=None, end_date=None, batch=None, selected_fields=None, provider="Markit"):
    """
    Fetch CDS Index daily data from gRPC API for a given ticker and date range.
    
    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval. 
                                                 If None, set not limits
    end_date (datetime.date or str, optional): End date for data retrieval.
                                               If None, uses today's date
    batch (str, optional): Batch name to be used for filtering. If None, gets all batches.
    selected_fields (list, optional): List of specific fields to retrieve. If None, gets all fields.
    provider (str): Data provider, default is "Markit"
    
    Returns:
    pd.DataFrame: DataFrame with Date as index and all available fields as columns
    """
    

    
    # All available fields
    all_fields = [
        "CompositePriceAsk", "CompositePriceBid", "CompositeSpreadAsk",
        "CompositeSpreadBid", "ConventionalSpread", "CreditDv01",
        "DefaultProbability", "Heat", "IrDv01", "JumpToDefault",
        "JumpToZero", "ModelPrice", "ModelSpread", "Price",
        "Rec01", "RiskyPv01", "SkewPrice", "SkewSpread"
    ]
    
    # Use all fields if none specified, otherwise validate selected fields
    if selected_fields is None:
        fields = all_fields
    else:
        fields = [f for f in selected_fields if f in all_fields]
        if not fields:
            raise ValueError("No valid fields selected")
        
    # Create identifier
    id = identifier.Identifier(
        asset_type=asset.AssetType.ASSET_TYPE_CDS_INDEX,
        ticker=ticker
    )
    id.provider.value = provider
    
    # Build constraints only if we have at least one date
    constraints_obj = None
    if start_date is not None or end_date is not None:
        # Create DateInterval with only the dates that are provided
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)
        
        constraints_obj = constraints.Constraints(
            date_intervals=[date_interval.DateInterval(**date_interval_kwargs)]
        )
    
    if batch is None:
        # Create request with or without constraints
        request_kwargs = {
            'identifier': id,
            'fields': fields
        }
        if constraints_obj is not None:
            request_kwargs['constraints'] = constraints_obj
    
    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()
            first = True
            rows = []
            field_names = []
            # Create service stub
            service = get_daily_service.DailyServiceStub(channel)
            

            if batch is None:
                          # Create request with or without constraints
                request_kwargs = {
                    'identifier': id,
                    'fields': fields
                }
                if constraints_obj is not None:
                    request_kwargs['constraints'] = constraints_obj
                
                vector_request = get_daily.DailyRequest(**request_kwargs)
                
                for data in service.DailyVectorStream(
                    request=vector_request, 
                    metadata=[('authorization', token)] 
                ):
                    if first:
                        field_names = list(data.info.fields)
                        first = False
                    else:
                        row = {'Date': pd.Timestamp(year=data.data.date.year, month=data.data.date.month, day=data.data.date.day)}
                        for field, value in zip(field_names, data.data.data):
                            row[field] = value
                        rows.append(row)
            
            else:
                
                request_kwargs = {
                    'identifier': id,
                    'fields': fields,
                    'key': batch
                }
                if constraints_obj is not None:
                    request_kwargs['constraints'] = constraints_obj
                    
                vector_key_request = get_daily.DailyVectorKeyRequest(**request_kwargs)
                
                for data in service.DailyVectorKeyStream(
                    request=vector_key_request, 
                    metadata=[('authorization', token)]
                ):
                    if first:
                        field_names = list(data.info.fields)
                        first = False
                    else:
                        row = {'Date': pd.Timestamp(year=data.data.date.year, month=data.data.date.month, day=data.data.date.day)}
                        for field, value in zip(field_names, data.data.data):
                            row[field] = value
                        rows.append(row)
    
        # Process the response
        if not rows or not field_names:
            print("No data received")
            return pd.DataFrame()

        # Sort by date for better readability
        df = pd.DataFrame(rows).set_index('Date').sort_index()

        return df
        
    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()

def get_cds_daily(ticker, start_date=None, end_date=None, batch=None, selected_fields=None, provider="Markit"):
    """
    Fetch CDS daily data from gRPC API for a given ticker and date range.
    
    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval. 
                                                 If None, set not limits
    end_date (datetime.date or str, optional): End date for data retrieval.
                                               If None, uses today's date
    batch (str, optional): Batch name to be used for filtering. If None, gets all batches.
    selected_fields (list, optional): List of specific fields to retrieve. If None, gets all fields.
    provider (str): Data provider, default is "Markit"
    
    Returns:
    pd.DataFrame: DataFrame with Date as index and all available fields as columns
    """
    

    
    # All available fields for individual CDS
    all_fields = [
        "ConventionalSpread",
        "ParSpread",
        "Upfront",
        "RealRecovery",
        "AssumedRecovery",
        "DefaultProbability",
        "JumpToDefault",
        "JumpToZero"
    ]
    
    # Use all fields if none specified, otherwise validate selected fields
    if selected_fields is None:
        fields = all_fields
    else:
        fields = [f for f in selected_fields if f in all_fields]
        if not fields:
            raise ValueError("No valid fields selected")
        
    # Create identifier for individual CDS (not index)
    id = identifier.Identifier(
        asset_type=asset.AssetType.ASSET_TYPE_CDS,
        ticker=ticker
    )
    id.provider.value = provider
    
    # Build constraints only if we have at least one date
    constraints_obj = None
    if start_date is not None or end_date is not None:
        # Create DateInterval with only the dates that are provided
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)
        
        constraints_obj = constraints.Constraints(
            date_intervals=[date_interval.DateInterval(**date_interval_kwargs)]
        )
    
    if batch is None:
        # Create request with or without constraints
        request_kwargs = {
            'identifier': id,
            'fields': fields
        }
        if constraints_obj is not None:
            request_kwargs['constraints'] = constraints_obj
    
    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()
            first = True
            rows = []
            field_names = []
            # Create service stub
            service = get_daily_service.DailyServiceStub(channel)
            

            if batch is None:
                          # Create request with or without constraints
                request_kwargs = {
                    'identifier': id,
                    'fields': fields
                }
                if constraints_obj is not None:
                    request_kwargs['constraints'] = constraints_obj
                
                vector_request = get_daily.DailyRequest(**request_kwargs)
                
                for data in service.DailyVectorStream(
                    request=vector_request, 
                    metadata=[('authorization', token)] 
                ):
                    if first:
                        field_names = list(data.info.fields)
                        first = False
                    else:
                        row = {'Date': pd.Timestamp(year=data.data.date.year, month=data.data.date.month, day=data.data.date.day)}
                        for field, value in zip(field_names, data.data.data):
                            row[field] = value
                        rows.append(row)
            else:
                request_kwargs = {
                    'identifier': id,
                    'fields': fields,
                    'key': batch
                }
                if constraints_obj is not None:
                    request_kwargs['constraints'] = constraints_obj
                    
                vector_key_request = get_daily.DailyVectorKeyRequest(**request_kwargs)
                
                for data in service.DailyVectorKeyStream(
                    request=vector_key_request, 
                    metadata=[('authorization', token)]
                ):
                    if first:
                        field_names = list(data.info.fields)
                        first = False
                    else:
                        row = {'Date': pd.Timestamp(year=data.data.date.year, month=data.data.date.month, day=data.data.date.day)}
                        for field, value in zip(field_names, data.data.data):
                            row[field] = value
                        rows.append(row)

        # Process the response
        if not rows or not field_names:
            print("No data received")
            return pd.DataFrame()

        # Sort by date for better readability
        df = pd.DataFrame(rows).set_index('Date').sort_index()

        return df
        
    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()

def get_index_tick(ticker, start_date=None, end_date=None, start_time=None, end_time=None, selected_fields=None, provider="GoldmanSachs"):
    """
    Fetch Index tick data from gRPC API for a given ticker and date range with optional client-side time filtering.    
    
    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval.
                                                 If None, set no limits
    end_date (datetime.date or str, optional): End date for data retrieval.
                                               If None, set no limits
    start_time (str, optional): Start time in 'HH:MM' format (e.g., '09:30') or 'HH:MM:ss' format (e.g., '09:30:05') or for client-side filtering.
                                If None, no time restriction
    end_time (str, optional): End time in 'HH:MM' format (e.g., '16:00') or 'HH:MM:ss' format (e.g., '16:25:45')for client-side filtering.
                              If None, no time restriction
    selected_fields (list, optional): List of specific fields to retrieve.
                                      If None, gets all fields.
    provider (str): Data provider, default is "GoldmanSachs"
    
    Returns:
    pd.DataFrame: DataFrame with Datetime as index and all available fields as columns
    """

    # All available fields for Index tick data
    all_fields = [
        "AskBenchmarkSpread",
        "AskCleanPrice", 
        "AskDirtyPrice",
        "AskGSpread",
        "AskModifiedDuration",
        "AskYield",
        "AskZSpread",
        "BidBenchmarkSpread",
        "BidCleanPrice",
        "BidDirtyPrice", 
        "BidGSpread",
        "BidModifiedDuration",
        "BidYield",
        "BidZSpread",
        "MidBenchmarkSpread",
        "MidCleanPrice",
        "MidDirtyPrice",
        "MidGSpread", 
        "MidModifiedDuration",
        "MidYield",
        "MidZSpread",
        "OfficialBenchmarkSpread",
        "OfficialCleanPrice",
        "OfficialDirtyPrice",
        "OfficialGSpread",
        "OfficialModifiedDuration", 
        "OfficialYield",
        "OfficialZSpread"
    ]    
    
    # Use all fields if none specified, otherwise validate selected fields
    if selected_fields is None:
        fields = all_fields
    else:
        fields = [f for f in selected_fields if f in all_fields]
        if not fields:
            raise ValueError("No valid fields selected")
    
    # Create identifier for Index
    id = identifier.Identifier(
        asset_type=asset.AssetType.ASSET_TYPE_INDEX,
        ticker=ticker
    )
    id.provider.value = provider
    
    # Build constraints only if we have at least one date (no time intervals due to server limitation)
    constraints_obj = None
    if start_date is not None or end_date is not None:
        # Create DateInterval with only the dates that are provided
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)
            
        constraints_obj = constraints.Constraints(
            date_intervals=[date_interval.DateInterval(**date_interval_kwargs)]
        )

    # Create request with or without constraints
    request_kwargs = {
        'identifier': id,
        'fields': fields
    }

    if constraints_obj is not None:
        request_kwargs['constraints'] = constraints_obj
        
    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()
            first = True
            rows = []
            field_names = []
            # Create service stub for Tick service
            service = get_tick_service.TickServiceStub(channel)
            scalar_request = get_tick.TickRequest(**request_kwargs)
            
            for data in service.TickScalarStream(request=scalar_request, metadata=[('authorization', token)]):
                if first:
                    field_names = list(data.info.fields)
                    first = False
                else:
                    row = {'Datetime': pd.Timestamp(year=data.data.date.year, month=data.data.date.month, day=data.data.date.day, hour=data.data.time.hours, minute=data.data.time.minutes, second=data.data.time.seconds)}
                    for field, value in zip(field_names, data.data.data):
                        row[field] = value
                    rows.append(row)

        # Process the response
        if not rows or not field_names:
            print("No data received")
            return pd.DataFrame()


        # Create DataFrame
        df = pd.DataFrame(rows).set_index('Datetime').sort_index()
        
        # Apply client-side time filtering if needed
        if not df.empty and (start_time is not None or end_time is not None):
            
            # Convert string times to time objects if needed
            if isinstance(start_time, str):
                time_parts = start_time.split(':')
                hour = int(time_parts[0])
                minute = int(time_parts[1]) if len(time_parts) > 1 else 0
                start_time_obj = datetime.min.time().replace(hour=hour, minute=minute)
            else:
                start_time_obj = start_time
            
            if isinstance(end_time, str):
                time_parts = end_time.split(':')
                hour = int(time_parts[0])
                minute = int(time_parts[1]) if len(time_parts) > 1 else 0
                end_time_obj = datetime.min.time().replace(hour=hour, minute=minute)
            else:
                end_time_obj = end_time
            
            # Apply time filtering
            if start_time_obj is not None and end_time_obj is not None:
                df = df.between_time(start_time_obj, end_time_obj)
            elif start_time_obj is not None:
                df = df[df.index.time >= start_time_obj]
            elif end_time_obj is not None:
                df = df[df.index.time <= end_time_obj]

        return df
    
    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()

def get_cds_index_intraday(ticker, start_date=None, end_date=None, sampling=sampling.SAMPLING_ONE_MINUTE, selected_fields=None, provider="Markit"):
    """
    Fetch CDS Index intraday data from gRPC API for a given ticker and date range.    
    
    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval.
                                                 If None, set not limits
    end_date (datetime.date or str, optional): End date for data retrieval.
                                               If None, set not limits
    sampling (sampling, optional): Sampling perdiod for intrday. Default to one minute.
    selected_fields (list, optional): List of specific fields to retrieve.
                                      If None, gets all fields.
    provider (str): Data provider, default is "Markit"
            Returns:
    pd.DataFrame: DataFrame with Date as index and all available fields as columns
    """

    # All available fields
    all_fields = [
        'BidConventionalSpread',
        'BidPrice',
        'MidConventionalSpread',
        'MidPrice',
        'AskConventionalSpread',
        'AskPrice'
    ]    
    
    # Use all fields if none specified, otherwise validate selected fields
    if selected_fields is None:
        fields = all_fields
    else:
        fields = [f for f in selected_fields if f in all_fields]
        if not fields:
            raise ValueError("No valid fields selected")
    
    # Create identifier
    id = identifier.Identifier(
        asset_type=asset.AssetType.ASSET_TYPE_CDS_INDEX,
        ticker=ticker
    )
    id.provider.value = provider
    
    # Build constraints only if we have at least one date
    constraints_obj = None
    if start_date is not None or end_date is not None:
        # Create DateInterval with only the dates that are provided
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)

        constraints_obj = constraints.Constraints(
            date_intervals=[date_interval.DateInterval(**date_interval_kwargs)]
        )

    # Create request with or without constraints
    request_kwargs = {
        'identifier': id,
        'fields': fields,
        'sampling': sampling
    }

    if constraints_obj is not None:
        request_kwargs['constraints'] = constraints_obj
    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()
            first = True
            response = []
            info = None
            # Create service stub
            service = get_intraday_service.IntradayServiceStub(channel)
            scalar_request = get_intraday.IntradayRequest(**request_kwargs)
            
            for data in service.IntradayScalarStream(request=scalar_request, metadata=[('authorization', token)]):
                if first:
                    info = data
                    first = False
                else:
                    response.append(data.data)

        # Process the response
        if not response or info is None:
            print("No data received")
            return pd.DataFrame()

        # Get field indices
        available_fields = [f for f in info.info.fields]
        field_indices = {field: available_fields.index(field)
                        for field in fields if field in available_fields}

        rows = []
        for d in response:
            row = {
                "Datetime": pd.Timestamp(
                    year=d.datetime.year,
                    month=d.datetime.month,
                    day=d.datetime.day,
                    hour=d.datetime.hours,
                    minute=d.datetime.minutes,
                    second=d.datetime.seconds,
                ),
            }
            for field_name, field_index in field_indices.items():
                row[field_name] = d.data[field_index]
            rows.append(row)

        if not rows:
            print("No data received.")
            return pd.DataFrame()

        return (
            pd.DataFrame(rows)
            .set_index("Datetime")
            .sort_index()
        )

    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()

def get_cds_intraday(ticker, start_date=None, end_date=None, sampling=sampling.SAMPLING_ONE_MINUTE, selected_fields=None, provider="Markit"):
    """
    Fetch CDS intraday data from gRPC API for a given ticker and date range.    
    
    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval.
                                                 If None, set not limits
    end_date (datetime.date or str, optional): End date for data retrieval.
                                               If None, set not limits
    sampling (sampling, optional): Sampling perdiod for intrday. Default to one minute.
    selected_fields (list, optional): List of specific fields to retrieve.
                                      If None, gets all fields.
    provider (str): Data provider, default is "Markit"
            Returns:
    pd.DataFrame: DataFrame with Date as index and all available fields as columns
    """

    # All available fields for individual CDS
    all_fields = [
        'BidConventionalSpread',
        'BidParSpread',
        'BidUpfront',
        'MidConventionalSpread',
        'MidParSpread',
        'MidUpfront',
        'AskConventionalSpread',
        'AskParSpread',
        'AskUpfront'
    ]    
    
    # Use all fields if none specified, otherwise validate selected fields
    if selected_fields is None:
        fields = all_fields
    else:
        fields = [f for f in selected_fields if f in all_fields]
        if not fields:
            raise ValueError("No valid fields selected")
    
    # Create identifier for individual CDS (not index)
    id = identifier.Identifier(
        asset_type=asset.AssetType.ASSET_TYPE_CDS,
        ticker=ticker
    )
    id.provider.value = provider
    
    # Build constraints only if we have at least one date
    constraints_obj = None
    if start_date is not None or end_date is not None:
        # Create DateInterval with only the dates that are provided
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)
            
        constraints_obj = constraints.Constraints(
            date_intervals=[date_interval.DateInterval(**date_interval_kwargs)]
        )

    # Create request with or without constraints
    request_kwargs = {
        'identifier': id,
        'fields': fields,
        'sampling': sampling
    }

    if constraints_obj is not None:
        request_kwargs['constraints'] = constraints_obj
    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()
            first = True
            response = []
            info = None
            # Create service stub
            service = get_intraday_service.IntradayServiceStub(channel)
            scalar_request = get_intraday.IntradayRequest(**request_kwargs)
            
            for data in service.IntradayScalarStream(request=scalar_request, metadata=[('authorization', token)]):
                if first:
                    info = data
                    first = False
                else:
                    response.append(data.data)

        # Process the response
        if not response or info is None:
            print("No data received")
            return pd.DataFrame()

        # Get field indices
        available_fields = [f for f in info.info.fields]
        field_indices = {field: available_fields.index(field)
                        for field in fields if field in available_fields}

        rows = []
        for d in response:
            row = {
                "Datetime": pd.Timestamp(
                    year=d.datetime.year,
                    month=d.datetime.month,
                    day=d.datetime.day,
                    hour=d.datetime.hours,
                    minute=d.datetime.minutes,
                    second=d.datetime.seconds,
                ),
            }
            for field_name, field_index in field_indices.items():
                row[field_name] = d.data[field_index]
            rows.append(row)

        if not rows:
            print("No data received.")
            return pd.DataFrame()

        return (
            pd.DataFrame(rows)
            .set_index("Datetime")
            .sort_index()
        )

    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()

def get_future_daily(ticker, start_date=None, end_date=None, provider="FirstRateData"):
    """
    Fetch Future daily data from gRPC API for a given ticker and optionally filter by date range.
    
    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval (format: '2025-05-28'). 
                                                 If None, no start limit is applied
    end_date (datetime.date or str, optional): End date for data retrieval (format: '2025-05-28').
                                               If None, no end limit is applied
    provider (str): Data provider, default is "FirstRateData"

    # Example usage:
    # df = get_future_daily('CL1 Comdty')  # Get all available data
    # df = get_future_daily('CL1 Comdty', start_date='2024-01-01')  # From Jan 1, 2024 onwards  
    # df = get_future_daily('CL1 Comdty', end_date='2024-12-31')    # Up to Dec 31, 2024
    # df = get_future_daily('CL1 Comdty', start_date='2024-01-01', end_date='2024-12-31')  # Full year 2024
    
    Returns:
    pd.DataFrame: DataFrame with Date as index and all available fields as columns
    """
    
    def _parse_date_for_filtering(date_input):
        """Parse date input for DataFrame filtering (returns date object, not Google date)"""
        if date_input is None:
            return None
        if isinstance(date_input, date):
            return date_input
        if isinstance(date_input, datetime):
            return date_input.date()
        if isinstance(date_input, str):
            return datetime.strptime(date_input, '%Y-%m-%d').date()
        raise ValueError(f"Invalid date type: {type(date_input)}")
    
    id = identifier.Identifier(
        ticker=ticker, 
        asset_type=asset.AssetType.ASSET_TYPE_FUTURE
    )
    id.provider.value = provider
    
    request = daily_bars.DailyBarsRequest(identifier=id)

    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()

            # Create service stub
            service = daily_bars_service.DailyBarsServiceStub(channel)
            response = service.DailyBars(request=request, metadata=[('authorization', token)])

        # Process the response
        if not response or not response.data:
            print("No data received")
            return pd.DataFrame()
        
        rows = []
        for b in response.data:
            row = {
                "Date": pd.Timestamp(
                    year=b.date.year,
                    month=b.date.month,
                    day=b.date.day,
                ),
                "Open":   b.open,
                "High":   b.high,
                "Low":    b.low,
                "Close":  b.close,
                "Volume": b.volume,
            }
            rows.append(row)

        if not rows:
            print("No data received.")
            return pd.DataFrame()

        df = (
            pd.DataFrame(rows)
            .set_index("Date")
            .sort_index()
        )

        # Apply date filtering if specified
        if start_date is not None or end_date is not None:
            # Parse date inputs
            if start_date is not None:
                start_date_parsed = _parse_date_for_filtering(start_date)
                start_datetime = datetime.combine(start_date_parsed, datetime.min.time())

            if end_date is not None:
                end_date_parsed = _parse_date_for_filtering(end_date)
                end_datetime = datetime.combine(end_date_parsed, datetime.max.time())

            # Filter the DataFrame
            if start_date is not None and end_date is not None:
                df = df[(df.index >= start_datetime) & (df.index <= end_datetime)]
            elif start_date is not None:
                df = df[df.index >= start_datetime]
            elif end_date is not None:
                df = df[df.index <= end_datetime]

        return df

    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()

def get_equity_daily(ticker, start_date=None, end_date=None, provider="FirstRateData"):
    """
    Fetch Equity daily data from gRPC API for a given ticker and optionally filter by date range.

    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval (format: '2025-05-28').
                                                 If None, no start limit is applied
    end_date (datetime.date or str, optional): End date for data retrieval (format: '2025-05-28').
                                               If None, no end limit is applied
    provider (str): Data provider, default is "FirstRateData"

    # Example usage:
    # df = get_equity_daily('AAPL US Equity')  # Get all available data
    # df = get_equity_daily('AAPL US Equity', start_date='2024-01-01')  # From Jan 1, 2024 onwards
    # df = get_equity_daily('AAPL US Equity', end_date='2024-12-31')    # Up to Dec 31, 2024
    # df = get_equity_daily('AAPL US Equity', start_date='2024-01-01', end_date='2024-12-31')  # Full year 2024

    Returns:
    pd.DataFrame: DataFrame with Date as index and all available fields as columns
    """

    def _parse_date_for_filtering(date_input):
        """Parse date input for DataFrame filtering (returns date object, not Google date)"""
        if date_input is None:
            return None
        if isinstance(date_input, date):
            return date_input
        if isinstance(date_input, datetime):
            return date_input.date()
        if isinstance(date_input, str):
            return datetime.strptime(date_input, '%Y-%m-%d').date()
        raise ValueError(f"Invalid date type: {type(date_input)}")

    id = identifier.Identifier(
        ticker=ticker,
        asset_type=asset.AssetType.ASSET_TYPE_EQUITY
    )
    id.provider.value = provider

    request = daily_bars.DailyBarsRequest(identifier=id)

    try:
        # Open gRPC channel
        with channel_helpers.get_grpc_channel() as channel:
            # Send request and receive response
            token = token_helpers.get_token()

            # Create service stub
            service = daily_bars_service.DailyBarsServiceStub(channel)
            response = service.DailyBars(request=request, metadata=[('authorization', token)])

        # Process the response
        if not response or not response.data:
            print("No data received")
            return pd.DataFrame()

        rows = []
        for b in response.data:
            row = {
                "Date": pd.Timestamp(
                    year=b.date.year,
                    month=b.date.month,
                    day=b.date.day,
                ),
                "Open":   b.open,
                "High":   b.high,
                "Low":    b.low,
                "Close":  b.close,
                "Volume": b.volume,
            }
            rows.append(row)

        if not rows:
            print("No data received.")
            return pd.DataFrame()

        df = (
            pd.DataFrame(rows)
            .set_index("Date")
            .sort_index()
        )

        # Apply date filtering if specified
        if start_date is not None or end_date is not None:
            # Parse date inputs
            if start_date is not None:
                start_date_parsed = _parse_date_for_filtering(start_date)
                start_datetime = datetime.combine(start_date_parsed, datetime.min.time())

            if end_date is not None:
                end_date_parsed = _parse_date_for_filtering(end_date)
                end_datetime = datetime.combine(end_date_parsed, datetime.max.time())

            # Filter the DataFrame
            if start_date is not None and end_date is not None:
                df = df[(df.index >= start_datetime) & (df.index <= end_datetime)]
            elif start_date is not None:
                df = df[df.index >= start_datetime]
            elif end_date is not None:
                df = df[df.index <= end_datetime]

        return df

    except grpc.RpcError as e:
        print(f"gRPC Error: {e.code().name}")
        print(f"Details: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {str(e)}")
        return pd.DataFrame()

def get_equity_intraday(ticker, start_date=None, end_date=None, start_time=None, end_time=None, sampling=sampling.SAMPLING_ONE_MINUTE, provider="FirstRateData"):
    """
    Fetch Equity intraday data from gRPC API for a given ticker and optionally filter by date/time range.

    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval (format: '2025-05-28').
                                                 If None, no start limit is applied
    end_date (datetime.date or str, optional): End date for data retrieval (format: '2025-05-28').
                                               If None, no end limit is applied
    start_time (datetime.time or str, optional): Start time filter (format: 'HH:MM' or 'HH:MM:SS').
                                                 If None, no start time limit is applied
    end_time (datetime.time or str, optional): End time filter (format: 'HH:MM' or 'HH:MM:SS').
                                               If None, no end time limit is applied
    sampling (sampling, optional): Sampling period for intraday. Default to one minute.
    provider (str): Data provider, default is "FirstRateData"

    # Example usage:
    # df = get_equity_intraday('AAPL US Equity')  # Get all available data
    # df = get_equity_intraday('AAPL US Equity', start_date='2024-01-01')  # From Jan 1, 2024 onwards
    # df = get_equity_intraday('AAPL US Equity', start_date='2024-01-01', end_date='2024-12-31')  # Full year 2024
    # df = get_equity_intraday('AAPL US Equity', start_date='2024-01-01', start_time='09:30', end_time='16:00')  # With time filter

    Returns:
    pd.DataFrame: DataFrame with Datetime as index and OHLCV + count/vwap as columns
    """

    id = identifier.Identifier(
        ticker=ticker,
        asset_type=asset.AssetType.ASSET_TYPE_EQUITY
    )
    id.provider.value = provider

    # Build date interval if dates are provided
    date_interval_obj = None
    if start_date is not None or end_date is not None:
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)
        date_interval_obj = date_interval.DateInterval(**date_interval_kwargs)

    # Build time interval if times are provided
    time_interval_obj = None
    if start_time is not None or end_time is not None:
        time_interval_kwargs = {}
        if start_time is not None:
            time_interval_kwargs['start_time'] = _parse_time_input(start_time)
        if end_time is not None:
            time_interval_kwargs['end_time'] = _parse_time_input(end_time)
        time_interval_obj = time_interval.TimeInterval(**time_interval_kwargs)

    request_kwargs = {
        'identifier': id,
        'sampling': sampling,
    }
    if date_interval_obj is not None:
        request_kwargs['date_interval'] = date_interval_obj
    if time_interval_obj is not None:
        request_kwargs['time_interval'] = time_interval_obj

    request = intraday_bars.IntradayBarsRequest(**request_kwargs)

    try:
        with channel_helpers.get_grpc_channel() as channel:
            token = token_helpers.get_token()
            service = intraday_bars_service.IntradayBarsServiceStub(channel)
            response = service.IntradayBars(request=request, metadata=[('authorization', token)])

        if not response or not response.data:
            print("No data received")
            return pd.DataFrame()

        rows = []
        for b in response.data:
            row = {
                "Datetime": pd.Timestamp(b.time_stamp.seconds, unit='s'),
                "Open":     b.open,
                "High":     b.high,
                "Low":      b.low,
                "Close":    b.close,
                "Volume":   b.volume,
                "Count":    b.count,
                "Vwap":     b.vwap,
            }
            rows.append(row)

        if not rows:
            print("No data received.")
            return pd.DataFrame()

        return (
            pd.DataFrame(rows)
            .set_index("Datetime")
            .sort_index()
        )

    except grpc.RpcError as e:
        print(f"gRPC Error [{e.code().name}]: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()

def get_future_intraday(ticker, start_date=None, end_date=None, start_time=None, end_time=None, sampling=sampling.SAMPLING_ONE_MINUTE, provider="FirstRateData"):
    """
    Fetch Future intraday data from gRPC API for a given ticker and optionally filter by date/time range.

    Parameters:
    ticker (str): The ticker symbol
    start_date (datetime.date or str, optional): Start date for data retrieval (format: '2025-05-28').
                                                 If None, no start limit is applied
    end_date (datetime.date or str, optional): End date for data retrieval (format: '2025-05-28').
                                               If None, no end limit is applied
    start_time (datetime.time or str, optional): Start time filter (format: 'HH:MM' or 'HH:MM:SS').
                                                 If None, no start time limit is applied
    end_time (datetime.time or str, optional): End time filter (format: 'HH:MM' or 'HH:MM:SS').
                                               If None, no end time limit is applied
    sampling (sampling, optional): Sampling period for intraday. Default to one minute.
    provider (str): Data provider, default is "FirstRateData"

    # Example usage:
    # df = get_future_intraday('CL1 Comdty')  # Get all available data
    # df = get_future_intraday('CL1 Comdty', start_date='2024-01-01')  # From Jan 1, 2024 onwards
    # df = get_future_intraday('CL1 Comdty', start_date='2024-01-01', end_date='2024-12-31')  # Full year 2024
    # df = get_future_intraday('CL1 Comdty', start_date='2024-01-01', start_time='09:30', end_time='16:00')  # With time filter

    Returns:
    pd.DataFrame: DataFrame with Datetime as index and OHLCV + count/vwap as columns
    """

    id = identifier.Identifier(
        ticker=ticker,
        asset_type=asset.AssetType.ASSET_TYPE_FUTURE
    )
    id.provider.value = provider

    # Build date interval if dates are provided
    date_interval_obj = None
    if start_date is not None or end_date is not None:
        date_interval_kwargs = {}
        if start_date is not None:
            date_interval_kwargs['start_date'] = _parse_date_input(start_date)
        if end_date is not None:
            date_interval_kwargs['end_date'] = _parse_date_input(end_date)
        date_interval_obj = date_interval.DateInterval(**date_interval_kwargs)

    # Build time interval if times are provided
    time_interval_obj = None
    if start_time is not None or end_time is not None:
        time_interval_kwargs = {}
        if start_time is not None:
            time_interval_kwargs['start_time'] = _parse_time_input(start_time)
        if end_time is not None:
            time_interval_kwargs['end_time'] = _parse_time_input(end_time)
        time_interval_obj = time_interval.TimeInterval(**time_interval_kwargs)

    request_kwargs = {
        'identifier': id,
        'sampling': sampling,
    }
    if date_interval_obj is not None:
        request_kwargs['date_interval'] = date_interval_obj
    if time_interval_obj is not None:
        request_kwargs['time_interval'] = time_interval_obj

    request = intraday_bars.IntradayBarsRequest(**request_kwargs)

    try:
        with channel_helpers.get_grpc_channel() as channel:
            token = token_helpers.get_token()
            service = intraday_bars_service.IntradayBarsServiceStub(channel)
            response = service.IntradayBars(request=request, metadata=[('authorization', token)])

        if not response or not response.data:
            print("No data received")
            return pd.DataFrame()

        rows = []
        for b in response.data:
            row = {
                "Datetime": pd.Timestamp(b.time_stamp.seconds, unit='s'),
                "Open":     b.open,
                "High":     b.high,
                "Low":      b.low,
                "Close":    b.close,
                "Volume":   b.volume,
                "Count":    b.count,
                "Vwap":     b.vwap,
            }
            rows.append(row)

        if not rows:
            print("No data received.")
            return pd.DataFrame()

        return (
            pd.DataFrame(rows)
            .set_index("Datetime")
            .sort_index()
        )

    except grpc.RpcError as e:
        print(f"gRPC Error [{e.code().name}]: {e.details()}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error: {e}")
        return pd.DataFrame()


# Helpers functions

def _python_date_to_google_date(py_date):
    """Convert Python date to Google Date protobuf message"""
    return date_pb2.Date(year=py_date.year, month=py_date.month, day=py_date.day)


def _parse_date_input(date_input):
    """Convert string dates to date objects if needed."""
    if date_input is None:
        return None
    if isinstance(date_input, str):
        d = datetime.strptime(date_input, '%Y-%m-%d').date()
        return _python_date_to_google_date(d)
    if isinstance(date_input, date):
        return _python_date_to_google_date(date_input)
    if isinstance(date_input, datetime):
        return _python_date_to_google_date(date_input.date())

    raise ValueError(f"Invalid date type: {type(date_input)}")


def _parse_time_input(time_input):
    """Convert string or datetime.time to Google TimeOfDay protobuf message.

    Accepts:
        - datetime.time object
        - str in 'HH:MM' or 'HH:MM:SS' format
    """
    if time_input is None:
        return None
    if isinstance(time_input, datetime):
        t = time_input.time()
        return timeofday.TimeOfDay(hours=t.hour, minutes=t.minute, seconds=t.second)
    from datetime import time as time_type
    if isinstance(time_input, time_type):
        return timeofday.TimeOfDay(hours=time_input.hour, minutes=time_input.minute, seconds=time_input.second)
    if isinstance(time_input, str):
        parts = time_input.split(':')
        h = int(parts[0])
        m = int(parts[1]) if len(parts) > 1 else 0
        s = int(parts[2]) if len(parts) > 2 else 0
        return timeofday.TimeOfDay(hours=h, minutes=m, seconds=s)
    raise ValueError(f"Invalid time type: {type(time_input)}")


def _build_strike_filter(strike) -> "filter.DoubleFilter":
    """
    Build a DoubleFilter proto from a Python value.

    Examples
    --------
    _build_strike_filter(100.0)            # exact
    _build_strike_filter((80.0, 120.0))    # range [80, 120)
    _build_strike_filter((None, 120.0))    # open lower bound, less_than 120
    _build_strike_filter((80.0, None))     # greater_or_equal_than 80, open upper bound
    """
    if isinstance(strike, (int, float)):
        return filter.DoubleFilter(exact=float(strike))

    if isinstance(strike, tuple) and len(strike) == 2:
        lo, hi = strike
        range_kwargs = {}
        if lo is not None:
            range_kwargs["greater_or_equal_than"] = wrappers_pb2.DoubleValue(value=float(lo))
        if hi is not None:
            range_kwargs["less_than"] = wrappers_pb2.DoubleValue(value=float(hi))
        if not range_kwargs:
            raise ValueError("strike_interval tuple must have at least one non-None bound.")
        return filter.DoubleFilter(range=filter.DoubleFilterRange(**range_kwargs))

    raise TypeError(
        "strike_interval must be a float (exact) or a (min, max) tuple "
        f"with at least one non-None bound. Got: {strike!r}"
    )

def _build_maturity_filter(maturity) -> "filter.DateFilter":
    """
    Build a DateFilter proto from a Python value.

    Examples
    --------
    _build_maturity_filter("2025-06-20")                         # exact date
    _build_maturity_filter(datetime.date(2025, 6, 20))           # exact date
    _build_maturity_filter(("2025-03-01", "2025-12-31"))         # date range
    _build_maturity_filter((None, "2025-12-31"))                 # open lower bound
    _build_maturity_filter(("2025-03-01", None))                 # open upper bound
    """
        
    # Exact match
    if isinstance(maturity, (date, str)):
        proto_d = _parse_date_input(maturity)
        return filter.DateFilter(exact=proto_d)

    # Range
    if isinstance(maturity, tuple) and len(maturity) == 2:
        start, end = maturity
        range_kwargs = {}
        if start is not None:
            range_kwargs["greater_or_equal_than"] = _parse_date_input(start)
        if end is not None:
            range_kwargs["less_than"] = _parse_date_input(end)
        if not range_kwargs:
            raise ValueError("maturity_date tuple must have at least one non-None bound.")
        return filter.DateFilter(range=filter.DateFilterRange(**range_kwargs))

    raise TypeError(
        "maturity_date must be a date/str (exact) or a (start, end) tuple "
        f"with at least one non-None bound. Got: {maturity!r}"
    )




def _proto_enum_parse(proto_enum_cls, prefix, value):
    """
    Convert a user-supplied string or int to a proto enum int value.

    Accepts:
    - int / existing proto int         → returned as-is
    - full proto name  e.g. "OPTION_TYPE_CALL"
    - short name       e.g. "Call", "CALL", "call"
    - underscore-free  e.g. "FloatingDelta", "floatingdelta"

    Parameters
    ----------
    proto_enum_cls : proto enum descriptor  (e.g. OptionType)
    prefix         : proto name prefix to strip  (e.g. "OPTION_TYPE_")
    value          : user input
    """
    if isinstance(value, int):
        return value

    if isinstance(value, str):
        # Try full proto name first (e.g. "OPTION_TYPE_CALL")
        try:
            return proto_enum_cls.Value(value.upper())
        except ValueError:
            pass

        # Try with prefix prepended (e.g. "call" → "OPTION_TYPE_CALL")
        try:
            return proto_enum_cls.Value(prefix + value.upper())
        except ValueError:
            pass

        # Fuzzy: strip prefix from all known names, normalise underscores,
        # then compare case-insensitively
        normalised = value.strip().lower().replace("_", "")
        for name in proto_enum_cls.keys():
            short = name.replace(prefix, "").lower().replace("_", "")
            if short == normalised:
                return proto_enum_cls.Value(name)

    valid = [n.replace(prefix, "") for n in proto_enum_cls.keys()]
    raise ValueError(
        f"Unknown value {value!r} for {proto_enum_cls.DESCRIPTOR.name}. "
        f"Valid values: {valid}"
    )


def _proto_enum_name(proto_enum_cls, prefix, int_value):
    """
    Convert a proto enum int back to a short human-readable string.

    e.g. 1 → "OPTION_TYPE_CALL" → "Call"
    """
    full_name = proto_enum_cls.Name(int_value)          # e.g. "OPTION_TYPE_CALL"
    short     = full_name.replace(prefix, "").title()   # e.g. "Call"
    return short.replace("_", "")                        # e.g. "FloatingDelta"


# Convenience wrappers for the two enums used here

def _parse_option_type(value) -> int:
    return _proto_enum_parse(OptionType.OptionType, "OPTION_TYPE_", value)

def _parse_strike_type(value) -> int:
    return _proto_enum_parse(StrikeType.StrikeType, "STRIKE_TYPE_", value)

def _format_option_type(int_value) -> str:
    return _proto_enum_name(OptionType.OptionType, "OPTION_TYPE_", int_value)

def _format_strike_type(int_value) -> str:
    return _proto_enum_name(StrikeType.StrikeType, "STRIKE_TYPE_", int_value)
