#Download file.txt  as downloaded.pdf
import boto3
BUCKET_NAME = "ajaytraining23145999"
s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(BUCKET_NAME, 'file.txt')
s3_object.download_file('downloaded.pdf')
print("File has been downloaded")



