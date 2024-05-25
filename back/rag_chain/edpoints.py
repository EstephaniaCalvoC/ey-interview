from typing import Any, Dict

from fastapi import Depends, HTTPException, Request
from langchain.pydantic_v1 import BaseModel as LangchainBaseModel
from langserve import add_routes
from pydantic import BaseModel

RAG_PATH = "/rag"


class Input(LangchainBaseModel):
    input: str


class Output(LangchainBaseModel):
    output: str


class RequestBody(BaseModel):
    input: Dict[str, Any]


async def validate_invoke_request_body(request: Request):
    path = request.url.path

    if path != f"{RAG_PATH}/invoke":
        return

    body = await request.json()

    try:
        RequestBody.model_validate(body)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid body schema. Please check {RAG_PATH}/input_schema")


def create_chain_routes(app, rag_chain):
    # TODO: Consider disable the playground and other debug routes

    add_routes(
        app,
        rag_chain.with_types(input_type=Input),
        path=RAG_PATH,
        dependencies=[Depends(validate_invoke_request_body)],
    )
