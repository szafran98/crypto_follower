<template>
    <div class="not-found-wrapper">
        <h1>404 <br> Not found!</h1>
        <a class="waves-effect waves-light btn" @click="backToPreviousAddress">Go back!</a>
        <div>
	        <svg height="345" width="500">
		        <polygon points="300,60 200, 60 20,340 480,340" class="triangle" />
            </svg>
        </div>
    </div>
</template>

<script>
    export default {
        name: "NotFound",
        methods: {
            backToPreviousAddress() {
                this.$router.push({ name: 'Home'})
            }
        }
    }
</script>

<style scoped>
    .triangle{
        fill: #394066;
        stroke: white;
        stroke-width: 8;
    }
    .not-found-wrapper{
        background-color: #ee6e73;
        height: 90%;
        margin-top: -50px;
        text-align: center;
    }
    .not-found-wrapper h1{
        width: 100%;
        padding-top: 10rem;
        color: #394066;
    }
    .not-found-wrapper div{
        width: 100%;
        position: absolute;
        margin-top: -45px;
    }
</style>