from app.knowledgebase.blob_loader import store_documents
from app.knowledgebase.indexing import indexing_information_with_azure

if __name__ == "__main__":

    store_documents()
    indexing_information_with_azure()
