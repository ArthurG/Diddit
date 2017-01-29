<template>
  <div class="SurveyResponseList">
    <h2>GEEE</h2>
    <ul>
      <li v-for="question in questions" v-on:click="clickQuestion(question)">
        {{question.key}} 
        <div v-for="answer in question.val" v-if="question.show">
          {{answer}}
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      questions: [],
      msg: 'Welcome to Your Vue.js App'
    }
  },
  methods: {
    clickQuestion: function(e, f){
      console.log(e);
      e.show=!e.show;
    }
  },
  created: function(){
    this.$http.get('http://localhost:5000/answers?username=Harman&surveyname=Test1').then(
      response => {
        var q = [];
        var question = JSON.parse(response.data);
        var keys = Object.keys(question);
        keys.forEach(key=>
            q.push({"key": key, "val": question[key], "show": true})
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
