# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.intraday.v1 import intraday_prices_pb2 as systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__prices__pb2


class IntradayPricesServiceStub(object):
    """Called to request intraday prices data. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IntradayPrices = channel.unary_unary(
                '/systemathics.apis.services.intraday.v1.IntradayPricesService/IntradayPrices',
                request_serializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__prices__pb2.IntradayPricesRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__prices__pb2.IntradayPricesResponse.FromString,
                )


class IntradayPricesServiceServicer(object):
    """Called to request intraday prices data. 
    """

    def IntradayPrices(self, request, context):
        """Gets intraday historical prices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IntradayPricesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IntradayPrices': grpc.unary_unary_rpc_method_handler(
                    servicer.IntradayPrices,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__prices__pb2.IntradayPricesRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__prices__pb2.IntradayPricesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.intraday.v1.IntradayPricesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IntradayPricesService(object):
    """Called to request intraday prices data. 
    """

    @staticmethod
    def IntradayPrices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.intraday.v1.IntradayPricesService/IntradayPrices',
            systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__prices__pb2.IntradayPricesRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__prices__pb2.IntradayPricesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)