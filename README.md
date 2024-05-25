# Custom ChatUI Backend

This repository contains the backend services designed to work with the custom Huggingface ChatUI frontend. It includes a Flask application, Celery for handling asynchronous tasks, and Redis as a message broker. The backend serves as an example or a wrapper around an LLM project to interface with this custom [ChatUI](https://github.com/ChaZachBrown/chatui-custom-backend).

## Overview

The backend provides API endpoints for the ChatUI frontend to interact with. It processes requests asynchronously using Celery and Redis, allowing for efficient handling of complex tasks. This setup is intended to be a modular example that can be adapted to different LLM projects.

### Features

- **Flask API**: A simple and scalable Flask application for handling API requests.
- **Celery**: A distributed task queue for managing asynchronous tasks.
- **Redis**: An in-memory data structure store used as a message broker by Celery.
- **Docker**: Containerized services for easy deployment and scalability.

## Installation

### Prerequisites

- Docker and Docker Compose installed
- Python 3.11 or higher

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd chatui-backend
2. **Build:**
    * ``` docker-compose build ```
3. **Run:**
    * ``` docker-compose up ```
