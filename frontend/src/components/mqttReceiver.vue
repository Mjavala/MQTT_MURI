<template>
  <div id="app">
    <div id="wrapper">
      <!-- Vuetify buttons - https://vuetifyjs.com/en/components/buttons/ -->
      <v-btn icon depressed rounded id="live" v-if="this.status">
        <v-icon id="live-icon" color="#76FF03">mdi-wifi</v-icon>
      </v-btn>
      <!-- props - https://vuejs.org/v2/guide/components-props.html -->
      <!-- sends message obj to the filter ID component for processing a list of global device IDs -->
      <filterID v-bind:message="this.message" />
      <div id='conFeedWrap'>
        <v-btn @click="connect">
          Connect
        </v-btn>
        <v-btn @click="disconnect">
          Disconnect
        </v-btn>
      </div>
    </div>
    <!-- General data feed component -->
    <Feed v-bind:message="message" />
  </div>
</template>

<script>
// --- Main wrapper for the MQTT message feed --- //
import filterID from './filterID'
import Feed from './feed'

export default{
  data () {
    return {
      // --- Vue data object - https://vuejs.org/v2/guide/instance.html --- //
      message: '',
      logs: [],
      status: false,
      clientID: "clientID-" + parseInt(Math.random() * 100),
      host: process.env.MQTT_HOST,
      port: 9001,
      username: process.env.MQTT_USER,
      password: process.env.MQTT_PASSWORD
    }
  },
  components: {
    filterID,
    Feed
  },
  methods: {
    // --- Regular MQTT callback functions --- //
    connect () {
      this.client = new window.Paho.MQTT.Client(this.host, this.port, this.clientID);
      this.client.connect({      
        onSuccess: this.onConnect,
        useSSL: true, 
        userName : this.username,
        password : this.password
        }
      );
      this.client.onMessageArrived = this.onMessageArrived;
      this.client.onConnectionLost = this.onConnectionLost
    },
    onConnect(){
        // Once a connection has been made, make a subscription and send a message.
        this.status = true
        this.client.subscribe("muri/raw");
    },
    onConnectionLost() {
      this.status = 'disconnected'
    },
    disconnect(){
      this.client.disconnect()
      this.status = false
    },
    onMessageArrived(message) {
      // --- Assign MQTT raw message to message variable, used as a prop for child components --- //
      this.message = message.payloadString
    },
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 20px;
    position: relative;
  }
  #wrapper{
    position: relative;
    height: 105%;
  }
  #conFeedWrap{
    margin-top: 3%;
  }
  #live{
    position: fixed;
    top: 1.5%;
    left: 1.5%;
    z-index: 1001;
    background: transparent;
  }
  #live-icon{
    animation: shadow-pulse 3s infinite;
    border-radius: 50%;
  }

  @keyframes shadow-pulse
  {
    0% {
      box-shadow: 0 0 0 0px rgba(0, 0, 0, 0.2);
    }
    100% {
      box-shadow: 0 0 0 15px rgba(0, 0, 0, 0);
    }
  }
</style>