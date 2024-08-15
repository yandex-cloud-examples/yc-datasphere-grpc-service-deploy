import os

import grpc

from echo.v1 import echo_pb2, echo_pb2_grpc

NODE_ENDPOINT = "node-api.datasphere.yandexcloud.net:443"
IAM_TOKEN = os.environ["NODE_IAM"]
FOLDER_ID = os.environ["FOLDER_ID"]
NODE_ID = os.environ["NODE_ID"]

REQUEST_METADATA = (
    ("authorization", f"Bearer {IAM_TOKEN}"),
    ("x-node-id", NODE_ID),
    ("x-permission", "datasphere.projects.exec"),
    ("x-folder-id", FOLDER_ID),
)


def main():
    message = "Hello, world!"
    credentials = grpc.ssl_channel_credentials()
    with grpc.secure_channel(NODE_ENDPOINT, credentials) as channel:
        client = echo_pb2_grpc.EchoStub(channel)
        response, _ = client.Reflect.with_call(
            echo_pb2.EchoRequest(message=message),
            metadata=REQUEST_METADATA,
        )
    print(f"Echo message: {response.message}")


if __name__ == "__main__":
    main()
