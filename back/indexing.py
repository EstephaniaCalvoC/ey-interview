import os

from azure.storage.blob import BlobServiceClient

from loaders import Loader, DocumentsAzureContainer
from models.embedding_model import AzureOpenAIEmbeddingModel
from vector_dbs import VectorDB, AzureAISearchVectorDB
from utils.logging import logger
from configs import DocumentsAzureContainerConfig


def store_documents_into_blob() -> None:
    logger.info("Init")
    
    blob_service_client = BlobServiceClient.from_connection_string(
        DocumentsAzureContainerConfig.connection_string
        )
    local_path = DocumentsAzureContainerConfig.local_path

    for root, _, files in os.walk(local_path):
        for file in files:
            file_path = os.path.join(root, file)
            blob_name = os.path.relpath(file_path, local_path)

            blob_client = blob_service_client.get_blob_client(
                container=DocumentsAzureContainerConfig.name,
                blob=blob_name
            )

            with open(file_path, "rb") as data:
                blob_client.upload_blob(data)

    logger.info("Documents loaded correctly")


def indexing_information(vector_db: VectorDB, loader: Loader) -> None:
    logger.info("Init")
    
    vector_db.embed_documents(loader.chunks)

    logger.info("Documents embedded successfully")


if __name__ == "__main__":

    store_documents_into_blob()

    embeddings = AzureOpenAIEmbeddingModel()

    indexing_information(
        vector_db=AzureAISearchVectorDB(embeddings),
        loader=DocumentsAzureContainer()
    )
