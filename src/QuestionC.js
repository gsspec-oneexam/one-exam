import React , { useEffect , useState,useContext} from 'react';
import { Button } from 'react-bootstrap';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import {BrowserRouter as Router,Switch,Route,Link,useLocation} from 'react-router-dom';
import { If, Then, ElseIf, Else } from 'react-if-elseif-else-render';
import axios from "axios";
import ProgressBar from 'react-bootstrap/ProgressBar';
import VoiceRecorder from "./recorder.js";
//import AudioRecorder from 'react-audio-recorder';
import ado from './Reeti.mp3';
import ReactAudioPlayer from 'react-audio-player';
import { Progress } from 'antd';
import Questions from "./questions_dynamic.js";

import {domain} from "./config.js";

import questionContext from "./App";
function QuestionChoice(props) {


const Domain = useContext(domain)
const [answer, setAnswer] = useState()
const { state } = useLocation();
console.log(state,"staet check")
useEffect(() => {
    console.log(state.dat.participant_id,"staet");
  }, []);

    console.log(state.dat,"staet");
//
//    console.log(state.dat.Instructions,"sout taet");
//const testing = useContext(context);
//console.log(testing,"q context test")
//console.log(this.props.location.state,"q props.n")
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

console.log(answer,"ans");

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
console.log(state.dat.section,"lencheck");
const [quest_length, setQuest_length] = useState(state.dat.questions.length)
const [questions,setQuestions] = useState([]);
//useEffect(() =>{
//axios.get('http://localhost:8000/questions')
//.then(res =>{
//setQuest_length(res.data.data.length)
//setQuestions(res.data.data)
//
//})

//setQuest_length(state.dat.questions.length)
//},[state.dat.questions]);

console.log(quest_length,"quest_length check 1");



  useEffect(() => {
    // use set timeout and be confident because updateTime will cause rerender
    // rerender mean re call this effect => then it will be similar to how setinterval works
    // but with easy to understand logic
    const token = setTimeout(updateoTime, 1000)

    return function cleanUp() {
      clearTimeout(token);
    }
  },[])
const [count,setCount] = useState(0)
function inc_count(){

setCount(prevCount => prevCount +1 )
setSeconds(30);
      setMinutes(1);
}
function dec_count(){

setAns(prevCount => prevCount -1 )
setCount(prevCount => prevCount -1 )
setSeconds(30);
      setMinutes(1);
}

const [pgbar,setPgbar] =  useState(0)
useEffect(() => {
    setPgbar((count / quest_length)*100)
  })
  const [ans,setAns] = useState(0)
 function skip_q(){
const requestOptions = {
        method: 'POST',
        body: JSON.stringify({ participant_id: state.dat.participant,
                                paper_name:state.dat.paper_name,
                                paper_instance_id : state.dat.paper_instance_id,
                                question_id:questions.q_id,
                                ans:"null"

         })
    };
    fetch('http://'+Domain+'/exam_ans', requestOptions)
        .then(res =>res.json())
        .then(setAnswer())
setCount(prevCount => prevCount +1 )

setSkipped(prevCount => prevCount +1 )
setSeconds(30);
      setMinutes(1);
}
  function ans_q(){
const requestOptions = {
        method: 'POST',
        body: JSON.stringify({ participant_id: state.dat.participant,
                                paper_name:state.dat.paper_name,
                                paper_instance_id : state.dat.paper_instance_id,
                                question_id:questions.q_id,
                                ans:answer

         })
    };
    fetch('http://'+Domain+'/exam_ans', requestOptions)
        .then(res =>res.json())
        .then(setAnswer())
//        .then(data => {setDta(data);setInstructions(data.Instructions);setPaper(data.paper_name)
//}
//)
setCount(prevCount => prevCount +1 )

setAns(prevCount => prevCount +1 )
setSeconds(30);
      setMinutes(1);
}

useEffect(() =>{
//axios.get('http://localhost:8000/questions')
//.then(res => {
//console.log(props.qlist.paper_name,"props -1")
setQuestions(state.dat.questions[count])
//
//})
});

  {if(count   != quest_length){
  return (



<div>
<div className="content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">{state.dat.paper_name}</label>
</div>
<div className="grid-container">
    <div className="font">
       <label className="section-label">{state.dat.section}</label>&nbsp;&nbsp;
	    <label className="question-label">Question {count +1} / {quest_length}</label>
    </div>

    <div className="font">
    <If condition={seconds <= 9}>

<Then>

    <If condition={seconds <= 9 && minutes == 0}>
    <Then>
        <label className="time-label" >Time Left: <label className="time-label" style={{color: "red"}}>0{minutes}:0{seconds}</label> </label>
        </Then>
        <Else>
        <label className="time-label">Time Left: 0{minutes}:0{seconds}</label>
        </Else>
        </If>
        </Then>
        <Else>
        <label className="time-label">Time Left: 0{minutes}:{seconds}</label>
        </Else>
        </If>



    </div>

</div>


<div className="middle-div ">


<If condition={questions.q_type == "C"}>

<Then><>
<h2 className="mt-3 ml-4 text-left">{count +1}) {questions.q_name}</h2>
	<table  className="custom-font mt-4">
	  <tr>
		<td>
    <div className="radio-item">
    <input type="radio" checked = {answer == questions.opt1} onChange={event => setAnswer(event.target.value)} id={questions.opt1} name={questions.q_name} value={questions.opt1}/>
    <label for={questions.opt1}>{questions.opt1}</label>
    </div>
		</td>
		<td>
    <div className="radio-item">
    <input type="radio" checked = {answer == questions.opt2} onChange={event => setAnswer(event.target.value)} id={questions.opt2} name={questions.q_name} value={questions.opt2}/>
    <label for={questions.opt2}>{questions.opt2}</label>
    </div>
		</td>
	  </tr>
	  <tr>
		<td>
    <div className="radio-item">
    <input onChange={event => setAnswer(event.target.value)} checked = {answer == questions.opt3} type="radio" id={questions.opt3} name={questions.q_name} value={questions.opt3}/>
    <label for={questions.opt3}>{questions.opt3}</label>
    </div>
		</td>
		<td>
    <div className="radio-item">
  <input type="radio" onChange={event => setAnswer(event.target.value)} checked = {answer == questions.opt4} id={questions.opt4} name={questions.q_name} value={questions.opt4}/>
    <label for={questions.opt4}>{questions.opt4}</label>
    </div>
		</td>
	  </tr>
	  <tr>
	  <td>
    <div className="radio-item">
    <input onChange={event => setAnswer(event.target.value)} checked = {answer == questions.opt5} type="radio" id={questions.opt5} name={questions.q_name} value={questions.opt5}/>
    <label for={questions.opt5}>{questions.opt5}</label>
    </div>
	  </td>
	  </tr>
	</table>
	<br/><br/>
</>
</Then>

<ElseIf condition={questions.q_type == "I"}>
<>
<h2 className="mt-3 ml-4 text-left">{count + 1}) {questions.q_name}</h2><br/><br/>
	<input onChange={event => setAnswer(event.target.value)} className="Inputfield"/>
</>
</ElseIf>



<ElseIf condition={questions.q_type == "P"}>

<If condition={questions.mediasource == 'F'}>


<Then>

<>
<h2 className="mt-3 ml-4 text-left">{count + 1}) {questions.q_name}</h2>
<img src={require('./kittu_123456.jpg')} alt="image_display_error" className="text-left" width="300" height="150" /><br/><br/>
	<input onChange={event => setAnswer(event.target.value)} className="Inputfield1"/>
</>
</Then>

<Else>

<>
<h2 className="mt-3 ml-4 text-left">{count +1}) {questions.q_name}</h2>
<img src={questions.media_url} alt="image_display_error" className="text-left" width="300" height="150" /><br/><br/>
	<input onChange={event => setAnswer(event.target.value)} className="Inputfield1"/>
</>
</Else>
      </If>


</ElseIf>
<ElseIf condition={questions.q_type == "A"}>
<>

	<h1>{count +1}){questions.q_name}</h1>
	<ReactAudioPlayer  src={ado}  autoPlay  controls/>

    <br/><br/>
 <input onChange={event => setAnswer(event.target.value)} className="Inputfield2"/>
<br/><br/>


</>
</ElseIf>


<ElseIf condition={questions.q_type == "R"}>
<>

	<h1>{count + 1}) {questions.q_name}</h1>
	     <br/><br/>
	     <VoiceRecorder />
	     <br/><br/>
	     <br/><br/>

</>

</ElseIf>
<Else>

<button className="btn btn-custom"
style={{ display:'show' }} > <Link className = "cstyle" to = "/f">Proceed</Link></button>
</Else>
      </If>


<div className="nav-button-div text-center">
  <If condition={count == 0}>
        <Then>

<button className="btn btn-custom" onClick={dec_count} disabled>Back</button>{' '}
        </Then>

        <Else>

<button className="btn btn-custom" onClick={dec_count}>Back</button>{' '}
        </Else>
      </If>
<button className="btn btn-custom ml-5"  onClick={skip_q}>Skip</button>{' '}
   <If condition={answer}>

<Then>

<button className="btn btn-custom ml-5" onClick={ans_q} >Next</button>{' '}
        </Then>
        <Else>

<button className="btn btn-custom ml-5" onClick={ans_q} disabled>Next</button>{' '}
        </Else>
        </If>
</div>
    <ProgressBar className="mt-4" now={pgbar} />




</div>
</div>
</div>

  );
  }else{return (


<div>
<div className="content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">{state.dat.paper_name}</label>
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
  );

  }}

}

export default QuestionChoice;
