import os

api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    print(f"GOOGLE_API_KEY: {api_key}")
else:
    print("GOOGLE_API_KEY is not set.")










