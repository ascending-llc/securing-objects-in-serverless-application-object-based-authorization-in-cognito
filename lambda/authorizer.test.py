from authorizer import HttpVerb,AuthPolicy
import unittest

class TestStringMethods(unittest.TestCase):

    def test_auth(self):
    	policy = AuthPolicy('12345678', '12345678')

    	policy.restApiId = "asdfgh"
    	region = "us-east-1"
    	stage = "test"

    	policy.allowMethod('GET', '/user')
    	policy.allowMethod('POST', '/user')
    	policy.denyMethod('POST', '/admin')
    	authResponse = policy.build()
    	# print(authResponse['policyDocument']['Statement'])
    	self.assertEqual(len(authResponse['policyDocument']['Statement']), 2)
    	self.assertEqual(len(authResponse['policyDocument']['Statement'][0]['Resource']), 2)
    	self.assertEqual(authResponse['policyDocument']['Statement'][1]['Resource'][0], 'arn:aws:execute-api:*:12345678:asdfgh/*/POST/admin')

if __name__ == '__main__':
    unittest.main()
