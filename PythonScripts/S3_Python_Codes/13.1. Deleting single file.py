
# Deleting simgle File from Bucket

import boto3

# Create an S3 resource
s3 = boto3.resource('s3')

# Specify the bucket name and object key
bucket_name = 'ajaytraining23145999'
object_key = 'file.txt'

# Get the bucket object
bucket = s3.Bucket(bucket_name)

# Delete the object
response = bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': object_key
            },
        ]
    }
)

print(response)
