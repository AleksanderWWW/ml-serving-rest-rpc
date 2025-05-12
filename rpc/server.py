from concurrent import futures
import joblib

from pathlib import Path
import grpc
import model_pb2
import model_pb2_grpc

import numpy as np


# gRPC service implementation
class ModelService(model_pb2_grpc.ModelServiceServicer):
    def __init__(self):
        self.model = joblib.load(Path(__file__).parents[0] / "model.pkl")

    def Predict(self, request: model_pb2.PredictRequest, context):
        print(f"Received request: {request}")
        result = self.model.predict(np.array([[request.x1, request.x2]]))[0]
        return model_pb2.PredictResponse(result=result)


# Start the server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_pb2_grpc.add_ModelServiceServicer_to_server(ModelService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
