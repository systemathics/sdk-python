"""Systemathics Ganymede  API Token Helpers

This module helps to create tokens to access Systemathics Ganymede authenticated API.

functions:
    get_cds_index_daily - Get CDS Index daily data as a DataFrame using Ganymede gRPC API.
    get_cds_index_intraday - Get CDS Index intraday data as a DataFrame using Ganymede gRPC API.
    get_future_daily - Get future daily data as a DataFrame using Ganymede gRPC API.
"""


import grpc
import pandas as pd
from datetime import date,datetime
from google.type import date_pb2
from google.type import datetime_pb2

from systemathics.apis.type.shared.v1 import asset_pb2 as asset
from systemathics.apis.type.shared.v1 import constraints_pb2 as constraints
from systemathics.apis.type.shared.v1 import date_interval_pb2 as date_interval
import systemathics.apis.type.shared.v1.sampling_pb2 as sampling
import systemathics.apis.type.shared.v1.identifier_pb2 as identifier
import systemathics.apis.services.daily.v1.daily_bars_pb2 as daily_bars
import systemathics.apis.services.daily.v1.daily_bars_pb2_grpc as daily_bars_service
import systemathics.apis.services.daily.v2.get_daily_pb2 as get_daily
import systemathics.apis.services.daily.v2.get_daily_pb2_grpc as get_daily_service
import systemathics.apis.services.intraday.v2.get_intraday_pb2 as get_intraday
import systemathics.apis.services.intraday.v2.get_intraday_pb2_grpc as get_intraday_service

import systemathics.apis.helpers.token_helpers as token_helpers
import systemathics.apis.helpers.channel_helpers as channel_helpers

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
            response = []
            info = None
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
                        info = data
                        first = False
                    else:
                        response.append(data.data)
            
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
        
        # Extract dates
        dates = [date(d.date.year, d.date.month, d.date.day) for d in response]
        
        # Extract keys
        keys = [b.key for b in response]
        
        # Create dictionary for DataFrame
        data_dict = {'Key': keys}
        
        # Extract data for each field
        for field_name, field_index in field_indices.items():
            data_dict[field_name] = [b.data[field_index] for b in response]
        
        # Create DataFrame
        df = pd.DataFrame(data_dict, index=dates)
        df.index.name = 'Date'
        
        # Sort by date for better readability
        df = df.sort_index()
    
        
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

        # Extract dates
        dates = [datetime(d.datetime.year, d.datetime.month, d.datetime.day, d.datetime.hours, d.datetime.minutes, d.datetime.seconds) for d in response]

        # Create dictionary for DataFrame
        data_dict = {}
        
        # Extract data for each field
        for field_name, field_index in field_indices.items():
            data_dict[field_name] = [b.data[field_index] for b in response]

        # Create DataFrame
        df = pd.DataFrame(data_dict, index=dates)
        df.index.name = 'Datetime'

        # Sort by date for better readability
        df = df.sort_index()
        return df
    
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
        
        dates = [datetime(b.date.year, b.date.month, b.date.day) for b in response.data]
        opens = [b.open for b in response.data]
        highs = [b.high for b in response.data]
        lows = [b.low for b in response.data]
        closes = [b.close for b in response.data]
        volumes = [b.volume for b in response.data]

        data_dict = {'Date': dates, 'Open': opens, 'High': highs, 'Low': lows, 'Close': closes, 'Volume': volumes}
        df = pd.DataFrame(data=data_dict)
        df = df.set_index('Date')
        
        # Sort by date for better readability
        df = df.sort_index()
        
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
        
        dates = [datetime(b.date.year, b.date.month, b.date.day) for b in response.data]
        opens = [b.open for b in response.data]
        highs = [b.high for b in response.data]
        lows = [b.low for b in response.data]
        closes = [b.close for b in response.data]
        volumes = [b.volume for b in response.data]

        data_dict = {'Date': dates, 'Open': opens, 'High': highs, 'Low': lows, 'Close': closes, 'Volume': volumes}
        df = pd.DataFrame(data=data_dict)
        df = df.set_index('Date')
        
        # Sort by date for better readability
        df = df.sort_index()
        
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

def _python_date_to_google_date(py_date):
    """Convert Python date to Google Date protobuf message"""
    return date_pb2.Date(year=py_date.year, month=py_date.month, day=py_date.day)

# Helper function to parse date strings
def _parse_date_input(date_input):
    """Convert string dates to date objects if needed."""
    if date_input is None:
        return None
    if isinstance(date_input, date):
        return _python_date_to_google_date(date_input)
    if isinstance(date_input, datetime):
        return _python_date_to_google_date(date_input.date())
    if isinstance(date_input, str):
        d = datetime.strptime(date_input, '%Y-%m-%d').date()
        return _python_date_to_google_date(d)
    raise ValueError(f"Invalid date type: {type(date_input)}")