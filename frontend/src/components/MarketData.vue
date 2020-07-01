<template>
    <div class="row data-wrapper">
        <div class="col s12 m3">
            <div class="card-panel">
                <span>Market cap</span>
                <span>{{ marketData.market_cap_usd | currency}}</span>
            </div>
        </div>
        <div class="col s12 m3">
            <div class="card-panel">
                <span>Number of cryptocurrencies</span>
                <span>{{ marketData.cryptocurrencies_number }}</span>
            </div>
        </div>
        <div class="col s12 m3">
            <div class="card-panel">
                <span>Last 24h change</span>
                <span v-bind:class="{ lower: marketData.market_cap_change_24h < 0, higher: marketData.market_cap_change_24h > 0}">
                    {{ marketData.market_cap_change_24h}}%</span>
            </div>
        </div>
        <div class="col s12 m3">
            <div class="card-panel">
                <span>Last updated</span>
                <span>{{ marketData.last_updated | moment("MMMM Do YYYY, h:mm:ss a") }}</span>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "MarketData",
        data() {
            return {
                marketData: {}
            }
        },
        methods: {
            getMarketOverview() {
                axios.get('https://api.coinpaprika.com/v1/global')
                .then(res => {
                    this.marketData = {
                        market_cap_usd : res.data.market_cap_usd,
                        cryptocurrencies_number : res.data.cryptocurrencies_number,
                        market_cap_change_24h : res.data.market_cap_change_24h,
                        last_updated : res.data.last_updated
                    }
                })
            }
        },
        beforeMount() {
            this.getMarketOverview()
        }
    }
</script>

<style scoped>
    .card-panel{
        display: grid;
        text-align: center;
    }
    .data-wrapper{
        position: fixed;
        z-index: 1000;
        width:100%;
        background-color: #ee6e73;
    }

</style>