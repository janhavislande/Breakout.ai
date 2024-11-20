import os
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
import gspread
import pandas as pd
import streamlit as st
st.title("Welcome to the AI Agent Project")

# Load environment variables from the .env file
load_dotenv()

# Access the API key from the environment variable (which should point to google-key3.json)
key_file_path = os.getenv("GOOGLE_API_KEY")

if key_file_path is None:
    st.error("GOOGLE_API_KEY not found in the environment variables!")
else:
    # Define the required scopes for Google Sheets and Drive API
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

    # Authenticate using the service account key file (google-key3.json)
    creds = Credentials.from_service_account_file(key_file_path, scopes=scope)
    gc = gspread.authorize(creds)

    # Streamlit app layout
    st.title('AI Agent: Data Upload')

    # File uploader to upload a CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # If a file is uploaded, display its contents
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write(df)

    # Google Sheets connection logic
    if st.button('Connect to Google Sheet'):
        try:
            # Open the sheet by name or by key (replace 'My_AI_Sheet' with the actual sheet name)
            sheet = gc.open('My_AI_Sheet').sheet1
            data = sheet.get_all_records()  # Fetch all records from the sheet
            df = pd.DataFrame(data)
            st.write(df)  # Display the sheet data
        except Exception as e:
            st.error(f"Error accessing Google Sheets: {e}")


