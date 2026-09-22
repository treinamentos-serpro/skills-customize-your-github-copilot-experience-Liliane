from typing import Literal

from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task API")


class TaskCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str


class TaskUpdate(BaseModel):
    status: Literal["pending", "in_progress", "done"]


class Task(TaskCreate):
    id: int
    status: Literal["pending", "in_progress", "done"] = "pending"


# Os dados ficam em memória para que o foco seja a construção da API.
tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/tasks")
def list_tasks() -> list[Task]:
    """Retorne todas as tarefas."""
    pass


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    """Crie uma tarefa e atribua um identificador único."""
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    """Retorne uma tarefa pelo identificador."""
    pass


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate) -> Task:
    """Atualize o status de uma tarefa."""
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    """Remova uma tarefa existente."""
    pass
