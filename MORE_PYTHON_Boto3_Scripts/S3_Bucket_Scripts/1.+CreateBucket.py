import boto3


client = boto3.client('s3')

response = client.create_bucket(
    Bucket = "training23145999",
    ACL = "private",

)

print(response)