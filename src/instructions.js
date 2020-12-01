import React , { useEffect ,useRef, useState,useContext} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory } from 'react-router-dom';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import QuestionChoice from "./QuestionC.js";
import { If, Then, ElseIf, Else } from 'react-if-elseif-else-render';

import {domain} from "./config.js";

function Instructions(props) {
const history = useHistory();
function handleClick() {
    history.push("/quest");
  }
console.log(props.code,"code test");

const[dat,setDta] = useState([])

const[paper,setPaper] = useState("")
const [instructions,setInstructions] = useState([]);

const [instr,setInstr] = useState(props.code);

const Domain = useContext(domain)
useEffect(() => {
console.log(props.code,"get code")
const requestOptions = {
        method: 'POST',
        body: JSON.stringify({ participant_key: props.code })
    };
    fetch('http://'+Domain+'/oneexam', requestOptions)
        .then(res =>res.json())
        .then(data => {setDta(data);setInstructions(data.Instructions);setPaper(data.paper_name)
})



}, []);
console.log(dat,"dta check")

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
  <If condition={1 == 1}>
        <Then>
          <p>Then: 1</p>
        </Then>
        <ElseIf condition={1 == 2}>
          <p>ElseIf: 2</p>
        </ElseIf>
        <Else>
          <p>Else</p>
        </Else>
      </If>
<p className="text-left ml-3 mt-2">{instructions}</p>




<button className="btn btn-custom mt-5" > <Link className = "cstyle" to ={{ pathname: "/quest", state: {dat}}} >



Proceed</Link></button>
</div>
</div>


</>
  );
}
export default Instructions;