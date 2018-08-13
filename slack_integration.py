""" Sends notification with snapshot to slack"""
#import json
import requests

def send_snapshot_feed(token, filepath, filename, channelname):
    """ Send snapshot feed to slack room """
    my_file = {
        'file' : (filepath, open(filepath, 'rb'), 'jpg')
    }
    payload={
      "filename": filename,
      "token":token,
      "channels":[channelname],
    }
    r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
