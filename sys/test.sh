#!/bin/bash

export PYTHONPATH=./src/
PY="$(which python)"

echo "Python bin is $PY"
python -m nltk.downloader all

py.test --verbose -c pytest.ini --capture=sys
