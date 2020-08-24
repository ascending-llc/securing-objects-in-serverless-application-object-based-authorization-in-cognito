#!/bin/bash
python lambda/authorizer.test.py
sam package --s3-bucket ascending-devops --output-template-file out.yaml
sam deploy --template-file out.yaml --region us-east-1 --capabilities CAPABILITY_IAM --stack-name $1-authorizer --parameter-overrides Environment=$1