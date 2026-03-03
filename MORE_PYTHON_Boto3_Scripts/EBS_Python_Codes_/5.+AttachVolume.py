import boto3


ec2_resource = boto3.resource('ec2')

volume = ec2_resource.Volume('vol-0c65ed03ca559a04b')
print(f'Volume {volume.id} status -> {volume.state}')

volume.attach_to_instance(
    Device = '/dev/sdh',
    InstanceId='i-0e528c6f4a93c041d'
)

print(f'Volume {volume.id} Status -> {volume.state}')