import React , { useEffect , useState} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';

function Code_check(props) {
useEffect(() =>{
console.log(props.exam_code);
console.log(props.code.length);
});
{
if(props.code == "null"){
return(
<>
<h1></h1>
</>
);

}
else if (props.exam_code.includes(props.code) && props.code.length > 10) {
return(
<button className="btn btn-custom"
style={{ display:'show' }} > <Link className = "cstyle" to = "/ins">Proceed</Link></button>
)

} else if(props.code.length > 10) {
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