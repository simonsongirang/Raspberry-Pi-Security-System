import RPi.GPIO as GPIO
import time
import configparser
from aws_notification import aws_send_notification






def main():
    print ("Reading configuration file")
    config = configparser.ConfigParser()
    config.read('config', encoding='utf-8')
    Start_Counter = int(config['General']['Start_Counter'])
    GPIO_Sensor_Pin = int(config['Sensor']['GPIO_Sensor_Pin'])
    AWS_Notification = config['AWS_Notification']['AWS_Notification']
    AWS_Topic_ARN = config['AWS_Notification']['AWS_Topic_ARN']
    Subject = config['Notification']['Motion_Subject']
    Message = config['Notification']['Motion_Message']
    Timeout = int(config['Notification']['Notification_Timeout'])
    Limit = int(config['Notification']['Notification_Limit'])

    print ("Waiting for sensor to start")
    time.sleep(Start_Counter)
    print ("Sensor Started")

    # Setting GPIO Pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(GPIO_Sensor_Pin, GPIO.IN)
    c = 0

    while True:
        motion = GPIO.input(GPIO_Sensor_Pin)
        if motion == 1:
            print ("Motion Detected!")
            if c < Limit:
                print ("Sending Notification")
                aws_send_notification(AWS_Topic_ARN, Subject, Message)
                c = c + 1
            time.sleep(Timeout)

main()
