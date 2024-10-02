# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from systemathics.apis.services.static_data.v1 import set_static_data_pb2 as systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_set__static__data__pb2


class SetStaticDataServiceStub(object):
    """Called to set static data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStaticDataOtcStreaming = channel.unary_unary(
                '/systemathics.apis.services.static_data.v1.SetStaticDataService/CreateStaticDataOtcStreaming',
                request_serializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_set__static__data__pb2.StaticDataOtcStreamingRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class SetStaticDataServiceServicer(object):
    """Called to set static data.
    """

    def CreateStaticDataOtcStreaming(self, request, context):
        """Creates Option Static data from OTC Streaming
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SetStaticDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateStaticDataOtcStreaming': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStaticDataOtcStreaming,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_set__static__data__pb2.StaticDataOtcStreamingRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.static_data.v1.SetStaticDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SetStaticDataService(object):
    """Called to set static data.
    """

    @staticmethod
    def CreateStaticDataOtcStreaming(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.static_data.v1.SetStaticDataService/CreateStaticDataOtcStreaming',
            systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_set__static__data__pb2.StaticDataOtcStreamingRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
