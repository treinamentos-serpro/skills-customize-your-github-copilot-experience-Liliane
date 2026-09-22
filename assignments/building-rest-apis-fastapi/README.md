# 📘 Atividade: Building REST APIs with FastAPI

## 🎯 Objetivo

Aprenda a construir uma API REST usando o framework FastAPI, definindo rotas, validando dados com modelos Pydantic e retornando códigos de status HTTP apropriados.

## 📝 Tarefas

### 🛠️ Criar o endpoint de listagem

#### Descrição

Complete a API inicial para que ela disponibilize uma rota `GET /tasks` capaz de retornar todas as tarefas armazenadas em memória.

#### Requisitos

O programa concluído deve:

- Iniciar uma aplicação FastAPI usando o objeto `app`
- Implementar a rota `GET /tasks`
- Retornar a lista de tarefas em formato JSON
- Permitir que a API seja executada com `uvicorn starter-code:app --reload`

### 🛠️ Adicionar criação e validação de tarefas

#### Descrição

Crie um modelo Pydantic para validar novas tarefas e implemente a rota `POST /tasks`. Cada tarefa deve receber um identificador único e começar com o status `pending`.

#### Requisitos

O programa concluído deve:

- Validar os campos `title` e `description` recebidos no corpo da requisição
- Exigir que `title` tenha pelo menos 3 caracteres
- Rejeitar dados inválidos automaticamente com uma resposta `422`
- Criar e armazenar uma nova tarefa com um identificador inteiro único
- Retornar a tarefa criada com o código de status `201`

Exemplo de requisição:

```json
{
  "title": "Estudar FastAPI",
  "description": "Praticar rotas e modelos Pydantic"
}
```

### 🛠️ Implementar consulta, atualização e remoção

#### Descrição

Complete o conjunto de operações da API adicionando endpoints para consultar uma tarefa pelo identificador, atualizar seu status e removê-la.

#### Requisitos

O programa concluído deve:

- Implementar `GET /tasks/{task_id}`
- Retornar `404` quando o identificador não existir
- Implementar `PATCH /tasks/{task_id}` para alterar o status da tarefa
- Aceitar somente os status `pending`, `in_progress` e `done`
- Implementar `DELETE /tasks/{task_id}`
- Retornar `204` após remover uma tarefa existente
- Manter as respostas em formato JSON, exceto na resposta `204`

Exemplos de rotas:

```text
GET    /tasks/1
PATCH  /tasks/1
DELETE /tasks/1
```
