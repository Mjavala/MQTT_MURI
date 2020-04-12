import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler

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

def log_obj(id):
    daily_path,  hourly_path= build_dir(id)

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

    print(logger)
    return logger

def build_dir(id):
    path_hourly = 'C:/Users/jose/Projects/muri/logs/{0}/hourly'.format(id)
    path_daily = 'C:/Users/jose/Projects/muri/logs/{0}/daily'.format(id)
    try:
        os.makedirs(path_hourly, mode=0o777, exist_ok=True)
        os.makedirs(path_daily, mode=0o777, exist_ok=True)
    except OSError as e:
        sys.exit("Can't create {dir}: {err}".format(dir=output_dir, err=e))
    else:
        pass
    return path_daily, path_hourly


log_obj('wdadw')