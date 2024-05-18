from knowledgebase_loader.blob import store_documents
from loaders import Loader, DocumentsAzureContainer
from models.embedding_model import AzureOpenAIEmbeddingModel
from vector_dbs import VectorDB, AzureAISearchVectorDB
from utils.logging import logger


def indexing_information(vector_db: VectorDB, loader: Loader) -> None:
    logger.info("Init")
    
    vector_db.embed_documents(loader.chunks)

    logger.info("Documents embedded successfully")


if __name__ == "__main__":

    store_documents()

    embeddings = AzureOpenAIEmbeddingModel()

    indexing_information(
        vector_db=AzureAISearchVectorDB(embeddings),
        loader=DocumentsAzureContainer()
    )
