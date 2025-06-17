#!/bin/bash

# Cross-platform shutdown script for OpsCenter
# Updates requirements.txt with current venv packages

VENV_DIR="venv"
REQ_FILE="requirements.txt"

if [[ "$(uname -s)" == *"NT"* || "$(uname -o 2>/dev/null)" == *"Msys"* || "$(uname -o 2>/dev/null)" == *"Cygwin"* ]]; then
    # Windows logic
    echo "Detected Windows OS."
    .\$VENV_DIR\Scripts\activate
    echo "✅ Virtual environment activated."
    pip freeze > $REQ_FILE
    echo "requirements.txt updated with current dependencies."
    deactivate
else
    # Mac/Linux logic
    echo "Detected Mac/Linux OS."
    source $VENV_DIR/bin/activate
    echo "✅ Virtual environment activated."
    pip freeze > $REQ_FILE
    echo "requirements.txt updated with current dependencies."
    deactivate
fi
