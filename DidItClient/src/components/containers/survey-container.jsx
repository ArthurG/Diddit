import React, { Component } from 'react';
import LoginService from '../../services/login-service.js';
import axios from 'axios';


var Router = require('react-router');


class SurveyContainer extends React.Component {

constructor(props) {
    super(props);
    this.state = {surveyNames : []};



    this.handleSurveyClick = this.handleSurveyClick.bind(this);
    this.backToHome = this.backToHome.bind(this);
      
 
  }

    componentDidMount() {

   axios.get('http://localhost:5000/survey?username='+this.props.params.username)       
         .then(response => {
           
           console.log(response.data);
           console.log(this.state.surveyName);
           console.log(this.state);

           this.setState({
               surveyNames: response.data
           });
         }
         );
    }

  componentWillUnmount() {
    
  }

  handleSurveyClick(surveyName) {

  Router.browserHistory.push('/details/' + this.props.params.username + '/' + surveyName);

  }

  backToHome(){
      Router.browserHistory.push('/profile/' + this.props.params.username);
  }


  render() {

 
var rows =[];
 this.state.surveyNames.forEach((surveyName) => {

        rows.push(<div className = "big-text list-group-item" id={surveyName} onClick={() => this.handleSurveyClick(surveyName)}> {surveyName} </div>)
     });

 return (
     <div> 
     <div className="container">
     <div> Your Surveys: </div>
     <div className="list-group">
     {rows}
     </div>
     </div>
     <button className="" onClick={() => this.backToHome()}> Back to Home! </button>
     </div>

    );
    
 }


}

export default SurveyContainer;