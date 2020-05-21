#!/usr/bin/python3

# Muri App Main Program
# Program Structure: 
#   - muri_app_main (runs async, mult instances allowed)
#   - muri_app_mqtt (runs async, sgl instance)
#   - muri_db (sgl instance, single operation (R/W) connection to DB)
#   - muri_app_log (sgl instance, needs to be configured for your directory structure)
#   - Muri App Main Program (muri_app_main)
#       - Async. Runs logging, MQTT and Database service. Watchdog. General Logging

import asyncio
import logging
import logging.handlers as handlers
import time
import json
from muri.backend.muri_app_mqtt import muri_app_mqtt as mqttc
import muri.backend.muri_db as muri_db


# TODO: General Logging
STAT_INTERVAL = 5

mqtt_conn = mqttc()
db = muri_db.muri_db()

async def main_loop(): 

    last_stat = time.time()
    #logger = logging.getLogger()

    try: 

        while (True):
           
            #if (mqtt_conn.isConnected() == True): 
                #log connection alive + stats

            if (time.time() - last_stat > STAT_INTERVAL): 
                last_stat = time.time() 
                stat_msg = {"mqtt": mqtt_conn.get_stats()}

                # stat msg to database
                db.msg_in(stat_msg)

                #logger.log_app(json.dumps(stat_msg))
            await asyncio.sleep(0.01)


    except Exception as e: 
        print(e)
        #logger.log_app("Main Loop Exception: %s" % e)



if __name__ == '__main__':
    #logger = logging.getLogger()


    #logger.log_app("Starting DGRS Main Program")

    #logger.log_app("Receiver 1 Comm Port Requested: {0}".format(args.rcvr_1_port))

    loop = asyncio.get_event_loop()

    tasks = [asyncio.ensure_future(main_loop()),
             asyncio.ensure_future(mqtt_conn.main_loop()),
             asyncio.ensure_future(db.main_loop())]

    loop.run_until_complete(asyncio.gather(*tasks))
