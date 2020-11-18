import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';

import axios from "axios";
import { hashHistory,browserHistory  } from "react-router";
import logo from './logo.svg';
import qpic from './kittu_123456.jpg';
import ReactAudioPlayer from 'react-audio-player';
import ado from './Reeti.mp3';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import Question from "./questions";
import samtext from "./questions";
import QuestionChoice from "./QuestionC.js";
import Instructions from "./instructions.js";
import Qpc from "./pc.js";
import Iq from "./iq.js";
import Aq from "./aq.js";
import F from "./final.js";
import L from "./lis.js";
import Code_check from "./exam_code.js"


function App() {

const [code, setCode] = useState('null')


  return (
  <Router>

<Switch>

<Route exact path = "/quest" exact component={QuestionChoice} />




<Route exact path = "/ins" exact component={Instructions} />
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
