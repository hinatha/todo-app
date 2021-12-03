from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

backend_url = os.getenv('BACKEND_URL', 'http://localhost:5000')
task_url = f'''{backend_url}/tasks'''


@app.route("/")
def index():
    r = requests.get(task_url)
    r.raise_for_status()
    tasks = r.json()
    return render_template('index.html', tasks=tasks)

@app.route("/create-task")
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