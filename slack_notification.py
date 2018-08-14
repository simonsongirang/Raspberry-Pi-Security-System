""" Sends notification with snapshot to slack"""
import logging
import requests

def send_snapshot_feed(token, filepath, filename, channelname):
    """ Send snapshot feed to specified channel """
    try:
        logging.info('Sending Slack notification with image')
        logging.info('File path: %s', filepath)
        logging.info('File name: %s', filename)
        logging.info('Channel name: %s', channelname)
        my_file = {
            'file' : (filepath, open(filepath, 'rb'), 'jpg')
        }
        payload = {
            'filename': filename,
            'token': token,
            'channels': [channelname],
        }
        response = requests.post("https://slack.com/api/files.upload",
                                 params=payload, files=my_file)
        logging.info('Posted an image to the slack channel')
    except requests.exceptions.RequestException as exception:
        logging.info('Error while sending HTTP request')
        logging.info(exception)
        logging.info('Response:')
        logging.info(response)
    except IOError as exception:
        logging.info('Unable to read file')
        logging.info(exception)

def send_slack_message(token, message, channelname):
    """ Send message to specified channel """
    try:
        logging.info('Sending Slack message')
        logging.info('File path: %s', message)
        logging.info('Channel name: %s', channelname)
        payload = {
            "text": message,
            "token":token,
            "channels":[channelname],
        }
        response = requests.post("https://slack.com/api/chat.postMessage", params=payload)
        logging.info('Posted a message to the slack channel')
    except requests.exceptions.RequestException as exception:
        logging.info('Error while sending HTTP request')
        logging.info(exception)
        logging.info('Response:')
        logging.info(response)
