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

## Submission (Step 7)

Before submitting, prepare these items and place screenshots in the `main/docs/` folder:

- GitHub repo link: add your group's repository URL here (e.g. https://github.com/<owner>/flask-lab-project)
- CI/CD screenshot: save a screenshot of a successful Actions run as `main/docs/ci-screenshot.png`
- Docker screenshot: save a screenshot of the app running from Docker as `main/docs/docker-screenshot.png`

Please replace the roles above with your actual team members and roles. The following quick-check guide will help you capture the required screenshots and verify the project is ready to submit.

How to capture the CI/CD screenshot

1. Push your final changes to GitHub on the branch you use for the workflow (for this repo it's often `backend` or `main`).
2. Open the repository on GitHub, click the Actions tab, open the latest successful workflow run, and take a screenshot that shows all jobs completed (or the run summary).
3. Save the image as `ci-screenshot.png` and place it in `main/docs/`.

How to capture the Docker screenshot

1. Build the Docker image locally:

```bash
# from the project `main/` directory
docker build -t flask-lab-project:latest .
```

2. Run the container and open the app:

```bash
docker run -p 5000:5000 flask-lab-project:latest
# open http://localhost:5000 in your browser
```

3. Take a screenshot showing the running app in the browser (and, if useful, the terminal with the `docker run` output). Save it as `docker-screenshot.png` and place it in `main/docs/`.

Final submission bundle

When you're ready, submit the following to your instructor or LMS:

- GitHub repository URL
- `main/docs/ci-screenshot.png`
- `main/docs/docker-screenshot.png`
- Ensure `main/README.md` lists each member and their role

If you want, I can commit these documentation files to your current branch and push them for you, or I can help run the tests and verify the CI workflow file at `main/.github/workflows/ci-cd.yml` is configured correctly.
