import os  # Import os module to use path functions

try:
    # Check if the file exists at the specified location
    with open(r"C:\Users\janha\Desktop\google-key.json", 'r') as file:
        print("File opened successfully.")
        content = file.read()  # Read file to check for access
        print(content[:100])  # Print first 100 characters
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error: {e}")


