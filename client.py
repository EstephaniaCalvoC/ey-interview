import requests


if __name__ == "__main__":

    # response = requests.post(
    #     "http://localhost:8000/rag/invoke",
    #     json={'input': {"input": "How is Mercedez-Benz using AI?"}}
    # )
    # print(response.json()["output"])

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
