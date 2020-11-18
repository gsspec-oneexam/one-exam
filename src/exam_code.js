import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';

import Instructions from "./instructions.js";


import axios from "axios";
function Code_check(props) {

const [exam_code,setExam_code] = useState([]);

useEffect(() =>{

axios.get('http://localhost:8000/exam_codes')
.then(res =>{
setExam_code(res.data.data)
//for (const [index, value] of (res.data.data).entries()) {
//
//setExam_code(exam_code =>[...exam_code,value.exam_code])
//}

}
)

},[]);
console.log(exam_code,"code out");

{
if(props.code == "null"){
return(
<>
<h1></h1>
</>
);

}
else if (exam_code.includes(props.code) && props.code.length == 15) {
return(<>
<button className="btn btn-custom"
style={{ display:'show' }} > <Link className = "cstyle"  to = "/ins"><div hidden>
<Instructions code = {props.code} /></div>Proceed</Link></button>
</>)

} else if( props.code.length > 14 ) {
return(
<>
<h4 className="invalid-text">Invalid Code</h4>
</>
)}
else  {
return(
<>
<h1></h1>
</>
);}
}
}


export default Code_check;