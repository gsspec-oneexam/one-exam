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
//

import Code_check from "./exam_code.js";

const questionContext = React.createContext();
function App() {
window.onbeforeunload = function() {
    return "Refresh not allowed";
}







const [code, setCode] = useState('null')

  return (
  <Router>

<Switch>
<Route exact path = "/quest" exact component={QuestionChoice} />
<Route exact path = "/ins" exact component={Instructions} />


<Route exact path = "/paper_selection" exact component={Paper_selection} />
<Route exact path = "/participant_registered" exact component={Registered} />
<Route exact path = "/participant_form" exact component={Partcipant_form} />

<div className="code-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">OneExam</label>
</div>
<div className="code-div ">
<p>Please enter entrance code to proceed for online examination</p>
<input onChange={event => setCode(event.target.value)}/>&nbsp;
<Code_check code={code} />
</div>
</div>




</Switch>
</Router>
  );

}

export default App;
