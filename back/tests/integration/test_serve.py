from fastapi.testclient import TestClient
import pytest

from langchain_community.llms.fake import FakeListLLM
from langchain_community.embeddings import FakeEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from rag_chain.retrieval_chain import get_azure_retrieval_chain
from serve import app, create_chain_routes

from unittest.mock import patch


def fake_llm_model(responses):
    return FakeListLLM(responses=responses)
    

def fake_retriever():
    embedder = FakeEmbeddings(size=1352)
    
    db_vector = FAISS.from_documents(
        [Document(page_content="Knowlage 1"),
         Document(page_content="Knowlage 2")],
        embedder
        )
    
    return db_vector.as_retriever()


class TestAPIHappyPaths:
    
    responses = ["Final Answer 1", "Final Answer 2"]

    @pytest.fixture(scope="class")
    def client(self):
        with patch('models.chats.AzureChatOpenAI', return_value=fake_llm_model(self.responses)), \
             patch('rag_chain.retrievers.AzureAISearchRetriever', return_value=fake_retriever()):
            rag_chain = get_azure_retrieval_chain()
            create_chain_routes(app, rag_chain)
            return TestClient(app)

    def test_rag_invoke_valid_call_cls(self, client):
    
        response = client.post(
            "/rag/invoke",
            json={"input": {"input": "Is going this test going to pass?"}}
            )
        assert response.status_code == 200
        assert response.json()["output"] in self.responses
        