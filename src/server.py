import sys
import grpc
from concurrent import futures

from generated import service_pb2 as service_pb2
from generated import service_pb2_grpc as service_pb2_grpc


class ExampleService(service_pb2_grpc.ExampleServiceServicer):
    def UnaryCall(self, request, context):
        return service_pb2.Response(reply=f"Hello {request.message}")

    def ClientStreaming(self, request_iterator, context):
        messages = " ".join(req.message for req in request_iterator)
        return service_pb2.Response(reply=f"Received: {messages}")

    def ServerStreaming(self, request, context):
        for i in range(5):
            yield service_pb2.Response(reply=f"Reply {i} to {request.message}")

    def BidirectionalStreaming(self, request_iterator, context):
        for request in request_iterator:
            yield service_pb2.Response(reply=f"Echo: {request.message}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleService(), server)
    server.add_insecure_port("localhost:5000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Server starting...")
    serve()
