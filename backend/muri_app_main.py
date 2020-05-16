#!/usr/bin/python3
import asyncio
import logging
import logging.handlers as handlers
import time
import json
from muri_app_mqtt import muri_app_mqtt as mqttc
import muri_db


# Need to implement main logger from custom log module
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

                # stat message goes to db node receiver
                db.msg_in(stat_msg)

                #logger.log_app(json.dumps(stat_msg))
            await asyncio.sleep(0.01)


    except Exception as e: 
        print('error')
        #logger.log_app("Main Loop Exception: %s" % e)

    finally: 
        pass



if __name__ == '__main__':
    #logger = logging.getLogger()


    #logger.log_app("Starting DGRS Main Program")

    #logger.log_app("Receiver 1 Comm Port Requested: {0}".format(args.rcvr_1_port))

    loop = asyncio.get_event_loop()

    tasks = [asyncio.ensure_future(main_loop()),
             asyncio.ensure_future(mqtt_conn.main_loop()),
             asyncio.ensure_future(db.main_loop())]

    loop.run_until_complete(asyncio.gather(*tasks))
