import grpc
import model_pb2
import model_pb2_grpc


def run() -> None:
    channel = grpc.insecure_channel("localhost:50051")
    stub = model_pb2_grpc.ModelServiceStub(channel)
    request = model_pb2.PredictRequest(x1=5.5, x2=3.1)
    print(f"Sending request: {request} (hex form: {request.SerializeToString().hex()})")
    response = stub.Predict(request)
    print(f"Predicted result: {round(response.result, 2)}")


if __name__ == "__main__":
    run()
