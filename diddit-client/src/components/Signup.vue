<template>
  <div class="container">
    <h1>Signup</h1>
    <form>
      <input class="username" placeholder="Username" v-model="username" />
      <input class="password" placeholder="Password" v-model='password' />
      <input class="password-confirm" placeholder="Password Confirmation" v-model='passwordconfirm'/>
      <input class="email" placeholder="Email" v-model="email"/>
      <input text="email-agree" type="checkbox" name="agree-email" class="checkbox" v-model='emailagree' /> <p> I wish to be included on the email list </p>
      <input text="terms-agree" type="checkbox" name="agree-terms" class="checkbox" v-model='termsagree' /> <p>I agree to the terms and conditions </p>
      <button type="submit" v-on:click='submitForm'>Send</button>
    </form>

  </div>
</template>

<script>
export default {
  name: 'Signup',
  data () {
    return {
      username: '',
      password: '',
      passwordconfirm: '',
      email: '',
      emailagree: '',
      termsagree: ''
    }
  },
  methods: {
    submitForm: function (event) {
      // TODO: Validation of form before submission
      console.log('submitting')
      this.$http.post('http://localhost:5000/signup', {username: this.username, password: this.password, email: this.email, termsagree: this.termsagree, emailagree: this.emailagree}).then(response => {
        console.log(response.status)
        console.log(response.statusText)
      }, response => {
        console.log('failure')
      })
      event.preventDefault()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.container{
  border: 1px solid red;
  text-align: left;
  padding: 2em;
}

input{
  width: 100%;
  font-size: 1.2em;
  padding: 0.5em;
  width: 100%;
  margin: 0.5em 0;
  height: 2.2em;
  background-color: #d7d7d7;
  color: #white;
  border: 0px;
}

input.checkbox{
  margin: 0;
  height: 1.5em;
  width: auto;
}

button{
  float: right;
  padding: 0.5em 2em;
  background-color: #efefef;
  border: None;
}

</style>
