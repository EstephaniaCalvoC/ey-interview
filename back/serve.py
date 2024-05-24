import uvicorn
from rag_chain.retrieval_chain import get_azure_retrieval_chain
from rag_chain.edpoints import create_chain_routes
from fastapi import FastAPI


app = FastAPI(
    title="LangChain Server", version="1.0", description="A simple API server using LangChain's Runnable interfaces"
)


if __name__ == "__main__":
    rag_chain = get_azure_retrieval_chain()
    create_chain_routes(app, rag_chain)
    uvicorn.run(app, host="localhost", port=8000)
