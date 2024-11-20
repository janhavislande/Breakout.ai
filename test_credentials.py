from google.auth import default

credentials, project = default()
print("Credentials loaded successfully.")
print(f"Project ID: {project}")
