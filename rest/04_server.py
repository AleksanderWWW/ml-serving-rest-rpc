from pathlib import Path

import fastapi
import joblib
import numpy as np
from pydantic import BaseModel


class Data(BaseModel):
    x1: float
    x2: float


class Result(BaseModel):
    result: float


app = fastapi.FastAPI()


@app.post("/predict")
def predict(data: Data) -> Result:
    model = joblib.load(Path(__file__).parents[0] / "model.pkl")

    result = model.predict(np.array([[data.x1, data.x2]]))

    return Result(result=result)


# x1=3 x2=4
# {
#     "x1": 3,
#     "x2": 4,
# }
