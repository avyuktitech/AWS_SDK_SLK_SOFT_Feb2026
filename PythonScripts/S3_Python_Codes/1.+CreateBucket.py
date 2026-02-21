import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket = "ajayslktraining2222",
    ACL = "private",

)

print(response)