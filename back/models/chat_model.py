import abc
import os
from dotenv import load_dotenv


from langchain_openai import AzureChatOpenAI

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
        self.__model = AzureChatOpenAI(
            openai_api_version=self._version,
            azure_deployment=self._name
            )

    @property
    def name(self):
        return self._name
    
    @property
    @abc.abstractmethod
    def model(self):
        return self.__model
    