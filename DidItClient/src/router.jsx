import React from 'react';
import {Router, Route, browserHistory, IndexRoute} from 'react-router';
import {App} from './App';
import { Login } from './components/layouts/login-layout.jsx';

export default(
    <Router history={browserHistory}>
        <Route component={App}>
             <Route path="/" component={Login} />
        </Route>
    </Router>

);