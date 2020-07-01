<template>
    <div class="popular-root">
        <div class="container">
            <section v-if="choosedChart === 'bitcoin'">
                <div class="card-panel">
                    <div class="chart-wrapper">
                        <iframe src="https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=859&pref_coin_id=1505"></iframe>
                    </div>
                </div>
            </section>
            <section v-else-if="choosedChart === 'ethereum'">
                <div class="card-panel">
                    <div class="chart-wrapper">
                        <iframe src="https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=145&pref_coin_id=1505"></iframe>
                    </div>
                </div>
            </section>
            <section v-else-if="choosedChart === 'ripple'">
                <div class="card-panel">
                    <div class="chart-wrapper">
                        <iframe src="https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=619&pref_coin_id=1505"></iframe>
                    </div>
                </div>
            </section>
            <section v-else-if="choosedChart === 'btcash'">
                <div class="card-panel">
                    <div class="chart-wrapper">
                        <iframe src="https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=157&pref_coin_id=1505"></iframe>
                    </div>
                </div>
            </section>
            <section v-else-if="choosedChart === 'litecoin'">
                <div class="card-panel">
                    <div class="chart-wrapper">
                        <iframe src="https://widget.coinlib.io/widget?type=chart&theme=light&coin_id=359&pref_coin_id=1505"></iframe>
                    </div>
                </div>
            </section>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Details",
        props: ['choosedChart']
    }
</script>

<style scoped>
    .chart-wrapper{
        height:440px;
        overflow:hidden;
    }
    h2{
        font-family: 'Raleway', sans-serif;
        font-weight: bold;
        color: white;
    }
    section{
        text-align: center;
        border: 1px solid #ee6e73;
    }
    .popular-root{
        background-color: #ee6e73;
        padding-top: 1rem;
        height: 81%;
    }
    iframe{
        border: 0;
        width: 100%;
        height: 536px;
    }

</style>