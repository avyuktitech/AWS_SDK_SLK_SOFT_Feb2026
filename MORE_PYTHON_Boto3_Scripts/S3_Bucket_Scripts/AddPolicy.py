import boto3
import json

bucket_name = "training231001"

bucket_policy = {
	"Version": "2012-10-17",
	"Id": "Policy1670146696267",
	"Statement": [
		{
			"Sid": "Stmt1670146603372",
			"Effect": "Deny",
			"Principal": "*",
			"Action": "s3:PutObject",
			"Resource": f'arn:aws:s3:::{bucket_name}/*',
			"Condition": {
				"StringNotEquals": {
					"s3:x-amz-server-side-encryption": "AES256"
				}
			}
		},
		{
			"Sid": "Stmt1670146692796",
			"Effect": "Deny",
			"Principal": "*",
			"Action": "s3:PutObject",
			"Resource": f'arn:aws:s3:::{bucket_name}/*',
			"Condition": {
				"Null": {
					"s3:x-amz-server-side-encryption": "true"
				}
			}
		}
	]
}

bucket_policy = json.dumps(bucket_policy)

s3_cleint = boto3.client('s3')
response = s3_cleint.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
print(response)