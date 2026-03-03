import boto3

ec2_resource = boto3.resource('ec2')

volume = ec2_resource.Volume('vol-04a7e5595205649d8')

if volume.state == "available":
    volume.delete()
    print("Volume Deleted")
else:
    print("Can not delete volume attached")