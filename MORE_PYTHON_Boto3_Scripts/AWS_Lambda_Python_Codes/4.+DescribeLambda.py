import boto3
from pprint import pprint

lambda_client = boto3.client('lambda')

response = lambda_client.get_function(
    FunctionName='helloWorldLambda'
)

pprint(response)

