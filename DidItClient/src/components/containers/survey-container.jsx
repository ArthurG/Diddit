import React, { Component } from 'react';
import LoginService from '../../services/login-service.js';
import axios from 'axios';

class SurveyContainer extends React.Component {

constructor(props) {
    super(props);
    this.state = {surveyNames : ['poop', 'peep', 'deep','poop', 'peep', 'deep','poop', 'peep', 'deep','poop', 'peep', 'deep']};

    this.handleSurveyClick = this.handleSurveyClick.bind(this);
  }

/*
ES6

Use an arrow function:

return (
  <th value={column} onClick={() => this.handleSort(column)}>{column}</th>
);


*/


  handleSurveyClick(event, surveyName) {

      console.log(surveyName);
   // alert('Your username is: ' + this.state.username);

  /*
    axios.post('http://localhost:5000/login', {
        username: this.state.username,
        password: this.state.password
    }).then(function(response) {
           // this.state.response = response;
            alert(response.data);
        })
        .catch(function(error) {
          //  this.state.error = error;
            alert(error);
        });

*/
    axios.get()


   /* LoginService.login(this.state.username, this.state.password)
        .then(function(response) {
         //   this.state.response = response;
            alert(response.data);
        })
        .catch(function(error) {
           // this.state.error = error;
            alert(error);
       });

    
    event.preventDefault();
    */
  }


  render() {
 
/*
var indents = [];
for (var i = 0; i < this.props.level; i++) {
  indents.push(<span className='indent' key={i}></span>);
}
return (
   <div>
    {indents}
    "Some text value"
   </div>
);

{onClick=> {() => this.handleSurveyClick(surveyName[i])}}
*/

  /* 

var rows = [];
for (var i=0; i < this.state.surveyName.length; i++) {
    rows.push(
        <div id = {this.state.surveyName[i]} >            
        <label>{this.state.surveyName[i]}</label>
        fook
        </div>
    );
}
*/
 
var rows =[];
 this.state.surveyNames.forEach((surveyName) => {

        rows.push(<div className = "big-text list-group-item" id={surveyName} onClick={() => this.handleSurveyClick(this, surveyName)}> {surveyName } </div>)
     });

 return (
     <div className="container">
     <div> Your Surveys: </div>
     <div className="list-group">
     {rows}
     </div>
     </div>
    );
    
 }


}

export default SurveyContainer;