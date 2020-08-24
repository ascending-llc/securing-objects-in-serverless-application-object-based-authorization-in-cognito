#!/bin/bash
set -eo pipefail
rm -rf package
cd lambda
pip install --target ../package/python -r requirements.txt