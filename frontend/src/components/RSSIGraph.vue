<template>
    <div class="wrapper">
        <Plotly  class="graph" :data="data" :layout="layout" :display-mode-bar="false"></Plotly>
    </div>
</template>

<script>
import { Plotly } from 'vue-plotly'

export default {
    name: 'altitudeGraph',
  components: {
    Plotly
  },
  props: [
      'idList',
      'filteredAltitude'
  ],
  watch: {
        filteredAltitude(newVal){
            let objKey = Object.keys(newVal)
            let objKeyMap = Object.keys(newVal).map((k) => newVal[k]);
            this.altitude = objKeyMap[0] / 1000
            this.sensorList.add(objKey)
            this.sensor = objKey[0]
            if (!(this.listOfDevices === undefined)){
                this.updateTrace(this.sensor, this.listOfDevices)
            }
        },
        idList(newVal, oldVal){
            this.listOfDevices = newVal
        
            if (newVal.length > oldVal.length){
                //a new device has been found, we need to now add a trace for altitude
                console.log('a new device has been found, we need to now add a trace for altitude')
                //this.addTrace()                
            }
            if (newVal.length < oldVal.length){
                console.log(' a device has been lost, we need to alert the user & remove trace')
                // a device has been lost, we need to alert the user & remove trace
            }
            if (newVal.length === oldVal.length){

                for (let id of newVal){
                    if (id === this.sensor){
                        this.updateTrace(this.sensor, newVal)
                    }
                }
                console.log(JSON.stringify((this.data[0].y)))
            }
        }
  },
  data () {
    return {
        altitude: Number,
        sensorList: new Set(),
        sensor: '',
        data:[{
            x: [],
            y: [],
            mode:"lines",
            type: 'scatter',
            line: {color: '#DF56F1'}

        }],
        layout: {
            yaxis: {
                title: {
                    text: 'Altitude',
                },
                rangemode: 'nonnegative'
            },
            xaxis: {
                rangemode: 'nonnegative'
            },
            height: 450,
            }
        }
    },
    methods: {
        addTrace(){
            const time = new Date()
            const trace = {
                y: [this.altitude],
                x: [time],
                mode: 'lines',
                type: 'line',
                line: {color: '#DF58F1'}
            }
            this.data.push(trace)
        },
        addPoint (point) {
            this.data[0].x.push(point['x']);
            this.data[0].y.push(point['y']);
        },
        updateTrace(device, listOfDevices){
            let self = this
            const time = new Date()
            self.data[0].y.push(this.altitude)
            self.data[0].x.push([time])
            for (const [sensor] of listOfDevices.entries()){
                if (sensor === device){
                    console.log('trace on...')
                    //const index = i + 1
                }
            }
        }
    }
}
</script>

<style scoped>
    .wrapper {
        display: inline-block;
        position: absolute;
        top: 0;
        width: 45vw;
    }
</style>