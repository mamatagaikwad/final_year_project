#!/bin/bash
export DB_HOST=localhost
export DB_USER=root
export DB_PASS=password
export DB_NAME=skindb
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
