import requests


if __name__ == "__main__":

    response = requests.post(
        "http://localhost:8000/rag/invoke",
        json={'input': {"input": "How is Mercedez-Benz using AI?"}}
    )
    print(response.json()["output"])
    