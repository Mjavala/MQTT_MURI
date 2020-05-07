import paho.mqtt.client as mosquitto
import json
import time
import asyncio
import muri_app_log

MQTT_USER = "muri"
MQTT_PASS = "demo2020"
MQTT_HOST = "irisslive.net"
MQTT_PORT = 8883


class muri_app_mqtt():

    def __init__(self): 

        self.connected = False

        self.mqttc = mosquitto.Client()
        self.mqttc.on_connect = self.on_mqtt_conn
        self.mqttc.on_disconnect = self.on_mqtt_disc
        self.mqttc.on_message = self.on_mqtt_msg

        self.id = str
        self.id_set = set()
        self.last_stat_time = time.time()
        self.last_stats = {}
        self.msg_cnt = 0

    def on_mqtt_conn(self, client, userdata, flags, rc):
        if rc == 0:
            self.connected = True
            self.mqttc.subscribe('muri/raw')
            print("--- MQTT Connected! ---")
            #self.logger.log_app("--- MQTT Connected! ---")
        else: 
            self.connected = False
            print("!!! MQTT Connection Failed! !!!")
            #self.logger.log_app("!!! MQTT Connection Failed! !!!")

    def on_mqtt_disc(client, userdata, rc): 
        print("!!! MQTT Disconnceted Unexpectedly !!!")
        self.connected = False
        if (rc != 0): 
            print("!!! MQTT Disconnceted Unexpectedly !!!")
            #self.logger.log_app("!!! MQTT Disconnceted Unexpectedly !!!")
        else: 
            #self.logger.log_app("!!! MQTT Disconnceted Planned !!!")
            self.connected = False

    def on_mqtt_msg(self, client,  userdata, message):
        print('---Message Received---')

        self.message_unpack(str(message.payload.decode()))


    def message_unpack(self, payload):
        message = json.loads(payload)

        self.id = message['data']['ADDR_FROM']
        self.id_set.add(self.id)

        muri_app_log.device_logger(self.id_set, self.id, payload)
    
    def isConnected(self): 
        return self.connected

    def stats(self):
        stat_time = time.time() - self.last_stat_time
        self.last_stat_time = time.time()

        self.last_stats = {
            "last_update": time.time(), 
            "period": stat_time, 
            "mqtt_count": self.msg_cnt, 
            "device_id": self.id,
            "device_list": self.id_set
            }
        
        self.msg_cnt = 0

    def get_stats(self): 
        return self.last_stats


    async def start_mqtt(self):
    
        try:
            self.mqttc.username_pw_set(MQTT_USER, MQTT_PASS)

            #self.logger.log_app("Connecting to MQTT Server....")
            self.mqttc.connect_async(MQTT_HOST, MQTT_PORT, keepalive=15)
            self.mqttc.loop_start()
            #self.logger.log_app("Done!")

        except Exception as e: 
            print(e)
            #logging.getLogger().log_app("Exception in MQTT Start Script: %s" % e)

    async def main_loop(self):
        last_time = time.time()
        try: 
            await self.start_mqtt()
            while(True):

                if (time.time() - last_time > 5): 
                    #self.logger.log_app("MQTT Status: Connnected: %s, qOut: %d qIn: %d" % (self.connected, self.qOut.qsize(), self.qIn.qsize()))
                    last_time = time.time()

                await asyncio.sleep(0.1)
        except Exception as e:
            print("Exception in MQTT: %s" % e) 
            #logging.getLogger().log_app("Exception in MQTT: %s" % e)
        finally: 
            pass


      



if __name__ == "__main__":
    mqtt_conn = muri_app_mqtt()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.ensure_future(mqtt_conn.main_loop()))

