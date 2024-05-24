from blob_loader import store_documents
from rag_chain.loaders import Loader, DocumentsAzureContainer
from models.embeddings import AzureOpenAIEmbeddingModel
from vector_dbs import VectorDB, AzureAISearchVectorDB
from utils.logging import logger
from utils.error_handler import log_error


def indexing_information(vector_db: VectorDB, loader: Loader) -> None:
    logger.debug("Init")

    vector_db.embed_documents(loader.chunks)

    logger.info("Documents embedded successfully")


@log_error(logger)
def indexing_information_with_azure() -> None:
    logger.debug("Init")

    embeddings = AzureOpenAIEmbeddingModel()

    indexing_information(vector_db=AzureAISearchVectorDB(embeddings), loader=DocumentsAzureContainer())


if __name__ == "__main__":

    store_documents()
    indexing_information_with_azure()
