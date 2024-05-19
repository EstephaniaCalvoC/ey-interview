from langserve import add_routes
import uvicorn
from retrieval_chain import get_azure_retrieval_chain
from utils.app_config import create_app, Input

rag_chain = get_azure_retrieval_chain()

app = create_app()

add_routes(
    app,
    rag_chain.with_types(input_type=Input),
    path="/rag"
    )
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
