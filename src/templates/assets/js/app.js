import React from "react";
import ReactDOM from "react-dom";
import CreateProduct from "./components/CreateProduct";
import TestReact from "./components/TestReact";
// import TestReact from 

// require('./bootstrap');
// require('./sb-admin');
const propsContainer = document.getElementById("variants");
const props = Object.assign({}, propsContainer.dataset);

if (props.component==='test') {
    console.log('hitted')
    ReactDOM.render(
        <React.StrictMode>
            <TestReact />
        </React.StrictMode>,
        document.getElementById('test')
    );
} else if(props.component==='root') {
    console.log(props)
    ReactDOM.render(
        <React.StrictMode>
            <CreateProduct {...props} />
        </React.StrictMode>,
        document.getElementById('root')
    );
}



// {% comment %} import React from "react";
// import ReactDOM from "react-dom";
// import CreateProduct from "./components/CreateProduct";

// // require('./bootstrap');
// // require('./sb-admin');

// const propsContainer = document.getElementById("variants");
// const props = Object.assign({}, propsContainer.dataset);
// {% comment %} console.log(JSON.parse(props.variants.replaceAll("'", '"'))) {% endcomment %}
// ReactDOM.render(
//     <React.StrictMode>
//         <CreateProduct {...props}/>
//     </React.StrictMode>,
//     document.getElementById('root')
// );

//  {% endcomment %}
