.PHONY: proto
proto:
	python -m grpc_tools.protoc -I ./proto --python_out=. --grpc_python_out=. ./proto/echo/v1/echo.proto

.PHONY: clean
clean:
	rm -f ./echo/v1/echo_pb2.py ./echo/v1/echo_pb2_grpc.py
