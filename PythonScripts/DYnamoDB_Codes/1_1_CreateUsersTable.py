import boto3
from botocore.exceptions import ClientError

REGION = "us-east-1"
TABLE_NAME = "UsersTable"

dynamodb = boto3.client("dynamodb", region_name=REGION)

try:
    response = dynamodb.create_table(
        TableName=TABLE_NAME,
        AttributeDefinitions=[
            {
                "AttributeName": "id",
                "AttributeType": "S"  # String
            }
        ],
        KeySchema=[
            {
                "AttributeName": "id",
                "KeyType": "HASH"  # Partition key
            }
        ],
        BillingMode="PAY_PER_REQUEST"
    )

    print("✅ Table creation initiated...")
    
    # Wait until table exists
    waiter = dynamodb.get_waiter("table_exists")
    waiter.wait(TableName=TABLE_NAME)

    print("✅ Table created successfully!")

except dynamodb.exceptions.ResourceInUseException:
    print("⚠ Table already exists")

except ClientError as e:
    print("❌ Error:", e)