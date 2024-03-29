# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.indices.v1 import components_pb2 as systemathics_dot_apis_dot_services_dot_indices_dot_v1_dot_components__pb2


class ComponentsServiceStub(object):
    """Called to request index weights data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Components = channel.unary_unary(
                '/systemathics.apis.services.indices.v1.ComponentsService/Components',
                request_serializer=systemathics_dot_apis_dot_services_dot_indices_dot_v1_dot_components__pb2.ComponentsRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_indices_dot_v1_dot_components__pb2.ComponentsResponse.FromString,
                )


class ComponentsServiceServicer(object):
    """Called to request index weights data.
    """

    def Components(self, request, context):
        """Gets index components data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComponentsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Components': grpc.unary_unary_rpc_method_handler(
                    servicer.Components,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_indices_dot_v1_dot_components__pb2.ComponentsRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_indices_dot_v1_dot_components__pb2.ComponentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.indices.v1.ComponentsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ComponentsService(object):
    """Called to request index weights data.
    """

    @staticmethod
    def Components(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.indices.v1.ComponentsService/Components',
            systemathics_dot_apis_dot_services_dot_indices_dot_v1_dot_components__pb2.ComponentsRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_indices_dot_v1_dot_components__pb2.ComponentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
