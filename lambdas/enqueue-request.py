import boto3
import json
import os

SQS_CLIENT = boto3.client('sqs')
queue_url = os.getenv('SQS_URL')

def lambda_handler(event, context):
    url = event['url']
    depth = event['depth']
    
    qmessage = {}
    qmessage["url"] = url
    qmessage["depth"] = depth
    
    print(SQS_CLIENT.send_message(
        QueueUrl=queue_url,
        MessageBody=json.dumps(qmessage)
    ))
    return ''
