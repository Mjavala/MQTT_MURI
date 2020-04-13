import paho.mqtt.client as mosquitto
import sys
import os
import json
import time
import asyncio
import threading
import muri_logging

class MQTT_SAMPLE_NODE():

    def on_connect(self, client, userdata, flags, rc):
            print("Connected to %s" % client)

    def on_message(self, client,  userdata, message):
        self.message_throttle += 1
        print(self.message_throttle)
        if self.message_throttle == 30:
            self.message_throttle = 0
            self.message_unpack(str(message.payload.decode()))

    def on_subscribe(self, client, userdata, mid, granted_qos):
        pass

    
    def publish_message_wrap(self, channel, message_func):
        return self.mqttc.publish(channel, str(json.dumps(message_func)), qos = 2)


    def connect(self):
        self.heartbeat = True

        t = threading.Timer(30.0, self.connect)
        t.daemon = True

        self.publish_message_wrap("muri/test", self.mission_request_message())
        
        t.start()

    def message_unpack(self, payload):
        message = json.loads(payload)
        self.id = self.id_set
        self.id.add(message['ADDR_FROM'])

        muri_logging.logger_generator(self.id, message['ADDR_FROM'], payload)


    async def init_mqtt(self):

        MQTT_USER = "muri"
        MQTT_PASS = "demo2020"
        MQTT_HOST = "irisslive.net"
        MQTT_PORT = 8883

        self.mqttc.username_pw_set(MQTT_USER, MQTT_PASS)

        self.mqttc.on_message = self.on_message
        self.mqttc.on_connect = self.on_connect
        self.mqttc.on_subscribe = self.on_subscribe

        print("Connecting to MQTT Server")
        self.mqttc.connect(MQTT_HOST, MQTT_PORT)

        self.mqttc.loop_start()

        print("Subscribing to Topics")
        self.mqttc.subscribe('muri/#')

        while True:
            pass


    def __init__(self): 
        self.mqttc = mosquitto.Client()
        self.heartbeat = False
        self.id = None
        self.id_set = set()
        self.message_throttle = 0

        self.timestamp = None

      



if __name__ == "__main__":
    mqtt_conn = MQTT_SAMPLE_NODE()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.ensure_future(mqtt_conn.init_mqtt()))

