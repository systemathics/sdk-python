# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.v1 import marketdata_pb2 as systemathics_dot_apis_dot_services_dot_v1_dot_marketdata__pb2


class MarketDataServiceStub(object):
    """The market data service definition
    It allows to replay tick by tick data
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MarketData = channel.unary_stream(
                '/systemathics.apis.services.v1.MarketDataService/MarketData',
                request_serializer=systemathics_dot_apis_dot_services_dot_v1_dot_marketdata__pb2.MarketDataRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_v1_dot_marketdata__pb2.MarketDataResponse.FromString,
                )


class MarketDataServiceServicer(object):
    """The market data service definition
    It allows to replay tick by tick data
    """

    def MarketData(self, request, context):
        """Get Market Data 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MarketData': grpc.unary_stream_rpc_method_handler(
                    servicer.MarketData,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_v1_dot_marketdata__pb2.MarketDataRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_v1_dot_marketdata__pb2.MarketDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.v1.MarketDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MarketDataService(object):
    """The market data service definition
    It allows to replay tick by tick data
    """

    @staticmethod
    def MarketData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/systemathics.apis.services.v1.MarketDataService/MarketData',
            systemathics_dot_apis_dot_services_dot_v1_dot_marketdata__pb2.MarketDataRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_v1_dot_marketdata__pb2.MarketDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
