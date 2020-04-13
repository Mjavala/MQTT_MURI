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
  name: 'App',

  components: {
    HelloWorld,
    NavBar
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>
  #v-content{
    padding: 0px;
  }
</style>
