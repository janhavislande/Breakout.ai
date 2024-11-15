from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Setup is complete and Flask is working!"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI-Agent Dashboard!"

@app.route('/about')
def about():
    return "This project is designed to process datasets and retrieve web information "

@app.route('/contact')
def contact():
    return "Contact us at: breakoutai@gmail.com"
if __name__ == '__main__':
    app.run(debug=True)