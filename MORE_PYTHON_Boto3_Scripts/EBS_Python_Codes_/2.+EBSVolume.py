import boto3

'''
ec2_client = boto3.client('ec2')

new_volume = ec2_client.create_volume(
    AvailabilityZone = 'us-east-1d',
    Size = 5,
    VolumeType='gp2',
    TagSpecifications = [
        {
            'ResourceType':'volume',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Python & Boto3'
                }
            ]
        }
    ]
)

print("Created Volume ID : {} ".format(new_volume["VolumeId"]))

'''


ec2_client = boto3.resource('ec2')

new_volume = ec2_client.create_volume(
    AvailabilityZone = 'us-east-1d',
    Size = 5,
    VolumeType='gp2',
    TagSpecifications = [
        {
            'ResourceType':'volume',
            'Tags':[
                {
                    'Key':'Name',
                    'Value':'Python & Boto3 with resource'
                }
            ]
        }
    ]
)

print("Created Volume ID : {} ".format(new_volume.id))
