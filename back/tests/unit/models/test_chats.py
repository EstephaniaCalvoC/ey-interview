import pytest
from models.chats import AzureOpenAIChatModel
from utils.exceptions import ExternalException


@pytest.fixture
def mock_azure_chat_openai(mocker):
    return mocker.patch("models.chats.AzureChatOpenAI")


def test_azure_open_ai_chat_model_exception(mock_azure_chat_openai):
    mock_azure_chat_openai.side_effect = Exception("Connection error")
    with pytest.raises(ExternalException):
        AzureOpenAIChatModel()
