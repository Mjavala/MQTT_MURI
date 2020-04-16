from flask import Flask
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
from flask_bootstrap import Bootstrap
import eventlet
import muri_logging
import json

ID = None
id_set = set()
    
eventlet.monkey_patch()

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'irisslive.net'
app.config['MQTT_BROKER_PORT'] = 8883
app.config['MQTT_USERNAME'] = 'muri'
app.config['MQTT_PASSWORD'] = 'demo2020'
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
mqtt = Mqtt(app)
socketio = SocketIO(app)
bootstrap = Bootstrap(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print("connected to mqtt broker" + app.config['MQTT_BROKER_URL'])
    mqtt.subscribe('muri/#')

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    payload = str(message.payload.decode())
    message_unpack(payload)

def message_unpack(payload):
    message = json.loads(payload)
    ID = id_set
    ID.add(message['ADDR_FROM'])

    muri_logging.logger_generator(ID, message['ADDR_FROM'], payload)


if __name__ == '__main__':
    # important: Do not use reloader because this will create two Flask instances.
    # Flask-MQTT only supports running with one instance
    socketio.run(app, host='0.0.0.0', port=5000, use_reloader=False, debug=False)