<template>
  <div class="container">
    <h1>
      Get In Touch
    </h1>
    <form class="form-horizontal">
      <input v-model='email' class='email' placeholder="Email">
      <input v-model='subject' class='subject' placeholder="Subject">
      <textarea v-model='message' class='message' placeholder="Message"/>
      <button type="submit" v-on:click='submitForm'>Send</button>
    </form>
  </div>
</template>

<script>
export default {
  data: {
    email: '',
    subject: '',
    message: ''
  },
  name: 'ContactBanner',
  methods: {
    submitForm: function (e) {
      e.preventDefault()
      console.log(this.email)
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.container{
  border: 2px solid orange;
}

input, textarea{
  font-size: 1.2em;
  padding: 0.5em;
  width: 100%;
  margin: 0.5em 0;
  height: 2.2em;
  background-color: #d7d7d7;
  border: 0px;
}

button{
  float: right;
  padding: 0.5em 2em;
  background-color: #efefef;
  border: None;

}

.message{
  min-height: 10em;
  vertical-align: top;
}


</style>
