# Start from a minimal official Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy Python dependencies first for cache efficiency
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest (source and config)
COPY . .

# Expose port
EXPOSE 8000

# Default: use Gunicorn with Uvicorn worker for FastAPI
CMD ["gunicorn", "src.app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
