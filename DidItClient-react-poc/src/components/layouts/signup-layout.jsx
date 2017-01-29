import React, { Component } from 'react';
import LoginService from '../../services/login-service.js';
import axios from 'axios';

class Signup extends React.Component {
  
constructor(props) {
    super(props);
    this.state = {username: '', password: '', email: '', storename: '', location: ''};

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






    
    event.preventDefault();
  }


  render() {
 
    return (
      <div>

           <div className="grid">
          <form onSubmit={this.handleSubmit} className="form login">
            <div className="form__field">
              <label htmlFor="signup__username"><svg className="icon"></svg><span className="hidden">Username</span></label>
              <input id="signup__username" type="text" name="username" className="form__input" placeholder="Username" required />
            </div>
            <div className="form__field">
              <label htmlFor="signup__password"><svg className="icon"></svg><span className="hidden">Password</span></label>
              <input id="signup__password"  type="password" name="password" className="form__input" placeholder="Password" required />
            </div>
            <div className="form__field">
              <label htmlFor="signup__email"><svg className="icon"></svg><span className="hidden">Email</span></label>
              <input id="signup__email"  type="text" name="password" className="form__input" placeholder="Email" required />
            </div>
            <div className="form__field">
              <label htmlFor="signup__confirmpassword"><svg className="icon"></svg><span className="hidden">Confirm Password</span></label>
              <input id="signup__confirmpassword" type="text" name="password" className="form__input" placeholder="Confirm Password" required />
            </div>
             <div className="form__field">
              <label htmlFor="storeName"><svg className="icon"></svg><span className="hidden">Store Name</span></label>
              <input id="storeName"  type="text" name="storename" className="form__input" placeholder="Store Name" required />
            </div>
            <div className="form__field">
              <label htmlFor="location"><svg className="icon"></svg><span className="hidden">Location</span></label>
              <input id="location" type="text" name="password" className="form__input" placeholder="Location" required />
            </div>
            <div className="form__field">
              <input type="submit" defaultValue="Sign Up" />
            </div>
          </form>
        </div>  
      </div>
    );
    
 }


}

export default Signup;