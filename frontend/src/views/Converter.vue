<template>
    <div class="converter-root">
        <div class="container">
            <div class="row">
                <div class="col s12 m8 l6 offset-m2 offset-l3">
                    <transition name="slide-fade">
                        <div class="card-panel" v-if="calcAnim">
                            <span>Ammount</span>
                            <input type="number" v-model="ammount">
                            <transition name="component-fade" mode="out-in">
                                <component :is="fromComponent"
                                           v-on:selectedFiat="selectedFiat = $event"
                                           v-on:selectedCoin="selectedCoin = $event"
                                           v-bind:resetField="resetField"
                                           v-bind:lastCrypto="lastCrypto"
                                           v-bind:lastFiat="lastFiat"/>
                            </transition>
                            <i class="material-icons medium arrow">expand_more</i>
                            <transition name="component-fade" mode="out-in">
                                <component :is="toComponent"
                                           v-on:selectedFiat="selectedFiat = $event"
                                           v-on:selectedCoin="selectedCoin = $event"
                                           v-bind:resetField="resetField"
                                           v-bind:lastCrypto="lastCrypto"
                                           v-bind:lastFiat="lastFiat"/>
                            </transition>
                            <a class="waves-effect waves-light btn-small" @click="resetFields">
                                <i class="material-icons left">refresh</i>
                                Reset
                            </a>
                            <a class="waves-effect waves-light btn-small" @click="swapComponents">
                                <i class="material-icons left">swap_vert</i>
                                Swap
                            </a>
                            <h4>{{ convert()}}</h4>
                        </div>
                    </transition>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import ChooseCrypto from "../components/ChooseCrypto"
    import ChooseFiat from "../components/ChooseFiat"
    import 'vue-select/dist/vue-select.css'


    export default {
        name: "Converter",
        components: {
            ChooseCrypto,
            ChooseFiat
        },
        data() {
            return {
                resetField: false,
                ammount: 0,
                selectedCoin: null,
                selectedFiat: null,
                fromComponent: ChooseCrypto,
                toComponent: ChooseFiat,
                calcAnim: false,
                lastCrypto: this.selectedCoin,
                lastFiat: this.selectedFiat
            }
        },
        methods: {
            convert() {
                try {
                    if(this.fromComponent === ChooseCrypto) {
                        let returnValue = (this.selectedCoin && this.selectedFiat) !== undefined ? (this.ammount * parseFloat(this.selectedCoin.price_usd) * this.selectedFiat.value) : 0
                        return `~${this.$options.filters.currency(returnValue, '')} ${this.selectedFiat.name}`
                    } else {
                        let returnValue = (this.selectedCoin && this.selectedFiat) !== undefined ? (this.ammount / parseFloat(this.selectedCoin.price_usd) / this.selectedFiat.value) : 0
                        return `~${this.$options.filters.currency(returnValue, '', 8)} ${this.selectedCoin.symbol}`
                    }
                }
                catch (e) {
                    return 0
                }
            },
            resetFields() {
                this.ammount = 0
                this.selectedCoin = null
                this.selectedFiat = null
                this.resetField = !this.resetField
            },
            swapComponents() {
                let fromComp = this.fromComponent
                this.fromComponent = this.toComponent
                this.toComponent = fromComp
            },
            loadingAnimTimeout() {
                setTimeout(() => {
                    this.calcAnim = true
                }, 100)
            }
        },
        created() {
            this.loadingAnimTimeout()
        },
        updated() {
            this.lastCrypto = this.selectedCoin
            this.lastFiat = this.selectedFiat
        }
    }
</script>

<style>
    .style-chooser{
        margin-bottom: 20px;
    }
    .converter-select .style-chooser .vs__search{
        height: auto;
        appearance: none;
        line-height: 1.4;
        font-size: 1em;
        border: 1px solid transparent !important;
        border-left: none;
        outline: none;
        margin: 4px 0 0 !important;
        background: none !important;
        box-shadow: none !important;
        width: 0;
        max-width: 100%;
        flex-grow: 1;
        z-index: 1;
        margin-bottom: 50px;
    }
    .style-chooser .vs__dropdown-toggle,
    .style-chooser .vs__dropdown-menu {
        background: #ee6e73;
        border: none;
        color: #394066;
        text-transform: lowercase;
        font-variant: small-caps;
    }

    .style-chooser .vs__clear,
    .style-chooser .vs__open-indicator {
        fill: #394066;
    }
    .component-fade-enter-active, .component-fade-leave-active {
        transition: opacity .5s ease;
    }
    .component-fade-enter, .component-fade-leave-to
    {
        opacity: 0;
    }
    .slide-fade-enter-active {
        transition: all .5s ease;
    }
    .slide-fade-leave-active {
        transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
    }
    .slide-fade-enter, .slide-fade-leave-to
    {
        transform: translateX(10px);
        opacity: 0;
    }
    .converter-root{
        width: 100vw;
        height: 87%;
        background-color: #ee6e73
    }
    .converter-root .container{
        background-color: #394066;
        padding-top: 1%;
        height: 100%
    }
    .card-panel span{
        font-family: Open-Sans, sans-serif;
    }
    .arrow{
        text-align: center;
        width: 100%;
    }
    .card-panel a{
        width: 100%;
        background-color: #394066;
        margin-bottom: 20px;
    }
    .card-panel a i{
        margin-right: -10%;
    }
    .card-panel h4{
        text-align: center;
    }
</style>