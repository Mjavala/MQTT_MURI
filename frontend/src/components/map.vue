<template>
  <div class="map">
    <l-map 
      v-bind="mapConfig"
    >
    <l-tile-layer 
      v-bind="mapRender"
    />
      <l-marker 
        :key="marker.id"
        v-for="marker in markers"
        :lat-lng="marker.latlng"
      >
        <l-icon v-bind="iconConfig" />
      </l-marker>
    </l-map>
  </div>
</template>

<script>
//TODO: Test render of markers / popups / prop data
import {LMap, LTileLayer, LMarker, LIcon} from 'vue2-leaflet'
import L from 'leaflet';
import Pin from '../assets/pin.png'

export default {
  name: 'mapUI',
  components: { 
    LMap, 
    LTileLayer, 
    LMarker,
    LIcon,
  },
  props: [
    'masterSet'
  ],
  watch: {
    masterSet(newVal){
      let objKeys = []
      let objKeysMap = []
      let markersArray = []
        
      for (let sensor of newVal){
          let objKey = Object.keys(sensor)
          let objKeyMap = Object.keys(sensor).map((k) => sensor[k]);
          
          objKeys.push(objKey)
          objKeysMap.push(objKeyMap)
      }
      //console.log(objKeys.values())
      for (const value of objKeysMap.values()){
        //console.log(value[0])
        //console.log(value[0].lat, value[0].lng)
        markersArray.push({
          id: 'test',
          latlng: L.latLng(value[0].lat, value[0].lng)})
      }
      this.markers = markersArray
      //console.log(this.markers)
    }
  },
  data() {
    return {
      marker: '',
      listOfIds: [],
      markers: [{
        id: 1,
        latlng: L.latLng(39, -105)
      }],
      messageOBJ: {},
      mapConfig: {
        zoom: 7,
        minZoom: 2,
        center: L.latLng(39, -105),
        Bounds: [
          [-90, -180],
          [90, 180]
        ],
        maxBounds: [
          [-90, -180],
          [90, 180]
        ],
      },
      iconConfig: {
        'icon-url': Pin,
        'icon-size': [30,30],
      },
      mapRender: {
        url:'https://maps.heigit.org/openmapsurfer/tiles/roads/webmercator/{z}/{x}/{y}.png',
        attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      },
    }
  },
  methods: {
    latLng(lat,long){
      return L.latLng(lat,long)
    },
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.map{
  height: 70vh;
  width: 50vw;
  display: inherit;
  padding: 1% 2% 2% 1%;
}
.leaflet-container a.leaflet-popup-close-button{
  color: #121212;
  width: 15px;
  padding: 0;
}
.leaflet-popup-content-wrapper, .leaflet-popup-tip{
  background: #121212;
}
.leaflet-control-attribution {
  display: none;
}
.leaflet-marker-icon{
  opacity: .85;
}
.leaflet-control-zoom {
  padding: 2%;
  border: none !important;
}
.leaflet-control-zoom-in{
  background: white !important;
  color: #121212 !important;
}
.leaflet-control-zoom-out{
  background: white !important;
  color: #121212 !important;
}
</style>