#!/bin/bash

python -m venv myvenv &&
./myvenv/Scripts/pip install "fastapi[standard]" uvicorn &&
./myvenv/Scripts/pip install keras
./myvenv/Scripts/pip install tensorflow
