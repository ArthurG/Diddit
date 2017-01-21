import React, {Component} from 'react';
import logo from './logo.svg';

import {Link} from 'react-router'

class App extends Component {
    render() {
        return ( 
            <div>
        <h1>App</h1>
     
        <ul>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/inbox">Inbox</Link></li>
        </ul>

        {this.props.children}
      </div>
        );
    }
}

export default App;