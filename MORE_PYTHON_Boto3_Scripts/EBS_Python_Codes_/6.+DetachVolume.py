import boto3

ec2_resource = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

volume = ec2_resource.Volume('vol-0c65ed03ca559a04b')

volume.detach_from_instance(
    Device = '/dev/sdh',
    InstanceId='i-0e528c6f4a93c041d'
)

waiter = ec2_client.get_waiter('volume_available')
waiter.wait(
    VolumeIds=[
        volume.id
    ]
)

print(f'Volume {volume.id} Status -> {volume.state}')