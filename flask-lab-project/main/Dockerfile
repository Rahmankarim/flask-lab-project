# Use official Python slim image
FROM python:3.11-slim

# Set a directory for the app
WORKDIR /app

# Install system deps (if needed) and cleanup
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage layer caching
COPY requirements.txt .

# Install python deps
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port
EXPOSE 5000

# Use gunicorn for production; bind to 0.0.0.0 so Docker can reach it
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2", "--threads", "2"]
