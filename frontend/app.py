from flask import Flask, render_template
from dotenv import load_dotenv
import requests

import os

load_dotenv()

app = Flask(__name__)

backend_url = os.getenv('BACKEND_URL', 'http://localhost:5000')

@app.route("/", methods=['GET'])
def hello():
    
    r = requests.get(backend_url)
    items = r.text

    return render_template('index.html', items=items)

if __name__ == "__main__":
    app.run(debug=True)