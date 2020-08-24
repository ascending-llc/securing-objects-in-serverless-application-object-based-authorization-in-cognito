import json
import boto3
import os

def addUserToAcl(event, content):
    # Invoked by Cognito post confirmation trigger
    uuid = event["request"]["userAttributes"]["sub"]
    table = boto3.resource('dynamodb').Table('test-auth-policy')
    response = table.put_item(
        Item={
            'uuid': uuid,
            'employee': {
                'allow': {
                    '/employee': 'GET',
                    '/employee/' + uuid: 'GET'
                }
            },
            'paystubs': {
                'allow': {
                    '/paystubs/1': 'GET'
                }
            }
        }
    )
    return event

def updateAcl(event, content):
    # Read dynamoDB stream from paystub table
    table = boto3.resource('dynamodb').Table('test-auth-policy')
    for record in event['Records']:
        principalId = record['dynamodb']['Keys']['uuid']['S']
        paystubId = record['dynamodb']['NewImage']['paystub']['M']["S"]
        paystubPolicy = {
            '/employee': 'GET'
        }
        
        # If paystub record is deleted, we delete it from acl table
        if record['eventName'] == 'REMOVE':
            response = table.update_item(
                # Remove paystub from acl table
                Key={
                    'uuid': principalId
                },
                UpdateExpression="set paystub.allow=:a",
                ExpressionAttributeValues={
                    ':a': paystubPolicy
                },
        )
            
        # Update paystub to the acl table
        else:
            client = boto3.client('dynamodb')
            response = record['dynamodb']['NewImage']
           
            response = table.update_item(
                # Update acl table
                Key={
                    'uuid': principalId
                },
                UpdateExpression="set paystub=:a",
                ExpressionAttributeValues={
                    ':a': paystubPolicy
                },
                ReturnValues="UPDATED_NEW"
            )
            print(response)
            
    return event
