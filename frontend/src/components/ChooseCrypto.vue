<template>
    <div class="converter-select">
        <span>Crypto</span>
        <v-select class="style-chooser" label="name" :options="cryptocurrencies" v-model="selectedCoin"></v-select>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "ChooseCrypto",
        props: ['resetField', 'lastCrypto'],
        data() {
            return {
                cryptocurrencies: [],
                selectedCoin: null
            }
        },

        watch: {
            selectedCoin: function () {
                this.$emit('selectedCoin', this.selectedCoin)
            },
            resetField: function () {
                this.selectedCoin = null
            },
        },
        methods: {
            getCoins() {
                axios.get('https://api.coinpaprika.com/v1/ticker')
                .then(res => {
                    res.data.forEach(coin => {
                        this.cryptocurrencies.push({
                            symbol : coin.symbol,
                            name : coin.name,
                            price_usd : parseFloat(coin.price_usd)
                        })
                    })
                })
            },
        },
        created() {
            this.getCoins()
            this.selectedCoin = this.lastCrypto
        }
    }
</script>

<style scoped>

</style>