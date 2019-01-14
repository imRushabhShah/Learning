<template>
  <div id="app">
    <h1>Welcome To LMS</h1>
    <hr>
    <router-link to="/">Home</router-link>
    <router-link to="/login">login</router-link>
    <hr/>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

</style>
