# securing-objects-in-serverless-application-object-based-authorization-in-cognito

## SAM Local Test
### Install environment using pipenv

```
pipenv install
pipenv shell
```

### Use sam to invoke function

`sam local invoke LambdaAuthorizer`

### Check redis using redis-cli
`docker exec -it 64baa3d813e0 /bin/bash`
`redis-cli keys '*'`

### Check the values of specified key
`redis-cli MGET 'abcd-1234'`
