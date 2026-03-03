import boto3

db = boto3.client('dynamodb')


'''
response = db.create_backup(
    TableName='employee',
    BackupName='ArticleBackUp'
)

print(response)

'''


response = db.delete_backup(
    BackupArn='arn:aws:dynamodb:us-east-1:651366224884:table/employee/backup/01644585631214-8e886bd4'

)

print(response)