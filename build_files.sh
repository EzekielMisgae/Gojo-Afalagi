#!/bin/bash

# build_files.sh
echo "Building the project..."
pip install -r requirements.txt
python3.9 manage.py collectstatic