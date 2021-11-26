import string
import random
import boto3
import json
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['DYNAMODB_TABLE']
table = dynamodb.Table(TABLE_NAME)

def create(body):
    task_id = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    task = body["task"]
    detail = body["detail"]
    item = {
        "task_id": task_id,
        "task": task,
        "detail": detail
        }
    table.put_item(Item=item)
    return json.dumps(item)