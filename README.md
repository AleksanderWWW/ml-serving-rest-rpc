# Co się dzieje po treningu
## Wprowadzenie do serwowania modeli uczenia maszynowego w architekturze REST i RPC


Niniejsze repozytorium zawiera kod użyty podczas warsztatów.
W razie pytań lub potrzeby konsultacji przy tworzeniu własnej wersji sugerowanego projektu zapraszam
do kontaktu.

---

## Setup

```commandline
git clone https://github.com/AleksanderWWW/ml-serving-rest-rpc.git
cd ml-serving-rest-rpc
pip install .[dev]
```

## REST

Linux/MacOS
```commandline
cd src/rest
```

Windows
```commandline
cd src\\rest
```

### Przykładowy server

```commandline
fastapi dev 01_basic_server.py
```

### Regresja liniowa

```commandline
python 03_linear_regression.py
```

### Serwer z regresją liniową

```commandline
fastapi dev 04_server.py
```

### Klient do predykcji

```commandline
python 05_client.py
```

---

## RPC

Linux/MacOS
```commandline
cd src/rpc
```

Windows
```commandline
cd src\\rpc
```

### Kompilacja pliku `proto`

```commandline
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. --mypy_out=. model.proto
```

### Serwer

```commandline
python server.py
```

### Klient

```commandline
python client.py
```
