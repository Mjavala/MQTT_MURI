<template>
  <div>
    <testGraph :idList="idList" :filteredAltitude="filteredAltitude" />
  </div>
</template>

<script>
import testGraph from './testGraph'

export default {

  props: ['id', 'message'],
  components: {
    testGraph
  },
  watch: {
    message(newVal) {
      this.payload = newVal
      this.filterMessage(this.payload)
    },
    id(newVal){
      this.idList = newVal
    }
  },
  data() {
    return {
        payload: [],
        messageOBJ: [],
        idList: [],
        filteredAltitude: {},
        filteredRSSI: {},
        altitude: {},
        rssi: Number
    }
  },
  methods: {
    filterMessage(message){
        this.messageOBJ = JSON.parse(message)
        // console.log(this.messageOBJ)
        this.assignDataObjects(this.messageOBJ)
    },
    assignDataObjects(message){
        const id = message.data['ADDR_FROM']

        this.filteredAltitude = {
            [id] : message.data.frame_data['gps_alt']
            }

        this.filteredRSSI = {
            [id] : message['RSSI_RX']
            }
        }
    }
}
</script>