import boto3


ec2_client = boto3.client('ec2')
volume_id = 'vol-0c65ed03ca559a04b'

response = ec2_client.modify_volume(
    VolumeId=volume_id,
    Size=7
)

print(response)