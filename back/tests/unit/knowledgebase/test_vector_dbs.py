import pytest
from app.knowledgebase.vector_dbs import AzureAISearchVectorDB
from app.utils.exceptions import ExternalException


@pytest.fixture
def mock_azure_search(mocker):
    return mocker.patch("app.knowledgebase.vector_dbs.AzureSearch")


def test_azure_ai_search_vector_db_exception(mocker, mock_azure_search):
    mock_azure_search.side_effect = Exception("Connection error")
    with pytest.raises(ExternalException):
        AzureAISearchVectorDB(mocker.MagicMock())


def test_azure_ai_search_vector_db_embed_documents_error(mocker, mock_azure_search):
    mock_azure_search.return_value.add_documents.side_effect = Exception("Connection error")
    with pytest.raises(ExternalException):
        AzureAISearchVectorDB(mocker.MagicMock()).embed_documents(mocker.MagicMock())
