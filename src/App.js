import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import Login from './Component/Login';
import SignUp from './Component/SignUp';
import { BrowserRouter, Route, Switch } from "react-router-dom";



function App() {
  return (
    <div className="container">
       <BrowserRouter>
       <Switch>
       <Route exact path={"/"} component={Login} />
       <Route exact path={"/signup"} component={SignUp} />
      </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
