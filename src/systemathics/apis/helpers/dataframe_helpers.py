"""Systemathics Ganymede  API Token Helpers

This module helps to create tokens to access Systemathics Ganymede authenticated API.

functions:
    get_cds_index - Get CDS Index data as a DataFrame using Ganymede gRPC API.
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