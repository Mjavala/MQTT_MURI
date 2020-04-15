import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler
import sys
from pathlib import Path

# format the log entries


def logger_generator(device_list, id, message):
    #if the device is streaming and there is no logger created
    for i in device_list:
        if id in device_list and id not in logging.root.manager.loggerDict:
            #create a logger
            logger = log_obj(id)
            logger.info(message)
        elif id in device_list and id in logging.root.manager.loggerDict:
            #logger exists
            logger = logging.getLogger(id)
            logger.info(message)
        elif id not in device_list:
            raise
    # check for new files
    print('here')
    for path in Path('logs').rglob('*.log'):
        print(path.name)

def log_obj(id):
    daily_path,  hourly_path = build_dir(id)

    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

    handler_daily = TimedRotatingFileHandler(daily_path, 
                                    when= 'D',
                                    backupCount = 10 )
    handler_hourly = TimedRotatingFileHandler(hourly_path, 
                                    when= 'H',
                                    backupCount = 10 )    

    handler_hourly.setFormatter(formatter)
    handler_daily.setFormatter(formatter)

    logger = logging.getLogger(id)

    logger.addHandler(handler_hourly)
    logger.addHandler(handler_daily)
    logger.setLevel(logging.INFO)

    logger.info('helllo!!')
    return logger

def build_dir(id):
    

    path_hourly = '/home/jose/MQTT_MURI/backend/logs/{0}/hourly/'.format(id)
    path_daily = '/home/jose/MQTT_MURI/backend/logs/{0}/daily/'.format(id)

    try:
        
        os.makedirs(path_hourly, mode=0o777, exist_ok=True)
        os.makedirs(path_daily, mode=0o777, exist_ok=True)
    except OSError as e:
        sys.exit("Can't create dir: {err}".format(err=e))

    timestamp = time.strftime('%Y-%m-%d-%H:%M', time.localtime(time.time()))    

    return path_daily + '{0}.log'.format(timestamp), path_hourly + '{0}.log'.format(timestamp)
