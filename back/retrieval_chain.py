from dotenv import load_dotenv

from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from utils.logging import logger
from models.chats import ChatModel, AzureOpenAIChatModel
from retrievers import Searcher, AzureAISearchDocumentsRetriever


def get_chain(searcher: Searcher, chat_model: ChatModel):
    """
    A function to get a RAG chain

    Returns:
        retrieval_chain: The generated retrieval chain
    """
    logger.info("Init")     
    
    prompt = ChatPromptTemplate.from_template(
        "Answer the following question based only on the next context:"
        "\n<context>\n{context}\n</context>"
        "\nQuestion: {input}"
        )
    
    document_chain = create_stuff_documents_chain(chat_model.model, prompt)
    
    retrieval_chain = create_retrieval_chain(searcher.retriever, document_chain) | (lambda x: x["answer"])
    
    return retrieval_chain


if __name__ == "__main__":
    
    rag_chain = get_chain(
        searcher=AzureAISearchDocumentsRetriever(),
        chat_model=AzureOpenAIChatModel()
    )
    result = rag_chain.invoke({"input": "How can EY helpme to integrate AI in my process?"})
    
    print(result)
