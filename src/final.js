import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';


import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
//import 'bootstrap/dist/css/bootstrap.css';
import Question from "./questions";
import samtext from "./questions";
import QuestionChoice from "./QuestionC.js";
import Instructions from "./instructions.js";


function F() {

const [seconds, setSeconds] = useState(30)
  const [minutes, setMinutes] = useState(0)
  const [qno, setQno] = useState(1)

const [question, setQuestion] = useState("1)  Who is the creator of Carnatic Music Learning Syllabus?")

const [opt, setOpt] = useState({opt1:"Thyagaraj",opt2:"Purandara Das",opt3:"Muthu Swami",opt4:"Bhyma Sasthri",opt5:"None of the Above"})

function nextQuestion(){

setQno("2")
setQuestion("2)  Number of Alphabets?")
setOpt({opt1:"15",opt2:"21",opt3:"36",opt4:"5",opt5:"none"})
setSeconds(30);
      setMinutes(0);

}


  function updateTime() {
    if (minutes == 1 && seconds == 1) {

      nextQuestion();
      setSeconds(30);
      setMinutes(0);

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


  return (
  <Router>




<Switch>

<div className="ins-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">Swarabharathi Carnatic Music Exam</label>
</div>

<h3>Test summary</h3>
<div className="ins-div ">
<p>Questions answered : 4/6</p>
<p>Questions skipped : 2/6</p>

<button className="btn btn-custom" >Close</button>
</div>
</div>
</Switch>
</Router>
  );
}

export default F;