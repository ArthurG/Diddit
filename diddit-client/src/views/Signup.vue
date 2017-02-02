<template>
  <div>
    <TopNav></TopNav>
    <Signup></Signup>
    <Footer></Footer>
  </div>
</template>

<script>
import TopNav from './../components/TopNav'
import Signup from './../components/Signup'
import Footer from './../components/Footer'

export default {
  name: 'Home',
  components: {
    TopNav,
    Signup,
    Footer
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
