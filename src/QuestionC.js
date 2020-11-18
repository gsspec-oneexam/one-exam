import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';
import Question from "./questions"
import samtext from "./questions"
import axios from "axios";
import ProgressBar from 'react-bootstrap/ProgressBar';

import { Progress } from 'antd';
import Questions from "./questions_dynamic.js"



function QuestionChoice(props) {
const [seconds, setSeconds] = useState(30)
  const [minutes, setMinutes] = useState(1)
  const [qno, setQno] = useState(1)

  const [skipped,setSkipped] = useState(0)




  function updateTime() {

  {if(count - 1 != quest_length){


     if (minutes == 0 && seconds == 0) {

      setSeconds(30);
      setMinutes(1);
      inc_count();

    setSkipped(prevCount => prevCount +1 )

    }
    else {
      if (seconds == 0) {
        setMinutes(minutes => minutes - 1);
        setSeconds(59);
      } else {
        setSeconds(seconds => seconds - 1);
      }
    }
  }}}



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
  {if(count - 1 != quest_length){
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
  }}

const [quest_length, setQuest_length] = useState('')
const [questions,setQuestions] = useState([]);
useEffect(() =>{
axios.get('http://localhost:8000/questions')
.then(res =>{
setQuest_length(res.data.data.length)
setQuestions(res.data.data)

})
},[setQuestions]);




  useEffect(() => {
    // use set timeout and be confident because updateTime will cause rerender
    // rerender mean re call this effect => then it will be similar to how setinterval works
    // but with easy to understand logic
    const token = setTimeout(updateoTime, 1000)

    return function cleanUp() {
      clearTimeout(token);
    }
  })
const [count,setCount] = useState(1)
function inc_count(){

setCount(prevCount => prevCount +1 )
setSeconds(30);
      setMinutes(1);
}
function dec_count(){

setCount(prevCount => prevCount -1 )
setSeconds(30);
      setMinutes(1);
}

const [pgbar,setPgbar] =  useState(0)
useEffect(() => {
    setPgbar((count / quest_length)*100)
  },[count])
  const [ans,setAns] = useState(0)
  function skip_q(){

setCount(prevCount => prevCount +1 )

setSkipped(prevCount => prevCount +1 )
setSeconds(30);
      setMinutes(1);
}
  function ans_q(){

setCount(prevCount => prevCount +1 )

setAns(prevCount => prevCount +1 )
setSeconds(30);
      setMinutes(1);
}
  {if(count - 1  != quest_length){
  return (
  <Router>
<Switch>


<Route exact path = "/quest2" exact component={Question} />
<div>
<div className="content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">{props.paper}</label>
</div>
<div className="grid-container">
    <div className="font">
       <label className="section-label">Section-1</label>&nbsp;&nbsp;
	    <label className="question-label">Question {count} / {quest_length}</label>
    </div>

    <div className="font">
        <label className="time-label">Time Left: 0{minutes}:{seconds}</label>
    </div>

</div>

<div className="middle-div ">
<Questions quest={questions} total_q={quest_length} count={count}/>

<div className="nav-button-div text-center">
<button className="btn btn-custom" onClick={dec_count}>Back</button>{' '}
<button className="btn btn-custom ml-5"  onClick={skip_q}>Skip</button>{' '}
<button className="btn btn-custom ml-5" onClick={ans_q} >Next</button>{' '}
</div>
    <ProgressBar className="mt-4" now={pgbar} />




</div>
</div>
</div>
</Switch>
</Router>
  );
  }else{return (


  <Router>
<Switch>


<Route exact path = "/quest2" exact component={Question} />
<div>
<div className="content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">Carnatic Music Theory Exam Paper - 1</label>
</div>
    <div className="font">
       <center>Exam Summary</center>
    </div>




<div className="ins-div text-center">
<p className="mt-4">Questions answered : {ans}/{quest_length}</p>
<p>Questions skipped : {skipped}/{quest_length}</p>

<button className="btn btn-custom" >Close</button>
</div>






</div>
</div>
</Switch>
</Router>
  );

  }}

}

export default QuestionChoice;
