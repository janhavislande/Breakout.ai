import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

# Basic route for testing
@app.route('/')
def index():
    return render_template('index.html')  # Make sure index.html exists in the templates folder

if __name__ == '__main__':
    app.run(debug=True)

load_dotenv()  # This loads the variables from .env into the environment

app = Flask(__name__)

# Load the API key from environment variables
API_KEY = os.getenv('API_KEY')

@app.route('/')
def index():
    print("Rendering index page")  # Add this line for debugging
    return render_template('index.html')

@app.route('/test')
def test_page():
    return "<h1>Flask is working!</h1>"

@app.route('/')
def index():
    return render_template('index.html')  # This is the main landing page


@app.route('/home')
def home():
    return render_template('upload.html')  # Or google_sheets.html


# This route handles POST requests for the form submission
@app.route('/api', methods=['POST'])
def api_endpoint():
    try:
        query = request.json.get('query')
        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Return a mock response for now (you can add your logic here)
        return jsonify({"response": f"Received query: {query}"})
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# This route handles GET requests for making an API request using the API_KEY
@app.route('/make_api_request', methods=['GET'])
def make_api_request():
    try:
        if not API_KEY:
            return "API_KEY not set", 400

        headers = {
            "Authorization": f"Bearer {API_KEY}"
        }

        # Example API request to Google API (Replace with your actual endpoint)
        response = requests.get(
            "https://www.googleapis.com/robot/v1/metadata/x509/ai-agent-service-account%40deep-beanbag-442016-v5.iam.gserviceaccount.com", 
            headers=headers
        )
        response.raise_for_status()  # This will raise an exception for 4xx/5xx status codes
        return jsonify(response.json())  # Return the response in JSON format
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error during API request: {str(e)}"}), 500


# This route handles POST requests for making an API request with a query
@app.route('/api/query', methods=['POST'])
def api_query():
    try:
        data = request.get_json()  # Expecting JSON input
        query = data.get('query')  # Extract the query

        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Make the API request using the query and API_KEY
        if not API_KEY:
            return jsonify({"error": "API_KEY not set"}), 400

        url = f"https://www.googleapis.com/robot/v1/metadata/x509/ai-agent-service-account%40deep-beanbag-442016-v5.iam.gserviceaccount.com/search?query={query}&key={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            return jsonify(response.json())  # Return the API response as JSON
        else:
            return jsonify({"error": "Failed to fetch data", "details": response.text}), 500

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)




