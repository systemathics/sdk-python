# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.static_data.v1 import static_data_pb2 as systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2


class StaticDataServiceStub(object):
    """Called to request reference data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StaticData = channel.unary_unary(
                '/systemathics.apis.services.static_data.v1.StaticDataService/StaticData',
                request_serializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2.StaticDataRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2.StaticDataResponse.FromString,
                )


class StaticDataServiceServicer(object):
    """Called to request reference data.
    """

    def StaticData(self, request, context):
        """Gets reference data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StaticDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StaticData': grpc.unary_unary_rpc_method_handler(
                    servicer.StaticData,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2.StaticDataRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2.StaticDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.static_data.v1.StaticDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StaticDataService(object):
    """Called to request reference data.
    """

    @staticmethod
    def StaticData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.static_data.v1.StaticDataService/StaticData',
            systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2.StaticDataRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_static__data__pb2.StaticDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)