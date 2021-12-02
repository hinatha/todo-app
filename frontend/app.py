from flask import Flask, render_template
from dotenv import load_dotenv
import requests

import os

load_dotenv()

app = Flask(__name__)

backend_url = os.getenv('BACKEND_URL', 'http://localhost:5000')


@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

@app.route("/createtask")
def create():
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)