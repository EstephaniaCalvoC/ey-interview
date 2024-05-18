import abc

from back.models.embeddings import EmbeddingModel
from configs import AzureAISearchConfig
from langchain_community.vectorstores.azuresearch import AzureSearch


class VectorDB(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def embed_documents(self):
        return None


class AzureAISearchVectorDB():
    
    def __init__(self, embeddings: EmbeddingModel) -> None:
        self.__vector_store = AzureSearch(
            azure_search_endpoint= AzureAISearchConfig.endpoint,
            azure_search_key=AzureAISearchConfig.key,
            index_name=AzureAISearchConfig.index_name,
            embedding_function=embeddings.model.embed_query
            )    

    
    def embed_documents(self, documents) -> None:
        self.__vector_store.add_documents(documents=documents) 
        