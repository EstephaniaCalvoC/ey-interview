import abc
import os
from dotenv import load_dotenv


from langchain_openai import AzureChatOpenAI

from utils.exceptions import ExternalException

load_dotenv()


class ChatModel(metaclass=abc.ABCMeta):
    
    @property
    @abc.abstractmethod
    def name(self):
        return None
    
    @property
    @abc.abstractmethod
    def model(self):
        return None



class AzureOpenAIChatModel():
    
    def __init__(self):
        self._name: str = os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"]
        self._version: str = os.environ["AZURE_OPENAI_API_VERSION"]
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
            return AzureChatOpenAI(
                openai_api_version=self._version,
                azure_deployment=self._name
                )
        except Exception as e:
            raise ExternalException("There was an error connecting to Azure OpenAI", e)
    