import boto3

ec2_resource = boto3.resource('ec2')

for volume in ec2_resource.volumes.filter(
    Filters = [
        {
            'Name':'tag:Name',
            'Values': [
                'Python & Boto3',
            ]
        }
    ]
):
    print(f'Volume {volume.id} ({volume.size} Gib) -> {volume.state}')
