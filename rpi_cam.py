""" Module for PiCamera"""
# ToDo Migrate time to new file
from datetime import datetime
from picamera import picamera


def get_current_time():
    """ Returns current time in string """
    return datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

def gen_file_name():
    """ Generates filename based on current time"""
    time = get_current_time()
    filename = time + ".jpg"
    filepath = "./photo/" + filename
    return filepath, filename

def snapshot():
    """ Takes Snapshot"""
    camera = PiCamera()
    filepath, filename = gen_file_name()
    camera.capture(filepath)
    return filepath, filename
