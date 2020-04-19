<template>
  <div class="map">
    <l-map 
      v-bind="mapConfig"
    >
    <l-tile-layer 
      v-bind="mapRender"
    />
      <l-marker
        :key="index"
        v-bind:id="item"
        v-for="(item, index) in this.listOfIds"
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
  props: {
    idList: Array,
    ID: String , 
    lat: Number, 
    lon: Number
  },
  watch: {
    message(newVal){
      this.payload = newVal
      this.filter(newVal)
    },
  },
  data() {
    return {
      payload: '',
      markerlat: 0,
      markerlon: 0,
      listOfIds: this.idList,
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
    check(){
      this.messageOBJ = JSON.parse(this.payload)
      console.log(this.messageOBJ.frame_data['GPS Lat'])
    }
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