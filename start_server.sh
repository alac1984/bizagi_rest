#!/bin/bash
# my app is in main.py and the FastAPI class instance is named 'app'
alembic upgrade head
uvicorn application.main:app --host 0.0.0.0 --port 10000
