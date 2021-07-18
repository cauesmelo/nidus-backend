from fastapi.testclient import TestClient

URL = "/hello/hello"

def test_hello_world(client: TestClient) -> None:
    response = client.get(URL)
    assert response.status_code == 200
    assert response.json() == "Hello World!"
