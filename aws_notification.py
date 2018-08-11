""" Module that sends notification to AWS"""
import boto3
CLIENT = boto3.client('sns')

def aws_send_notification(aws_topic_arn, subject, message):
    """Sends Notification"""
    print("Notification Sent")
    response = CLIENT.publish(TopicArn=aws_topic_arn,
                              Subject=subject,
                              Message=message,
                              MessageStructure='string')
