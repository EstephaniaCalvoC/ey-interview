# ey-interview / Backend


## How to run

1. **Set environment variables in .env** <a id="env-vars"></a>

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
    ~~~   

2. **Set virtual environment** <a id="venv"></a>

    ~~~bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ~~~

3. **Indexing the information**
    ~~~bash
    python indexing.py
    ~~~

4. **Run service**

    ~~~bash
    python serve.py
    ~~~

## How to call
- **Using request**
    ~~~python
    import requests

    response = requests.post(
        "http://localhost:8000/markdown/invoke",
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

- **Using the Navigator**

    Open `http://localhost:8000/rag/playground` in the navigator.


# TODOs

- [ ] Add error handling and tests
- [ ] Research how monitor the calls and evaluate the - [ ] results with Azuer OpenAI Studio
- [ ] Add forntend
- [ ] Research why the models classes cannot be instanciated with the abstract class
