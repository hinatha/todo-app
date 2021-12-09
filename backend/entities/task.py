from flask import jsonify
import uuid
import boto3
import json
import os
import logging

# Set up logger
logger = logging.getLogger("awslog")
logger.setLevel(logging.INFO)

# Set up dynamoDB table
dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ["DYNAMODB_TABLE"]
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
        table.put_item(Item=item)
    except Exception as err:
        rc = 1
        logger.error(f'''An exception occured while executing table.put_item method. [RETURN CODE: {rc}][ERROR: {err}]''')
        raise Exception((f'''An exception occured while executing table.put_item method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    return jsonify(item)

def get_all():
    '''
    Execute Scan API
    FYI: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Scan.html
    '''
    logger.info("### execute get_all method")
    try:
        response = table.scan()
        items = response["Items"]
    except Exception as err:
        rc = 1
        logger.error(f'''An exception occured while executing table.scan method. [RETURN CODE: {rc}][ERROR: {err}]''')
        raise Exception((f'''An exception occurred while executing table.scan method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    return jsonify(items)

def get(taskId):
    '''
    Execute Get API
    FYI: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Get.html
    '''
    logger.info("### execute get method")
    try:
        response = table.get_item(Key={"task_id": taskId})
        item = response["Item"]
    except Exception as err:
        rc = 1
        logger.error(f'''An exception occured while executing table.get method. [RETURN CODE: {rc}][ERROR: {err}]''')
        raise Exception((f'''An exception occured while executing table.get method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    return jsonify(item)


