from types import SimpleNamespace as Namespace
import logging
import json

#   resource - https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object

def msg_in(self, message):
    msg_dict = json.loads(message, object_hook=lambda d: Namespace(**d))

    msg_to_db = self.check_msg_type(message)
    return msg_to_db

def check_msg_type(self, message):
    logger = logging.getLogger('app')
    #   interval index is only applicable for 0xC109 message
    value = message.get('FRAME_TYPE')

    if value == '0xC109':
        logger.log_app('--- 0xC109 Message Received ---')
        msg_to_db = {'0xC109': message}
        return msg_to_db 

    if value == '0xd2a8':
        logger.log_app('--- 0xd2a8 Message Received ---')
        msg_to_db = {'0xd2a8': message}
        return msg_to_db

    elif value == 'None':
        logger.log_app('--- RAW DB SERVICE ERROR: Undefined message type ---')

