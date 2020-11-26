import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';

import ado from './Reeti.mp3';
import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';
import samtext from "./questions"
import axios from "axios";

import ReactAudioPlayer from 'react-audio-player';
import QuestionChoice from "./QuestionC.js";
import Qpc from "./pc.js";
import Iq from "./iq.js";
import L from "./lis.js";

import F from "./final.js";
function Aq(){

const [seconds, setSeconds] = useState(30)
  const [minutes, setMinutes] = useState(1)



  function updateTime() {
    if (minutes == 0 && seconds == 0) {

      setSeconds(30);
      setMinutes(1);

    }
    else {
      if (seconds == 0) {
        setMinutes(minutes => minutes - 1);
        setSeconds(59);
      } else {
        setSeconds(seconds => seconds - 1);
      }
    }
  }



  useEffect(() => {
    // use set timeout and be confident because updateTime will cause rerender
    // rerender mean re call this effect => then it will be similar to how setinterval works
    // but with easy to understand logic
    const token = setTimeout(updateTime, 1000)

    return function cleanUp() {
      clearTimeout(token);
    }
  })


const [oseconds, setoSeconds] = useState(0)
  const [ominutes, setoMinutes] = useState(45)



  function updateoTime() {
    if (ominutes == 0 && oseconds == 0) {

      setoSeconds(0);
      setoMinutes(0);

    }
    else {
      if (oseconds == 0) {
        setoMinutes(ominutes => ominutes - 1);
        setoSeconds(59);
      } else {
        setoSeconds(oseconds => oseconds - 1);
      }
    }
  }



  useEffect(() => {
    // use set timeout and be confident because updateTime will cause rerender
    // rerender mean re call this effect => then it will be similar to how setinterval works
    // but with easy to understand logic
    const token = setTimeout(updateoTime, 1000)

    return function cleanUp() {
      clearTimeout(token);
    }
  })


const [questions,setQuestions] = useState([]);
useEffect(() =>{
axios.get('http://3.138.184.54:8000/questions')
.then(res =>{
console.log(res.data)
setQuestions(res.data.data[4])

})
},[]);
return(
<Router>
<Switch>

<Route exact path = "/iq" exact component={Iq} />

<Route exact path = "/f" exact component={F} />

<Route exact path = "/l" exact component={L} />
<div>
<div className="content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">Carnatic Music Theory Exam Paper - 1</label>
</div>
<div className="grid-container">
    <div className="font">
       <label className="section-label">Section-1</label>&nbsp;&nbsp;
	    <label className="question-label">Question 5 / 6</label>
    </div>

    <div className="font">
        <label className="time-label">Time Left: 0{minutes}:{seconds}</label>
    </div>

</div>
<div className="middle-div ">
<h1>5) listen audio?</h1>
	<ReactAudioPlayer  src={ado}  autoPlay  controls/>

    <br/><br/>
    <b>  {questions.q_name}</b><br/>
 <input />
</div>
<div className="nav-button-div text-center">
<button className="btn btn-custom"><Link className = "cstyle" to = "/iq">Back</Link></button>{' '}
<button className="btn btn-custom ml-5"><Link className = "cstyle" to = "/l">Skip</Link></button>{' '}
<button className="btn btn-custom ml-5" ><Link className = "cstyle" to = "/l">Next</Link></button>{' '}
</div>
<div className="grid-container timer-div">
    <div className="font">
       <label className="section-label">Time Consumed 00: 05: 40</label>

    </div>

    <div className="font">
        <label className="time-label">overall time left: 00:{ominutes}:{oseconds}</label>
    </div>

</div>



</div>
</div>

</Switch>
</Router>
  );
}
export default Aq