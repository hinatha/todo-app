from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import requests

import os

load_dotenv()

app = Flask(__name__)

backend_url = os.getenv('BACKEND_URL', 'http://localhost:5000')
create_url = os.getenv('CREATE_URL', 'http://localhost:5000')


@app.route("/", methods=['GET'])
def hello():

    r = requests.get(backend_url)
    items = r.text

    return render_template('index.html', items=items)

@app.route("/createtask", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        task = request.form.get('task')
        detail = request.form.get('detail')
        payload = {
            "task":task,
            "detail":detail
        }
        r = requests.post(create_url, json=payload)
        return redirect('/')
    else:
        return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)