""" Module for PiCamera"""
# ToDo Migrate time to new file
from datetime import datetime
import logging
from picamera import PiCamera

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
    try:
        logging.info('Taking snapshot using RPI Camera')
        camera = PiCamera()
        filepath, filename = gen_file_name()
        logging.info('Generated file path: %s', filepath)
        logging.info('Generated file name: %s', filename)
        camera.capture(filepath)
        camera.close()
        return filepath, filename
    except IOError as error:
        logging.info('Unexpected PI Camera error')
        logging.info(error)
        camera.close()
        return '0', '0'
