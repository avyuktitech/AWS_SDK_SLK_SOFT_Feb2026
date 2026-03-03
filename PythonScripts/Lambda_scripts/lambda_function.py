# This scrpt is for lambda function to trigger the step function for the data pipeline

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello from Slk-Lambda!'
    }