from picamera import picamera
from datetime import datetime

def get_current_time():
    """ Returns current time in string"""
    return datetime.now().strftime('%Y-%m-%d-%H:%M:%S')

def gen_file_name():
    """ Generates filename based on current time"""
    time = get_current_time()
    path = "./photo/" + time + ".jpg"
    return path

def snapshot():
    """ Takes Snapshot"""
    camera = PiCamera()
    camera.capture(gen_file_name)
