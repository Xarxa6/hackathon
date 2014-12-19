#!/bin/bash

echo "Checking environment..."

result=$PWD
ENV_FOLDER="$result/env"

if [ -d "$ENV_FOLDER" ]; then
    echo "Environment folder found!"
    echo "Executing init.py file..."
    exec "$ENV_FOLDER/bin/python" src/init.py
else
    echo "env folder ~> $ENV_FOLDER does not exist! In order to boot the api you need to set up virtual environment first."
fi
