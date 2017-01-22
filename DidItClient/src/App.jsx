import React from 'react'
import {render} from 'react-dom'

// First we import some modules...
import { Router, Route, IndexRoute, Link } from 'react-router'

// Then we delete a bunch of code from App and
// add some <Link> elements...
const App = React.createClass({
  render() {
    return (
      <div>
        {this.props.children}
      </div>
    )
  }
})

export default App;