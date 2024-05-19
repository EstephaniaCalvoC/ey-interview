from langserve import add_routes
import uvicorn
from retrieval_chain import get_chain
from utils.app_config import create_app, Input
from models.chats import AzureOpenAIChatModel
from retrievers import AzureAISearchDocumentsRetriever

rag_chain = get_chain(
        searcher=AzureAISearchDocumentsRetriever(),
        chat_model=AzureOpenAIChatModel()
    )

app = create_app()


add_routes(
    app,
    rag_chain.with_types(input_type=Input),
    path="/rag"
    )
    

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

