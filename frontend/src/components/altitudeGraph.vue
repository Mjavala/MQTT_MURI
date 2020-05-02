<template>
    <plotly :id='id' :layout="layout" :data="traces" :displayModeBar="false"/>
</template>

<script>
    import { Plotly } from "vue-plotly";

    export default {
        name: "SamplePlot",
        components: {
            Plotly
        },
        data() {
            return {
                traces: [{
                    x: [],
                    y: [],
                    mode: 'markers',
                    type: 'scatter'
                }],
                id: 'plotly-graph',
                layout: {
                    title:  "Sample plot",
                }
            }
        },
        methods: {
            addPoint: function(point) {
                this.traces[0].x.push(point['x']);
                this.traces[0].y.push(point['y']);
                console.log(this.traces[0].x)
                console.log(this.traces[0].y)
            },
            resetPlot: function() {
                this.clearData();
            },
            clearData: function() {
                this.traces[0]['x'] = [];
                this.traces[0]['y'] = [];
            },
        },
        created: function() {
            let self = this;
            let tm = setInterval(function () {
                let len = self.traces[0].x.length;
                self.addPoint({'x': len, 'y': Math.random()});
                if (len === 50) clearInterval(tm);
            }, 3000);
        }
    }
</script>