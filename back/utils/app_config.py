from fastapi import FastAPI
from langchain.pydantic_v1 import BaseModel


def create_app():
    app = FastAPI(
        title="LangChain Server",
        version="1.0",
        description="A simple API server using LangChain's Runnable interfaces"
        )
    return app


class Input(BaseModel):
    input: str


class Output(BaseModel):
    output: str
