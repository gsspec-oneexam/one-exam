import React , { useEffect ,useRef, useState} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link} from 'react-router-dom';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import QuestionChoice from "./QuestionC.js";


function Instructions(props) {

console.log(props.code,"code test");

const[dat,setDta] = useState([])

const[paper,setPaper] = useState("")
const [instructions,setInstructions] = useState([]);

const [instr,setInstr] = useState(props.code);

useEffect(() => {
console.log(props.code,"get code")
const requestOptions = {
        method: 'POST',
        body: JSON.stringify({ participant_key: props.code })
    };
    fetch('http://localhost:8000/sec_instructions', requestOptions)
        .then(res =>res.json())
        .then(data => {setDta(data);setInstructions(data.Instructions);setPaper(data.paper_name)
})



}, []);
console.log(dat.instructions,"dta check")

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
  <Router>



<Switch>
  <Route exact path = "/quest" exact component={QuestionChoice} />

<div className="ins-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">{dat.paper_name}</label>
</div>

<h3>Instructions</h3>
<div className="ins-div text-center">

<div hidden><QuestionChoice paper={dat.paper_name}/></div>
<button className="btn btn-custom mt-5" > <Link className = "cstyle" to = "/quest">Proceed</Link></button>
</div>
</div>
</Switch>
</Router>
  );
}
export default Instructions;