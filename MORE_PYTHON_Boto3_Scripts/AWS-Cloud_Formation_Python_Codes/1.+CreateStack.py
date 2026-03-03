import boto3


cf_client = boto3.client('cloudformation')
#cf_resource = boto3.resource('cloudformation')

with open('Dynamodb.yml', 'r') as f:
    dy_template = f.read()
    #print(dy_template)


params = [
    {
        'ParameterKey': 'HashKeyElementName',
        'ParameterValue':'EmployeeId'
    }

]

response = cf_client.create_stack(
    StackName='dynamostack',
    TemplateBody=dy_template,
    Parameters=params

)
print(response)