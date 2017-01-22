import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

import Login from './components/layouts/login-layout.jsx';
import Signup from './components/layouts/signup-layout.jsx'
import SurveyContainer from './components/containers/survey-container.jsx';



import Router from './router.jsx';

ReactDOM.render( < SurveyContainer />, document.getElementById('root') );