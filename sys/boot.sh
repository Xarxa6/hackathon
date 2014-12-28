#!/bin/bash

echo "Checking environment..."

CURRENT=$PWD
ENV_FOLDER="$CURRENT/env"
PY="$ENV_FOLDER/bin/python"

if [ -d "$ENV_FOLDER" ]; then
    echo "Environment folder found!"
    echo "Executing init.py file..."
    exec "$PY" src/init.py
else
    echo "env folder ~> $ENV_FOLDER does not exist! In order to boot the api you need to set up virtual environment first."
fi
