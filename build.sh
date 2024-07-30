#! /usr/bin/env bash
# exit on error

set -o errexit

pip3.9 install -r requirements.txt

python3.9 manage.py collectstatic --no-input
python3.9 manage.py migrate
