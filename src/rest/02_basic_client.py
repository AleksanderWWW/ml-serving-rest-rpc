import requests

r = requests.get("http://localhost:8000/hello")

print(r.json())

r = requests.get("http://localhost:8000/hello_with_query?name=SGH")
print(r.json())


r = requests.get("http://localhost:8000/model?year_born=1998")
print(r.json())
