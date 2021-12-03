from flask import Flask,request
from entities import task

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/tasks", methods=['POST'])
def create_task():
    event = request.get_json()
    return task.create(event)

   


