<template>
    <div>
        <Loader v-if="show"></loader>
        <NavBar/>
        <v-content>
        <HelloWorld/>
        </v-content>
    </div>
</template>

<script>
import HelloWorld from './HelloWorld'
import NavBar from './navbar'
import Loader from './loader'

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
