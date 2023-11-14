# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.daily_analytics.v1 import daily_bollinger_pb2 as systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__bollinger__pb2


class DailyBollingerServiceStub(object):
    """Called to request daily Bollinger bands data. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DailyBollinger = channel.unary_unary(
                '/systemathics.apis.services.daily_analytics.v1.DailyBollingerService/DailyBollinger',
                request_serializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__bollinger__pb2.DailyBollingerRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__bollinger__pb2.DailyBollingerResponse.FromString,
                )


class DailyBollingerServiceServicer(object):
    """Called to request daily Bollinger bands data. 
    """

    def DailyBollinger(self, request, context):
        """Gets daily Bollinger bands data
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DailyBollingerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DailyBollinger': grpc.unary_unary_rpc_method_handler(
                    servicer.DailyBollinger,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__bollinger__pb2.DailyBollingerRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__bollinger__pb2.DailyBollingerResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.daily_analytics.v1.DailyBollingerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DailyBollingerService(object):
    """Called to request daily Bollinger bands data. 
    """

    @staticmethod
    def DailyBollinger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.daily_analytics.v1.DailyBollingerService/DailyBollinger',
            systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__bollinger__pb2.DailyBollingerRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_daily__analytics_dot_v1_dot_daily__bollinger__pb2.DailyBollingerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)