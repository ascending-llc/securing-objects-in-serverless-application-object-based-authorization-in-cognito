# securing-objects-in-serverless-application-object-based-authorization-in-cognito

## Requirements
- [Python 3.7](https://www.python.org/downloads/)
- The Bash shell. For Linux and macOS, this is included by default. In Windows 10, you can install the [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to get a Windows-integrated version of Ubuntu and Bash.
- [The AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) v1.17 or newer.

## Setup
Download or clone this repository.

    $ git clone https://github.com/ascending-llc/securing-objects-in-serverless-application-object-based-authorization-in-cognito.git
    $ cd securing-objects-in-serverless-application-object-based-authorization-in-cognito

To build a Lambda layer that contains the function's runtime dependencies, run `build-layer.sh`. Packaging dependencies in a layer reduces the size of the deployment package that you upload when you modify your code.

```
securing-objects-in-serverless-application-object-based-authorization-in-cognito$ ./build-layer.sh
```

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

`python lambda/authorizer.test.py`

#### Update Acl

When paystubs table has been changed, the DynamoDB Streams will invoke UpdateAcl function and the auth-table will be updated.

`sam local invoke "UpdateAcl" -e lambda/test/events/ddbStream.json`

### Check Redis server using redis-cli

Suppose you are running a redis server in a container

```
docker exec -it 64baa3d813e0 /bin/bash

redis-cli keys '*'
```

### Check the values of specified key in the Redis server
`redis-cli MGET 'abcd-1234-0000'`

### Authorizer Unit Test
`python lambda/test/authorizer.py`
