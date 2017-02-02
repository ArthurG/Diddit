<template>
  <div class="container">
    <h1>Signup</h1>
    <form>
      <input class="username" placeholder="Username"/>
      <input class="password" placeholder="Password"/>
      <input class="password-confirm" placeholder="Password Confirmation"/>
      <input class="email" placeholder="Email"/>
      <input text="email-agree" type="checkbox" name="agree-email" class="checkbox"/> <p> I wish to be included on the email list </p>
      <input text="terms-agree" type="checkbox" name="agree-terms" class="checkbox"/> <p>I agree to the terms and conditions </p>
      <button type="submit" v-on:click='submitForm'>Send</button>
    </form>

  </div>
</template>

<script>
export default {
  name: 'Signup'
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
  color: #d7d7d7;
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
