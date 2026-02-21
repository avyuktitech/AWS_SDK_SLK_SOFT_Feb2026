import boto3

def stop_instance(instance_id):
    ec2_client = boto3.client('ec2')
    response = ec2_client.stop_instances(InstanceIds=[instance_id])

    print(response)

stop_instance('i-03a7cb74c1359c822')