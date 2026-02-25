import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    method = event.get("httpMethod")
    
    try:
        if method == "POST":
            # Create user
            body = json.loads(event.get("body", "{}"))
            user_id = body.get("id", "001") # Default ID if not provided
            item = {
                "id": user_id,
                "name": body.get("name", "Guest"),
                "email": body.get("email", "no-email@example.com")
            }
            table.put_item(Item=item)
            return response(201, {"message": "User Created", "user": item})

        elif method == "GET":
            # Get user from query string: ?id=001
            query_params = event.get("queryStringParameters") or {}
            user_id = query_params.get("id")
            
            if not user_id:
                return response(400, {"message": "Missing id parameter"})
                
            result = table.get_item(Key={"id": user_id})
            if "Item" not in result:
                return response(404, {"message": "User not found"})
            return response(200, result["Item"])

    except Exception as e:
        return response(500, {"error": str(e)})

def response(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"},
        "body": json.dumps(body)
    }
