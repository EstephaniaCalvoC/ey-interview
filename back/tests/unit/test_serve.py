from fastapi.testclient import TestClient
import pytest
# Patch AzureOpenAIChatModel.model
@pytest.fixture()
def mock_model(mocker):
    return mocker.patch('models.chats.AzureChatOpenAI', return_value={"name": "name", "version": "version"})

@pytest.fixture()
def mock_retriever(mocker):
    return mocker.patch('rag_chain.retrievers.AzureAISearchRetriever', return_value={"name": "name", "version": "version"})


# Patch AzureAISearchDocumentsRetriever.retriever

@pytest.fixture()
def client(mock_model, mock_retriever):
    import serve
    return TestClient(serve.app)


def test_rag_invoke_invalid_call(client):
    
    response = client.post("/rag/invoke",
                           json={"input": {"input": "How is Mercedez-Benz using AI?"}}
                           )
    assert response.status_code == 200
    assert response.json()["output"] == "cats"
