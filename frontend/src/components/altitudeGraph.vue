<template>
  <div id="altitude-graph">
        <altitudeReactivity :chart="chart" />
  </div>
</template>

<script>
import altitudeReactivity from './altitudeReactivity.vue'
export default {
    components: {
        altitudeReactivity
    },
    props: [
      'idList', 'filteredAltitude'
    ],
    watch: {
      filteredAltitude(newVal){
        //let objKey = Object.keys(newVal)
        let objKeyMap = Object.keys(newVal).map((k) => newVal[k]);
        let altitude = objKeyMap[0] / 1000
        this.addData(altitude)
      }
    },
    data() {
    return {
      altitude: Number,
      chart: {
        uuid: "123",
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
          title: 'Altitude vs Time Graph',
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
            title: 'Altitude (m)',
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
      addData: function(altitude) {
        this.chart.layout.datarevision = new Date().getTime();
        this.chart.traces[0].y.push(altitude);
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
        top: -3%;
        width: 45vw;
        height: 20vh;
    }

</style>