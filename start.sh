#!/bin/bash

# Cross-platform start script for OpsCenter
# Detects OS and runs appropriate commands for venv and requirements

VENV_DIR="venv"
REQ_FILE="requirements.txt"

if [[ "$(uname -s)" == *"NT"* || "$(uname -o 2>/dev/null)" == *"Msys"* || "$(uname -o 2>/dev/null)" == *"Cygwin"* ]]; then
    # Windows logic
    echo "Detected Windows OS."
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python -m venv $VENV_DIR
    fi
    .\$VENV_DIR\Scripts\activate
    echo "✅ Virtual environment activated."
    pip install -r $REQ_FILE
    cd backend
    echo "Starting the server..."
    uvicorn main:app --reload
else
    # Mac/Linux logic
    echo "Detected Mac/Linux OS."
    if [ ! -d "$VENV_DIR" ]; then
        echo "Creating virtual environment..."
        python3 -m venv $VENV_DIR
    fi
    source $VENV_DIR/bin/activate
    echo "✅ Virtual environment activated."
    pip install -r $REQ_FILE
    cd backend
    echo "Starting the server..."
    uvicorn main:app --reload
fi
