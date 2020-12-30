import React , { useEffect , useState,useContext} from 'react';
import { Button,Row,Form,Col } from 'react-bootstrap';
import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import './bootstrap.css';
import {BrowserRouter as Router,Switch,Route,useHistory,Link,useLocation} from 'react-router-dom';
import { If, Then, ElseIf, Else } from 'react-if-elseif-else-render';
import axios from "axios";
import ProgressBar from 'react-bootstrap/ProgressBar';
//import VoiceRecorder from "./recorder.js";
import AudioRecorder from 'react-audio-recorder';
import ado from './Reeti.mp3';
import ReactAudioPlayer from 'react-audio-player';
import { Progress } from 'antd';
import Questions from "./questions_dynamic.js";

import { useForm } from 'react-hook-form';
import {domain} from "./config.js";

import questionContext from "./App";
function Participant_form(props) {
window.onbeforeunload = function() {
    return "Refresh not allowed";
}
const history = useHistory();
const Domain = useContext(domain)
const [answer, setAnswer] = useState()
const { paper } = useLocation();
console.log(paper,"check")
const { register, handleSubmit } = useForm({paper:"1"});
  const onSubmit = data => {


data["paper_id"] = paper.paper_id;
    console.log(data);
const requestOptions = {
        method: 'POST',
        body: JSON.stringify(data)
    };
    fetch('http://'+Domain+'/participant_form', requestOptions)
        .then(res =>res.json())
        .then((res) =>
        {
console.log(res.statusCode,"res")
        if (res.statusCode=2){
        history.push("/participant_registered");
        console.log(res.statusCode,"resif")
        }}
        )
  };
return (
<>

<div className="participant_form-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">{paper.paper_name}</label>
</div>
<div class="paper_selection-div mb-3 ">
<h3 className="mt-3 text-center">Registration Form</h3>
<br/>
<Form onSubmit={handleSubmit(onSubmit)}>
  <Form.Group>
    <Form.Row>
    <Form.Label column style={{marginLeft:"30%"}} lg={2}>
      First Name
    </Form.Label>
    <Col>
      <Form.Control type="text" name="first_name" ref={register} required/>
    </Col>
  </Form.Row>
  <br />
  <Form.Row>
    <Form.Label column style={{marginLeft:"30%"}} lg={2}>
      Last Name
    </Form.Label>
    <Col>
      <Form.Control type="text" name="last_name" ref={register} required/>
    </Col>
  </Form.Row>
  <br />
  <Form.Row>
    <Form.Label column style={{marginLeft:"30%"}} lg={2}>
      Email
    </Form.Label>
    <Col>
      <Form.Control type="email" name="email" ref={register} required/>
    </Col>
  </Form.Row>
  <br />
  <Form.Row>
    <Form.Label column style={{marginLeft:"30%"}} lg={2}>
      Mobile No.
    </Form.Label>
    <Col>
      <Form.Control type="text" name="mobile_no" ref={register} required/>
    </Col>
  </Form.Row>
  <br />
  <Form.Row>
    <Form.Label column style={{marginLeft:"30%"}} lg={2}>
      City
    </Form.Label>
    <Col>
      <Form.Control type="text" name="City" ref={register} required/>
    </Col>
  </Form.Row>
  <br/>
  <Form.Row>
    <Form.Label column style={{marginLeft:"30%"}} lg={2}>
      State
    </Form.Label>
    <Col>
      <Form.Control type="text" name="state" ref={register} required/>
    </Col>
  </Form.Row>
  <br />
  <Form.Row>
    <Form.Label column style={{marginLeft:"30%"}} lg={2}>
      Country
    </Form.Label>
    <Col>
      <Form.Control type="text" name="country" ref={register} required/>
    </Col>

  </Form.Row>
  <br /><center>
<Button type="submit" className="mb-2">
        Submit

      </Button></center>
</Form.Group>
</Form>

</div>
</div>


</>
  );
}
export default Participant_form