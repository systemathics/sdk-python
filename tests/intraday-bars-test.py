#!/usr/bin/python

"""

In order for this to work, environment must be setup accordingly
You need to go to your dashboard in tokens section and adapt the bash snippet below

export CLIENT_ID="wrFSU96w9Q1lXGaJC8zQJqNOFU16fsCl"
export CLIENT_SECRET="5CsoEkx387Uqy9J-6PZFDYOC0ptbYp04pJGuc-luCrdXtZLleILwM_RV501M5FY4"
export AUDIENCE="https://prod.ganymede-prod"
export TENANT="ganymede-prod.eu.auth0.com"
export GRPC_APIS="grpc.systemathics.cloud"

"""

import grpc
from datetime import datetime

import systemathics.apis.type.shared.v1.identifier_pb2 as identifier
import systemathics.apis.type.shared.v1.sampling_pb2 as sampling
import systemathics.apis.services.intraday.v1.intraday_bars_pb2 as intraday_bars
import systemathics.apis.services.intraday.v1.intraday_bars_pb2_grpc as intraday_bars_service
import systemathics.helpers.token_helpers as token_helpers
import systemathics.helpers.channel_helpers as channel_helpers

ticker = 'AAPL'
exchange = 'BATS'

my_sampling = sampling.SAMPLING_FIFTEEN_MINUTE

request = intraday_bars.IntradayBarsRequest(
    identifier = identifier.Identifier(exchange = exchange, ticker = ticker),
    sampling = my_sampling
)

try:
    token = token_helpers.get_token()
    with channel_helpers.get_grpc_channel() as channel:
        service = intraday_bars_service.IntradayBarsServiceStub(channel)
        response = service.IntradayBars(
            request = request, 
            metadata = [('authorization', token)]
        )
        
    print("Total bars retrieved: ",len(response.data))
    for b in response.data:
       ts = datetime.fromtimestamp(b.time_stamp.seconds)
       print(f"{ts} open={b.open} high={b.high} low={b.low} close={b.close}")
except grpc.RpcError as e:
    print(e.code().name)
    print(e.details())
