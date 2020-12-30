import React , { useEffect ,useRef, useState,useContext} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';
import axios from 'axios';
//import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
//import 'bootstrap/dist/css/bootstrap.css';
import QuestionChoice from "./QuestionC.js";
import { If, Then, ElseIf, Else } from 'react-if-elseif-else-render';

import {domain} from "./config.js";

function Instructions(props) {
const history = useHistory();
window.onbeforeunload = function() {
    return "Refresh not allowed";
}
const { prt_code } = useLocation();
function handleClick() {
    history.push("/quest");
  }
//console.log(props.code,"code test");

const[dat,setDta] = useState([])

const[paper,setPaper] = useState("")

const[company,setCompany] = useState("")
const [instructions,setInstructions] = useState([]);

const [questions,setQuestions] = useState([]);
const [instr,setInstr] = useState(props.code);

const Domain = useContext(domain)
useEffect(() => {
//console.log(props.code,"get code")
const requestOptions = {
        method: 'POST',
        body: JSON.stringify({ participant_key: props.code })
    };
    fetch('http://'+Domain+'/oneexam', requestOptions)
        .then(res =>res.json())
        .then(data => {setDta(data);setInstructions(data.Instructions);setPaper(data.paper_name);setCompany(data.company_id)
})



}, []);
console.log(company,"company check")
{if(company==1){


require('./swarabharathi.css');
}
}
{(()=> {
          if (company==1) {

require('./swarabharathi.css');
          } else if (company==2) {

require('./tech_school.css');
          } else{

require('./App.css');
          }
        })()}
//
//useEffect(() =>{
//axios.get('http://localhost:8000/sec_instructions')
//.then(res =>{
//console.log(res.data.data)
//setInstructions(res.data.data)
//
//})
//},[setInstructions]);


  return (


<>

<div className="ins-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">{dat.paper_name}</label>
</div>

<h3>Instructions</h3>
<div className="ins-div text-center">
{instructions.map((instruction,index) => (
<p className="text-left ml-3 mt-1">

        {index+1}) {instruction}

      </p> ))}




<button className="btn btn-custom mt-5" > <Link className = "cstyle" to ={{ pathname: "/quest", state: {dat}}} >



Proceed</Link></button>
</div>
</div>


</>
  );
}
export default Instructions;