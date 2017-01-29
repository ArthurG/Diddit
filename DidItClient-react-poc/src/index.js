import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

import Login from './components/layouts/login-layout.jsx';
import Signup from './components/layouts/signup-layout.jsx'
import SurveyContainer from './components/containers/survey-container.jsx';
import SurveyDetailsContainer from './components/containers/survey-details-container.jsx';
import ProfileLayout from './components/layouts/profile-layout.jsx';

import {Router, Route, browserHistory, IndexRoute} from 'react-router';



ReactDOM.render( 
   <Router history={browserHistory}>
    <Route path="/" component={App}>
      <IndexRoute component={Login} />
      <Route path="signup" component={Signup} />
      <Route path="profile/:username" component={ProfileLayout} />
      <Route path="create/:username" component={ProfileLayout} />
      <Route path="delete/:username" component={ProfileLayout} />
      <Route path="view/:username" component={SurveyContainer} />
      <Route path="details/:username/:surveyname" component={SurveyDetailsContainer} />
    </Route>
  </Router>
  
  
  , document.getElementById('root') );