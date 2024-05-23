from langserve import add_routes
import uvicorn
from rag_chain.retrieval_chain import get_azure_retrieval_chain
from utils.app_config import create_app, Input


app = create_app()

def create_chain_routes(app, rag_chain):

    add_routes(
        app,
        rag_chain.with_types(input_type=Input),
        path="/rag"
        )
    

if __name__ == "__main__":
    rag_chain = get_azure_retrieval_chain()
    create_chain_routes(app, rag_chain)
    uvicorn.run(app, host="localhost", port=8000)
