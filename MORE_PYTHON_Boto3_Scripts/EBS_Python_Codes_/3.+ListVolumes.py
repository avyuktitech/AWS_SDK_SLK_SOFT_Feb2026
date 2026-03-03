import boto3


ec2_resource = boto3.resource('ec2')

for volume in ec2_resource.volumes.all():
    print(volume)