import typing as t
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root() -> t.Dict[str, str]:
    return {"message": "Hello World"}
