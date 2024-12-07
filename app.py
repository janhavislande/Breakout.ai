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
        # Construct the URL for the Google Places API request
        url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={query}&key={google_api_key}"
        
        # Make the API request
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()  # Parse and return the JSON response
        elif response.status_code == 403:
            st.error("Access denied: Invalid API key or insufficient permissions.")
        elif response.status_code == 429:
            st.error("Rate limit exceeded. Please try again later.")
        else:
            st.error(f"Unexpected error: {response.status_code}")
            st.write(response.text)
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        return None
