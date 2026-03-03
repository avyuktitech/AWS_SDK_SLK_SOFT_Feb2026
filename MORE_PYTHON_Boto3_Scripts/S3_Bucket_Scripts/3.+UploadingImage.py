import boto3

client = boto3.client('s3')

with open('aws.png', 'rb') as f:
    data = f.read()

response = client.put_object(
    Bucket="ajaytraining23145999",
    Body=data,
    Key='aws.png'
)

print("Upload successful")
print(response)
