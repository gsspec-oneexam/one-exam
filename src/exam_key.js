import React , { useEffect , useState,useContext} from 'react';

import Code_check from "./exam_code.js";

function Exam_key(props) {
window.onbeforeunload = function() {
    return "Refresh not allowed";
}

const [code, setCode] = useState('null')

return (
<>
<div className="code-content-div" align="center">
<div className="title-div"><br /><br />
	<label className="title-label">OneExam</label>
</div>
<div className="code-div ">
<p>Please enter entrance code to proceed for online examination</p>
<input onChange={event => setCode(event.target.value)}/>&nbsp;
<Code_check code={code} />
</div>
</div>

</>)
}
export default Exam_key