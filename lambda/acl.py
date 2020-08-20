import json
import boto3
import os

def addUserToAcl(event, content):
    uuid = event["request"]["userAttributes"]["sub"]
    table = boto3.resource('dynamodb').Table('test-auth-policy')
    response = table.put_item(
        Item={
            'uuid': uuid,
            'employee': {
                'allow': {
                    '/employee': '*',
                    '/employee/' + uuid: '*'
                }
            },
            'paystubs': {
                'allow': {
                    '/paystubs': '*'
                }
            }
        }
    )
    return event

def updateAcl(event, content):
    # Read dynamoDB stream from paystub table
    for record in event['Records']:
        principalId = record['dynamodb']['Keys']['uuid']['S']
        
        # If paystub record is deleted, we delete it from acl table
        if record['eventName'] == 'REMOVE':
            response = table.update_item(
                # Remove paystub from acl table
                Key={
                    'uuid': principalId
                },
                UpdateExpression="set paystub.allow=:a",
                ExpressionAttributeValues={
                    # ':a': new paystub lists
                },
        )
            
        # Update paystub to the acl table
        else:
            client = boto3.client('dynamodb')
            response = record['dynamodb']['NewImage']
            table = boto3.resource('dynamodb').Table(os.environ.get('AUTH_TABLE'))
            response = table.update_item(
                # Update acl table
                Key={
                    'uuid': principalId
                },
                UpdateExpression="set paystub.allow=:a",
                ExpressionAttributeValues={
                    # ':a': new paystub lists
                },
            )
    return event
