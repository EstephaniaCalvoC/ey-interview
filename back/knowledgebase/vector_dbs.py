import abc

from models.embeddings import EmbeddingModel
from utils.exceptions import ExternalException
from configs import AzureAISearchConfig
from langchain_community.vectorstores.azuresearch import AzureSearch


class VectorDB(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def embed_documents(self):
        return None


class AzureAISearchVectorDB():
    
    def __init__(self, embeddings: EmbeddingModel) -> None:
        self.embeddings = embeddings
        self.__vector_store = self.__get_vector_store() 

    
    def embed_documents(self, documents) -> None:
        try:
            self.__vector_store.add_documents(documents=documents) 
        except Exception as e:
            raise ExternalException("There was an error connecting to Azure Search", e)
    
    
    def __get_vector_store(self) -> AzureSearch:
        try:
            return AzureSearch(
            azure_search_endpoint= AzureAISearchConfig.endpoint,
            azure_search_key=AzureAISearchConfig.key,
            index_name=AzureAISearchConfig.index_name,
            embedding_function=self.embeddings.model.embed_query
            )  
        except Exception as e:
            raise ExternalException("There was an error connecting to Azure Search", e)
        