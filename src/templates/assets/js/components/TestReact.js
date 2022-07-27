import React, { useState } from 'react';
import TagsInput from 'react-tagsinput';
import 'react-tagsinput/react-tagsinput.css';
import Dropzone from 'react-dropzone'

const TestReact = () => {
  const [count, setCount] = useState(0)
  return (
      <div>
          <h1> hello </h1>
          <p className='text-center text-primary' style={{fontSize:'40px', fontWeight:'bolder'}}>{count}</p>
          <button className='btn btn-primary' onClick={()=>setCount(count+1)} >click</button>
          
      </div>
  );
};


export default TestReact;




