# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.static_data.v1 import sector_pb2 as systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_sector__pb2


class SectorServiceStub(object):
    """Called to request sector and industry classification data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Sector = channel.unary_unary(
                '/systemathics.apis.services.static_data.v1.SectorService/Sector',
                request_serializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_sector__pb2.SectorRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_sector__pb2.SectorResponse.FromString,
                )


class SectorServiceServicer(object):
    """Called to request sector and industry classification data.
    """

    def Sector(self, request, context):
        """Gets static sector and industry data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SectorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Sector': grpc.unary_unary_rpc_method_handler(
                    servicer.Sector,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_sector__pb2.SectorRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_sector__pb2.SectorResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.static_data.v1.SectorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SectorService(object):
    """Called to request sector and industry classification data.
    """

    @staticmethod
    def Sector(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.static_data.v1.SectorService/Sector',
            systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_sector__pb2.SectorRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_static__data_dot_v1_dot_sector__pb2.SectorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
