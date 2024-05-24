import pytest


@pytest.fixture(autouse=True)
def mock_azure_search_config(mocker):
    mock = mocker.patch("configs.AzureAISearchConfig")
    mock.endpoint = "endpoint"
    mock.key = "key"
    mock.index_name = "index_name"
    return mock


@pytest.fixture(autouse=True)
def mock_azure_blob_config(mocker):
    mock = mocker.patch("configs.AzureBlobConfig")
    mock.connection_string = "connection_string"
    return mock


@pytest.fixture(autouse=True)
def mock_documents_azure_container_config(mocker):
    mock = mocker.patch("configs.DocumentsAzureContainerConfig")
    mock.name = "name"
    mock.local_path = "local_path"
    return mock


@pytest.fixture(autouse=True)
def mock_azure_openai_chat_model_config(mocker):
    mock = mocker.patch("configs.AzureOpenAIChatModelConfig")
    mock.name = "name"
    mock.version = "version"
    return mock


@pytest.fixture(autouse=True)
def mock_azure_openai_embeddings_model_config(mocker):
    mock = mocker.patch("configs.AzureOpenAIEmbeddingModelConfig")
    mock.name = "name"
    mock.version = "version"
    return mock
