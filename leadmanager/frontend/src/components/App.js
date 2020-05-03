import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import Header from './layout/Header';


class App extends Component{
    render() {
        return <Header>Hello React</Header>;
    }
}

ReactDOM.render(<App/>, document.getElementById("app"));