import requests


def invoke_chain():
    response = requests.post(
        "http://localhost:8000/rag/invoke", json={"input": {"input": "How is Mercedez-Benz using AI?"}}
    )
    return response.json()["output"]


if __name__ == "__main__":

    # print(invoke_chain())

    response = requests.post(
        "http://localhost:8000/rag/invoke", json={"input": {"answer": "How is Mercedez-Benz using AI?"}}
    )
    print(response.text)

    # response = requests.post(
    #     "http://localhost:8000/rag/invoke",
    #     json={'input': "How is Mercedez-Benz using AI?"}
    # )
    # print(response.text)

    # response = requests.get(
    #     "http://localhost:8000/rag/input_schema"
    # )
    # print(response.text)
