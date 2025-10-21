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
