#!/bin/bash

set -e -x

mkdir private _site public

python manage.py migrate
python manage.py import_contributors_data
python manage.py collectstatic --noinput
python manage.py distill-local public --force
