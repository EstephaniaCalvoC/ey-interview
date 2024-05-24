import os
from dotenv import load_dotenv

load_dotenv()

class AzureAISearchConfig():
    endpoint: str = os.getenv("VECTOR_STORE_ADDRESS")
    key: str = os.environ.get("AZURE_AI_SEARCH_API_KEY")
    index_name: str = os.getenv("AZURE_AI_SEARCH_INDEX_NAME")
 
 
class AzureBlobConfig():
    connection_string = os.environ.get("AZURE_CONN_STRING")

class DocumentsAzureContainerConfig(AzureBlobConfig):
    name = os.environ.get("DOCUMENTS_CONTAINER_NAME")
    local_path = os.getenv("LOCAL_DOCUMENTS_ABS_PATH")


class AzureOpenAIChatModelConfig():
    name = os.environ.get("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME")
    version = os.environ.get("AZURE_OPENAI_API_VERSION")
    
    
class AzureOpenAIEmbeddingModelConfig():
    name = os.environ.get("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
    version = os.environ.get("AZURE_OPENAI_EMBEDDING_VERSION")
