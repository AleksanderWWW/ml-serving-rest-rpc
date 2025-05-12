import grpc
import model_pb2
import model_pb2_grpc


def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = model_pb2_grpc.ModelServiceStub(channel)
    response = stub.Predict(model_pb2.PredictRequest(x1=5.5, x2=3.1))
    print(f"Predicted result: {response.result}")


if __name__ == "__main__":
    run()
