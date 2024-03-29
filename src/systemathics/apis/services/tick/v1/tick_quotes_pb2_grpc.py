# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.tick.v1 import tick_quotes_pb2 as systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__quotes__pb2


class TickQuotesServiceStub(object):
    """Called to request tick by tick normalized quotes data (MBO).
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TickQuotes = channel.unary_stream(
                '/systemathics.apis.services.tick.v1.TickQuotesService/TickQuotes',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__quotes__pb2.TickQuotesRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__quotes__pb2.TickQuotesResponse.FromString,
                )


class TickQuotesServiceServicer(object):
    """Called to request tick by tick normalized quotes data (MBO).
    """

    def TickQuotes(self, request, context):
        """Get tick by tick normalized quotes 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TickQuotesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TickQuotes': grpc.unary_stream_rpc_method_handler(
                    servicer.TickQuotes,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__quotes__pb2.TickQuotesRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__quotes__pb2.TickQuotesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.tick.v1.TickQuotesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TickQuotesService(object):
    """Called to request tick by tick normalized quotes data (MBO).
    """

    @staticmethod
    def TickQuotes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/systemathics.apis.services.tick.v1.TickQuotesService/TickQuotes',
            systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__quotes__pb2.TickQuotesRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_tick_dot_v1_dot_tick__quotes__pb2.TickQuotesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
