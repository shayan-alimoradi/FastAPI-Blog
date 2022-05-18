# FastAPI-Blog
*This repository implement a simple blog app with FastAPI*

## Technologies used in this project

```
    Python 3.9 - Programming Language
    FastAPI 0.68.1 - Web API's
    Docker - Container Platform
    Pytest - Testing tool
    Git - Version Control
    PostgreSQL - PostgreSQL Database
    SQLAlchemy - SQL Toolkit and ORM
    Uvicorn - ASGI web server
```

## Simple Example

```
    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Hello World"}
```

## Installation

First **clone** or **download** this project.
```
$ git clone https://github.com/Shayan-9248/FastAPI-Blog
```

Then download and install docker and docker-compose

* [docker](https://docs.docker.com/engine/install/)
* [docker-compose](https://docs.docker.com/compose/install/)  

Then run the project with **docker-compose**.
```
$ docker-compose up
```

If you want to run in the background
```
$ docker-compose up -d
```

*You can see the list of all the API's from this url: **localhost:8000/docs/***