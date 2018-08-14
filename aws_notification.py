""" Module that sends notification to AWS"""
import logging
import boto3

def aws_send_notification(aws_topic_arn, subject, message):
    """Sends AWS Notification"""
    try:
        logging.info('Sending AWS notification')
        logging.info('Subject: ' + subject + ' Message: ' + message)
        client = boto3.client('sns')
        response = client.publish(TopicArn=aws_topic_arn,
                                  Subject=subject,
                                  Message=message,
                                  MessageStructure='string')
        logging.info('AWS notification sent')
    except boto3.exceptions.botocore.exceptions.ClientError as error:
        logging.info('Error while sending message...')
        logging.info('Result:')
        logging.info(response)
        logging.info('Exception:')
        logging.info(error)
