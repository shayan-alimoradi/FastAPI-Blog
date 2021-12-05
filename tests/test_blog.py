from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_blog():
    response = client.get("/blogs/1")
    assert response.status_code == 200


def test_sign_in_error():
    response = client.post("/sign-in", data={"username": "", "password": ""})
    access_token = response.json().get("access_token")
    assert access_token == None
    message = response.json().get("detail")[0].get("msg")
    assert message == "field required"


def test_sign_in_success():
    response = client.post(
        "/sign-in", data={"username": "shayan@email.com", "password": "shayan"}
    )
    access_token = response.json().get("access_token")
    assert access_token


def test_create_blog():
    auth = client.post(
        "/sign-in", data={"username": "shayan@email.com", "password": "shayan"}
    )
    access_token = auth.json().get("access_token")

    assert access_token

    response = client.post(
        "/blogs/create",
        json={"title": "test77", "user_id": 2},
        headers={"Authorization": "bearer " + access_token},
    )
    assert response.status_code == 201
    assert response.json().get("title") == "test77"
