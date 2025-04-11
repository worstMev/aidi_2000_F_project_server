#!/bin/bash

python -m venv myvenv &&
./myvenv/Scripts/pip install "fastapi[standard]" uvicorn &&
./myvenv/Scripts/pip install opencv-python &&
./myvenv/Scripts/pip install numpy &&
./myvenv/Scripts/pip install Pillow &&
./myvenv/Scripts/pip install keras &&
./myvenv/Scripts/pip install tensorflow 
