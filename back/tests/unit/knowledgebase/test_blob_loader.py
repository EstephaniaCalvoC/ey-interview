import pytest
from app.knowledgebase.blob_loader import BlobServiceClient, get_blob_service_client, upload_file_to_blob
from app.utils.exceptions import ExternalException


@pytest.fixture
def mock_blob_service_client(mocker):
    return mocker.patch.object(BlobServiceClient, "from_connection_string")


@pytest.fixture
def mock_blob_client(mocker):
    return mocker.patch.object(BlobServiceClient, "get_blob_client")


def test_get_blob_service_client_connection_error(mock_blob_service_client):

    mock_blob_service_client.side_effect = Exception("Connection error")

    with pytest.raises(ExternalException):
        get_blob_service_client()


def test_upload_file_to_blob_error(mocker, mock_blob_client):

    file_path = "test.txt"

    with pytest.raises(ExternalException):
        mock_blob_client.return_value.upload_blob.side_effect = Exception("Upload error")
        upload_file_to_blob(mocker.MagicMock(), "test.txt", file_path)
