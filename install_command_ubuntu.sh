#!/bin/bash

#ubuntu commands
echo "INFO : update and installing python and libsm6 libxext6 installed" &&
sudo apt update && 
sudo apt install python3-pip &&
sudo apt-get install ffmpeg libsm6 libxext6 &&
echo "INFO : pyhton installed , ffmpeg libsm6 libxext6 installed" &&
echo "INFO : create ./buffer directory, ./temp_student_pic directory" &&
mkdir -p  buffer && 
mkdir -p temp_student_pic &&
echo "INFO : create virtual environment python" &&
sudo apt install python3.12-venv &&
python3 -m venv myvenv &&
echo "INFO : pip install fastapi and  uvicorn" &&
./myvenv/bin/pip install "fastapi[standard]" uvicorn &&
./myvenv/bin/pip install tensorflow &&
./myvenv/bin/pip install tf-keras &&
./myvenv/bin/pip install keras 
