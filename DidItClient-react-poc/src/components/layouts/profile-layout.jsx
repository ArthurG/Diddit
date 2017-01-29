import React, { Component } from 'react';
import axios from 'axios';

import {Link} from 'react-router'
class ProfileLayout extends React.Component {
  
constructor(props) {
    super(props);
    this.state = {};

    this.handleSubmit = this.handleSubmit.bind(this);
  }



  handleSubmit(event) {
 
    
  
    axios.post('http://localhost:5000/login', {
        username: this.state.username,
        password: this.state.password,
        storename: this.state.storename,
        email: this.state.email,
        location: this.state.location

    }).then(function(response) {
           // this.state.response = response;
            alert(response.data);
        })
        .catch(function(error) {
          //  this.state.error = error;
            alert(error);
        });

  }


  render() {
 
    return (
      <div>
      <span> Welcome to your Surveys {this.props.params.username}! </span>
      <div class = "navbar navbar-inverse navbar-fixed-left">
        <li><Link to={"/new/" + this.props.params.username}>Create New Survey</Link> </li> 
        <li><Link to={"/delete/" + this.props.params.username}>Delete Old Surveys </Link> </li> 
       <li><Link to={"/view/" + this.props.params.username}>View Survey Responses </Link> </li> 
       </div>
      </div>
    );
    
 }


}

export default ProfileLayout;