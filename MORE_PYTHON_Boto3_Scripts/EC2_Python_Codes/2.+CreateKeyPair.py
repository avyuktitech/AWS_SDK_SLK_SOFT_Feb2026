import boto3

# Initialize Secrets Manager client
# Creates a new client object for interacting with AWS Secrets Manager
client = boto3.client('secretsmanager')

# Retrieve the secret value
try:
    # Calls the get_secret_value API operation to retrieve the secret value
    # Replace 'your-secret-id' with the actual ARN or name of your secret
    resp = client.get_secret_value(SecretId='your-secret-id')
except Exception as e:
    # Handles any exceptions that may occur during the API call
    print(f"Error retrieving secret: {e}")
    exit(1)

# Save the KeyMaterial to a local file
try:
    # Opens 'mykey.pem' file in write mode
    # The 'with' statement ensures the file is properly closed after writing
    with open('mykey.pem', 'w') as file:
        # Writes the SecretString (which contains the KeyMaterial) to the file
        file.write(resp['SecretString'])
    # Prints a success message
    print("Key material saved to 'mykey.pem'")
except Exception as e:
    # Handles any exceptions that may occur during file writing
    print(f"Error saving key material: {e}")
