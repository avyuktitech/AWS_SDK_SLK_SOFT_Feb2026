import boto3


ec2_resource = boto3.resource('ec2')
volume_id = 'vol-0d1a530e0b9563aca'

snapshot = ec2_resource.create_snapshot(
    VolumeId=volume_id,
    TagSpecifications = [
        {
            'ResourceType':'snapshot',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Python Snapshot'
                }
            ]
        }
    ]
)

print('Snapshot is created')