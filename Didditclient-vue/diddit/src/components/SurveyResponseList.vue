<template>
  <div class="SurveyResponseList">
    <ul>
      <li v-for="question in questions"> {{question.key}} <p v-for="answer in question.val"> {{answer}}</p></li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'hello',
  questions: [],
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
  },
  created: function(){
    this.$http.get('http://localhost:5000/answers?username=Harman&surveyname=Test1').then(
      response => {
        var q = [];
        var question = JSON.parse(response.data);
        console.log(Object.keys(question));
        var keys = Object.keys(question);
        keys.forEach(key=>
          q.push({"key": key, "val": question[key]})
        );
        this.questions = q;
        console.log(this.questions);

      }, response=>{
        console.log("err");
      }
    );
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
