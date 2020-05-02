<template>
  <div id="altitude-graph">
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
        //let objKey = Object.keys(newVal)
        let objKeyMap = Object.keys(newVal).map((k) => newVal[k]);
        let rssi = objKeyMap[0]
        this.addData(rssi)
      }
    },
    data() {
    return {
      chart: {
        uuid: "1233",
        traces: [
          {
            y: [],
            x: [],
            type: 'scatter',
            mode: 'lines+markers',
            connectgaps: true
          }
        ],
        layout: {
          title: 'RSSI Graph',
          xaxis: {
            tickmode: 'auto',
            gridcolor: '#bdbdbd',
            gridwidth: 1,
            title: 'time (s)',
            titlefont: {
              size: 16
            }
          },
          yaxis: {
            title: 'RSSI',
            titlefont: {
              size: 16
            },
            gridwidth: 1,
            gridcolor: '#bdbdbd',
          }
        }
      }
    }
    },
    methods: {
      addData: function(rssi) {
        this.chart.layout.datarevision = new Date().getTime();
        this.chart.traces[0].y.push(rssi);
        let time = new Date()
        this.chart.traces[0].x.push(time);
        if (this.chart.traces[0].x.length === 10){
          this.chart.traces[0].x.shift()
          this.chart.traces[0].y.shift()
        }
    }
  }
}
</script>

<style scoped>
    #altitude-graph{
        display: inline-block;
        padding: 1%;
        position: absolute;
        top: 35.5%;
        width: 45vw;
        height: 20vh;
    }

</style>