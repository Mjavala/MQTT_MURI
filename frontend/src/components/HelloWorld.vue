<template>
  <div id="app">
    <v-btn icon depressed rounded id="live" v-if=" this.status === 'Connected'">
      <v-icon id="live-icon" color="#76FF03">mdi-wifi</v-icon>
    </v-btn>
    <idFilter v-bind:message="this.message"/>   
    <Graphs id="graph1" />
    <Graphs id="graph2"/>
    <Graphs id="graph3"/>
    <div id='conFeedWrap'>
      <v-btn @click="connect">
        Connect
      </v-btn>
      <v-btn @click="disconnect">
        Disconnect
      </v-btn>
      <Feed v-bind:message="this.message" />
    </div>
  </div>
</template>

<script>
import Feed from './feed'
import Graphs from './graphs'
import idFilter from './filter'


export default{
  data () {
    return {
      message: '',
      logs: [],
      status: '',
      clientID: "clientID-" + parseInt(Math.random() * 100),
      host: 'irisslive.net',
      port: 9001,
      username: 'muri',
      password: 'demo2020'
    }
  },
  components: {
    Feed,
    Graphs,
    idFilter
  },
  methods: {
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
        console.log("Connected");
        this.status = 'Connected'
        this.client.subscribe("muri/#");
        console.log('subscribed')
    },
    onConnectionLost() {
      console.log('disconnected')
      this.status = 'disconnected'
    },
    disconnect(){
      this.client.disconnect()
    },
    onMessageArrived(message) {
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
  #conFeedWrap{
    margin-top: 3% !important;
  }
  #graph2{
    top: 25vh;
  }
  #graph3{
    top: 49vh;
  }

  #live{
    position: fixed;
    top: 1.5%;
    left: 1.5%;
    z-index: 10;
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