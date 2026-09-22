# 📘 Assignment: Testing REST APIs with FastAPI

## 🎯 Objective

Aprenda a escrever testes automatizados para uma API REST usando `pytest` e o `TestClient` do FastAPI. Você irá verificar respostas de sucesso, validação de dados, erros HTTP e operações que alteram o estado da API.

## 📝 Tasks

### 🛠️ Escrever o primeiro teste de leitura

#### Descrição

Use o `TestClient` para testar o endpoint `GET /tasks`. O teste deve confirmar que a rota responde corretamente e devolve uma lista de tarefas.

#### Requisitos

O programa concluído deve:

- Criar um cliente de testes a partir do objeto `app`
- Fazer uma requisição `GET /tasks`
- Verificar que o código de status é `200`
- Verificar que o corpo da resposta é uma lista JSON
- Executar com `pytest` sem iniciar um servidor Uvicorn

### 🛠️ Testar criação e validação

#### Descrição

Adicione testes para a criação de tarefas. Cubra tanto uma requisição válida quanto entradas que devem ser rejeitadas pela validação do modelo Pydantic.

#### Requisitos

O programa concluído deve:

- Testar `POST /tasks` com título e descrição válidos
- Verificar que uma tarefa válida retorna `201`
- Verificar que a resposta contém `id`, `title`, `description` e `status`
- Testar uma requisição sem título ou com título menor que 3 caracteres
- Verificar que dados inválidos retornam `422`
- Garantir que cada teste possa ser executado de forma independente

### 🛠️ Cobrir erros e operações completas

#### Descrição

Complete a suíte de testes para consultar, atualizar e remover tarefas. Inclua os casos de sucesso e os casos de erro mais importantes.

#### Requisitos

O programa concluído deve:

- Testar `GET /tasks/{task_id}` para uma tarefa existente
- Verificar que um identificador inexistente retorna `404`
- Testar `PATCH /tasks/{task_id}` com os status permitidos
- Testar que um status inválido retorna `422`
- Testar `DELETE /tasks/{task_id}` e verificar o status `204`
- Verificar que uma tarefa removida não pode mais ser consultada
- Conter pelo menos 8 testes automatizados passando

Execute os testes com:

```bash
pip install fastapi uvicorn pytest httpx
pytest -q
```
