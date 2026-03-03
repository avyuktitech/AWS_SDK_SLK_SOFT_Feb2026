import boto3

iam = boto3.client('iam')

role_name = 'MyNewEC2Role'

instance_profile_name = 'MyNewEC2Profile'

iam.add_role_to_instance_profile(
    InstanceProfileName=instance_profile_name,
    RoleName=role_name
)

print(f"IAM Role {role_name} added to IAM instance profile {instance_profile_name}")