import os
import boto3

SQS_CLIENT = boto3.client('sqs')
queue_url = os.getenv('SQS_URL')

def lambda_handler(event, context):
    print(SQS_CLIENT.send_message(
        QueueUrl=queue_url,
        MessageBody='sent message'
    ))
    return ''
