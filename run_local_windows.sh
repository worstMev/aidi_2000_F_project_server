#!/bin/bash
mkdir -p image &&
rm -f image/* &&
./myvenv/Scripts/uvicorn.exe app.main:app --host 0.0.0.0 --port 8000 --reload
