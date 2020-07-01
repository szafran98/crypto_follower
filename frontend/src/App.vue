<template>
    <div id="app">
        <div id="nav">
            <Navbar v-bind:token="token"
                    v-on:extendPopular="setExtendPopular"
                    v-on:showMarketData="showMarketData = !showMarketData"
                    v-on:searchedCrypto="searchedCrypto = $event"
                    v-on:choosedChart="setChoosedChart"
                    v-on:logout="token = null" />
        </div>
        <transition name="fade">
            <MarketData v-if="showMarketData"/>
        </transition>
        <LiveTracker v-bind:extendPopular="extendPopular" />
        <router-view v-bind:token="token"
                     v-bind:choosedChart="choosedChart"
                     v-bind:searchedCrypto="searchedCrypto"
        />
    </div>
</template>

<script>
    import Navbar from "./components/Navbar";
    import MarketData from "./components/MarketData";
    import LiveTracker from "./components/LiveTracker";
    export default {
        name: 'App',
        components: {
            Navbar,
            MarketData,
            LiveTracker
        },
        data() {
            return {
                token: localStorage.getItem('user-token') || null,
                showMarketData: false,
                searchedCrypto: null,
                extendPopular: false,
                choosedChart: 'bitcoin'
            }
        },
        watch: {
            '$route' (to, from) {
                document.title = to.meta.title || 'Crypto Follower'
            },
            immediate: true
        },
        methods: {
            setExtendPopular(extendPopularValue) {
                this.extendPopular = extendPopularValue
            },
            setChoosedChart(choosedChartValue) {
                this.choosedChart = choosedChartValue
            }
        },
        updated() {
            this.token = localStorage.getItem('user-token') || null
        }
    }
</script>

<style>
    .fade-enter-active, .fade-leave-active {
        transition: opacity .7s;
    }
    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
        opacity: 0;
    }
    body, html {
        height: 100%;
    }
    #app{
        height: inherit;
    }
</style>
