<template>
    <Map v-bind="filteredMessageObj" />
</template>

<script>
import L from 'leaflet';
export default {
  
  name: 'mapUI',
  props: ['message'],
  watch: {
    message(newVal) {
      this.payload = newVal
      this.addIdAndFilterMessage(this.payload)
    },
    masterSet(){
      console.log('set changed...')
    },
    filteredMessageObj(){
      console.log('new message object created')
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
    arrayPush(messageLite){
      this.masterSet.push(messageLite)
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
      console.log(sensors.length)
      if (sensors.lenght > Object.keys(this.masterSet).length){
        for (let sensor of sensors) {
          console.log(sensor)
            if (message['ADDR_FROM'] === sensor){
              if (!(sensor in this.masterSet)){
                console.log('hello world2')
                this.latLngDataCleanup(message.frame_data['GPS Lat'], message.frame_data['GPS Lon'])
                const lat = this.lat
                const lon = this.lon
                this.filteredMessageObj = {
                  [sensor]: L.latLng(lat, lon)
                }
                this.masterSet.push(this.filteredMessageObj)
                console.log('first mark succesfull')
              }
              break
          }
        }
      }
      if (sensors.lenght === Object.keys(this.masterSet).length){
        console.log('lalallaa')
        //for (let sensor in sensors){
          //console.log('updating lat long...')
          //console.l
          //masterSet[sensor] = L.latLng(this.lat, this.lon)
      }
      console.log('first message logged')
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
