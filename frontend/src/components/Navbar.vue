<template>
    <div class="navbar-fixed">
        <nav class="nav-extended" v-bind:style="navStyle">
            <div class="nav-wrapper">
                <a class="brand-logo">
                    <router-link :to="{ name: 'Home' }">Crypto Follower</router-link>
                </a>
                <ul id="nav-mobile" class="right hide-on-med-and-down" v-if="token">
                    <li class="input-field" style="height: auto">
                        <input id="search" type="search" required
                               @keyup="$emit('searchedCrypto', $event.target.value)">
                        <label for="search" class="label-icon">
                            <i class="material-icons">search</i>
                        </label>
                    </li>
                    <li id="converter" ref="converter"
                        @click="$emit('calcAnim') && (activeEl = $refs.converter) && (extendPopular = false) & (navStyle = 'height: inherit')"
                        :class="{ active : activeEl === $refs.converter }">
                        <router-link :to="{ name: 'Converter' }">Converter</router-link>
                    </li>
                    <li id="marketData" ref="marketData" @click="activeEl = $refs.marketData"
                        :class="{ active : activeEl === $refs.marketData }">
                        <a @click="$emit('showMarketData')">Market data</a>
                    </li>
                    <li id="popular" ref="popular"
                        @click="(activeEl = $refs.popular) && (extendPopular = true) & (navStyle = 'height: auto')"
                        :class="{ active : activeEl === $refs.popular }">
                        <router-link :to="{ name: 'Popular' }">Popular charts</router-link>
                    </li>
                    <li id="cryptocurrencies" ref="cryptocurrencies"
                        @click="(activeEl = $refs.cryptocurrencies) && (extendPopular = false) & (navStyle = 'height: inherit')"
                        :class="{ active : activeEl === $refs.cryptocurrencies }">
                        <router-link :to="{ name: 'Crypto' }">Cryptocurrencies</router-link>
                    </li>
                    <li id="followed" ref="followed"
                        @click="(activeEl = $refs.followed) && (extendPopular = false) & (navStyle = 'height: inherit')"
                        :class="{ active : activeEl === $refs.followed }">
                        <router-link :to="{ name: 'Followed' }">Followed</router-link>
                    </li>
                    <li @click="extendPopular = false">
                        <a @click="logout">Logout</a>
                    </li>
                </ul>
            </div>
            <div class="nav-content" v-if="extendPopular">
                <ul class="tabs tabs-transparent">
                    <li class="tab" @click="$emit('choosedChart', 'bitcoin')">
                        <a>Bitcoin</a>
                    </li>
                    <li class="tab" @click="$emit('choosedChart', 'ethereum')">
                        <a>Ethereum</a>
                    </li>
                    <li class="tab" @click="$emit('choosedChart', 'ripple')">
                        <a>Ripple</a>
                    </li>
                    <li class="tab" @click="$emit('choosedChart', 'btcash')">
                        <a>Bitcoin Cash</a>
                    </li>
                    <li class="tab" @click="$emit('choosedChart', 'litecoin')">
                        <a>Litecoin</a>
                    </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>

    export default {
        name: "Navbar",
        props: ['token'],
        data() {
            return {
                extendPopular: false,
                navStyle: 'height: inherit',
                activeEl: null,
            }
        },
        watch: {
            extendPopular: function () {
                    this.$emit('extendPopular', this.extendPopular)
            }
        },
        methods: {
            logout() {
                localStorage.removeItem('user-token')
                this.$emit('logout')
                this.$router.push({name: 'Home'})
            },
        },
        created() {
            if(this.$router.currentRoute.name === 'Popular') {
                this.extendPopular = true
            }
        }
    }
</script>

<style scoped>
    .brand-logo{
        padding-left: 10px;
        font-family: 'Indie Flower', cursive;
    }
    .nav-content{
        background-color: #ee6e73;
    }
</style>