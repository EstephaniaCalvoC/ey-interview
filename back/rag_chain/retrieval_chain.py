from langchain.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

from utils.error_handler import log_error
from utils.exceptions import ExternalException
from utils.logging import logger
from models.chats import ChatModel, AzureOpenAIChatModel
from rag_chain.retrievers import Searcher, AzureAISearchDocumentsRetriever


def get_chain(searcher: Searcher, chat_model: ChatModel):
    """
    A function to get a RAG chain

    Returns:
        retrieval_chain: The generated retrieval chain
    """
    logger.debug("Init")

    try:
        prompt = ChatPromptTemplate.from_template(
            "Answer the following question based only on the next context:"
            "\n<context>\n{context}\n</context>"
            "\nQuestion: {input}"
        )

        document_chain = create_stuff_documents_chain(chat_model.model, prompt)

        retrieval_chain = create_retrieval_chain(searcher.retriever, document_chain) | (lambda x: x["answer"])

        return retrieval_chain

    except Exception as e:
        raise ExternalException("There was an error creating the retrieval chain", e)


@log_error(logger)
def get_azure_retrieval_chain():
    return get_chain(searcher=AzureAISearchDocumentsRetriever(), chat_model=AzureOpenAIChatModel())


if __name__ == "__main__":
    rag_chain = get_azure_retrieval_chain()
    result = rag_chain.invoke({"input": "How can EY helpme to integrate AI in my process?"})

    print(result)
