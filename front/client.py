import requests


def invoke_chain():
    response = requests.post(
        "http://localhost:8000/rag/invoke", json={"input": {"input": "How is Mercedez-Benz using AI?"}}
    )
    return response.json()["output"]


def invoke_chain_without_input_field():
    response = requests.post(
        "http://localhost:8000/rag/invoke", json={"input": {"answer": "How is Mercedez-Benz using AI?"}}
    )
    return response.text


def input_schema():
    response = requests.get("http://localhost:8000/rag/input_schema")
    return response.text


if __name__ == "__main__":

    # print(invoke_chain())

    print(invoke_chain_without_input_field())

    # response = requests.post(
    #     "http://localhost:8000/rag/invoke",
    #     json={'input': "How is Mercedez-Benz using AI?"}
    # )
    # print(response.text)

    # print(input_schema())
