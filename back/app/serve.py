from app.rag_chain.edpoints import create_chain_routes
from app.rag_chain.retrieval_chain import get_azure_retrieval_chain
from fastapi import FastAPI

app = FastAPI(
    title="LangChain Server", version="1.0", description="A simple API server using LangChain's Runnable interfaces"
)

rag_chain = get_azure_retrieval_chain()
create_chain_routes(app, rag_chain)
