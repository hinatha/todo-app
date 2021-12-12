# Overview
Project for todo app

## Structure

```bash
.
├── README.md
├── backend
│   ├── README.md
│   ├── app.py
│   ├── entities
│   ├── node_modules
│   ├── package-lock.json
│   ├── package.json
│   ├── requirements.txt
│   └── serverless.yml
└── frontend
    ├── README.md
    ├── __pycache__
    ├── app.py
    ├── requirements.txt
    └── templates

6 directories, 10 files
```

# Features
This app is able to use below function.

## User Story
- Add a task.
- Check detail of tasks.
- See the list of tasks.
- Delete tasks.
- Change status of task.
- Edit tasks.

# Using of language, framework, technology
- Python
- HTML/CSS
- Flask
- Serverless framework
- Lambda
- DynamoDB
- API Gateway
  
# Requirement
- Homebrew==3.3.4
- serverless framework==2.66.2
- AWS CLI==2.3.3
- boto3==1.20.12
- venv
- Flask==2.0.2
- python-dotenv==0.19.2
- requests==2.26.0
- WTForms==3.0.0
 
# Installation
 
```bash
(.venv) $ pip install -r requirements.txt
```
 
# Usage
 
```bash
(.venv) $ python app.py
```
 
# Future plans
- Dockerizing frontend/backend
- Deploy by EC2 
