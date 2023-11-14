# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.sustainability.v1 import sustainability_pb2 as systemathics_dot_apis_dot_services_dot_sustainability_dot_v1_dot_sustainability__pb2


class SustainabilityServiceStub(object):
    """Called to request sustainability data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sustainability = channel.unary_unary(
                '/systemathics.apis.services.sustainability.v1.SustainabilityService/Sustainability',
                request_serializer=systemathics_dot_apis_dot_services_dot_sustainability_dot_v1_dot_sustainability__pb2.SustainabilityRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_sustainability_dot_v1_dot_sustainability__pb2.SustainabilityResponse.FromString,
                )


class SustainabilityServiceServicer(object):
    """Called to request sustainability data.
    """

    def Sustainability(self, request, context):
        """Gets sustainability data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SustainabilityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sustainability': grpc.unary_unary_rpc_method_handler(
                    servicer.Sustainability,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_sustainability_dot_v1_dot_sustainability__pb2.SustainabilityRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_sustainability_dot_v1_dot_sustainability__pb2.SustainabilityResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.sustainability.v1.SustainabilityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SustainabilityService(object):
    """Called to request sustainability data.
    """

    @staticmethod
    def Sustainability(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.sustainability.v1.SustainabilityService/Sustainability',
            systemathics_dot_apis_dot_services_dot_sustainability_dot_v1_dot_sustainability__pb2.SustainabilityRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_sustainability_dot_v1_dot_sustainability__pb2.SustainabilityResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)