# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.tick_analytics.v1 import tick_priips_pb2 as systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2


class TickPriipsServiceStub(object):
    """Called to request TickPriipsService. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TickPriips = channel.unary_unary(
                '/systemathics.apis.services.tick_analytics.v1.TickPriipsService/TickPriips',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2.TickPriipsRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2.TickPriipsResponse.FromString,
                )


class TickPriipsServiceServicer(object):
    """Called to request TickPriipsService. 
    """

    def TickPriips(self, request, context):
        """Gets PRIIPs transaction cost analytics
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TickPriipsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TickPriips': grpc.unary_unary_rpc_method_handler(
                    servicer.TickPriips,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2.TickPriipsRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2.TickPriipsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.tick_analytics.v1.TickPriipsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TickPriipsService(object):
    """Called to request TickPriipsService. 
    """

    @staticmethod
    def TickPriips(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.tick_analytics.v1.TickPriipsService/TickPriips',
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2.TickPriipsRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_tick__analytics_dot_v1_dot_tick__priips__pb2.TickPriipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)