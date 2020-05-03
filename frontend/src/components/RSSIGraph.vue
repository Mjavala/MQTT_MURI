<template>
  <div id="rssi-graph">
        <rsssiReactivity :chart="chart" />
  </div>
</template>

<script>
import rsssiReactivity from './RSSIReactivity'

export default {
    components: {
        rsssiReactivity
    },
    props: [
      'idList', 'filteredRSSI'
    ],
    watch: {
      filteredRSSI(newVal){
        let objKey = Object.keys(newVal)
        this.currentDevice = objKey[0]
        let objKeyMap = Object.keys(newVal).map((k) => newVal[k]);
        this.rssi = objKeyMap[0]
        this.addData(this.rssi)
      },
      idList(newVal, oldVal){
        if (newVal.length === oldVal.length){
          // current device message
          this.findTrace(newVal)
        }
        if (newVal.length > oldVal.length){
          // new device detected, add trace
          this.addTrace()
          this.findTrace(newVal)
        }
      }
    },
    data() {
    return {
      rssi: Number,
      currentDevice: '',
      chart: {
        uuid: "1233",
        traces: [
          {
            y: [],
            x: [new Date()],
            type: 'scatter',
            mode: 'lines+markers',
            connectgaps: true
          }
        ],
        layout: {
          height: 325,
          title: 'RSSI vs Time',
          xaxis: {
            tickmode: 'auto',
            gridcolor: '#bdbdbd',
            gridwidth: 1,
            title: 'time (s)',
            titlefont: {
              size: 11
            },
            tickfont:{
              size: 10
            }
          },
          yaxis: {
            title: 'RSSI',
            titlefont: {
              size: 11
            },
            gridwidth: 1,
            gridcolor: '#bdbdbd',
          }
        }
      }
    }
    },
    methods: {
      addData (rssi, traceIndex) {
        this.chart.layout.datarevision = new Date().getTime();
        this.chart.traces[traceIndex].y.push(rssi);
        let time = new Date()
        this.chart.traces[0].x.push(time);
        if (this.chart.traces[traceIndex].x.length === 10){
          this.chart.traces[traceIndex].x.shift()
          this.chart.traces[traceIndex].y.shift()
        }
      },
      findTrace (deviceList) {
        for (const [i, id] of deviceList.entries()){
          if (id === this.currentDevice){
            this.addData(this.rssi, i)
          }
        }
      },
    }
  }
</script>

<style scoped>
    #rssi-graph{
        display: inline-block;
        position: absolute;
        top: 41%;
    }
</style>