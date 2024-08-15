import logging

from echo.v1 import echo_pb2, echo_pb2_grpc

log = logging.getLogger(__name__)

SERVICE_NAME = echo_pb2.DESCRIPTOR.services_by_name["Echo"].full_name


class EchoServicer(echo_pb2_grpc.EchoServicer):
    def Reflect(self, request, context):
        log.info("Got echo request '%s'", request.message)
        return echo_pb2.EchoResponse(message=request.message)
