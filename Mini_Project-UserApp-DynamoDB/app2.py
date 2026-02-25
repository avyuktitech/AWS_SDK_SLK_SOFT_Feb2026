import streamlit as st
import boto3
import uuid
from datetime import datetime
from botocore.exceptions import ClientError

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="HR Management App",
    page_icon="👩‍💼",
    layout="wide"
)

# -------- CUSTOM STYLING --------
st.markdown("""
<style>
.main {
    background-color: #f4f6f9;
}
.title-text {
    font-size:32px !important;
    font-weight:700;
    color:#1f4e79;
}
.section-header {
    font-size:22px !important;
    font-weight:600;
    color:#2e86c1;
    margin-top:20px;
}
.stButton>button {
    background-color:#1f77b4;
    color:white;
    border-radius:8px;
    height:3em;
    width:100%;
    font-weight:600;
}
.stButton>button:hover {
    background-color:#145a86;
    color:white;
}
.card {
    padding:20px;
    border-radius:10px;
    background-color:white;
    box-shadow:0px 2px 10px rgba(0,0,0,0.1);
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: white;
    color: #1f4e79;
    text-align: center;
    padding: 10px;
    font-weight: 600;
    border-top: 1px solid #e6e6e6;
}
</style>
""", unsafe_allow_html=True)

# -------- CONFIG --------
REGION = "us-east-1"
TABLE_NAME = "UserTable"

# -------- CONNECT TO DYNAMODB --------
try:
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    table = dynamodb.Table(TABLE_NAME)
except Exception as e:
    st.error(f"Error connecting to DynamoDB: {e}")
    st.stop()

# -------- SIDEBAR --------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
st.sidebar.title("HR Admin Panel")
menu = st.sidebar.radio("Navigation", ["Add Employee", "View Employees"])

# -------- HEADER --------
st.markdown('<p class="title-text">👩‍💼 HR Employee Management System</p>', unsafe_allow_html=True)
st.write("Manage employee records securely using AWS DynamoDB.")

# -------- ADD EMPLOYEE --------
if menu == "Add Employee":
    st.markdown('<p class="section-header">Add New Employee</p>', unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("Full Name")
            department = st.text_input("Department")

        with col2:
            email = st.text_input("Email Address")
            designation = st.text_input("Designation")

        if st.button("Save Employee"):
            if name and email:
                try:
                    employee_id = str(uuid.uuid4())

                    table.put_item(
                        Item={
                            "id": employee_id,
                            "name": name,
                            "email": email,
                            "department": department,
                            "designation": designation,
                            "created_at": datetime.utcnow().isoformat()
                        }
                    )

                    st.success("✅ Employee successfully added!")

                except ClientError as e:
                    st.error(f"Error saving employee: {e}")
            else:
                st.warning("⚠ Name and Email are required fields.")

        st.markdown('</div>', unsafe_allow_html=True)

# -------- VIEW EMPLOYEES --------
if menu == "View Employees":
    st.markdown('<p class="section-header">Employee Directory</p>', unsafe_allow_html=True)

    try:
        response = table.scan()
        items = response.get("Items", [])

        if items:
            st.metric("Total Employees", len(items))
            st.dataframe(items, use_container_width=True)
        else:
            st.info("No employees found.")

    except ClientError as e:
        st.error(f"Error fetching employees: {e}")

# -------- FOOTER --------
st.markdown("""
    <div class="footer">
        Made by SLK Dev Team with Intelligence 🚀
    </div>
""", unsafe_allow_html=True)