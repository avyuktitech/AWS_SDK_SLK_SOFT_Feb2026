import boto3
import json
from datetime import datetime

# Create an IAM client
iam = boto3.client('iam')

# Get the current date in ISO 8601 format without the time (e.g., "2023-10-03")
current_date = datetime.utcnow().strftime('%Y-%m-%d')

# Define the start and end times for the access window in ISO 8601 format
start_time = f"{current_date}T01:00:00Z"
end_time = f"{current_date}T03:00:00Z"

policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::parwiz-forogh-12/*",
            "Condition": {
                "DateGreaterThan": {"aws:CurrentTime": start_time},
                "DateLessThan": {"aws:CurrentTime": end_time}
            }
        }
    ]
}

response = iam.create_policy(
    PolicyName='AccessWindowPolicyNew',
    PolicyDocument = json.dumps(policy_document)
)

print("IAM Conditional Policy is created")