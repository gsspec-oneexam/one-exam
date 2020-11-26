import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';

import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';
import samtext from "./questions"

import QuestionChoice from "./QuestionC.js";
import Qpc from "./pc.js";

import axios from "axios"
function Question(){

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
console.log(res.data.data.length)
setQuestions(res.data.data[1])


})
},[]);



return(
<Router>
<Switch>

  <Route exact path = "/quest" exact component={QuestionChoice} />

<Route exact path = "/qpc" exact component={Qpc} />
<div>
<div className="content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">Carnatic Music Theory Exam Paper - 1</label>
</div>
<div className="grid-container">
    <div className="font">
       <label className="section-label">Section-1</label>&nbsp;&nbsp;
	    <label className="question-label">Question 2 / 6</label>
    </div>

    <div className="font">
        <label className="time-label">Time Left: 0{minutes}:{seconds}</label>
    </div>

</div>
<div className="middle-div ">
<h2 className="mt-3 ml-4 text-left">{questions.q_name}</h2>
	<table  className="custom-font mt-4">
	  <tr>
		<td>
    <div className="radio-item">
    <input type="radio" id={questions.opt1} name="que1" value={questions.opt1}/>
    <label for="thyagaraj">{questions.opt1}</label>
    </div>
		</td>
		<td>
    <div className="radio-item">
    <input type="radio" id={questions.opt2} name="que1" value={questions.opt2}/>
    <label for={questions.opt2}>{questions.opt2}</label>
    </div>
		</td>
	  </tr>
	  <tr>
		<td>
    <div className="radio-item">
    <input type="radio" id={questions.opt3} name="que1" value={questions.opt3}/>
    <label for={questions.opt3}>{questions.opt3}</label>
    </div>
		</td>
		<td>
    <div className="radio-item">
  <input type="radio" id={questions.opt4} name="que1" value={questions.opt4}/>
    <label for={questions.opt4}>{questions.opt4}</label>
    </div>
		</td>
	  </tr>
	  <tr>
	  <td>
    <div className="radio-item">
    <input type="radio" id={questions.opt5} name="que1" value={questions.opt5}/>
    <label for={questions.opt5}>{questions.opt5}</label>
    </div>
	  </td>
	  </tr>
	</table>
	<br/><br/>
</div>
<div className="nav-button-div text-center">
<button className="btn btn-custom"><Link className = "cstyle" to = "/quest">Back</Link></button>{' '}
<button className="btn btn-custom ml-5"><Link className = "cstyle" to = "/qpc">Skip</Link></button>{' '}
<button className="btn btn-custom ml-5" ><Link className = "cstyle" to = "/qpc">Next</Link></button>{' '}
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
export default Question