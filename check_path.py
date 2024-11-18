import os

# Correct relative path
relative_path = os.path.join("static", "google-key.json")

# Correct absolute path
absolute_path = r"C:\Users\janha\OneDrive\Desktop\AI Agent Project\static\google-key.json"

print(f"Current working directory: {os.getcwd()}")
print(f"File exists in relative path: {os.path.exists(relative_path)}")
print(f"File exists at absolute path: {os.path.exists(absolute_path)}")







