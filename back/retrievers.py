import abc
from langchain_community.retrievers import AzureAISearchRetriever

from configs import AzureAISearchConfig

class Searcher(metaclass=abc.ABCMeta):
    
    @property
    @abc.abstractmethod
    def retriever(self):
        return None


class AzureAISearchDocumentsRetriever(Searcher):
    
    def __init__(self):
        self._retriever = AzureAISearchRetriever()
        
    @property
    def retriever(self) -> AzureAISearchRetriever:
        return self._retriever
    