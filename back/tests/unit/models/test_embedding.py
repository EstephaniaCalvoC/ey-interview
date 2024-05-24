import pytest
from models.embeddings import AzureOpenAIEmbeddingModel
from utils.exceptions import ExternalException


@pytest.fixture
def mock_azure_openai_embeddings(mocker):
    return mocker.patch("models.embeddings.AzureOpenAIEmbeddings")


def test_get_model_exception(mock_azure_openai_embeddings):
    mock_azure_openai_embeddings.side_effect = Exception("Connection error")
    with pytest.raises(ExternalException):
        AzureOpenAIEmbeddingModel()
