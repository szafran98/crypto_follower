<template>
     <div>
         <loading :active.sync="isLoading"
        :is-full-page="fullPage"
        :loader="loaderStyle"></loading>
        <div class="row">
            <h3 v-if="cryptocurrencies.length < 1">No followed cryptocurrencies</h3>
            <div class="col s12 m6 l4" v-for="(crypto, index) in filterCrypto" :key="index">
                <div class="card blue-grey darken-1">
                    <div class="card-content white-text">
                        <span class="card-title crypto-title">{{ crypto.symbol }}</span>
                        <p>Price: {{ crypto.price_usd }} USD</p>
                        <p>Volume: {{ crypto.volume_24h_usd }} USD</p>
                        <p v-bind:class="{lower : crypto.change24h, higher: !crypto.change24h }">24h change: {{ crypto.percent_change_24h }} %</p>
                        <p v-bind:class="{lower : crypto.change7d, higher: !crypto.change7d }">7d change: {{ crypto.percent_change_7d }} %</p>
                        <a class="btn-floating small waves-effect waves-light red"
                           @click="removeFromFollowed(crypto.id)">
                            <i class="material-icons">delete</i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import Loading from 'vue-loading-overlay'
    import 'vue-loading-overlay/dist/vue-loading.css'

    export default {
        name: "Followed",
        props: ['token', 'searchedCrypto'],
        components: {
          Loading
        },
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
            getCoin(coin_id) {
                axios.get(`https://api.coinpaprika.com/v1/ticker/${coin_id}`)
                    .then(res => {
                        let response = res.data
                        response.price_usd = parseFloat(response.price_usd).toFixed(2)
                        response.volume_24h_usd = parseFloat(response.volume_24h_usd).toFixed(2)
                        response.change24h = parseFloat(response.percent_change_24h) < 0
                        response.change7d = parseFloat(response.percent_change_7d) < 0
                        this.cryptocurrencies.push(response)
                    })
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
                };
                axios.post('http://127.0.0.1:8000/api/followed/get_followed_by_user/', postData, axiosConfig)
                .then(res => {
                    this.isLoading = true
                    let i = 1
                    let animationLength = res.data.result.length
                    res.data.result.forEach(crypto => {
                        setTimeout(() => {
                            this.getCoin(crypto.coin_id)
                        }, 105 * i)
                        i++

                    })
                    setTimeout(() => {
                        this.isLoading = false
                    }, 105 * animationLength)

                })
            },
            removeFromFollowed(coin_id) {
                let axiosConfig = {
                    headers: {
                        'Authorization': 'Token ' + this.token
                    }
                }
                let postData = {
                    token: this.token,
                    coin_id: coin_id
                };
                axios.post('http://127.0.0.1:8000/api/followed/delete_followed_by_user/', postData, axiosConfig)
                .then(() => {
                    this.cryptocurrencies = this.cryptocurrencies.filter(crypto => {
                        return crypto.id !== coin_id
                    })
                }
            )}
        },
        created() {
            this.getFollowed()
        }
    }
</script>

<style scoped>
    h3{
        font-family: Raleway, sans-serif;
        width: 100%;
        text-align: center
    }
</style>