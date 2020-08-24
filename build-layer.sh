#!/bin/bash
set -eo pipefail
rm -rf package
pipenv lock -r > requirements.txt
pip install --target ./package/python -r requirements.txt