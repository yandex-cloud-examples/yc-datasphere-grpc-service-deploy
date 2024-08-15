import logging
import os
from concurrent import futures

import grpc
from grpc_health.v1 import health, health_pb2, health_pb2_grpc
from grpc_reflection.v1alpha import reflection
from prometheus_client import start_http_server
from py_grpc_prometheus.prometheus_server_interceptor import PromServerInterceptor

from echo.v1 import echo, echo_pb2_grpc

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

GRPC_HOST = os.getenv("GRPC_HOST", "0.0.0.0")
GRPC_PORT = int(os.getenv("GRPC_PORT", 9875))
METRICS_PORT = int(os.getenv("METRICS_PORT", 9876))


def main():
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=(PromServerInterceptor(),),
    )

    # setup echo server
    echo_service = echo.EchoServicer()
    echo_pb2_grpc.add_EchoServicer_to_server(echo_service, server)

    # setup healthcheck
    reflection.enable_server_reflection(
        service_names=(
            echo.SERVICE_NAME,
            health.SERVICE_NAME,
            reflection.SERVICE_NAME,
        ),
        server=server,
    )

    health_servicer = health.HealthServicer()
    health_servicer.set(
        echo.SERVICE_NAME,
        health_pb2.HealthCheckResponse.ServingStatus.SERVING,
    )
    health_pb2_grpc.add_HealthServicer_to_server(health_servicer, server)

    # start prometheus server
    start_http_server(METRICS_PORT)

    # start server
    server.add_insecure_port(f"{GRPC_HOST}:{GRPC_PORT}")
    server.start()
    log.info("GRPC echo server started")
    server.wait_for_termination()
    log.info("GRPC echo server stopped")


if __name__ == "__main__":
    main()
