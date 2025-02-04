# gRPC Template

## Установка зависимостей / Dependency installation
```
pip install -r requirements.txt
```

## Генерация gRPC файлов / Generation of gRPC files
```
bash generate.sh
```

### Разбор команды генерации gRPC-файлов / Parsing the gRPC file generation command:
```sh
python -m grpc_tools.protoc -Iproto --python_out=src/generated --pyi_out=src/generated --grpc_python_out=src/generated proto/service.proto
```
- `-Iproto` – Указывает каталог с `.proto`-файлом, чтобы компилятор знал, где искать определение gRPC-сервисов.
- `--python_out=src/generated` – Генерирует Python-классы сообщений (`service_pb2.py`) в указанной папке (`src/generated`).
- `--pyi_out=src/generated` – Создаёт `.pyi`-файл с аннотациями типов для статического анализа и автодополнения.
- `--grpc_python_out=src/generated` – Генерирует код gRPC-сервера и клиента (`service_pb2_grpc.py`).
___
- `-Iproto` – Specifies the directory containing `.proto` files so the compiler knows where to find the gRPC service definitions.
- `--python_out=src/generated` – Generates Python message classes (`service_pb2.py`) in the specified `src/generated` directory.
- `--pyi_out=src/generated` – Creates a `.pyi` file with type annotations for static analysis and autocompletion.
- `--grpc_python_out=src/generated` – Generates gRPC server and client stubs (`service_pb2_grpc.py`).

## Запуск сервера / Server startup
```
python src/server.py
```

## Запуск клиента / Starting the client
```
python src/client.py
```