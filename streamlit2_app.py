import streamlit as st
import pandas as pd
import requests

# Streamlit App Title
st.title("AI Agent Project")
st.write("Welcome to the Streamlit version of the AI Agent Project!")

# File Uploader Section
uploaded_file = st.file_uploader("Upload your file (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Display file content
    try:
        if uploaded_file.name.endswith(".csv"):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".xlsx"):
            data = pd.read_excel(uploaded_file)
        st.write("File uploaded successfully! Here's a preview:")
        st.dataframe(data.head())
    except Exception as e:
        st.error(f"Error reading file: {e}")

# Fetch Data Function
def fetch_data(query):
    try:
        url = f"https://api.example.com/data?query={query}&key={google_api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching data: {e}")
        return None

# Access Google API Key
try:
    google_api_key = st.secrets["general"]["GOOGLE_API_KEY"]
    st.success("Google API key loaded successfully!")
except KeyError as e:
    st.error(f"Error loading Google API key: {e}")
    st.write("Available secrets:", st.secrets)

