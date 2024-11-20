import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variables
API_KEY = os.getenv("API_KEY")

# Function to read customers data from CSV file
def read_customers_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("Error: The 'customers.csv' file was not found.")
        return None

# Function to process data
def process_data(data):
    # Extract necessary columns from the data
    columns_needed = ["Customer Id", "Email", "Phone Number", "Company"]
    customers_data = data[columns_needed].to_dict(orient="records")
    return customers_data



