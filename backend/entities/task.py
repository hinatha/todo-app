from flask import jsonify
import uuid
import boto3
import os
import logging

'''
Execute logger
FYI: https://hacknote.jp/archives/17690/
'''
logger = logging.getLogger("awslog")
logger.setLevel(logging.INFO)

'''
Execute boto3
FYI: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#table
'''
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
        '''
        Execute uuid
        FYI: https://docs.python.org/ja/3/library/uuid.html
        '''
        task_id = str(uuid.uuid4())
        task = body["task"]
        detail = body["detail"]
        status = body["status"]
        item = {
            "task_id": task_id,
            "task": task,
            "detail": detail,
            "status": status
            }
        table.put_item(Item=item)
    except Exception as err:
        '''
        Execute except
        https://docs.python.org/ja/3/tutorial/errors.html
        '''
        rc = 1
        logger.error(f'''An exception occured while executing table.put_item method. [RETURN CODE: {rc}][ERROR: {err}]''')
        '''
        Execute raise Exception
        https://uxmilk.jp/39845
        '''
        raise Exception((f'''An exception occured while executing table.put_item method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    '''
    Execute jsonify
    FYI: https://admin-it.xyz/python/flask-jsonify-jsondumps-difference/
    '''
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
    Execute GetItem API
    FYI: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_GetItem.html
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

def delete(taskId):
    '''
    Execute DeleteItem API
    FYI: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DeleteItem.html
    '''
    logger.info("### execute delete method")
    try:
        key = {"task_id": taskId}
        table.delete_item(Key={"task_id": taskId})
        item = key
    except Exception as err:
        rc = 1
        logger.error(f'''An exception occured while executing table.delete method. [RETURN CODE: {rc}][ERROR: {err}]''')
        raise Exception((f'''An exception occured while executing table.delete method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    return jsonify(item)

def update(taskId, body):
    '''
    Execute UpdateItem API
    FYI: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_UpdateItem.html
    '''
    logger.info(("### execute update method"))
    try:
        task = body["task"]
        detail = body["detail"]
        status = body["status"]
        item = {
            "task_id": taskId,
            "task": task,
            "detail": detail,
            "status": status
            }
        logger.info(("### execute create item"))
        '''
        Execute update_item
        FYI: https://dev.classmethod.jp/articles/dynamodb-update-expression-actions/
        '''
        table.update_item(
            Key={"task_id": taskId},
            UpdateExpression="set #task = :task, #detail = :detail, #status = :status",
            ExpressionAttributeNames = {
                "#task": "task",
                "#detail": "detail",
                "#status": "status",
            },
            ExpressionAttributeValues = {
                ":task": task,
                ":detail": detail,
                ":status": status
            }
        )
    except Exception as err:
        rc = 1
        logger.error(f'''An exception occured while executing table.update method. [RETURN CODE: {rc}][ERROR: {err}]''')
        raise Exception((f'''An exception occurred while executing table.update method. [RETURN CODE: {rc}][ERROR: {err}]'''))
    return jsonify(item)
