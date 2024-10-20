# FastAPI Web Server

This is a FastAPI web server project managed with [Poetry](https://python-poetry.org/), a dependency management and packaging tool. The server is lightweight and asynchronous, designed to provide RESTful API endpoints with high performance and scalability.

## Install

```bash
poetry env use <path-path-to-a-local-python-version>
```

```bash
poetry install
```

## Start up

Activate virtual env

```bash
source .venv/bin/activate 
```

Run running the package as a python module

```bash
python -m webserver
```

## Start up with Docker

```bash
docker-compose -f docker/docker-compose.yml up
```
