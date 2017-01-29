<template>
  <div id="app">
    <img src="./assets/logo.png">
    <SurveyResponseList></SurveyResponseList>
  </div>
</template>

<script>
import SurveyResponseList from './components/SurveyResponseList'

export default {
  name: 'app',
  components: {
    SurveyResponseList
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
  margin-top: 60px;
}
</style>
