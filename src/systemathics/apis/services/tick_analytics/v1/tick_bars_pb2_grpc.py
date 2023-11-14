# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.tick_analytics.v1 import tick_bars_pb2 as systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__bars__pb2


class TickBarsServiceStub(object):
    """Called to request tick by tick bars data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TickBars = channel.unary_stream(
                '/systemathics.apis.services.tick_analytics.v1.TickBarsService/TickBars',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__bars__pb2.TickBarsRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__bars__pb2.TickBarsResponse.FromString,
                )


class TickBarsServiceServicer(object):
    """Called to request tick by tick bars data.
    """

    def TickBars(self, request, context):
        """Gets tick by tick bars data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TickBarsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TickBars': grpc.unary_stream_rpc_method_handler(
                    servicer.TickBars,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__bars__pb2.TickBarsRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__bars__pb2.TickBarsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.tick_analytics.v1.TickBarsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TickBarsService(object):
    """Called to request tick by tick bars data.
    """

    @staticmethod
    def TickBars(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/systemathics.apis.services.tick_analytics.v1.TickBarsService/TickBars',
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__bars__pb2.TickBarsRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__bars__pb2.TickBarsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)