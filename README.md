# Todo API

A small FastAPI Todo service, containerized with Docker and automated with a GitHub Actions CI/CD pipeline.

## Endpoints

| Method | Path           | Description            |
|--------|----------------|------------------------|
| GET    | `/health`      | Health check           |
| GET    | `/todos`       | List all todos         |
| POST   | `/todos`       | Create a todo          |
| DELETE | `/todos/{id}`  | Delete a todo by id    |

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs for the interactive API docs.

## Run the tests

```bash
pytest tests/ -v
```

## Run with Docker

```bash
docker build -t todo-api .
docker run -p 8000:8000 todo-api
```

Then visit http://localhost:8000/health.

## CI/CD

On every push to `main`, GitHub Actions (`.github/workflows/ci-cd.yml`):

1. Installs dependencies and runs the test suite.
2. If tests pass, builds the Docker image and pushes it to Docker Hub.

Pushing to Docker Hub requires two repository secrets:

- `DOCKERHUB_USERNAME` — your Docker Hub username
- `DOCKERHUB_TOKEN` — a Docker Hub access token

Add them under **Settings → Secrets and variables → Actions** in the GitHub repo.
