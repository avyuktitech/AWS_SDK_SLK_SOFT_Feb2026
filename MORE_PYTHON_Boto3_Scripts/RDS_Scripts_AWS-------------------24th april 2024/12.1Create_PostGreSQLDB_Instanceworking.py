import boto3
from pprint import pprint

# Initialize the RDS client
rds_client = boto3.client('rds')

try:
    # Create PostgreSQL instance
    response = rds_client.create_db_instance(
        DBName='mydatabase111',  # Replace with your desired database name
        DBInstanceIdentifier='mydbinstance111',  # Replace with your desired instance identifier
        AllocatedStorage=20,  # Storage size in GB
        DBInstanceClass='db.t3.micro',  # Instance type
        Engine='postgres',  # PostgreSQL engine
        MasterUsername='Username123',  # Replace with your desired master username
        MasterUserPassword='Password123',  # Replace with your desired master password
        Port=5432,  # PostgreSQL default port
        EngineVersion='16.1',  # PostgreSQL version
        PubliclyAccessible=True,  # Set to True if you want the instance to be publicly accessible
        StorageType='gp2',  # General Purpose SSD storage type
        DBSubnetGroupName='shashikanthsubnetsgroup1231'  # Replace with the name of your custom subnet group in the desired VPC
    )

    # Print the response
    pprint(response)

except Exception as e:
    print(f"Error creating RDS instance: {e}")
