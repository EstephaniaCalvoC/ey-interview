import abc
import os
from dotenv import load_dotenv

from langchain_openai import AzureOpenAIEmbeddings

load_dotenv()


class EmbeddingModel(metaclass=abc.ABCMeta):
    
    @property
    @abc.abstractmethod
    def name(self):
        return None
    
    @property
    @abc.abstractmethod
    def model(self):
        return None



class AzureOpenAIEmbeddingModel():
    
    def __init__(self):
        self._name: str = os.environ.get("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
        self._version: str = "2023-05-15"
        self.__model = AzureOpenAIEmbeddings(
            azure_deployment=self._name,
            openai_api_version=self._version)

    @property
    def name(self):
        return self._name
    
    @property
    @abc.abstractmethod
    def model(self):
        return self.__model
