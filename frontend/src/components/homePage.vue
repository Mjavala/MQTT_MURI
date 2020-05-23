<template>
    <!-- Home page component, brings in the MQTT receiver, loader, and navbar components -->
    <div>
        <Loader v-if="show"></loader>
        <NavBar/>
        <v-content>
        <Receiver />
        </v-content>
    </div>
</template>

<script>
import Receiver from './mqttReceiver'
import NavBar from './navbar'
import Loader from './loader'

export default {

  components: {
    Receiver,
    NavBar,
    Loader
  },
  data () {
    return {
      show: true
    }
  },
  mounted() {
    this.showToggle()
  },
  methods: {
    showToggle(){
      setTimeout(() => {
        this.show = false
      }, 1500)
    }
  }
};
</script>

<style scoped>
  #v-content{
    padding: 0px;
  }
  #app{
    margin: 0 !important;
  }
</style>
