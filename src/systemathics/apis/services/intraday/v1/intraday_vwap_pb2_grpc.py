# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.intraday.v1 import intraday_vwap_pb2 as systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__vwap__pb2


class IntradayVwapsServiceStub(object):
    """Called to request intraday VWAP data. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.IntradayVwaps = channel.unary_unary(
                '/systemathics.apis.services.intraday.v1.IntradayVwapsService/IntradayVwaps',
                request_serializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__vwap__pb2.IntradayVwapsRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__vwap__pb2.IntradayVwapsResponse.FromString,
                )


class IntradayVwapsServiceServicer(object):
    """Called to request intraday VWAP data. 
    """

    def IntradayVwaps(self, request, context):
        """Gets intraday historical VWAPs
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IntradayVwapsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'IntradayVwaps': grpc.unary_unary_rpc_method_handler(
                    servicer.IntradayVwaps,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__vwap__pb2.IntradayVwapsRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__vwap__pb2.IntradayVwapsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.intraday.v1.IntradayVwapsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IntradayVwapsService(object):
    """Called to request intraday VWAP data. 
    """

    @staticmethod
    def IntradayVwaps(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.intraday.v1.IntradayVwapsService/IntradayVwaps',
            systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__vwap__pb2.IntradayVwapsRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_intraday_dot_v1_dot_intraday__vwap__pb2.IntradayVwapsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)