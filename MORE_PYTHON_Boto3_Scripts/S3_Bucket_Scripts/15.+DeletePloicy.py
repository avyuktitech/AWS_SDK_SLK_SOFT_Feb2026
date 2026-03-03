import boto3

client = boto3.client('s3')

response = client.delete_bucket_policy(
    Bucket="training231001"
)

print(response)