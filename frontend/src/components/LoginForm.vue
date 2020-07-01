<template>
    <div class="row login-form">
        <form class="col s12 m8 l6 offset-l3 offset-m2" @submit.prevent="login">
            <div class="row">
                <div class="input-field col s6">
                    <input id="id_username" type="text" class="validate" v-model="username">
                    <label for="id_username">Username</label>
                </div>
                <div class="input-field col s6">
                    <input id="id_password" type="password" class="validate" v-model="password">
                    <label for="id_password">Password</label>
                </div>
                <span v-if="errorMsg">{{ errorMsg }}</span>
            </div>
            <button class="waves-effect waves-light btn" type="submit">Login</button>
        </form>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        name: "LoginForm",
        data() {
            return {
                username: null,
                password: null,
                errorMsg: null
            }
        },
        methods: {
            login() {
                axios.post('http://127.0.0.1:8000/auth/', {
                    username: this.username,
                    password: this.password,
                })
                .then(res => {
                    localStorage.setItem('user-token', res.data.token)
                    this.$router.push({name: 'Crypto'})
                })
                .catch(() => {
                    this.errorMsg = 'Bad login or password!'
                })
            }
        }
    }
</script>

<style scoped>
    .login-form{
        background-color: #f8f8f8;
        border-radius: 5px;
        padding-top: 2rem;
    }
    .login-form span{
        font-family: Open-Sans, sans-serif;
        color: red;
    }
    .row button{
        margin-bottom: 20px;
    }
</style>