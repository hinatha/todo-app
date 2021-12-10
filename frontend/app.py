from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import requests
import os
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField, HiddenField

load_dotenv()

app = Flask(__name__)

# Enable CSRF measures
app.config["SECRET_KEY"] = "123456789"
app.config["WTF_CSRF_ENABLED"] = True


# Difine API url
backend_url = os.getenv("BACKEND_URL", "http://localhost:5000")
task_url = f"""{backend_url}/tasks"""


class TaskForm(FlaskForm):
    # For CSRF measures
    hidden_field_1 = HiddenField("HiddenField 1")
    hidden_field_2 = HiddenField("HiddenField 2")
    hidden_field_3 = HiddenField("HiddenField 3")
    # Set task form to add task
    task = StringField(validators=[DataRequired()])
    detail = StringField(validators=[DataRequired()])
    submit = SubmitField("Resister")

# Display top page
@app.route("/", methods=["GET"])
def index():
    r = requests.get(task_url)
    r.raise_for_status()
    tasks = r.json()
    return render_template("index.html", tasks=tasks)

@app.route("/create-task", methods=["GET", "POST"])
def create():
    form = TaskForm()
    # Display create page
    if request.method == "GET":
        return render_template("create.html", form=form)
    else:
        # Send form to server
        if form.validate_on_submit():
            task = request.form.get("task")
            detail = request.form.get("detail")
            payload = {
                "task":task,
                "detail":detail
            }
            r = requests.post(task_url, json=payload)
            r.raise_for_status()
            return redirect("/")
        # In case of error
        else:
            return render_template("create.html", form=form)

@app.route("/detail/<taskId>", methods=["GET"])
def detail(taskId):
    taskId_url = f"""{task_url}/{taskId}"""
    r = requests.get(taskId_url)
    r.raise_for_status()
    tasks = r.json()
    print("alive")
    return render_template("detail.html", tasks=tasks)

if __name__ == "__main__":
    app.run(debug=True)