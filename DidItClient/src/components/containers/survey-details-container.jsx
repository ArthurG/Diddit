import React, { Component } from 'react';
import LoginService from '../../services/login-service.js';
import axios from 'axios';

var Router = require('react-router');


class SurveyDetailsContainer extends React.Component {

constructor(props) {
    super(props);

    this.surveyAnswerRate = this.surveyAnswerRate.bind(this);
    this.state = {surveyQuestionsAndAssociatedAnswers: [] , enabled: {}};
    this.toggle = this.toggle.bind(this);

    this.backToSurveys = this.backToSurveys.bind(this);
    this.backToHome = this.backToHome.bind(this);
      
};


 backToSurveys(){
      Router.browserHistory.push('/view/' + this.props.params.username);
  }

 backToHome(){
      Router.browserHistory.push('/profile/' + this.props.params.username);
  }



surveyAnswerRate(user, questionName, answer, rate){
  console.log(this.state.surveyQuestionsAndAssociatedAnswers[0]);
}

    componentDidMount() {


axios
  .get('http://localhost:5000/answers?username=' + this.props.params.username + '&surveyname=' + this.props.params.surveyname)
  .then(response => {
    this.setState({surveyQuestionsAndAssociatedAnswers: response.data});

    console.log(this.state.surveyQuestionsAndAssociatedAnswers);
    for (var key in this.state.surveyQuestionsAndAssociatedAnswers) {
      this.setState({
        enabled: key
      });
    }

         });


    }

  componentWillUnmount() {
    
  }

  toggle(event, key){
        
       console.log(event);

      this.setState({
        enabled: key
      });

    console.log(this.state.enabled);

  }




  render() {
 
    var rows = [];
    var hash = {};
    

   

    for(var key in this.state.surveyQuestionsAndAssociatedAnswers) {


         var rowz =[];
    
    this.state.surveyQuestionsAndAssociatedAnswers[key].forEach((answer) => {
        rowz.push(<div className = "big-text list-group-item" id={answer}> {answer } </div>)
     });



      rows.push(<div className="questionInSurvey" ref={key} onClick={() =>  this.toggle(this)}> 
      
      {key} 
      {key == this.state.enabled ? <div> {rowz} </div> : null}
      </div>);
  //    this.state.surveyQuestionsAndAssociatedAnswers[key].forEach((answer) => {
  //      console.log(key);
  //      rows.push[answer];
     // )};
    }

    console.log("THIS IS ROWS" + rows);


 return (
    <div>
     <div className="container">
     <div> Your Survey Questions: </div>
     <div> {rows} </div>
     <div className="list-group">
     </div>
        <button className="" onClick={() => this.backToHome()}> Back to Home! </button>
        <button className="" onClick={() => this.backToSurveys()}> Back to Surveys! </button>
     </div>
     </div>
    );
    
 }


}

export default SurveyDetailsContainer;