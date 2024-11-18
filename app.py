from flask import Flask, request
import os
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'data/uploaded_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route
@app.route('/')
def home():
    return "Welcome to the AI Agent Project!"

# Upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # This will print in the terminal when the /upload page is accessed
    print("Upload page accessed")

    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Get filename and save the file
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Read CSV file using pandas
            df = pd.read_csv(file_path)

            # Convert the DataFrame to an HTML table
            table = df.to_html(classes='table table-bordered')

            return f'''
                <h3>File '{filename}' uploaded successfully!</h3>
                <h4>CSV Data:</h4>
                {table}
            '''
    
    # If method is GET or no file is uploaded, show the upload form
    return '''
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

if __name__ == '__main__':
    # Ensure the app runs only when executed directly
    app.run(debug=True)

