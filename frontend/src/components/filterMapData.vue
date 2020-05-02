<template>
  <div>
    <MapUI :masterSet="masterSet" />
  </div>

</template>

<script>
import L from 'leaflet';
import MapUI from './map'
export default {
  
  name: 'mapUI',
  props: ['id', 'message'],
  components: {
    MapUI
  },
  watch: {
    message(newVal) {
      this.payload = newVal
      this.addIdAndFilterMessage(this.payload)
    },
    id(newVal){
      this.deviceList = newVal
    }
  },
  data() {
    return {
        payload: [],
        messageOBJ: [],
        filteredMessageObj: {},
        masterSet: [],
        lat: Number,
        lon: Number,
        key: '',
        ID: '',
    }
  },
  methods: {
    addIdAndFilterMessage(message){
        this.messageOBJ = JSON.parse(message)
        // console.log(this.messageOBJ)
        // Initial Condition
        if (!(this.deviceList === undefined)){
          this.filterMessage(this.deviceList, this.messageOBJ)
        }
    },
    latLng(lat,long){
      return L.latLng(lat,long)
    },
    filterMessage(sensors, message){
      if (sensors.length === 0){
        console.log('No devices detected...')
      }
      if (sensors.length <= 1){
        console.log('Single device detected...')
      }
      if (sensors.length > 1){
        console.log('Mulitple devices detected...')
      }
      if (sensors.length >= Object.keys(this.masterSet).length){
        for (let sensor of sensors) {
          if (message.data['ADDR_FROM'] === sensor){
            if (!(sensor in this.masterSet)){
              this.latLngDataCleanup(message.data.frame_data['gps_lat'], message.data.frame_data['gps_lon'])
              const lat = this.lat
              const lon = this.lon
              this.filteredMessageObj = {
                [sensor]: L.latLng(lat, lon)
              }
              this.masterSet.push(this.filteredMessageObj)
              break
            }
          }
        }
      }
      if (sensors.length == Object.keys(this.masterSet).length){
        for (let sensor of sensors){
          if (message['ADDR_FROM'] === sensor){
            this.latLngDataCleanup(message.data.frame_data['GPS Lat'], message.data.frame_data['GPS Lon'])
            const lat = this.lat
            const lon = this.lon
            this.masterSet[sensor] = L.latLng(lat, lon)
            break
          }
        }
      }
    },
    latLngDataCleanup(latitude, longitude){
      latitude = (latitude / 10000000).toFixed(1)
      longitude = (longitude / 10000000).toFixed(1)
      this.lat = latitude
      this.lon = longitude
    }
  }
}
</script>
