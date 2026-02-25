# This is Mini Project - for User App using DynamoDB.
#1. Libraries 
from datetime import datetime
import streamlit as st
import boto3
import uuid #UUID library to generate unique user IDs
from botocore.exceptions import ClientError

#2. ------AWS Configuration--------------
REGION = 'us-east-1'
TABLE_NAME = 'UserTable'
#-------------------------------------

#3. Initilize DynamoDB resource
try: 
    dynamodb = boto3.resource('dynamodb', region_name=REGION)
    table = dynamodb.Table(TABLE_NAME)

except Exception as e:
    st.error(f"Error initializing/Connecting to  DynamoDB: {e}")
    st.stop()

#4. --------- UI ------------------
st.title("User Management App with DynamoDB")
st.subheader("Add New User")
name = st.text_input("Name")
email = st.text_input("Email")

if st.button("Submitt User"):
    if name and email:
        try:
            user_id = str(uuid.uuid4()) # Generate a unique user ID using UUID
            table.put_item(Item={
                "id": user_id,  # Use 'ID' as the primary key in DynamoDB
                "name": name,   # Use 'Name' as the attribute for the user's name
                "email": email, # Use 'Email' as the attribute for the user's email
                "created_at": datetime.utcnow().isoformat() # Use 'CreatedAt' as the attribute for the timestamp of user creation
            })
            st.success(f"User {name} added successfully with ID: {user_id}")    
        except ClientError as e:
            st.error(f"Error adding user: {e.response['Error']['Message']}")    
    else:
        st.warning("Please enter both name and email to add a user/Fill all details.")

st.divider()    #UI Divider

st.subheader("View ALL Users")
if st.button("Load/Fetch Users"):
    try:
        response = table.scan() # Scan the DynamoDB table to get all items
        items = response.get('Items', [])

        if items:
            st.dataframe(items) # Display the items in a table format using Streamlit
        else:
            st.info("No users found in the database.")
    except ClientError as e:
        st.error(f"Error fetching users: {e.response['Error']['Message']}")

