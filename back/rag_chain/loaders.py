import abc
from typing import List

from langchain_community.document_loaders import AzureBlobStorageContainerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_core.documents import Document

from utils.exceptions import ExternalException
from configs import DocumentsAzureContainerConfig


class Loader(metaclass=abc.ABCMeta):

    @property
    @abc.abstractmethod
    def chunks(self):
        return None


class DocumentsAzureContainer(Loader):

    def __init__(self):
        self.__loader = self.__get_loader()
        self._chunks = self._get_chunks()

    @property
    def chunks(self) -> List[Document]:
        return self._chunks

    def _get_chunks(self) -> List[Document]:
        try:
            documents = self.__loader.load()

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=30)
            return text_splitter.split_documents(documents)
        except Exception as e:
            raise ExternalException("There was an error formatting documents", e)

    def __get_loader(self) -> AzureBlobStorageContainerLoader:
        try:
            return AzureBlobStorageContainerLoader(
                conn_str=DocumentsAzureContainerConfig.connection_string, container=DocumentsAzureContainerConfig.name
            )
        except Exception as e:
            raise ExternalException("There was an error lodding documents from Azure", e)
