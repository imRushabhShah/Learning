// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router';
// import Message from './message'
import Users from './Users.vue';
import Home from './Home.vue';
import VueResource from 'vue-resource'

Vue.use(VueRouter);
Vue.use(VueResource);


// Vue.http.headers.common['Access-Control-Request-Method'] = '*'

const routes = [
    {path: '/login', component: Users},
    {path: '/', component: Home}
];

const router = new VueRouter({
    routes,
    mode: 'history'
});

// Vue.component('app-message',Message)

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
});
