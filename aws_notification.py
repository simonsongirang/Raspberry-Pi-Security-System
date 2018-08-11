
import boto3

client = boto3.client('sns')

def aws_send_notification(AWS_Topic_ARN, Subject, Message):
    print ("Notification Sent")
    response = client.publish(TopicArn=AWS_Topic_ARN,
                              Subject=Subject,
                              Message=Message,
                              MessageStructure='string'
               )
