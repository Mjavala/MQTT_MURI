import paho.mqtt.client as mosquitto
import sys
import os
import json
import time
import asyncio
import threading
import muri_logging

msg1 = {
  "station": "TEST_01",
  "receiver": "rcvr_1",
  "data": {
    "TIMESTAMP": 1588353888.8910325,
    "ADDR_FROM": "test2",
    "RSSI_RX": 49,
    "FRAME_TYPE": "0xd2a8",
    "FRAME_CNT": 70,
    "FRAME": "d2a84e6d4e6d17bedcc3c14ee650001ac9f51d7c94b80315c7010000000000000000999999999999999901ff00ba0000ffff02fffffc0000fffd01ff01de011c0000027e0000",
    "frame_data": {
      "packet_id": 53928,
      "packet_num": 20077,
      "epoch index": 20077,
      "gps_lat": 398384323,
      "gps_lon": -1061793840,
      "gps_alt": 1735637,
      "gps_tow": 494703800,
      "gps_fix": 3,
      "gps_numsats": 21,
      "Batt Mon": 199,
      "Gondola Statu": 1,
      "RS41 Temp": 0,
      "RS41 Hum": 0,
      "RS41 Pres": 0,
      "temp Ta1 (amb)": 0,
      "temp Ti1 (int)": 39321,
      "temp Ta2 (amb)": 39321,
      "temp Ti2 (int)": 39321,
      "CW Chop Vr1": 39321,
      "CW Chop Vr2": 511,
      "CW Chop Vo1": 186,
      "CW Chop Vo2": 0,
      "CW Chop Cpot": 65535,
      "CW Chop Gpot": 2,
      "gps_veln": 255,
      "gps_vele": -4,
      "gps_vel_d": 0,
      "HW Chop Vr1": -3,
      "HW Chop Vr2": 511,
      "HW Chop Vo1": 478,
      "HW Chop Vo2": 284,
      "HW Chop Cpot": 0,
      "HW Chop Gpot": 2,
      "RMS Hor Vel": 126,
      "RMS Ver Vel": 0,
      "var_35": 0
    }
  }
}
msg2 = {
  "station": "TEST_01",
  "receiver": "rcvr_1",
  "data": {
    "TIMESTAMP": 1588353888.8910325,
    "ADDR_FROM": "test1",
    "RSSI_RX": 28,
    "FRAME_TYPE": "0xd2a8",
    "FRAME_CNT": 70,
    "FRAME": "d2a84e6d4e6d17bedcc3c14ee650001ac9f51d7c94b80315c7010000000000000000999999999999999901ff00ba0000ffff02fffffc0000fffd01ff01de011c0000027e0000",
    "frame_data": {
      "packet_id": 53928,
      "packet_num": 20077,
      "epoch index": 20077,
      "gps_lat": 388384323,
      "gps_lon": -1051793840,
      "gps_alt": 1755637,
      "gps_tow": 494703800,
      "gps_fix": 3,
      "gps_numsats": 21,
      "Batt Mon": 199,
      "Gondola Statu": 1,
      "RS41 Temp": 0,
      "RS41 Hum": 0,
      "RS41 Pres": 0,
      "temp Ta1 (amb)": 0,
      "temp Ti1 (int)": 39321,
      "temp Ta2 (amb)": 39321,
      "temp Ti2 (int)": 39321,
      "CW Chop Vr1": 38321,
      "CW Chop Vr2": 511,
      "CW Chop Vo1": 186,
      "CW Chop Vo2": 0,
      "CW Chop Cpot": 65535,
      "CW Chop Gpot": 2,
      "gps_veln": 255,
      "gps_vele": -4,
      "gps_vel_d": 0,
      "HW Chop Vr1": -3,
      "HW Chop Vr2": 511,
      "HW Chop Vo1": 478,
      "HW Chop Vo2": 284,
      "HW Chop Cpot": 0,
      "HW Chop Gpot": 2,
      "RMS Hor Vel": 126,
      "RMS Ver Vel": 0,
      "var_35": 0
    }
  }
}

class MQTT_SAMPLE_NODE():

    def on_connect(self, client, userdata, flags, rc):
        self.connected = True
        print("Connected to %s" % client)

    def on_message(self, client,  userdata, message):
        print(str(message.payload.decode()))

    def on_disconnect(client, userdata, rc):
        if rc != 0:
            self.connected = False
            print("Unexpected disconnection.")
    
    def on_subscribe(client, userdata, mid, granted_qos):
        pass

    
    def publish_message_wrap(self, channel, message_func):
        self.mqttc.publish(channel, str(json.dumps(message_func)), qos = 2)

    def logging_test(self):

        t = threading.Timer(3.0, self.logging_test)
        t.daemon = True

        self.publish_message_wrap("muri/raw", msg1)
        time.sleep(2)
        self.publish_message_wrap("muri/raw", msg2)
        
        t.start()

    def message_unpack(self, payload):
        try:
            message = json.loads(payload)
        except:
            print('hello world')

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
        try:
            self.mqttc.connect(MQTT_HOST, MQTT_PORT)
        except:
            print('Could not connect')

        self.mqttc.loop_start()

        print("Subscribing to Topics")
        self.mqttc.subscribe('muri/raw')

        self.logging_test()

        while (self.connected):
            pass


    def __init__(self): 
        self.mqttc = mosquitto.Client()
        self.id = None
        self.id_set = set()
        self.message_throttle = 0
        self.connected = True

        self.timestamp = None


if __name__ == "__main__":
    mqtt_conn = MQTT_SAMPLE_NODE()

    loop = asyncio.get_event_loop()

    loop.run_until_complete(asyncio.ensure_future(mqtt_conn.init_mqtt()))