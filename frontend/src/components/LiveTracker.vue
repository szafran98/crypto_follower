<template>
    <div v-bind:class="{ 'add-margin' : extendPopular, 'del-margin': !extendPopular }">
        <div class="tracker-wrapper">
            <iframe src="https://widget.coinlib.io/widget?type=horizontal_v2&theme=light&pref_coin_id=1505&invert_hover=no" width="100%" height="36px" frameborder="0"></iframe>
        </div>
    </div>
</template>

<script>
    export default {
        name: "LiveTracker",
        props: ['extendPopular'],
    }
</script>

<style scoped>
    .tracker-wrapper{
        height:42px;
        background-color: #ee6e73;
        overflow:hidden;
        box-sizing: border-box;
        text-align: right;
        line-height:14px;
        block-size:38px;
        font-size: 12px;
        font-feature-settings: normal;
        box-shadow: inset 0 -20px 0 0 #56667F;
        padding:1px;
        width: 100%;
    }
    .add-margin{
        margin-top: 50px;
    }
    .del-margin{
        margin-top: 0;
    }
</style>