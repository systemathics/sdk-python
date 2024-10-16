# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from systemathics.apis.services.tick.v2 import set_tick_scalar_pb2 as systemathics_dot_apis_dot_services_dot_tick_dot_v2_dot_set__tick__scalar__pb2


class SetTickScalarServiceStub(object):
    """Called to set tick prices data and clear. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetTickScalar = channel.stream_unary(
                '/systemathics.apis.services.tick.v2.SetTickScalarService/SetTickScalar',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick_dot_v2_dot_set__tick__scalar__pb2.SetTickScalarRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ClearTickScalar = channel.unary_unary(
                '/systemathics.apis.services.tick.v2.SetTickScalarService/ClearTickScalar',
                request_serializer=systemathics_dot_apis_dot_services_dot_tick_dot_v2_dot_set__tick__scalar__pb2.ClearTickScalarRequest.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class SetTickScalarServiceServicer(object):
    """Called to set tick prices data and clear. 
    """

    def SetTickScalar(self, request_iterator, context):
        """Sets tick scalar timeseries.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearTickScalar(self, request, context):
        """Delete tick scalar timeseries.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SetTickScalarServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetTickScalar': grpc.stream_unary_rpc_method_handler(
                    servicer.SetTickScalar,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick_dot_v2_dot_set__tick__scalar__pb2.SetTickScalarRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ClearTickScalar': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearTickScalar,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_tick_dot_v2_dot_set__tick__scalar__pb2.ClearTickScalarRequest.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.tick.v2.SetTickScalarService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SetTickScalarService(object):
    """Called to set tick prices data and clear. 
    """

    @staticmethod
    def SetTickScalar(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/systemathics.apis.services.tick.v2.SetTickScalarService/SetTickScalar',
            systemathics_dot_apis_dot_services_dot_tick_dot_v2_dot_set__tick__scalar__pb2.SetTickScalarRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearTickScalar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.tick.v2.SetTickScalarService/ClearTickScalar',
            systemathics_dot_apis_dot_services_dot_tick_dot_v2_dot_set__tick__scalar__pb2.ClearTickScalarRequest.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
