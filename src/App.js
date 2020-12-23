import React , { useEffect , useState,useContext,createContext} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';
//import { useBeforeunload } from 'react-beforeunload';
import axios from "axios";
import { hashHistory,browserHistory  } from "react-router";
import logo from './logo.svg';
import qpic from './kittu_123456.jpg';
import ReactAudioPlayer from 'react-audio-player';
import ado from './Reeti.mp3';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import Questions from "./questions_dynamic";
import QuestionChoice from "./QuestionC.js";
import Instructions from "./instructions.js";
import Paper_selection from "./paper_selection.js";
import Partcipant_form from "./participant_form.js";
import Registered from "./registered.js";
import Exam_key from "./exam_key.js";
//


const questionContext = React.createContext();
function App() {
window.onbeforeunload = function() {
    return "Refresh not allowed";
}








  return (
  <Router>

<Switch>




<Route exact path = "/" exact component={Paper_selection} />
<Route exact path = "/participant_registered" exact component={Registered} />
<Route exact path = "/participant_form" exact component={Partcipant_form} />


<Route exact path = "/oneexam" exact component={Exam_key} />
<Route exact path = "/ins" exact component={Instructions} />
<Route exact path = "/quest" exact component={QuestionChoice} />


</Switch>
</Router>
  );

}

export default App;
