# async-api-project

FastAPI crud application, implemented with different async technologies.

## Preconditions:

- Python 3.12
- FastAPI
- Pydantic
- SQLModel
- Asyncpg
- Alembic

## Clone the project

```
git clone git@github.com:avtavgen/async-api.git
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
docker compose up -d --build
docker compose exec web alembic upgrade head
```

## API documentation

```
http://0.0.0.0/docs
```
