import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';
import axios from 'axios';

import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import Question from "./questions";
import samtext from "./questions";
import QuestionChoice from "./QuestionC.js";
import Instructions from "./instructions.js";


function Insructions() {

const [seconds, setSeconds] = useState(30)
  const [minutes, setMinutes] = useState(0)
  const [qno, setQno] = useState(1)


  function updateTime() {
    if (minutes == 1 && seconds == 1) {

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


const [instructions,setInstructions] = useState([]);
useEffect(() =>{
axios.get('http://localhost:8000/sec_instructions')
.then(res =>{
console.log(res.data.data)
setInstructions(res.data.data)

})
},[]);


  return (
  <Router>




<Switch>
  <Route exact path = "/quest" exact component={QuestionChoice} />

<div className="ins-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">Swarabharathi Carnatic Music Exam</label>
</div>

<h3>Instructions</h3>
<div className="ins-div text-center">
{instructions.map(instruction => <p className="text-left ml-3 mt-2">{instruction.sect_ins}</p>)}



<button className="btn btn-custom mt-5" > <Link className = "cstyle" to = "/quest">Proceed</Link></button>
</div>
</div>
</Switch>
</Router>
  );
}

export default Insructions;