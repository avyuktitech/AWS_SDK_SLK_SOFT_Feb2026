#This script is for creating a lambda function using boto3
import boto3
import json
import time 

#Specify the region and the name of the lambda function
session = boto3.Session(region_name='us-east-1')
iam = session.client('iam')
lambda_client = session.client('lambda')

role_name = 'lambda-basic-role'
function_name = 'MyBoto3Lambda'
zip_file_name = '1_lambda_function.zip'

#1.Create a IAM ROle (if not exists)
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
try: 
    role = iam.create_role( 
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(assume_role_policy)
    )
    iam.attach_role_policy(
        RoleName = role_name,
        PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
    )
    print("IAM role Created")
    time.sleep(10) # Wait for the role to be fully propagated

except iam.exceptions.EntityAlreadyExistsException:
    print("IAM role already exists")
    role = iam.get_role(RoleName=role_name)

role_arn = role["Role"]["Arn"]

#2. Read from the ZIP file:
with open(zip_file_name, 'rb') as f:
    zip_code =f.read()

#3. Create or update the Lambda function
try:
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime='python3.12',
        Role=role_arn,
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': zip_code},
        Timeout=10,
        MemorySize=128
    )
    print("Lambda function created successfully.")
    print("Function ARN:", response['FunctionArn'])

except lambda_client.exceptions.ResourceConflictException:
    print("Lambda function already exists.--Updating the existing function code.")

    response = lambda_client.update_function_code(
        FunctionName=function_name,
        ZipFile=zip_code,
        Publish=True
    )
    print("Lambda function code updated successfully.")

#4. Wait until the Lambda function is active
print("Waiting for the Lambda function to become active...")
waiter = lambda_client.get_waiter('function_active_v2')
waiter.wait(FunctionName=function_name)
print("Lambda function is now active and ready to use.")

#5. Invoke the Lambda function
resonse = lambda_client.invoke(
    FunctionName=function_name, 
    InvocationType='RequestResponse'
)
print("Lambda invocation response:")
print(resonse["Payload"].read().decode())   
