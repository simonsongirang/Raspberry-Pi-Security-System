"""" Detects motion using sensor and sends notification accordingly"""
import time
import configparser
import logging
import RPi.GPIO as GPIO
from aws_notification import aws_send_notification
from slack_integration import send_snapshot_feed
from rpi_cam import snapshot

def main():
    """ Main function handles motion detection"""
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    print("Reading configuration file")
    logging.info('Application started')
    logging.info('Reading configuration file')
    config = configparser.ConfigParser()
    config.read('config', encoding='utf-8')
    start_counter = int(config['General']['Start_Counter'])
    gpio_sensor_pin = int(config['Sensor']['GPIO_Sensor_Pin'])
    aws_notification = config['AWS_Notification']['AWS_Notification']
    aws_topic_arn = config['AWS_Notification']['AWS_Topic_ARN']
    subject = config['Notification']['Motion_Subject']
    message = config['Notification']['Motion_Message']
    start_subject = config['Notification']['Start_Subject']
    start_message = config['Notification']['Start_Message']
    timeout = int(config['Notification']['Notification_Timeout'])
    limit = int(config['Notification']['Notification_Limit'])
    slack_notification = config['Slack_Notification']['Slack_Notification']
    slack_token = config['Slack_Notification']['Token']
    slack_channel = config['Slack_Notification']['Channel']

    print("Waiting for sensor to start")
    logging.info('Starting countdown......')
    for i in range(start_counter, -1, -1):
        logging.info('%s', i)
        print(str(i))
        time.sleep(1)
    print("Sensor Started")
    if aws_notification == 'ON':
        aws_send_notification(aws_topic_arn, start_subject, start_message)

    # Setting GPIO Pins
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_sensor_pin, GPIO.IN)
    motion_counter = 0

    while True:
        motion = GPIO.input(gpio_sensor_pin)
        if motion == 1:
            print("Motion Detected!")
            logging.info('Motion detected')

            if motion_counter < limit:
                print("Sending Notification")
                logging.info('Sending Notification...')
                logging.info('Taking Snapshot...')
                filepath, filename = snapshot()
                if aws_notification == 'ON':
                    aws_send_notification(aws_topic_arn, subject, message)
                if slack_notification == 'ON':
                    send_snapshot_feed(slack_token, filepath, filename, slack_channel)
                motion_counter = motion_counter + 1
            time.sleep(timeout)

if __name__ == '__main__':
    main()
