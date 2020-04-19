<template>
    <Map :idList="this.listOfIds" :ID="this.ID" :lat="this.lat" :lon="this.lon" />
</template>

<script>

export default {
  name: 'mapUI',
  props: ['message'],
  watch: {
    message(newVal) {
      this.payload = newVal
      this.addIdAndFilterMessage(this.payload)
    }
  },
  data() {
    return {
        payload: [],
        messageOBJ: [],
        listOfIds: new Set(),
        lat: 0,
        lon: 0,
        ID: ''
    }
  },
  methods: {
    latLng(lat,long){
      return L.latLng(lat,long)
    },
    addToIdList(message){
        this.messageOBJ = JSON.parse(message)
        this.listOfIds.add(this.messageOBJ['ADDR_FROM'])
        this.filterMessage(this.listOfIds, this.messageOBJ)
    },
    filterMessage(ids, message){
      if (this.listOfIds.size <= 1){
        console.log('Mulitple devices detected...')
      }
      if (this.listOfIds.size > 1){
        console.log('Mulitple devices detected...')
      }
      ids.forEach(id => {
          if (this.messageOBJ['ADDR_FROM'] === id){
              latLngDataCleanup(messageOBJ.frame_data['GPS Lat'], messageOBJ.frame_data['GPS lon'])
              this.ID = messageOBJ['ADDR_FROM']
              break
          } else {
            continue
          }
      })
    },
    latLngDataCleanup(latitude, longitude){
      this.lat = (latitude / 10000000).toFixed(1)
      this.lon = (longitude / 10000000).toFixed(1)
    }
  }
}
</script>
