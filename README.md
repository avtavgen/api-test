# api-test-project

Fast API test project

This is a simple api crud application

## Preconditions:

- Python 3.12
- FastAPI
- Uvicorn

## Clone the project

```
git clone git@github.com:avtavgen/api-test.git
```

## Run local

### Setup virtual environment

```
python -m venv venv
source venv/bin/activate
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
fastapi run main.py
```

### Run tests

```
pip install -r dev-requirements.txt
coverage run -m pytest . && coverage report -m 
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

## API documentation

```
http://0.0.0.0/docs
```