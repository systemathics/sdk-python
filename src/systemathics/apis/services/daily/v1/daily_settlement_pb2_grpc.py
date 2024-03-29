# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from systemathics.apis.services.daily.v1 import daily_settlement_pb2 as systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2


class DailySettlementsServiceStub(object):
    """Called to request daily Settlement price data. 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.DailySettlements = channel.unary_unary(
                '/systemathics.apis.services.daily.v1.DailySettlementsService/DailySettlements',
                request_serializer=systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2.DailySettlementsRequest.SerializeToString,
                response_deserializer=systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2.DailySettlementsResponse.FromString,
                )


class DailySettlementsServiceServicer(object):
    """Called to request daily Settlement price data. 
    """

    def DailySettlements(self, request, context):
        """Gets daily historical settlement prices
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DailySettlementsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'DailySettlements': grpc.unary_unary_rpc_method_handler(
                    servicer.DailySettlements,
                    request_deserializer=systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2.DailySettlementsRequest.FromString,
                    response_serializer=systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2.DailySettlementsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'systemathics.apis.services.daily.v1.DailySettlementsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DailySettlementsService(object):
    """Called to request daily Settlement price data. 
    """

    @staticmethod
    def DailySettlements(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/systemathics.apis.services.daily.v1.DailySettlementsService/DailySettlements',
            systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2.DailySettlementsRequest.SerializeToString,
            systemathics_dot_apis_dot_services_dot_daily_dot_v1_dot_daily__settlement__pb2.DailySettlementsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
