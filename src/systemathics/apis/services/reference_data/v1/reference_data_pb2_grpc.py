# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.reference_data.v1 import reference_data_pb2 as systemathics_dot_apis_dot_services_dot_reference__data_dot_v1_dot_reference__data__pb2


class ReferenceServiceStub(object):
    """Called to request reference data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Reference = channel.unary_unary(
                '/systemathics.apis.services.reference_data.v1.ReferenceService/Reference',
                request_serializer=systemathics_dot_apis_dot_services_dot_reference__data_dot_v1_dot_reference__data__pb2.ReferenceRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_reference__data_dot_v1_dot_reference__data__pb2.ReferenceResponse.FromString,
                )


class ReferenceServiceServicer(object):
    """Called to request reference data.
    """

    def Reference(self, request, context):
        """Gets reference data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ReferenceServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Reference': grpc.unary_unary_rpc_method_handler(
                    servicer.Reference,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_reference__data_dot_v1_dot_reference__data__pb2.ReferenceRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_reference__data_dot_v1_dot_reference__data__pb2.ReferenceResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.reference_data.v1.ReferenceService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ReferenceService(object):
    """Called to request reference data.
    """

    @staticmethod
    def Reference(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.reference_data.v1.ReferenceService/Reference',
            systemathics_dot_apis_dot_services_dot_reference__data_dot_v1_dot_reference__data__pb2.ReferenceRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_reference__data_dot_v1_dot_reference__data__pb2.ReferenceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
