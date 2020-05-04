<template>
  <v-app>
    <Loader v-if="show"></loader>
    <NavBar/>
    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import NavBar from './components/navbar'
import Loader from './components/loader'

export default {

  components: {
    HelloWorld,
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
