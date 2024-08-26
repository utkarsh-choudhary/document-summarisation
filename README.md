# PDF Summarizer

## Overview

This project is a **document summarization application** with a FastAPI backend and a React frontend. It allows users to input text passages and receive summarized versions of the input text.

## File Structure

```plaintext
fastapi-document-summarizer/
│
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   └── [other backend files]
│
├── frontend/
│   ├── Dockerfile
│   └── [frontend files, e.g., package.json, src/]
│
└── docker-compose.yml

```

## Requirements

- **Docker**: Ensure Docker is installed on your machine. You can download it from the [official Docker website](https://www.docker.com/get-started).

## Setup and Running the Application

### 1. Clone the Repository

Clone the repository to your local machine using the following commands:

```bash
git clone <repository-url>
cd fastapi-document-summarizer
```

2. Build and Start the Containers

Build and start the Docker containers with the following command:


```bash
docker-compose up --build
```

This will:

    Build the Docker images for both the backend (FastAPI) and frontend (React) if they don't already exist.
    Start the containers according to the configurations specified in docker-compose.yml.

3. Access the Application

Once the containers are running, access the application at:

    Backend (FastAPI): http://localhost:8000
    Frontend (React): http://localhost:3000

4. Stopping the Application

Stop the running containers with:


```bash
docker-compose down
```
