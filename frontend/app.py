from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import requests
import ast

import os

load_dotenv()

app = Flask(__name__)

backend_url = os.getenv('BACKEND_URL', 'http://localhost:5000')
task_url = f'''{backend_url}/tasks'''


@app.route("/")
def index():
    r = requests.get(task_url)
    l = ast.literal_eval(r.text)
    l_task = [d.get("task") for d in l]
    l_id = [d.get("task_id")for d in l]
    return render_template('index.html', l_task=l_task, l_id=l_id)

@app.route("/createtask")
def create():
    return render_template('create.html')

@app.route("/tasks", methods=['POST'])
def add():
    task = request.form.get('task')
    detail = request.form.get('detail')
    payload = {
        "task":task,
        "detail":detail
    }
    requests.post(task_url, json=payload)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)