import React , { useEffect ,useRef, useState,useContext} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './bootstrap.css';
import QuestionChoice from "./QuestionC.js";
import { If, Then, ElseIf, Else } from 'react-if-elseif-else-render';
import { RadioGroup, RadioButton,ReversedRadioButton } from 'react-radio-buttons';
import {domain} from "./config.js";

function Paper_selection() {
{if(1==1){


//require('./test.css');
}
}
window.onbeforeunload = function() {
    return "Refresh not allowed";
}
const [paper,setPaper] = useState([]);
const [selected_paper, setSelected_paper] = useState({paper_id:null,paper_name:null})
const Domain = useContext(domain)
useEffect(() =>{

axios.get('http://'+Domain+'/dashboard')
.then(res =>{
console.log(res.data.papers)
setPaper(res.data.papers)
//for (const [index, value] of (res.data.data).entries()) {
//
//setExam_code(exam_code =>[...exam_code,value.exam_code])
//}

}
)

},[]);

console.log(selected_paper.paper_id,"selected_paper");
  return (


<>

<div className="ins-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">OneExam</label>
</div>
<div class="paper_selection-div text-center ">
<h3 className="mt-3 ml-4 text-left ">Please select one paper</h3>
	<table  className="custom-font mt-4">
	{paper.map((paper_name,index) => (
<p className="text-left ml-3 mt-1">
  <tr>
		<td>
    <div className="radio">
          <label>
            <input type="radio" onChange={event => setSelected_paper({paper_id:event.target.value,paper_name:paper_name.paper_name})}  name ="papername" value={paper_name.paper_id} />
    {paper_name.paper_name}
          </label>
        </div>
		</td>
</tr>

      </p> ))}


	</table>
</div>
{(()=> {
          if (selected_paper.paper_id) {
          return (
<button className="btn btn-custom  mt-3" > <Link className = "cstyle" to ={{ pathname: "/participant_form", paper: selected_paper}} >
Proceed</Link></button>
)
}
else{
return (
<button className="btn btn-custom  mt-3" disabled>
Proceed</button>
)
}
})()}
</div>


</>
  );
}
export default Paper_selection;