#!/bin/bash

# Name of your virtual environment folder
VENV_DIR="venv"

# Check if virtual environment exists
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate
echo "✅ Virtual environment activated."

# Install dependencies if not already installed
pip install -r requirements.txt

# Start FastAPI dev server
uvicorn main:app --reload
