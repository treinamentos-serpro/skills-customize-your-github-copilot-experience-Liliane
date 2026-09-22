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


# Os dados ficam em memória para manter os testes simples e rápidos.
tasks: dict[int, Task] = {
    1: Task(
        id=1,
        title="Estudar testes",
        description="Praticar pytest e TestClient",
    )
}
next_task_id = 2


@app.get("/tasks")
def list_tasks() -> list[Task]:
    return list(tasks.values())


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task_data: TaskCreate) -> Task:
    global next_task_id
    task = Task(id=next_task_id, **task_data.model_dump())
    tasks[next_task_id] = task
    next_task_id += 1
    return task


@app.get("/tasks/{task_id}")
def get_task(task_id: int) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_data: TaskUpdate) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated_task = task.model_copy(update={"status": task_data.status})
    tasks[task_id] = updated_task
    return updated_task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int) -> Response:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)
