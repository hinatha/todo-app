# Import library
from flask import jsonify
import uuid
import boto3
import os
import logging

# Set up logger
logger = logging.getLogger('awslog')
logger.setLevel(logging.INFO)

# Define variables for environment variables
TABLE_NAME = os.environ["DYNAMODB_TABLE"]

# Set up boto3
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)

def create(body):
    '''
    Execute PutItem API
    FYI: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_PutItem.html
    '''
    logger.info("### execute create method")
    try:
        task_id = str(uuid.uuid4())
        task = body["task"]
        detail = body["detail"]
        item = {
            "task_id": task_id,
            "task": task,
            "detail": detail
            }
        # Execute table.put_item method
        table.put_item(Item=item)
    except Exception as err:
        rc = 1
        logger.error(f'''An exception occurred while executing table.put_item method. [RETURN CODE: {rc}][ERROR: {err}]''')
        raise Exception((f'''An exception occurred while executing table.put_item method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    return jsonify(item)

def get_all():
    '''
    Execute Scan API
    FYI: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html
    '''
    logger.info("### execute get_all method")
    try:
        # Execute table.scan method
        response = table.scan()
        items = response["Items"]
    except Exception as err:
        rc = 1
        logger.error(f'''An exception occurred while executing table.scan method. [RETURN CODE: {rc}][ERROR: {err}]''')
        raise Exception((f'''An exception occurred while executing table.scan method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    return jsonify(items)