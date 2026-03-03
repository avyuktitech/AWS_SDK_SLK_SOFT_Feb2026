import json
import boto3  # python sdk and it is available in here you don't need t install

s3 = boto3.resource('s3')


def lambda_handler(event, context):

    s3_buckets = []


    for bucket in s3.buckets.all():
        s3_buckets.append(bucket.name)


    return {
        "statusCode": 200,
        "body": s3_buckets
    }

