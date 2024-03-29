# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.tick_analytics.v1 import tick_ema_pb2 as systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__ema__pb2


class TickEmaServiceStub(object):
    """Called to request tick by tick exponential moving average data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TickEma = channel.unary_stream(
                '/systemathics.apis.services.tick_analytics.v1.TickEmaService/TickEma',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__ema__pb2.TickEmaRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__ema__pb2.TickEmaResponse.FromString,
                )


class TickEmaServiceServicer(object):
    """Called to request tick by tick exponential moving average data.
    """

    def TickEma(self, request, context):
        """Gets tick by tick exponential moving average data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TickEmaServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TickEma': grpc.unary_stream_rpc_method_handler(
                    servicer.TickEma,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__ema__pb2.TickEmaRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__ema__pb2.TickEmaResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.tick_analytics.v1.TickEmaService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TickEmaService(object):
    """Called to request tick by tick exponential moving average data.
    """

    @staticmethod
    def TickEma(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/systemathics.apis.services.tick_analytics.v1.TickEmaService/TickEma',
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__ema__pb2.TickEmaRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__ema__pb2.TickEmaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
