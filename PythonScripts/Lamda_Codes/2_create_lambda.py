import boto3
import json
import time

# 🔹 Specify region
session = boto3.Session(region_name="us-east-1")

iam = session.client("iam")
lambda_client = session.client("lambda")

role_name = "lambda-basic-role"
function_name = "MyBoto3Lambda"
zip_file_name = "1_lambda_function.zip"

# 1️⃣ Create IAM Role (if not exists)
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
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
        RoleName=role_name,
        PolicyArn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
    )

    print("✅ IAM role created")
    time.sleep(10)

except iam.exceptions.EntityAlreadyExistsException:
    role = iam.get_role(RoleName=role_name)
    print("⚠️ IAM role already exists")

role_arn = role["Role"]["Arn"]

# 2️⃣ Read ZIP file
with open(zip_file_name, "rb") as f:
    zipped_code = f.read()

# 3️⃣ Create OR Update Lambda
try:
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime="python3.12",
        Role=role_arn,
        Handler="lambda_function.lambda_handler",
        Code={"ZipFile": zipped_code},
        Timeout=10,
        MemorySize=128,
        Publish=True
    )

    print("✅ Lambda created successfully!")
    print("Function ARN:", response["FunctionArn"])

except lambda_client.exceptions.ResourceConflictException:
    print("⚠️ Lambda already exists — updating code...")

    response = lambda_client.update_function_code(
        FunctionName=function_name,
        ZipFile=zipped_code,
        Publish=True
    )

    print("✅ Lambda code updated successfully!")

# 4️⃣ Wait until Lambda is Active
print("⏳ Waiting for Lambda to become Active...")

waiter = lambda_client.get_waiter("function_active_v2")
waiter.wait(FunctionName=function_name)

print("✅ Lambda is now Active!")

# 5️⃣ Invoke Lambda
response = lambda_client.invoke(
    FunctionName=function_name,
    InvocationType="RequestResponse"
)

print("✅ Lambda invocation response:")
print(response["Payload"].read().decode())