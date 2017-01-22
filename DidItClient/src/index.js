import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

import Login from './components/layouts/login-layout.jsx';
import Signup from './components/layouts/signup-layout.jsx'
import SurveyContainer from './components/containers/survey-container.jsx';
import SurveyDetailsContainer from './components/containers/survey-details-container.jsx';

import {Router, Route, browserHistory, IndexRoute, hashHistory} from 'react-router';



ReactDOM.render( 
   <Router history={hashHistory}>
    <Route path="/" component={App}>
      <IndexRoute component={Login} />
      <Route path="about" component={Signup} />
      <Route path="inbox" component={SurveyContainer} />
    </Route>
  </Router>
  
  
  , document.getElementById('root') );