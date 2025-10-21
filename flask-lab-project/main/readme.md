# Flask Lab Project — main

This folder contains the Flask app, tests, Dockerfile, and CI workflow used in the lab.

Contents

- `app.py` — Flask application with `/`, `/health`, and `/data` endpoints.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — container image build.
- `tests/test_app.py` — pytest unit tests.
- `.github/workflows/ci-cd.yml` — GitHub Actions workflow.

How to build, test, and run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run tests

```bash
python -m pytest -q
```

3. Run the app locally

```bash
python app.py
```

4. Build Docker image

```bash
docker build -t flask-lab-project:latest .
docker run -p 5000:5000 flask-lab-project:latest
```

CI/CD notes

- Workflow triggers on push and PRs to `main` and will run tests and build the Docker image.
- To push to Docker Hub, configure `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` in repository secrets.

# Flask Lab Project (main)

## Overview

Simple Flask application for the Collaborative Lab: health, homepage, and /data POST endpoint.

## Roles

- Member 1 (Backend Lead): Implemented routes in `main/app.py` and unit tests.
- Member 2 (Frontend/API Integration): Responsible for `templates/` and `static/`.
- Member 3 (DevOps): Wrote `Dockerfile` and `.github/workflows/ci-cd.yml`.

## Build & Run (locally)

1. Create virtualenv and install deps:
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r main/requirements.txt
   ```
