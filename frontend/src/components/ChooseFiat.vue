<template>
    <div class="converter-select">
        <span>Fiat</span>
        <v-select class="style-chooser" label="name" :options="fiats" v-model="selectedFiat"></v-select>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "ChooseFiat",
        props: ['resetField', 'lastFiat'],
        data() {
            return {
                fiats: [],
                selectedFiat: null
            }
        },
        watch: {
            selectedFiat: function () {
                this.$emit('selectedFiat', this.selectedFiat)
            },
            resetField: function () {
                this.selectedFiat = null
            },
        },
        methods: {
            getFiats() {
                axios.get('https://api.exchangeratesapi.io/latest?base=USD')
                .then(res => {
                    for (const [key, value] of Object.entries(res.data.rates)) {
                        this.fiats.push({
                            name : key,
                            value : value
                        })
                    }

                })
            },
        },
        created() {
            this.getFiats()
            this.selectedFiat = this.lastFiat
        }
    }
</script>

<style scoped>

</style>