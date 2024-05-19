import pytest

from rag_chain.retrievers import AzureAISearchDocumentsRetriever
from utils.exceptions import ExternalException

@pytest.fixture
def mock_azure_ai_search_retriever(mocker):
    return mocker.patch('rag_chain.retrievers.AzureAISearchRetriever')

def test_azure_ai_search_documents_retriever(
    mock_azure_ai_search_retriever
    ):
    mock_azure_ai_search_retriever.side_effect = Exception('Connection error')
    with pytest.raises(ExternalException):
        AzureAISearchDocumentsRetriever()
        