""" Sends notification with snapshot to slack"""
#import json
import requests

def send_snapshot_feed(token, filepath, filename, channelname):
    """ Send snapshot feed to specified channel """
    my_file = {
        'file' : (filepath, open(filepath, 'rb'), 'jpg')
    }
    payload={
      "filename": filename,
      "token":token,
      "channels":[channelname],
    }
    r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)

def send_slack_message(token, message, channelname):
    """ Send message to specified channel """
    payload={
      "text": message,
      "token":token,
      "channels":[channelname],
    }
    r = requests.post("https://slack.com/api/files.upload", params=payload)
