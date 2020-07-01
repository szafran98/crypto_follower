<template>
    <div>
        <loading :active.sync="isLoading"
        :is-full-page="fullPage"
        :loader="loaderStyle"></loading>
        <div class="row">
            <div class="col s12 m6 l4" v-for="(crypto, index) in filterCrypto" :key="index">
                <div class="card blue-grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title crypto-title">{{ crypto.symbol }}</span>
                        <p>Price: {{ crypto.price_usd }} USD</p>
                        <p>Volume: {{ crypto.volume_24h_usd }} USD</p>
                        <p v-bind:class="{lower : crypto.change24h, higher: !crypto.change24h }">24h change: {{ crypto.percent_change_24h }} %</p>
                        <p v-bind:class="{lower : crypto.change7d, higher: !crypto.change7d }">7d change: {{ crypto.percent_change_7d }} %</p>
                        <a class="waves-effect waves-green btn-floating small red" v-if="token"
                           @click="addToFollowed(crypto.id, crypto.name)">
                            <i class="material-icons">add</i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import Loading from 'vue-loading-overlay'
    import 'vue-loading-overlay/dist/vue-loading.css'

    export default {
        name: "Crypto",
        components: {
            Loading
        },
        props: ['token', 'searchedCrypto'],
        data() {
            return {
                cryptocurrencies: [],
                isLoading: false,
                fullPage: true,
                loaderStyle: 'bars'
            }
        },
        computed: {
            filterCrypto() {
                if(this.searchedCrypto) {
                    return this.cryptocurrencies.filter(crypto => {
                        return crypto.symbol.startsWith(this.searchedCrypto.toUpperCase())
                    })
                } else {
                    return this.cryptocurrencies
                }
            }
        },
        methods: {
            getCoins() {
                this.isLoading = true
                axios.get('https://api.coinpaprika.com/v1/ticker')
                .then(res => {
                    res.data.forEach(crypto => {
                        crypto.price_usd = parseFloat(crypto.price_usd).toFixed(2)
                        crypto.volume_24h_usd = parseFloat(crypto.volume_24h_usd).toFixed(2)
                        crypto.change24h = parseFloat(crypto.percent_change_24h) < 0
                        crypto.change7d = parseFloat(crypto.percent_change_7d) < 0
                        this.cryptocurrencies.push(crypto)
                    })
                    this.token ? this.getFollowed() : this.isLoading = false

                })
                .catch(err => console.log(err))

            },
            addToFollowed(id, name) {
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                }
                let postData = {
                    name: name,
                    coin_id: id,
                    token: this.token
                }
                this.cryptocurrencies = this.cryptocurrencies.filter(crypto => {
                    return crypto.id !== id
                })

                axios.post('http://127.0.0.1:8000/api/followed/', postData, axiosConfig)
                .catch(err => console.log(err))
            },
            getFollowed() {
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                }
                let postData = {
                    token: this.token
                }
                axios.post('http://127.0.0.1:8000/api/followed/get_followed_by_user/', postData, axiosConfig)
                .then(res => {
                    res.data.result.forEach(crypto => {
                        this.cryptocurrencies = this.cryptocurrencies.filter(item => {
                            return item.id !== crypto.coin_id
                        })
                    })
                    this.isLoading = false
                })
            }
        },
        mounted() {
            this.getCoins()
        }
    }
</script>

<style>
    .crypto-title{
        font-size: 24px;
        text-align: center;
    }
    .lower{
        color: maroon;

    }
    .higher{
       color: darkgreen;
    }
    .search-input{
        max-width: 300px;
    }
    .search-container{
        width: 100vw;
        display: flex;
        flex-flow: column wrap;
        align-items: center;
    }
    .card-content a{
        position: absolute;
        right: 5%;
    }
</style>