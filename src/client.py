import grpc
import generated.service_pb2 as service_pb2
import generated.service_pb2_grpc as service_pb2_grpc


def unary_call():
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = service_pb2_grpc.ExampleServiceStub(channel)
        response = stub.UnaryCall(service_pb2.Request(message="World"))
        print("Unary Response:", response.reply)


def client_streaming():
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = service_pb2_grpc.ExampleServiceStub(channel)
        requests = [service_pb2.Request(message=f"Message {i}") for i in range(5)]
        response = stub.ClientStreaming(iter(requests))
        print("Client Streaming Response:", response.reply)


def server_streaming():
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = service_pb2_grpc.ExampleServiceStub(channel)
        responses = stub.ServerStreaming(service_pb2.Request(message="Stream request"))
        for response in responses:
            print("Server Streaming Response:", response.reply)


def bidirectional_streaming():
    with grpc.insecure_channel("localhost:5000") as channel:
        stub = service_pb2_grpc.ExampleServiceStub(channel)
        requests = [service_pb2.Request(message=f"Bidirectional {i}") for i in range(5)]
        responses = stub.BidirectionalStreaming(iter(requests))
        for response in responses:
            print("Bidirectional Streaming Response:", response.reply)


if __name__ == "__main__":
    unary_call()
    client_streaming()
    server_streaming()
    bidirectional_streaming()
