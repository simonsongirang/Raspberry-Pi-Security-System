import RPi.GPIO as GPIO
import time
import boto3
import configparser

# AWS
client = boto3.client('sns')

def send_notification(Topic, Message):
    print ("Notification Sent")
    response = client.publish(TopicArn=Topic,
                              Message=Message,
                              MessageStructure='string'
               )


def main():
    print ("Reading configuration file")
    with open("config") as file:
        config_file = file.read()
    config = configparser.ConfigParser(allow_mno_value=True)
    config.read(config_file)
    Start_Counter = int(config['General']['Start_Counter'])
    GPIO_Sensor_Pin = int(config['Sensor']['GPIO_Sensor_Pin'])
    AWS_Topic_ARN = config['Notification']['AWS_Topic_ARN']
    Message = config['Notification']['Message']

    print ("Waiting for sensor to start")
    time.sleep(Start_Counterm)
    print ("Sensor Started")

    # Setting GPIO Pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_Sensor_Pin, GPIO.IN)
    c = 0

    while True:
        motion = GPIO.input(gpin)
        if motion == 1:
            print ("Motion Detected!")
            if c < 1:
                print ("Sending Notification")
                #send_notification(AWS_Topic_ARN, Message)
                c = c + 1
            time.sleep(10)

main()
