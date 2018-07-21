import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import Header from './HeaderComponent'
import CollegesList from './FetchComponent';
import CollegeDetails from './CollegeDetailsComponet';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

class App extends Component {

  render() {
    const{title}=this.props;
    //const{count}=this.state;
    return (
    <Router>
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
          <Header isLoggedIn={false} title="djangopproject"/>
          <Route exact path="/" component={CollegesList} />
          <Route path="/college/:id" component={CollegeDetails} />
        </header>
        <p className="App-intro">
        </p>
      </div>
      </Router>
    );
  }
}

export default App;
