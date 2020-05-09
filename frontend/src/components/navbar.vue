<template>    
    <v-app-bar
        app
        color="primary"
        dark
        id="nav"
    >
        <v-img id="iriss-logo" max-height="100" max-width="225" src="../assets/iriss_logo.png" />
    </v-app-bar>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    #nav{
        position: fixed;
        z-index: 1000;
    }
    #iriss-logo{
        margin-left: 5%;
    }
</style>