import pytest
from rag_chain.loaders import DocumentsAzureContainer
from utils.exceptions import ExternalException


@pytest.fixture
def mock_azure_blob_storage_container_loader(mocker):
    return mocker.patch("rag_chain.loaders.AzureBlobStorageContainerLoader")


def test_documents_azure_container_loader_exception(mock_azure_blob_storage_container_loader):

    mock_azure_blob_storage_container_loader.side_effect = Exception("Connection error")
    with pytest.raises(ExternalException):
        DocumentsAzureContainer()


def test_documents_azure_container_chunks_exception(mock_azure_blob_storage_container_loader):
    mock_azure_blob_storage_container_loader.return_value.load = Exception("Connection error")
    with pytest.raises(ExternalException):
        DocumentsAzureContainer()
