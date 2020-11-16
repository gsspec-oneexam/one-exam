import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import AudioRecorder from 'react-audio-recorder';
import ado from './Reeti.mp3';
import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';
import samtext from "./questions"
import VoiceRecorder from "./recorder.js"
import axios from "axios";

import qpic from './kittu_123456.jpg';
import ReactAudioPlayer from 'react-audio-player';
import QuestionChoice from "./QuestionC.js";
import Qpc from "./pc.js";
import Iq from "./iq.js";
import L from "./lis.js";

import F from "./final.js";
import xtype from 'xtypejs'

function Questions(props) {



const [questions,setQuestions] = useState([]);
useEffect(() =>{
axios.get('http://localhost:8000/questions')
.then(res => {
setQuestions(res.data.data[props.count-1])

})
});


{
 if (questions.q_type == "M" ) {
return(<>
<h2 className="mt-3 ml-4 text-left">{props.count}) {questions.q_name}</h2>
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






</>)
} else if( questions.q_type == "I" ){
return(<>
<h2 className="mt-3 ml-4 text-left">{props.count}) {questions.q_name}</h2><br/><br/>
	<input  className="Inputfield"/>
</>
)
}
else if( questions.q_type == "P" ){
return(<>
<h2 className="mt-3 ml-4 text-left">{props.count}) {questions.q_name}</h2>
<img src={qpic} alt="Logo" className="text-left" width="300" height="150" /><br/><br/>
	<input className="Inputfield1"/>
</>
)
}else if( questions.q_type == "A" ){
return(<>

	<h1>{props.count}) listen audio?</h1>
	<ReactAudioPlayer  src={ado}  autoPlay  controls/>

    <br/><br/>
    <b>  {questions.q_name}</b><br/>
 <input className="Inputfield2"/>



</>
)
}else if( questions.q_type == "R" ){
return(<>

	<h1>{props.count}) {questions.q_name}</h1>
	     <br/><br/>
	     <VoiceRecorder />
		 <input className="Inputfield3"/>
</>
)
}else {
return(
<button className="btn btn-custom"
style={{ display:'show' }} > <Link className = "cstyle" to = "/f">Proceed</Link></button>
)
}
}

//{
//if (props.exam_code.includes(props.code) ) { console.log('IN if');
//return(
//<button className="btn btn-custom"
//style={{ display:'show' }} > <Link className = "cstyle" to = "/ins">Proceed</Link></button>
//)
//
//} else { console.log('IN else');
//return(
//<>
//<h1>Invalid Code</h1>
//</>
//);
//}
//}
}

export default Questions;