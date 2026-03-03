import boto3

# Initialize the RDS client
client = boto3.client('rds')

try:
    # Create a MariaDB DB instance
    response = client.create_db_instance(
        DBInstanceIdentifier='my-mariadb-instance',
        DBInstanceClass='db.t3.micro',
        Engine='mariadb',
        MasterUsername='Username123',
        MasterUserPassword='Password123',
        AllocatedStorage=20,
        DBName='mydatabase',
        VpcSecurityGroupIds=['sg-0dbbcc33e41978712'],  # Replace with the correct security group ID in the same VPC
        MultiAZ=False,
        PubliclyAccessible=True,
        Tags=[
            {
                'Key': 'Name',
                'Value': 'MyMariaDBInstance'
            }
        ]
    )

    print(f"MariaDB instance {response['DBInstance']['DBInstanceIdentifier']} is being created.")

except Exception as e:
    print(f"Error creating MariaDB instance: {e}")
