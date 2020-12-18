import React , { useEffect ,useRef, useState,useContext} from 'react';
import { Button } from 'react-bootstrap';
import {BrowserRouter as Router,Switch,Route,Link,useHistory,useLocation } from 'react-router-dom';
import axios from 'axios';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css';
import QuestionChoice from "./QuestionC.js";
import { If, Then, ElseIf, Else } from 'react-if-elseif-else-render';

import {domain} from "./config.js";

function Registered() {

window.onbeforeunload = function() {
    return "Refresh not allowed";
}

  return (


<>

<div className="participant_form-content-div" align="center">


<h3 className="mt-2">Registered Successfully</h3>
<div className="ins-div mb-3">
<br/>
<h6>You have been registered successfully.We will notify you via given email about the commencement of examination
for the paper you have selected.<br/><br/>Thank you.<br/>Good luck.</h6>





</div>
</div>


</>
  );
}
export default Registered;