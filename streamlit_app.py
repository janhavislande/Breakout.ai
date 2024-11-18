import streamlit as st
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread 

st.title("AI Agent - Data upload and Google Sheets Integration")

uploaded_file = st.file_uploader("Choose a CSV file",type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

st.write("Or connect to Google Sheets") 
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('google-key2.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("1Oea9eOUu51HY__mJdkN0KGivwTLlKkd5gLnaARHYmHM").sheet1
data = sheet.get_all_records()
df = pd.DataFrame(data) 
st.write(df)
import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Setup Google Sheets API and authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('ai_agentproject.json', scope)
client = gspread.authorize(creds)

# File upload and Google Sheets integration
st.title("AI Agent Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

# Google Sheets data display
sheet_key = "YOUR_GOOGLE_SHEET_KEY"
sheet = client.open_by_key(sheet_key).sheet1
data = sheet.get_all_records()
st.write("Google Sheets Data:")
st.dataframe(pd.DataFrame(data))
