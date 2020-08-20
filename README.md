# securing-objects-in-serverless-application-object-based-authorization-in-cognito

## SAM Local Test
### Install environment using pipenv

```
pipenv install
pipenv shell
```

### Use sam to invoke function

Post Confirmation Trigger
`sam local invoke "AddUserToAcl" -e lambda/test/events/postConfirmationEvent.json`

Lambda Authorizer
`sam local invoke "LambdaAuthorizer" -e lambda/test/events/authorizerEvent.json`


### Check redis using redis-cli
`docker exec -it 64baa3d813e0 /bin/bash`
`redis-cli keys '*'`

### Check the values of specified key
`redis-cli MGET 'abcd-1234-0000'`
