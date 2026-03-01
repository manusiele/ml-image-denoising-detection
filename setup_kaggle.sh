#!/bin/bash
# Load environment variables and run Kaggle setup

# Activate virtual environment
source venv/bin/activate

# Load .env file
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
    echo "✓ Loaded environment variables from .env"
else
    echo "✗ .env file not found!"
    exit 1
fi

# Run the setup script
python3 scripts/download_dataset.py
