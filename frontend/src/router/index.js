import Vue from 'vue'
import VueRouter from 'vue-router'
import Vue2Filters from 'vue2-filters'
import vSelect from 'vue-select'
import VueMoment from 'vue-moment'
import Home from '../views/Home.vue'
import Followed from "../views/Followed";
import Crypto from "../views/Crypto";
import Popular from "../views/Popular";
import Converter from "../views/Converter";
import NotFound from "../views/NotFound";

Vue.use(VueRouter)
Vue.use(Vue2Filters)
Vue.use(VueMoment)
Vue.component('v-select', vSelect)


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/followed',
        name: 'Followed',
        component: Followed,
        meta: {
            title: 'Followed'
        }
    },
    {
        path: '/cryptocurrencies',
        name: 'Crypto',
        component: Crypto,
        meta: {
            title: 'Cryptocurrencies'
        }
    },
    {
        path: '/popular',
        name: 'Popular',
        component: Popular,
        meta: {
            title: 'Popular Charts'
        }
    },
    {
        path: '/converter',
        name: 'Converter',
        component: Converter,
        meta: {
            title: 'Converter'
        }
    },
    {
        path: '*',
        name: 'NotFound',
        component: NotFound,
        meta: {
            title: 'Not Found'
        }
    }

]

const router = new VueRouter({
    routes,
    mode: 'history'
})

export default router
