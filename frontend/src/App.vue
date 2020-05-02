<template>
  <v-app>
    <NavBar/>
    <v-content>
      <HelloWorld/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import NavBar from './components/navbar'

export default {

  components: {
    HelloWorld,
    NavBar,
  }
};
</script>

<style scoped>
  #v-content{
    padding: 0px;
  }
</style>
