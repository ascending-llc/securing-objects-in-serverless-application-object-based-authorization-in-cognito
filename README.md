# securing-objects-in-serverless-application-object-based-authorization-in-cognito

## SAM Local Test
### Install environment using pipenv

```
pipenv install
pipenv shell
```

### Use sam to invoke function

#### Post Confirmation Trigger

Insert an item in dynamodb permission table to describe user’s permission as simple as following: sample upon user registration on Cognito.

`sam local invoke "AddUserToAcl" -e lambda/test/events/postConfirmationEvent.json`

#### Lambda Authorizer

Since we have built ACL for user’s permission on each object. It’s time to
generate an authorization policy(auth policy) document for the lambda
authorizer to evaluate if it should allow or deny the user API request.

`sam local invoke "LambdaAuthorizer" -e lambda/test/events/authorizerEvent.json`

#### Update Acl

When paystubs table has been changed, the DynamoDB Streams will invoke UpdateAcl function and the auth-table will be updated.

`sam local invoke "UpdateAcl" -e lambda/test/events/ddbStream.json`

### Check Redis server using redis-cli
```
docker exec -it 64baa3d813e0 /bin/bash

redis-cli keys '*'
```

### Check the values of specified key in the Redis server
`redis-cli MGET 'abcd-1234-0000'`

### Authorizer Unit Test
`python lambda/test/authorizer.py`
