import os

from azure.storage.blob import BlobServiceClient
from configs import DocumentsAzureContainerConfig
from knowledgebase.exceptions import NoFilesToLoadException
from utils.error_handler import log_error
from utils.exceptions import ExternalException
from utils.logging import logger


def get_blob_service_client() -> BlobServiceClient:
    logger.debug("Init")

    try:
        return BlobServiceClient.from_connection_string(DocumentsAzureContainerConfig.connection_string)
    except Exception as e:
        raise ExternalException("There was an error connecting to Azure Blob Storage", e)


def upload_file_to_blob(blob_service_client: BlobServiceClient, blob_name: str, file_path: str) -> None:
    logger.debug("Init")

    try:
        blob_client = blob_service_client.get_blob_client(container=DocumentsAzureContainerConfig.name, blob=blob_name)
        with open(file_path, "rb") as data:
            blob_client.upload_blob(data)
    except Exception as e:
        raise ExternalException("There was an error connecting to Azure Blob Storage", e)


@log_error(logger)
def store_documents() -> None:
    logger.debug("Init")
    local_path = DocumentsAzureContainerConfig.local_path

    blob_service_client = get_blob_service_client()

    loaded_files = 0

    for root, _, files in os.walk(local_path):

        for file in files:
            file_path = os.path.join(root, file)
            blob_name = os.path.relpath(file_path, local_path)

            upload_file_to_blob(blob_service_client, blob_name, file_path)
            loaded_files += 1

    if not loaded_files:
        raise NoFilesToLoadException(local_path)

    logger.info("Documents loaded correctly")
