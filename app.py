import streamlit as st
import pandas as pd
import requests

# Set up the app title and introductory description
st.title("AI Agent Project")
st.write("Welcome to the Streamlit version of the AI Agent Project!")

# Attempt to load the Google API key from secrets.toml
try:
    google_api_key = st.secrets["general"]["google_api_key"]
    st.success("Google API key loaded successfully!")
    other_setting = "your_other_value"
except KeyError as e:
    st.error(f"Error loading Google API key: {e}")
    st.write("Please make sure you have added the 'general' section to your secrets.toml file.")
    st.write("For more information on secrets management, see: [Secrets Management](https://docs.streamlit.io/develop/concepts/connections/secrets-management)")

# File upload functionality for CSV and Excel files
uploaded_file = st.file_uploader("Upload your file (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    try:
        # Check the file type and load it accordingly
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)
        
        # Display the first few rows of the uploaded file
        st.write("File uploaded successfully! Here's a preview:")
        st.dataframe(data.head())
    except Exception as e:
        st.error(f"Error reading the file: {e}")

# Fetch data function (example)
def fetch_data(query):
    try:
        url = f"https://api.example.com/data?query={query}&key={google_api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()  # Indented block here
        else:
            st.error(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        return None

# Example for using fetch_data (you can modify or remove this part)
if st.button("Test Fetch Data"):
    query = st.text_input("Enter a search query", "example query")
    if query:
        result = fetch_data(query)
        if result:
            st.write("Fetched data:", result)
