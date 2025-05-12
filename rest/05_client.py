import requests


url = "http://localhost:8000/predict"

r = requests.post(url, json={"x1": 5.5, "x2": 3.1})
print(r.json())
