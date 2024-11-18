import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up the scope and credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/janha/OneDrive/Desktop/AI Agent Project/static/google-key.json", scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1Oea9eOUu51HY__mJdkN0KGivwTLlKkd5gLnaARHYmHM").sheet1  # Replace with your actual sheet name

# Try reading the first row from the sheet
data = sheet.get_all_records()
print(data)
import pandas as pd
data = [{'Names ': 'Janhavi ', 'Age': 21, 'Birthday': '9.10.2003'},
        {'Names ': 'Sujay', 'Age': 11, 'Birthday': '2.7.13'}]

df = pd.DataFrame(data)
print(df)
import streamlit as st
import pandas as pd
from google.oauth2.service_account import Credentials
import gspread

# Google Sheets authentication
def authenticate_google_sheets():
    creds = Credentials.from_service_account_file('path/to/google-key.json')
    gc = gspread.authorize(creds)
    return gc

# Dashboard layout
st.title('AI Agent: Data Upload')
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Google Sheets connection
if st.button('Connect to Google Sheet'):
    gc = authenticate_google_sheets()
    sheet = gc.open('My_AI_Sheet').sheet1
    data = sheet.get_all_records()
    df = pd.DataFrame(data)
    st.write(df)

