import boto3
# Initialize the EC2 resource
ec2_resource = boto3.resource('ec2')
# Specify the subnet ID
subnet_id = 'subnet-01795c8fe2f5f1f50'  # Replace with your subnet ID
# Create a new EC2 instance
response = ec2_resource.create_instances(
    ImageId='ami-0e349888043265b96',  # AMI ID for the Amazon Linux 2 AMI (HVM), SSD Volume Type
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Instance type: t2.micro (Free Tier eligible)
    KeyName='ajayslkkey111',  # Replace with your key pair name
    SubnetId=subnet_id  # Specify the subnet ID
)
# Print the response
print(response)
