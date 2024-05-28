import abc

from app.utils.exceptions import ExternalException
from langchain_community.retrievers import AzureAISearchRetriever


class Searcher(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def retriever(self):
        return None


class AzureAISearchDocumentsRetriever(Searcher):

    def __init__(self):
        self._retriever = self.__get_retriver()

    @property
    def retriever(self) -> AzureAISearchRetriever:
        return self._retriever

    @staticmethod
    def __get_retriver() -> AzureAISearchRetriever:
        try:
            return AzureAISearchRetriever()
        except Exception as e:
            raise ExternalException("There was an error creating the Azure retriever", e)
