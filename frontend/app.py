from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
import requests
import os
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = "123456789"
app.config["WTF_CSRF_ENABLED"] = True

backend_url = os.getenv("BACKEND_URL", "http://localhost:5000")
task_url = f"""{backend_url}/tasks"""

# Set task form to add task
class TaskForm(FlaskForm):
    task = StringField(validators=[DataRequired()])
    detail = StringField(validators=[DataRequired()])
    submit = SubmitField()

@app.route("/", methods=["GET"])
def index():
    r = requests.get(task_url)
    r.raise_for_status()
    tasks = r.json()
    print("alive")
    return render_template("index.html", tasks=tasks)

@app.route("/create-task", methods=["GET", "POST"])
def create():
    form = TaskForm()
    if request.method == "GET":
        print("alive")
        return render_template("create.html", form=form)
    else:
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
        else:
            return render_template("create.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)