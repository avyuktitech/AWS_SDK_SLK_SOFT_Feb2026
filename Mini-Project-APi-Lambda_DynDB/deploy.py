import boto3, json, zipfile, time, botocore

REGION = "us-east-1"
TABLE_NAME = "SimpleUsersTable"
FUNCTION_NAME = "SimpleLambda"
ROLE_NAME = "SimpleLambdaRole"
API_NAME = "SimpleAPI"

# Clients
iam = boto3.client('iam')
db = boto3.client('dynamodb', region_name=REGION)
lmb = boto3.client('lambda', region_name=REGION)
agw = boto3.client('apigateway', region_name=REGION)

def setup():
    # 1. DynamoDB
    try:
        db.create_table(
            TableName=TABLE_NAME,
            AttributeDefinitions=[{'AttributeName': 'id', 'AttributeType': 'S'}],
            KeySchema=[{'AttributeName': 'id', 'KeyType': 'HASH'}],
            BillingMode='PAY_PER_REQUEST'
        )
        print("Creating Table...")
        db.get_waiter('table_exists').wait(TableName=TABLE_NAME)
    except: print("Table exists.")

    # 2. IAM Role
    role_arn = ""
    try:
        policy = {
            "Version": "2012-10-17",
            "Statement": [{"Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]
        }
        res = iam.create_role(RoleName=ROLE_NAME, AssumeRolePolicyDocument=json.dumps(policy))
        role_arn = res['Role']['Arn']
        iam.attach_role_policy(RoleName=ROLE_NAME, PolicyArn="arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess")
        iam.attach_role_policy(RoleName=ROLE_NAME, PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole")
        print("Waiting 15s for IAM...")
        time.sleep(15) 
    except:
        role_arn = iam.get_role(RoleName=ROLE_NAME)['Role']['Arn']

    # 3. Zip and Create Lambda
    with zipfile.ZipFile("lambda.zip", "w") as z:
        z.write("lambda_function.py")
    
    with open("lambda.zip", "rb") as f:
        code = f.read()
    
    try:
        lmb.create_function(
            FunctionName=FUNCTION_NAME, Runtime='python3.9', Role=role_arn,
            Handler='lambda_function.lambda_handler', Code={'ZipFile': code},
            Environment={'Variables': {'TABLE_NAME': TABLE_NAME}}
        )
        print("Lambda Created.")
    except:
        lmb.update_function_code(FunctionName=FUNCTION_NAME, ZipFile=code)
        print("Lambda Updated.")

    # 4. API Gateway
    api = agw.create_rest_api(name=API_NAME)
    api_id = api['id']
    root_id = agw.get_resources(restApiId=api_id)['items'][0]['id']
    
    resource = agw.create_resource(restApiId=api_id, parentId=root_id, pathPart='users')
    res_id = resource['id']

    account_id = boto3.client('sts').get_caller_identity()['Account']
    uri = f"arn:aws:apigateway:{REGION}:lambda:path/2015-03-31/functions/arn:aws:lambda:{REGION}:{account_id}:function:{FUNCTION_NAME}/invocations"

    for method in ['GET', 'POST']:
        agw.put_method(restApiId=api_id, resourceId=res_id, httpMethod=method, authorizationType='NONE')
        agw.put_integration(restApiId=api_id, resourceId=res_id, httpMethod=method, type='AWS_PROXY', integrationHttpMethod='POST', uri=uri)

    # Permission
    try:
        lmb.add_permission(FunctionName=FUNCTION_NAME, StatementId='apiperm', Action='lambda:InvokeFunction', Principal='apigateway.amazonaws.com')
    except: pass

    agw.create_deployment(restApiId=api_id, stageName='prod')
    print(f"\n URL: https://{api_id}.execute-api.{REGION}.amazonaws.com/prod/users")

if __name__ == "__main__":
    setup()