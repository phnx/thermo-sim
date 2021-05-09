<template>
    <div>
        <div class="columns">
            <div class="column">
                <JqxGauge ref="p1" @valueChanging="onValueChanging($event)"
                          :ranges="gaugeRanges200" :ticksMajor="gaugeTicksMajor" :value="0" 
                          :animationDuration="300" :max="200" :caption="{value: 'p1'}"
                          :width="gaugeWidth" :height="gaugeHeight" :labels="gaugeLabels200">
                </JqxGauge>
            </div>
            <div class="column">
                <JqxGauge ref="p2" @valueChanging="onValueChanging($event)"
                          :ranges="gaugeRanges200" :ticksMajor="gaugeTicksMajor" :value="0" 
                          :animationDuration="300" :max="200" :caption="{value: 'p2'}"
                          :width="gaugeWidth" :height="gaugeHeight" :labels="gaugeLabels200">
                </JqxGauge>
            </div>
            <div class="column">
                <JqxGauge ref="p3" @valueChanging="onValueChanging($event)"
                          :ranges="gaugeRanges100" :ticksMajor="gaugeTicksMajor" :value="0" 
                          :animationDuration="300" :max="100" :caption="{value: 'p3'}"
                          :width="gaugeWidth" :height="gaugeHeight" :labels="gaugeLabels100">
                </JqxGauge>
            </div>
            <div class="column">
                <JqxGauge ref="p34" @valueChanging="onValueChanging($event)"
                          :ranges="gaugeRanges100" :ticksMajor="gaugeTicksMajor" :value="0" 
                          :animationDuration="300" :max="100" :caption="{value: 'p34'}"
                          :width="gaugeWidth" :height="gaugeHeight" :labels="gaugeLabels100">
                </JqxGauge>
            </div>
            <div class="column">
                <JqxGauge ref="p4" @valueChanging="onValueChanging($event)"
                          :ranges="gaugeRanges100" :ticksMajor="gaugeTicksMajor" :value="0"
                          :animationDuration="300" :max="100" :caption="{value: 'Suction gauge'}"
                          :width="gaugeWidth" :height="gaugeHeight" :labels="gaugeLabels100">
                </JqxGauge>
            </div>
            <div class="column">
                <JqxGauge ref="heaterGauge" @valueChanging="onValueChanging($event)"
                          :ranges="gaugeRanges2000" :ticksMajor="gaugeTicksMajor" :value="0"
                          :animationDuration="300" :max="2000" :caption="{value: 'heater'}"
                          :width="gaugeWidth" :height="gaugeHeight" :labels="gaugeLabels2000">
                </JqxGauge>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <label for="twin">TWin</label>
                <input type="text" name="twin" v-model="twin-273.15" disabled>
            </div>
            <div class="column">
                <label for="twout">TWout</label>
                <input type="text" name="twout" v-model="twout-273.15" disabled>
            </div>
            <div class="column">
                <label for="t1">T1</label>
                <input type="text" name="t1" v-model="t1-273.15" disabled>
            </div>
            <div class="column">
                <label for="t2">T2</label>
                <input type="text" name="t2" v-model="t2-273.15" disabled>
            </div>
            <div class="column">
                <label for="t3">T3</label>
                <input type="text" name="t3" v-model="t3-273.15" disabled>
            </div>
            <div class="column">
                <label for="t4">T4</label>
                <input type="text" name="t4" v-model="t4-273.15" disabled>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <label for="linearWvalve">WValve</label>
                <JqxLinearGauge ref="linearWvalve" style="overflow: visible!important"
                        :width="120" :height="200" :min="0" :max="100" :orientation="'vertical'"
                        :ticksMajor="gaugeTicksMajorLinear100" :pointer="{ size: '5%' }" 
                        :colorScheme="'scheme05'" :labels="gaugeLabels100"
                        :ranges="gaugeRangesLinear100" :animationDuration="300">
                </JqxLinearGauge>
            </div>
            <div class="column">
                <label for="linearWeightScale">Weight Scale</label>
                <JqxLinearGauge ref="linearWeightScale" style="overflow: visible!important"
                        :width="120" :height="200" :min="0" :max="10" :orientation="'vertical'"
                        :ticksMajor="gaugeTicksMajorLinear10" :pointer="{ size: '5%' }" 
                        :colorScheme="'scheme05'" :labels="gaugeLabels10"
                        :ranges="gaugeRangesLinear10" :animationDuration="300">
                </JqxLinearGauge>
            </div>
            <div class="column">
                <label for="linearMcompout">MCompOut</label>
                <JqxLinearGauge ref="linearMcompout" style="overflow: visible!important"
                        :width="120" :height="200" :min="0" :max="0.05" :orientation="'vertical'"
                        :ticksMajor="gaugeTicksMajorLinear005" :pointer="{ size: '5%' }" 
                        :colorScheme="'scheme05'" :labels="gaugeLabels005"
                        :ranges="gaugeRangesLinear005" :animationDuration="300">
                </JqxLinearGauge>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <label for="wvalve">wvalve</label>
                <JqxKnob ref="wvalve" :value="30" :min="0" :max="100" :startAngle="120"
                     :endAngle="480" :snapToStep="true" :rotation="'clockwise'"
                     :marks="knobMarks100" :labels="knobLabels100" :progressBar="knobProgressBar" 
                     :pointer="knobPointer" :width="knobWidth" :height="knobHeight">
                </JqxKnob>
            </div>
            <div class="column">
                <label for="twin">Water Temperature</label>
                <input type="text" name="twin" v-model="twin" value="30">
            </div>
            <div class="column">
                <label for="dt">Time Step</label>
                <input type="text" name="dt" v-model="dt" value="20">
            </div>
            <div class="column">
                <label for="pump_rpm">pump_rpm</label>
                <input type="text" name="pump_rpm" v-model="pump_rpm" value="1500">
            </div>
            <div class="column">
                <label for="heater">heater</label>
                <JqxKnob ref="heater" :value="1000" :min="0" :max="2000" :startAngle="120"
                     :endAngle="480" :snapToStep="true" :rotation="'clockwise'"
                     :marks="knobMarks2000" :labels="knobLabels2000" :progressBar="knobProgressBar"
                     :pointer="knobPointer" :width="knobWidth" :height="knobHeight">
                </JqxKnob>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <div id="example">
                  <button v-on:click="updateCalculation">Iterate</button>
                </div>
            </div>
        </div>
        <div class="columns">
            <div class="column">
                <div>
                    <div class="field">
                        <label class="label">Result</label>
                        <pre id="calculation-result">
                            
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import JqxGauge from "jqwidgets-scripts/jqwidgets-vue/vue_jqxgauge.vue";
    import JqxLinearGauge from "jqwidgets-scripts/jqwidgets-vue/vue_jqxlineargauge.vue";
    import JqxKnob from "jqwidgets-scripts/jqwidgets-vue/vue_jqxknob.vue";

    export default {
        components: {
            JqxGauge,
            JqxLinearGauge,
            JqxKnob
        },
        data: function () {
            return {
                gaugeTicksMajor: { interval: 5, size: '5%' },
                gaugeWidth: "120px",
                gaugeHeight: "120px",
                knobWidth: "120px",
                knobHeight: "120px",
                gaugeRanges100: [
                    { startValue: 0, endValue: 25, style: { fill: '#4bb648', stroke: '#4bb648' }, endWidth: 2, startWidth: 1 },
                    { startValue: 25, endValue: 50, style: { fill: '#fbd109', stroke: '#fbd109' }, endWidth: 3, startWidth: 2 },
                    { startValue: 50, endValue: 75, style: { fill: '#ff8000', stroke: '#ff8000' }, endWidth: 4, startWidth: 3 },
                    { startValue: 75, endValue: 100, style: { fill: '#e02629', stroke: '#e02629' }, endWidth: 5, startWidth: 4 }
                ],
                gaugeRanges200: [
                    { startValue: 0, endValue: 50, style: { fill: '#4bb648', stroke: '#4bb648' }, endWidth: 2, startWidth: 1 },
                    { startValue: 50, endValue: 100, style: { fill: '#fbd109', stroke: '#fbd109' }, endWidth: 3, startWidth: 2 },
                    { startValue: 100, endValue: 150, style: { fill: '#ff8000', stroke: '#ff8000' }, endWidth: 4, startWidth: 3 },
                    { startValue: 150, endValue: 200, style: { fill: '#e02629', stroke: '#e02629' }, endWidth: 5, startWidth: 4 }
                ],
                gaugeRanges2000: [
                    { startValue: 0, endValue: 500, style: { fill: '#4bb648', stroke: '#4bb648' }, endWidth: 2, startWidth: 1 },
                    { startValue: 500, endValue: 1000, style: { fill: '#fbd109', stroke: '#fbd109' }, endWidth: 3, startWidth: 2 },
                    { startValue: 1000, endValue: 1500, style: { fill: '#ff8000', stroke: '#ff8000' }, endWidth: 4, startWidth: 3 },
                    { startValue: 1500, endValue: 2000, style: { fill: '#e02629', stroke: '#e02629' }, endWidth: 5, startWidth: 4 }
                ],
                gaugeLabels005: { interval: 0.01 },
                gaugeLabels10: { interval: 1 },
                gaugeLabels100: { interval: 20 },
                gaugeLabels200: { interval: 50 },
                gaugeLabels2000: { interval: 500 },
                gaugeTicksMajorLinear005: { size: '10%', interval: 0.01 },
                gaugeRangesLinear005: [
                    { startValue: 0, endValue: 0.02, style: { fill: '#FFF157', stroke: '#FFF157' } },
                    { startValue: 0.02, endValue: 0.04, style: { fill: '#FFA200', stroke: '#FFA200' } },
                    { startValue: 0.04, endValue: 0.05, style: { fill: '#FF4800', stroke: '#FF4800' } }
                ],
                gaugeTicksMajorLinear10: { size: '10%', interval: 1 },
                gaugeRangesLinear10: [
                    { startValue: 0, endValue: 3, style: { fill: '#FFF157', stroke: '#FFF157' } },
                    { startValue: 3, endValue: 6, style: { fill: '#FFA200', stroke: '#FFA200' } },
                    { startValue: 6, endValue: 10, style: { fill: '#FF4800', stroke: '#FF4800' } }
                ],
                gaugeTicksMajorLinear100: { size: '10%', interval: 10 },
                gaugeRangesLinear100: [
                    { startValue: 0, endValue: 33, style: { fill: '#FFF157', stroke: '#FFF157' } },
                    { startValue: 33, endValue: 66, style: { fill: '#FFA200', stroke: '#FFA200' } },
                    { startValue: 66, endValue: 100, style: { fill: '#FF4800', stroke: '#FF4800' } }
                ],
                knobMarks100: {
                    colorRemaining: { color: '#373636', border: '#373636' },
                    colorProgress: { color: '#373636', border: '#373636' },
                    type: 'line',
                    offset: '71%',
                    thickness: 1,
                    size: '6%',
                    majorSize: '9%',
                    majorInterval: 10
                },
                knobMarks2000: {
                    colorRemaining: { color: '#373636', border: '#373636' },
                    colorProgress: { color: '#373636', border: '#373636' },
                    type: 'line',
                    offset: '71%',
                    thickness: 1,
                    size: '6%',
                    majorSize: '9%',
                    majorInterval: 200
                },
                knobLabels100: {
                    offset: '88%',
                    step: 10
                },
                knobLabels2000: {
                    offset: '88%',
                    step: 200
                },
                knobProgressBar: {
                    size: '70%',
                    offset: '0%',
                    background: {
                        stroke: '#373636', strokeWidth: 1, fill: { color: '#a7a7a7', gradientType: "linear", gradientStops: [[0, 1], [50, 0.5], [100, 1]] }
                    }
                },
                knobPointer: {
                    type: 'circle', style: { fill: { color: '#a4a3a3', gradientType: "linear", gradientStops: [[0, 0.5], [50, 0.6], [100, 1]] }, stroke: '#333' },
                    size: '10%', offset: '50%'
                },

                // model input values
                pump_rpm: 1500,
                twin: 303,
                dt: 3,

                // derived values
                h1: null,
                p1: null,
                t1: null,
                h2: null,
                p2: null,
                t2: null,
                h3: null,
                p3: null,
                t3: null,
                p34: null,
                h4: null,
                p4: null,
                t4: null,

                mcompin: null,
                mcompout: null,
                hcompout: null,
                weight_scale: null,
                mcondin: null,
                mcondout: null,
                hcondout: null,
                twout: null,
                mwout: null,
                mexpain: null,
                mexpaout: null,
                hexpaout: null,
                mevapin: null,
                mevapout: null,
                hevapout: null,

            }
        },
        mounted: function () {

            // this.$refs.p1.value = 80;
            // this.$refs.p2.value = 40;
            // this.$refs.p3.value = 40;
            // this.$refs.p34.value = 40;
            // this.$refs.p4.value = 100;
            // this.$refs.heater.value = 150;

        },
        methods: {
            buildQuery: function() {
                let params = {
                    // input values
                    "pump_rpm": this.pump_rpm,
                    "twin": this.twin,
                    "wvalve": this.$refs.wvalve.value,
                    "heater": this.$refs.heater.value,
                    "dt": this.dt,
                };
                
                // derived values, if available
                if(this.h1 !== null) params.h1 = this.h1;
                if(this.p1 !== null) params.p1 = this.p1;
                if(this.t1 !== null) params.t1 = this.t1;
                if(this.h2 !== null) params.h2 = this.h2;
                if(this.p2 !== null) params.p2 = this.p2;
                if(this.t2 !== null) params.t2 = this.t2;
                if(this.h3 !== null) params.h3 = this.h3;
                if(this.p3 !== null) params.p3 = this.p3;
                if(this.t3 !== null) params.t3 = this.t3;
                if(this.p34 !== null) params.p34 = this.p34;
                if(this.h4 !== null) params.h4 = this.h4;
                if(this.p4 !== null) params.p4 = this.p4;
                if(this.t4 !== null) params.t4 = this.t4;

                if(this.mcompin !== null) params.mcompin = this.mcompin;
                if(this.mcompout !== null) params.mcompout = this.mcompout;
                if(this.hcompout !== null) params.hcompout = this.hcompout;
                if(this.weight_scale !== null) params.weight_scale = this.weight_scale;
                if(this.mcondin !== null) params.mcondin = this.mcondin;
                if(this.mcondout !== null) params.mcondout = this.mcondout;
                if(this.hcondout !== null) params.hcondout = this.hcondout;
                if(this.twout !== null) params.twout = this.twout;
                if(this.mwout !== null) params.mwout = this.mwout;
                if(this.mexpain !== null) params.mexpain = this.mexpain;
                if(this.mexpaout !== null) params.mexpaout = this.mexpaout;
                if(this.hexpaout !== null) params.hexpaout = this.hexpaout;
                if(this.mevapin !== null) params.mevapin = this.mevapin;
                if(this.mevapout !== null) params.mevapout = this.mevapout;
                if(this.hevapout !== null) params.hevapout = this.hevapout;

                return Object.keys(params)
                             .map(k => encodeURIComponent(k) + '=' + encodeURIComponent(params[k]))
                             .join('&');
            },
            onValueChanging: function (event) {
                // console.log(this.value);
            },
            updateCalculation: function(event) {

                let url = '/refrigeration?' + this.buildQuery();

                fetch(url)
                  .then(data => data.json())
                  .then((data) => {
                    console.log(data);
                    document.getElementById('calculation-result').innerHTML = JSON.stringify(data, null, 2)

                    // storing data
                    this.h1 = data.h1;
                    this.p1 = data.p1;
                    this.t1 = data.t1;
                    this.h2 = data.h2;
                    this.p2 = data.p2;
                    this.t2 = data.t2;
                    this.h3 = data.h3;
                    this.p3 = data.p3;
                    this.t3 = data.t3;
                    this.p34 = data.p34;
                    this.h4 = data.h4;
                    this.p4 = data.p4;
                    this.t4 = data.t4;

                    this.mcompin = data.mcompin;
                    this.mcompout = data.mcompout;
                    this.hcompout = data.hcompout;
                    this.weight_scale = data.weight_scale;
                    this.mcondin = data.mcondin;
                    this.mcondout = data.mcondout;
                    this.hcondout = data.hcondout;
                    this.twout = data.twout;
                    this.mwout = data.mwout;
                    this.mexpain = data.mexpain;
                    this.mexpaout = data.mexpaout;
                    this.hexpaout = data.hexpaout;
                    this.mevapin = data.mevapin;
                    this.mevapout = data.mevapout;
                    this.hevapout = data.hevapout;

                    // update for display
                    this.$refs.p1.value = this.p1 *14.50377/100000-14.6959;
                    this.$refs.p2.value = this.p2 *14.50377/100000-14.6959;
                    this.$refs.p3.value = this.p3 *14.50377/100000-14.6959;
                    this.$refs.p34.value = this.p34 *14.50377/100000-14.6959;
                    this.$refs.p4.value = this.p4 *14.50377/100000-14.6959;
                    this.$refs.heaterGauge.value = this.$refs.heater.value;
                    this.$refs.linearWvalve.value = this.$refs.wvalve.value;
                    this.$refs.linearWeightScale.value = this.weight_scale;
                    this.$refs.linearMcompout.value = this.mcompout;

                  }).catch(function (error) {
                    console.log(error);
                  });
            },
        }
    }
</script>

<style>
</style>