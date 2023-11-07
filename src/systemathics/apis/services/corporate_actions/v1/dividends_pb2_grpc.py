# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.corporate_actions.v1 import dividends_pb2 as systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2


class DividendsServiceStub(object):
    """Called to request dividends data.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Dividends = channel.unary_unary(
                '/systemathics.apis.services.corporate_actions.v1.DividendsService/Dividends',
                request_serializer=systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2.DividendsRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2.DividendsResponse.FromString,
                )


class DividendsServiceServicer(object):
    """Called to request dividends data.
    """

    def Dividends(self, request, context):
        """Gets dividends historical data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DividendsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Dividends': grpc.unary_unary_rpc_method_handler(
                    servicer.Dividends,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2.DividendsRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2.DividendsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.corporate_actions.v1.DividendsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DividendsService(object):
    """Called to request dividends data.
    """

    @staticmethod
    def Dividends(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.corporate_actions.v1.DividendsService/Dividends',
            systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2.DividendsRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_corporate__actions_dot_v1_dot_dividends__pb2.DividendsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
