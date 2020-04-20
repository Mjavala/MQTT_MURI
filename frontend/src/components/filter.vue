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
  props: ['message'],
  components: {
    MapUI
  },
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
        deviceList: [],
        listOfIds: new Set(), //Set() -  list of unique items
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
        this.listOfIds.add(this.messageOBJ['ADDR_FROM'])
        this.deviceList = Array.from(this.listOfIds)
        this.filterMessage(this.deviceList, this.messageOBJ)
    },
    latLng(lat,long){
      return L.latLng(lat,long)
    },
    filterMessage(sensors, message){
      if (sensors.lenght === 0){
        console.log('No devices detected...')
      }
      if (sensors.lenght <= 1){
        console.log('Single device detected...')
      }
      if (sensors.length > 1){
        console.log('Mulitple devices detected...')
      }
      if (sensors.length >= Object.keys(this.masterSet).length){
        for (let sensor of sensors) {
            if (message['ADDR_FROM'] === sensor){
              if (!(sensor in this.masterSet)){
                this.latLngDataCleanup(message.frame_data['GPS Lat'], message.frame_data['GPS Lon'])
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
              this.latLngDataCleanup(message.frame_data['GPS Lat'], message.frame_data['GPS Lon'])
              const lat = this.lat
              const lon = this.lon
              this.masterSet[sensor] = L.latLng(lat, lon)
              break
            }
          }
        //for (let sensor in sensors){
          //console.log('updating lat long...')
          //console.l
          //masterSet[sensor] = L.latLng(this.lat, this.lon)
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
