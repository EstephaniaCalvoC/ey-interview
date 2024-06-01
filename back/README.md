# ey-interview / Backend


## How to run

**Note:** Run the following steps in the back directory

1. **Set environment variables in `.env`** <a id="env-vars"></a>

    This API uses Azure cloud resources like Blob Storage and Azure AI Search.

    ~~~bash
    AZURE_CONN_STRING=
    DOCUMENTS_CONTAINER_NAME=
    LOCAL_DOCUMENTS_ABS_PATH=

    AZURE_AI_SEARCH_SERVICE_NAME=
    AZURE_AI_SEARCH_INDEX_NAME=
    AZURE_AI_SEARCH_API_KEY=
    VECTOR_STORE_ADDRESS=


    AZURE_OPENAI_API_VERSION=
    AZURE_OPENAI_ENDPOINT=
    AZURE_OPENAI_API_KEY=
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
    AZURE_OPENAI_EMBEDDING_VERSION=
    ~~~   

2. **Set virtual environment** <a id="venv"></a>

    ~~~bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ~~~

    If you are processing PDFs it's possible you need to install manually the following libraries

    ~~~bash
    pip install "unstructured[pdf]"
    apt-get update && apt-get install -y ffmpeg libsm6 libxext6
    sudo apt-get update
    sudo apt-get install -y libgl1-mesa-dev
    ~~~

3. **Indexing the information**
    ~~~bash
    python run_indexing.py
    ~~~

4. **Run service**

    ~~~bash
    python run_api.py
    ~~~

## How to call
- **Using request**
    ~~~python
    import requests

    response = requests.post(
        "http://localhost:8000/rag/invoke",
        json={'input': {"input": "Write your question here"}}
    )
    print(response.json()["output"])
    ~~~

- **Using RemoteRunnable**
    ~~~python
    from langserve import RemoteRunnable

     
    def main():
        """Client to interact with the served chain as if it were running client-side"""
        remote_chain = RemoteRunnable("http://localhost:8000/rag")
        response = remote_chain.invoke({"input": "Write your question here"})
        print(response)
        
    if __name__ == "__main__":
        main()
    ~~~
