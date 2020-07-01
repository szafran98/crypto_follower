<template>
    <div class="home">
        <div class="container">
            <h1>Crypto Follower</h1>
            <ul>
                <li>
                    <div class="collapsible-header">
                        <i class="material-icons">access_time</i>
                        Follow your favourite cryptocurrencies. Save your valuable time.
                    </div>
                </li>
                <li>
                    <div class="collapsible-header">
                        <i class="material-icons">accessibility</i>
                        Easy and intuitive. Even a child can make it.
                    </div>
                </li>
                <li>
                    <div class="collapsible-header">
                        <i class="material-icons">data_usage</i>
                        All data in one place. No more need to surf in various sites.
                    </div>
                </li>
            </ul>
            <div class="row">
                <div class="col s12 m12">
                    <div class="card-panel">
                        <a class="waves-effect waves-light btn" @click="showRegisterForm = !showRegisterForm">Register</a>
                        <a class="waves-effect waves-light btn" @click="showLoginForm = !showLoginForm">Login</a>
                        <LoginForm v-if="showLoginForm"/>
                        <RegisterForm v-if="showRegisterForm" v-on:showLoginForm="showLoginForm = true" />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import LoginForm from "../components/LoginForm"
    import RegisterForm from "../components/RegisterForm";

    export default {
        name: 'Home',
        props: ['token'],
        components: {
            LoginForm,
            RegisterForm
        },
        watch: {
            showLoginForm: function () {
                if(this.showLoginForm) this.showRegisterForm = false
            },
            showRegisterForm: function () {
                if(this.showRegisterForm) this.showLoginForm = false
            }
        },
        data() {
            return {
                showLoginForm: false,
                showRegisterForm: false
            }
        },
        created() {
            if(this.token) {
                this.$router.push({ name: 'Crypto'})
            }
        }
    }
</script>

<style scoped>
    .home{
        background-color: #394066;
        height: inherit;
        padding-top: 5px;
    }
    .container{
        text-align: center;
        background-color: #ee6e73;
    }
    .container .row{
        margin-bottom: -2rem;
    }
    .home .container{
        border: 1px solid #ee6e73;
        box-shadow: 0 2px 2px 0 rgba(0,0,0,0.14), 0 3px 1px -2px rgba(0,0,0,0.12), 0 1px 5px 0 rgba(0,0,0,0.2);
    }
    .card-panel{
        display: grid;
        background-color: #ee6e73;
        margin: 0;
    }
    .card-panel .btn{
        width: 200px;
        margin: 5px auto;
    }
    .collapsible-header{
        cursor: default;
    }
    h1 {
        font-family: Raleway, sans-serif;
        color: #f8f8f8;
    }
    div{
        font-family: Open-Sans, sans-serif;
    }

</style>
