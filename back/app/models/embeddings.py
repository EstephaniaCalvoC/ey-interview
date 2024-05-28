import abc

from app.configs import AzureOpenAIEmbeddingModelConfig
from app.utils.exceptions import ExternalException
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


class AzureOpenAIEmbeddingModel:

    def __init__(self):
        self._name: str = AzureOpenAIEmbeddingModelConfig.name
        self._version: str = AzureOpenAIEmbeddingModelConfig.version
        self.__model = self.__get_model()

    @property
    def name(self):
        return self._name

    @property
    @abc.abstractmethod
    def model(self):
        return self.__model

    def __get_model(self):
        try:
            return AzureOpenAIEmbeddings(azure_deployment=self._name, openai_api_version=self._version)
        except Exception as e:
            raise ExternalException("There was an error connecting to Azure OpenAI", e)
