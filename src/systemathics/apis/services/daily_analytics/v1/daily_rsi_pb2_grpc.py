# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.daily_analytics.v1 import daily_rsi_pb2 as systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__rsi__pb2


class DailyRsiServiceStub(object):
    """Called to request daily relative strength index data. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DailyRsi = channel.unary_unary(
                '/systemathics.apis.services.daily_analytics.v1.DailyRsiService/DailyRsi',
                request_serializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__rsi__pb2.DailyRsiRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__rsi__pb2.DailyRsiResponse.FromString,
                )


class DailyRsiServiceServicer(object):
    """Called to request daily relative strength index data. 
    """

    def DailyRsi(self, request, context):
        """Gets daily relative strength index data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DailyRsiServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DailyRsi': grpc.unary_unary_rpc_method_handler(
                    servicer.DailyRsi,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__rsi__pb2.DailyRsiRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__rsi__pb2.DailyRsiResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.daily_analytics.v1.DailyRsiService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DailyRsiService(object):
    """Called to request daily relative strength index data. 
    """

    @staticmethod
    def DailyRsi(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.daily_analytics.v1.DailyRsiService/DailyRsi',
            systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__rsi__pb2.DailyRsiRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__rsi__pb2.DailyRsiResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
