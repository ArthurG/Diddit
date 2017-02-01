<template>
  <div>
    <TopNav></TopNav>
    <MainBanner></MainBanner>
    <AnalyticsBanner></AnalyticsBanner>
    <ContactBanner></ContactBanner>
    <Footer></Footer>
  </div>
</template>

<script>
import TopNav from './../components/TopNav'
import MainBanner from './../components/MainBanner'
import AnalyticsBanner from './../components/AnalyticsBanner'
import ContactBanner from './../components/ContactBanner'
import Footer from './../components/Footer'

export default {
  name: 'Home',
  components: {
    TopNav,
    MainBanner,
    AnalyticsBanner,
    ContactBanner,
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
