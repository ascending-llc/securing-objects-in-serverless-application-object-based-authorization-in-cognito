import json
import boto3
import os

def lambda_handler(event, content):
    uuid = event["request"]["userAttributes"]["sub"]
    table = boto3.resource('dynamodb').Table(os.environ.get('AUTH_TABLE'))
    response = table.put_item(
        Item={
            'uuid': uuid,
            'employee': {
                'allow': [
                    '/5': '*',
                    '/5/*': '*'
                ]
            },
            'paystubs': {
                'allow': [
                    '1': '*',
                    '2': '*'
                ]
            }
        }
    )
    return event

def putAcl(uuid, rule):
    table = boto3.resource('dynamodb').Table(os.environ.get('AUTH_TABLE'))
    response = table.put_item(
        Item={
            'uuid': uuid,
            'employee': {
                'allow': [
                    '/5': '*',
                    '/5/*': '*'
                ]
            },
            'paystubs': {
                'allow': [
                    '1': '*',
                    '2': '*'
                ]
            }
        }
    )
