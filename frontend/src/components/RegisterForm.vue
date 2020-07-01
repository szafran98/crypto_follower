<template>
     <div class="row register-form">
        <form class="col s12 m10 l8 offset-m1 offset-l2" @submit.prevent="checkPasswords" v-if="!registered">
            <div class="row">
                <div class="input-field col s6">
                    <input id="id_email" type="email" class="validate" v-model="email">
                    <label for="id_email">Email</label>
                </div>
                <div class="input-field col s6">
                    <input id="id_username" type="text" class="validate" v-model="username">
                    <label for="id_username">Username</label>
                </div>
            </div>
            <div class="row">
                <div class="input-field col s6">
                    <input id="id_password" type="password" class="validate" v-model="password">
                    <label for="id_password">Password</label>
                </div>
                <div class="input-field col s6">
                    <input id="id_password1" type="password" class="validate" v-model="password1">
                    <label for="id_password1">Repeat password</label>
                </div>
                <span v-if="errorMsg">{{ errorMsg }}</span>
            </div>
            <button class="waves-effect waves-light btn" type="submit">Register</button>
        </form>
        <h4 v-if="registered">Registration completed, now you can login!</h4>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        name: "RegisterForm",
        data() {
            return {
                email: null,
                username: null,
                password: null,
                password1: null,
                errorMsg: null,
                registered: false
            }
        },
        methods: {
            checkPasswords() {
                this.password !== this.password1 ? this.errorMsg = 'Passwords not match!' : this.register()
            },
            register() {
                axios.post('http://127.0.0.1:8000/api/users/', {
                    email: this.email,
                    username: this.username,
                    password: this.password
                })
                .then(() => {
                    this.registered = true
                    this.$emit('showLoginForm')
                    alert('Registration completed, now you can login.')
                })
                .catch(() => {
                    this.errorMsg = 'User with this email or username already exists!'
                })
            }
        }
    }
</script>

<style scoped>
    .register-form{
        background-color: #f8f8f8;
        border-radius: 5px;
        padding-top: 2rem
    }
    .row button{
        margin-bottom: 20px;
    }
    .register-form span{
        font-family: Open-Sans, sans-serif;
        color: red;
    }
    .register-form h4{
        margin-top: -1rem;
    }
</style>