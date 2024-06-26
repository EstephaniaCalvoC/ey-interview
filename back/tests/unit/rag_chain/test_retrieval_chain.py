import pytest
from app.rag_chain.retrieval_chain import get_chain
from app.utils.exceptions import ExternalException


@pytest.fixture
def mock_create_retrieval_chain(mocker):
    return mocker.patch("app.rag_chain.retrieval_chain.create_retrieval_chain")


def test_get_retrieval_chain_exception(mocker, mock_create_retrieval_chain):
    mock_create_retrieval_chain.side_effect = Exception("Connection error")
    with pytest.raises(ExternalException):
        get_chain(mocker.MagicMock(), mocker.MagicMock())
