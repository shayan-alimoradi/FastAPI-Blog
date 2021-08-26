# FastAPI-Blog
*This repository implement a simple blog app with FastAPI*

### Usage

__Simple Example__
```
    from fastapi import FastAPI

    app = FastAPI()


    @app.get("/")
    async def root():
        return {"message": "Hello World"}
```

#### Requirements


__Python3.8+__

```
    1. Create a virtual environment via virtualenv venv.
    2. Activate venv through source venv/bin/activate.
    3. install all of the requirements package via command pip install -r requirements.txt.
```

__Now you can run the project with command **uvicorn main:app --reload**__