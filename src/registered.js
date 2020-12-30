import React , { useEffect ,useRef, useState,useContext} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
//import 'bootstrap/dist/css/bootstrap.css';
import QuestionChoice from "./QuestionC.js";
import { If, Then, ElseIf, Else } from 'react-if-elseif-else-render';

import {domain} from "./config.js";

function Registered() {



  return (


<>

<div className="participant_form-content-div" align="center">

<div className="title-div"><br /><br />
	<label className="title-label">Registered Successfully</label>
</div>
<div className="ins-div mb-3">
<br/>
<h6 style={{marginLeft: '15px'}}>You have been registered successfully.We will notify you via given email about the commencement of examination
for the paper you have selected.<br/><br/>Thank you,<br/>Good luck.</h6>





</div>
</div>


</>
  );
}
export default Registered;