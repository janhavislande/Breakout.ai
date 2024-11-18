from flask import Flask

# Create a single Flask app instance
app = Flask(__name__)

# Define routes
@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "This is the About Page!"

@app.route('/contact')
def contact():
    return "Feel free to Contact Us!"

# Ensure the app runs only when executed directly
if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, request, render_template
import os
import pandas as pd

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = './data/uploaded_files/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Home route
@app.route('/')
def home():
    return "Welcome to the AI Agent Project!"

# File upload route
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        file = request.files['file']
        if file.filename == '':
            return "No selected file"
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            data = pd.read_csv(filepath)
            return render_template('upload.html', tables=[data.to_html(classes='data')], titles=data.columns.values)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
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
    app.run(debug=False)  # Avoid debug=True to prevent reloader issue.

    
