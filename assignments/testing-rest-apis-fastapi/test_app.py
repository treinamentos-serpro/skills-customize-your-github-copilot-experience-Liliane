from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_list_tasks_returns_a_json_list():
    response = client.get("/tasks")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task_returns_created_task():
    response = client.post(
        "/tasks",
        json={
            "title": "Revisar testes",
            "description": "Escrever testes para endpoints",
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "Revisar testes"
    assert body["status"] == "pending"


# Adicione os testes pedidos no README abaixo desta linha.
